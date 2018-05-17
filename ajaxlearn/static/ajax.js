$(function(){
	$('#submitbutton').click(function(){
		$.ajax({
			type: 'POST',
			url:'/newlogin/',
			data:{
				'name': $('#user').val(),
				'password': $('#pass').val(),
				'csrfmiddlewaretoken' :$('input[name=csrfmiddlewaretoken]').val()
			},
			success:confirmationMessage,
			datatype: 'html'
		});
	});
});

function confirmationMessage(data, textStatus, jqXHR)
{
	$('#resultshow').html(data);
}
