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
    $('#error-time').remove()
    event.preventDefault();
    var reg = /(\d{4})-([0-9]|1[0-2])-([\d]|[1-2][\d]|3[0-1]) ([\d]|[1-2][\d]|2[0-4]):([\d]|[1-5][\d]):([\d{2}|[1-5][\d])/
    var date = $('#id_time').val();

    if(date.match(reg)) {
        $(this).unbind('submit').submit()
    }
    else {
        $('#id_time').parent().addClass('has-error');
        $('#id_time').after('<div id="error-time">Not Valid time</div>')
    }
  
})