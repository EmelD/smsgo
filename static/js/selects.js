$('#country').change(function(){                   
    if ($('#country').val() == 0) {
        alert('Если выбрать «все страны», то селект с регионами будет отключен — так как нет смысла выводить все регионы со всех стран. Но все операторы будут подгружены!');

        $('#region')
            .attr('disabled', true)
            .children('option')
            .attr('selected', false);
        $('#region option:first').attr('selected', true);
    }
    else {
        alert('Подгружаем через Ajax список регионов и операторов, находящихся в выбранной стране');
        $('#region').attr('disabled', false);
    }
});

$('#region').change(function(){                   
    alert('Подгружаем через Ajax список операторов, находящихся в выбранном регионе');
});