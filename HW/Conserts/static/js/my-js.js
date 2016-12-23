function func() {
	$('#myModal').modal('show')
}

setTimeout(func, 300)

$('button[type=submit]').click(function(ev){
	ev.preventDefault();
	ajaxform('signin', 'signin')
})

function ajaxform(form, url) {
	$.ajax({
		url: url,
		type: "POST",
		datatype: "html",
		data: $("#"+form).serialize(),
		success: function(resp) {
			data = resp.trim();
			if (data == 'N/A'){
				location = 'main_list/'
			}
			else {
				$('#errors').append(data);
			}
		},
		error: function(resp) {

		}
		
	})
}
