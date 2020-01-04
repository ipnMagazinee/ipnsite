
/*
    Show images preview
*/
$(document).on('change', '#id_image', function(evt){
    let files = evt.target.files; // FileList object
    for (let i = 0, f; f = files[i]; i++) {
        let reader = new FileReader();
        reader.onload = function() {
            $('#id_pre_view').append('<img src='+ reader.result +' name="image" class="element">');
        }
        reader.readAsDataURL(f);
    }
});

/*
    Show document view
*/
$(document).on('change', '#id_file', function(evt){
    let file = evt.target.files[0];
    let reader = new FileReader();
    reader.onload = function(file){
        $('#id_doc_name').html(evt.target.files[0].name);
    }
    reader.readAsDataURL(file);
});

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

/*
    Update form
*/
$(document).on('click', '#id_btn_update', function(){
    // validations
    let message = '';
    message += validate($('#id_tittle').val(), 'Enter tittle. ')
    message += validate($('#id_description').val(), 'Enter a description. ')

    if (message.length === 0){
        let form = $('#id_updPub_form');
        let request = $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: new FormData($(form)[0]),
            dataType: 'json',
            contentType: false,
            processData: false,
        });
        request.done(function(data){
            if(data.success){ window.location = data.url;}
            else{console.log(data.message);}
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

/*
    Delete publication
*/
$(document).on('click', '.delete', function(){
    let url = $(this).data('url');
    let id_publication = $(this).data('id');
    let publication = $(this).parents('.user-list');
    let csrftoken = $('input[name="csrfmiddlewaretoken"]').val();

    let request = $.ajax({
        url: url,
        type: 'post',
        data:{'csrfmiddlewaretoken': csrftoken,
         'id_publication': id_publication},
    });
    request.done(function(data){
        if(data.success){
            $('#id_message').addClass('msg-success');
            $('#id_message_text').html(data.message);
            $(publication).remove();
            setTimeout(function() {
                $("#id_message").fadeOut(800);
            },3000);
        }
    });
    request.fail(function(jqXHR, textStatus){
        $('#id_message').addClass('msg-error');
        $('#id_message_text').html('There was a problem deleting the publication');
        console.log(textStatus);
    });

});