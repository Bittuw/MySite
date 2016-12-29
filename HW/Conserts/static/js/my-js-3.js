var infinityList = {};
infinityList.updateGeneral = function(){
    var obj = this;
    obj.pageHeight = parseInt($(document).height());
    obj.winHeight = parseInt($(window).height());
}

infinityList.init = function(){
    var obj = this;

    obj.updateGeneral();

    obj.scrollIndex = 0;
    obj.eror_lock = false;
    obj.load_lock = false;
    obj.end_of_list  = false;

    // ловим событие скрола
    $(document).scroll(function () { 
        var pos = parseInt($(document).scrollTop());

        // console.log((pos + obj.winHeight > obj.pageHeight));
        console.log((pos + obj.winHeight));
        console.log(obj.pageHeight);

        if ((pos + obj.winHeight > obj.pageHeight - 20) &&  
            (!obj.load_lock) &&
            (!obj.end_of_list)) 
        {
            obj.scrollIndex++;
            console.log(obj.scrollIndex);
            obj.load_lock = true;
            $.ajax({
                url: '/main_list/' + obj.scrollIndex,
                type: 'GET',
                data: {},
                dataType: 'text',
                timeout: 60000,
                success: function(response){

                    // console.log('response***' + response + '****');

                    if ($(response).find('ul.media-list').text().trim() == 'N/A') {
                        obj.end_of_list = true;
                    }else{
                        $('ul.media-list').append($(response).find('li.media'));
                    }

                    obj.updateGeneral();
                    obj.load_lock = false;
                },
                error: function(){
                    if (!obj.eror_lock) {
                        obj.scrollIndex--;
                        obj.eror_lock = true;
                        $(document).scrollTop(0);
                        alert('Упс... Что то пошло не так, обновите страницу и повторите попытку.');
                        setTimeout(function() { 
                            location.reload();
                        }, 1);
                    }
                }
            });
        }else{
        }
    });

    // ресайз
    $(window).resize(function () {
        obj.updateGeneral();
    });
}

$(document).ready(function () {
    infinityList.init();
})

$('form').submit(function(event) {

    event.preventDefault();

    var arr = $('.has-error');
    for (var i = 0;i < arr.length; i++) {
        var elem = arr.get(i);
        $(elem).removeClass('has-error');
        $(elem).children('div').remove();
    }
   
    var reg = /(\d{4})-([0-9]|1[0-2])-([\d]|[1-2][\d]|3[0-1]) ([\d]|[1-2][\d]|2[0-4]):([\d]|[1-5][\d]):([\d{2}|[1-5][\d])/;
    var date = $('#id_time').val();
    var name = $('#id_name').val();
    var theatre = $('#id_theatre').val();
    var description = $('#id_description').val();

    if (!(name.length < 5 || name.length > 30)) {
        name = true;
    }
    else {
        $('#id_name').parent().addClass('has-error');
        $('#id_name').after('<div id="error-name">Not Valid name</div>');
        name = false;
    }
    if (!(theatre.length < 20 || theatre.length > 40)) {
       theatre = true;
    }   
    else {
        $('#id_theatre').parent().addClass('has-error');
        $('#id_theatre').after('<div id="error-theat">Not Valid theatre</div>');
        theatre = false;
    }
    if (!(description.length < 20 || description.length > 100)) {
        description = true;
    }
    else {
        $('#id_description').parent().addClass('has-error');
        $('#id_description').after('<div id="error-desc">Not Valid description</div>');
        description = false;
    }
    if(date.match(reg)) {
        date = true;
    }
    else {
        $('#id_time').parent().addClass('has-error');
        $('#id_time').after('<div id="error-time">Not Valid time</div>');
        date = false;
    }
    if (name && date && theatre && description) {
        $(this).unbind('submit').submit();
    }
})