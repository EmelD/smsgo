function selectOperator(){
    var number = $('#f_phone').val();
    if(number && number.length > 7){
        $('#captcha-status').html('');
        ajax_request('http://127.0.0.1:8000/operator/',phone=number,'test',undefined,undefined,'captcha')
    }
}

function send_message(){
    if($("#f_message").val() !='' && $("#f_captcha").val() != ''){
        var param = new Object();
        param.msg = $("#f_message").val();
        param.captcha = $("#f_captcha").val();
        ajax_request('http://127.0.0.1:8000/send_msg/',param);
    }

}

function ajax_request(url, params, response_div_id, button_id, redirect,img) {
    $.ajax({
        url: url,
        type: 'post',
        dataType: 'json',
        data: params,
        beforeSend: function () {
            //$(response_div_id).text('Loading...');
            //$(button_id).button('loading');
        },
        success: function (response) {
            //alert(response.callback.name)
            if(response){
                if(response.type != 'error'){
                    if (response.callback) {
                        callbacks[response.callback.name](response.callback.params);
                    }
                }
                else{

                }
            }
        }
    });
}
function form_send(url,values)
{
    $.ajax({
        url: url,
        type: 'post',
        //dataType: 'json',
        data: values,
        success: function(resp){
            alert(resp);
        },
        error: function(resp){
            var a = '123';
            alert('err');
        }
    })
}

var callbacks = {

    'captcha': function (params) {
        $('#f_operator_box').html(params.Operator);
        $('#captcha-status').html('');
        $('#captcha-image').attr("src",params.Captcha_url);
        $('#captcha-update').animate({height: "show"}, 0);
    },

    'send': function(params) {
        $('#captcha-image').attr("src",'');
        $('#captcha-update').animate({height: "hide"}, 0);
        //alert('send');
    },

    'get_notification': function(params) {
        $('#notifications_table').append(params.rendered);
        striped_table('#notifications_table');
    }

};
