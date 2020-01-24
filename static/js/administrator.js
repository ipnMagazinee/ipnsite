
$(document).ready(function(){
    $('#id_search_result').hide();
});

$('#btn_send').click(function(){
    let form = $('id_form_permission');

    let request = $.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: new FormData($(form)[0]),
        dataType: 'json',
        contentType: false,
        processData: false,
    });
    request.done(function(data){
        if(data.success){
            $('#id_message').addClass('msg-success');
            $('#id_message_text').html(data.message);
        }
        else{
            $('#id_message').addClass('msg-error');
            $('#id_message_text').html(data.message);
        }
    });
    request.fail(function(textStatus){
        $('#id_message').addClass('msg-error');
        $('#id_message_text').html('Error sending information');
        console.log(textStatus)
    });

});

/*
    Search for a username and display it
*/
$('#id_search').keyup(function(evt){
    let key = event.which || event.keyCode;
    if(key === 13){
      console.log("ENTER");
    }
    let text = $(this).val();

    if(text.length >= 4){
        request = $.ajax({
            url: $(this).data('url'),
            type: 'post',
            data: {'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                   'username': text},
            dataType: 'json'
        });
        request.done(function(data){
            if(data.success){
                $('#id_search_result').show();
                $('#id_search_result').empty();
                for(var x in data.username){
                    $('#id_search_result').append('<span class="element">' + data.username[x] + '</span>');
                }
            }else{
                $('#id_message').addClass('msg-error');
                $('#id_message_text').html(data.message);
            }
        });
        request.fail(function(contentType){
            $('#id_message').addClass('msg-error');
            $('#id_message_text').html('Sending error');
            console.log(contentType.statusText)
        })
    }else{
        $('#id_search_result').empty();
        $('#id_search_result').hide();
    }
});



