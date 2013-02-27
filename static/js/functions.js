function initializeSmsForm (type, freeForm, paidForm, freePhone, paidPhone) {
    
    if (type == 'free') {
        paidPhone.removeAttr('autofocus');
        freePhone.focus();
        var height = freeForm.height();
        freeForm.css('min-height', height);
        paidForm.css({
            'margin-top': height*(-1),
            'opacity': 0,
            'display': 'block',
            'min-height': paidForm.height()
        });
    };

    if (type == 'paid') {
        freePhone.removeAttr('autofocus');
        paidPhone.focus();
        var height = paidForm.height();
        paidForm.css('min-height', height);
        freeForm.css({
            'margin-top': height*(-1),
            'opacity': 0,
            'display': 'block',
            'min-height': freeForm.height()
        });
    };
}

function showFreeSms (freeForm, paidForm, showFreeSms, showPaidSms, freePhone, speed) {

    freeForm
        .stop()
        .animate({'left': '0%', 'opacity': 1}, speed, function() {
            $(this).css('z-index', 10);
            showPaidSms.removeClass('current');
            showFreeSms.removeClass('current').addClass('current');
            freePhone.focus();
            if (freePhone.val() != '') $(this).trigger('change');
        });

    paidForm
        .stop()
        .animate({'left': '50%', 'opacity': 0}, speed, function() {
            $(this).css('z-index', 5);
        });
}

function showPaidSms (freeForm, paidForm, showFreeSms, showPaidSms, paidPhone, speed) {

    freeForm
        .stop()
        .animate({'left': '-50%', 'opacity': 0}, 150, function() {
            $(this).css('z-index', 5);
        });

    paidForm
        .stop()
        .animate({'left': '0%', 'opacity': 1}, 150, function() {
            $(this).css('z-index', 10);
            showPaidSms.removeClass('current').addClass('current');
            showFreeSms.removeClass('current');
            paidPhone.focus();
            if (paidPhone.val() != '') $(this).trigger('change');
        } );
}

function cloneFormData (type, freePhone, freeMessage, paidPhone, paidMessage) {
    
    if (type == 'free') {
        var f_phone = freePhone.attr('value');
        var f_message = freeMessage.attr('value');
        if ( f_phone == '') {
            var p_phone = paidPhone.attr('value');
            if ( p_phone !== '') freePhone.attr('value', p_phone).trigger('change');
        };
        if ( f_message == '') {
            var p_message = paidMessage.attr('value');
            if ( p_message !== '') freeMessage.attr('value', p_message);
        };
    };

    if (type == 'paid') {
        var p_phone = paidPhone.attr('value');
        var p_message = paidMessage.attr('value');
        if (p_phone == '') {
            var f_phone = freePhone.attr('value');
            if ( f_phone !== '') paidPhone.attr('value', f_phone).trigger('change');
        };
        if (p_message == '') {
            var f_message = freeMessage.attr('value');
            if ( f_message !== '') paidMessage.attr('value', f_message);
        }; 
    };

}

function getLastTweet (user, place, loading) {

    place.text(loading);

    // using jquery built in get json method with twitter api, return only one result
    $.getJSON('http://twitter.com/statuses/user_timeline.json?screen_name=' + user + '&count=1&callback=?', function(data) {         
        // result returned
        var tweet = data[0].text;
        // process links
        tweet = tweet.replace(/(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig, function(url) {
            return '<a href="'+url+'">'+url+'</a>';
        });
        // output the result
        place.html(tweet);
    });
}

function initializeModalWindow (modalBox, overlay, modalClose, speed) {

    if($.browser.msie && (parseInt($.browser.version, 10) <= 6)) return true;
    else {
            modalBox
                .stop()
                .css({
                    'opacity': 0,
                    'display': 'block',
                    'margin-top': modalBox.height()/2*(-1),
                    'top': 0
                })
                .animate({'top': '50%', 'opacity': 1}, speed);

            overlay
                .clearQueue()
                .fadeIn(speed);

            function closeModalWindow () {
                modalBox
                .stop()
                    .animate({'margin-top': 0, 'opacity': 0}, speed, function () {
                        $(this).css('display', 'none');
                    });

                overlay
                    .stop()
                    .fadeOut(speed);
            };

            $(document).keyup(function(e) {
                if (e.keyCode == 27) closeModalWindow ();   // esc press
            });

            modalClose.click(closeModalWindow); // btn close press

        return false;
    }
}

function initializeFAQ (ul, speed) {

    ul.find('div').css('display', 'none');

    ul.find('a').click(
        function() {
            if ($(this).hasClass('current')) {
                $(this)
                    .removeClass('current')
                    .next('div')
                    .slideUp(speed);
            }
            else {
                $(this)
                    .addClass('current')
                    .next('div')
                    .slideDown(speed);
            }
        }
    );

    // expand answear
    if(window.location.hash) {
        var hash = window.location.hash.substring(1); //Puts hash in variable, and removes the # character
        var currentLi = ul.find('li[name=' + hash + ']');
        currentLi.children('div').css('display', 'block');
        currentLi.children('a').addClass('current');
    }
}

function reloadFAQ (links) {
    links.click(function(){
        window.location = $(this).attr('href');
        location.reload();
    });
}


function initializeJokes (refreshJokes, jokes, speed, senderInput, messageInput, idInput) {
    var totalPairs = jokes.length/2;
    jokes.css('display', 'none');
    jokes.slice(0, 2).slideDown(speed);

    refreshJokes
        .data('position', 0)
        .click(
            function(){
                var currentIncr = $(this).data('position') + 1;
                if ((totalPairs - currentIncr) <= 1) $(this).data('position', -1);
                else $(this).data('position', currentIncr);
                jokes.slideUp(speed);
                jokes.slice(currentIncr*2, currentIncr*2+2).slideDown(speed);

            }
        );

    jokes
        .children('a')
        .bind('click', function(){
            senderInput.val($(this).text());
            messageInput.val($(this).nextAll('span').text());
            idInput.val($(this).attr('href'));
        });
}

function messageCheck (textarea, maxLimit, limitBox) {

    var currentLength = textarea.val().length;
    var difference = maxLimit - currentLength;

    var decCache = [],
    decCases = [2, 0, 1, 1, 1, 2];

    function decOfNum(number, titles) {
        if(!decCache[number]) decCache[number] = number % 100 > 4 && number % 100 < 20 ? 2 : decCases[Math.min(number % 10, 5)];
        return titles[decCache[number]];
    }

    if(currentLength == 0) {
        limitBox.html('');
    }
    else {
        if(currentLength <= maxLimit){
            limitBox.html(' · осталось ' + difference + decOfNum(difference, [' символ', ' символа', ' символов']));
        }
        else {
            limitBox.html(' · вы ввели ' + Math.abs(difference) + decOfNum(Math.abs(difference), [' лишний символ', ' лишних символа', ' лишних символов']));
        }
    }
}

function defineLanguage (text) {

    var reg = /[а-яё]/i
    var layout = reg.test(text) ? 'ru' : 'en';

    return layout;
}

function setOperator (title, url, placeHolder) {
    if (title == '') placeHolder.html('');
    else {
        if (url == '') placeHolder.html(' · ' + title);
        else placeHolder.html(' · <a href="' + url + '" target="_blank">' + title + '</a>');
    }
}

// Валидация номера 
jQuery.validator.addMethod('phoneCheck', function(value, element) {
    var correct =/^\+?[\d\s.,_-]+$/i.test(value);
    if (correct) {
        var numbersCounter = value.replace(/[^\d]+/g, '').length;
        if ((numbersCounter >= 10) && (numbersCounter <= 15)) correct = true;
        else correct = false;
    }
    return this.optional(element) || correct;
}, 'Incorrect');

// Валидация отправителя 
jQuery.validator.addMethod('senderCheck', function(value, element) {
    var correct =/^\+?[\d\s.,_-]+$/i.test(value);
    
    // Если вводимая строка похожа на номер
    if (correct) {
        var numbersCounter = value.replace(/[^\d]+/g, '').length;
        if ((numbersCounter >= 10) && (numbersCounter <= 15)) correct = true;
        else {
            if (value.length <= 11) correct = /^[\w\@\$\!\"\%\&\‘\(\)\*\+\,\–\.\/\_\:]+$/g.test(value);
            else correct = false;
        }
    }
    // Если это не номер
    else {
        if (value.length <= 11) correct = /^[\w\@\$\!\"\%\&\‘\(\)\*\+\,\–\.\/\_\:]+$/g.test(value);
        else correct = false;
    }

    return this.optional(element) || correct;
}, 'Incorrect');

// Танцы с бубном, чтобы подружить плагин для валидации с получением данных об операторе. Сделано так, чтобы не делать два запроса — один на корректность данных, другой на получение информации об операторе
jQuery.validator.addMethod('dullCheck', function(value, element) {
    return this.optional(element) || false;
}, 'Incorrect');