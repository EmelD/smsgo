jQuery.fn.fullfilter = function(options) {
    
    var defaults ={
        // Показывать подробный фильтр
  		showFilter: true,
  		// Идентификатор контейнера с формой
  		filterForm: $('#filter-form'),
        // Идентификатор элемента, по клику на который будет разворачиваться форма фильтрации
        handle: $('#filter')
   	};
	
	var settings = jQuery.extend(defaults, options);	

    if (settings.showFilter === false) {
        settings.handle.attr('title', 'Показать форму фильтрации');
        settings.filterForm.css('display', 'none');
    }
    else{
        settings.handle.attr('title', 'Скрыть форму фильтрации');
        settings.filterForm.css('display', 'block');
    }
        
    $(this).bind('click',
        function(){
            if (settings.showFilter === false){
                settings.handle.attr('title', 'Скрыть форму фильтрации');
                settings.filterForm.slideDown(100);
                settings.showFilter = true;
            }
            else{
                settings.handle.attr('title', 'Показать форму фильтрации');
                settings.filterForm.slideUp(100);
                settings.showFilter = false;
            }
            return false;
        }
    );
    
    return this;	
};