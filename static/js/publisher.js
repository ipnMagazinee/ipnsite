
/*
    Send new publication form
*/
$(document).on('click', '#id_btn_send', function(){

    // validations
    let message = '';
    message += validate($('#id_tittle').val(), 'Enter tittle. ')
    message += validate($('#id_description').val(), 'Enter a description. ')

    if (message.length === 0){
        let form = $('#id_newPub_form');
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
                console.log(data.url);
                window.location = data.url;
            }else{
                console.log(data.message);
            }
        });
        request.fail(function(jqXHR, textStatus){
            $('#id_message').addClass('msg-error');
            $('#id_message_text').html(message);
        });
    } else{
        $('#id_message').addClass('msg-error');
        $('#id_message_text').html(message);
    }

});

function validate(elem, message){
    if (elem.length !== 0){
        return ''
    }else{
        return message;
    }
}

/* Download image */
