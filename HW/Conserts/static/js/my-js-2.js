function func() {
	$('#myModal').modal('show')
}

setTimeout(func, 300);

$('button[type=submit]').click(function(ev){
	ev.preventDefault();
	ajaxform('signup', 'signup')
})

function ajaxform(form, url) {
	$.ajax({
		url: url,
		type: "POST",
		datatype: "html",
		data: $("#"+form).serialize(),
		success: function(resp) {

			if (resp.error == 'True'){
				for (var i in resp.errors){
					$('input[name='+i+']').after(resp.errors[i]);
					$('input[name='+i+']').parent().addClass('has-error')
				}
			}
			else {
				location = './main'
			}

		},
		error: function(resp) {

		}
		
	})
}
