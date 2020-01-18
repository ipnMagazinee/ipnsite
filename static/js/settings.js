
$('#id_image').change(function( evt){
    let file = evt.target.files[0];
    let fileReader = new FileReader();
    fileReader.onload = function(){
        $('#id_image_preview').attr('src', fileReader.result);
    }
    fileReader.readAsDataURL(file);
});

/*
    Send settings user form
*/
$('#btn_user').click(function(){
    let name = $('#id_name').val();
    if (name === ''){
        $('#id_message').addClass('msg-error');
        $('#id_message_text').html('Enter name');
    }
    else{
        let form = $('#id_form_user');
        let request = $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: new FormData($(form)[0]),
            dataType: 'json',
            contentType: false,
            processData: false,
        });
        request.done(function(data){
            if(data.success){ $('#id_message').addClass('msg-success'); }
            else{ $('#id_message').addClass('msg-error'); }
            $('#id_message_text').html(data.message);
        });
        request.fail(function(jqXHR, textStatus){
            $('#id_message').addClass('msg-error');
            $('#id_message_text').html('Error sending information ');
            console.log(textStatus);
        });
    }
});