
/*
    Get template : new publisher
*/
$(document).on('click', '#btn-new-pub', function(){
    let url = $(this).data('url');
    let csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    let id_publisher = $(this).data('id-publisher'); // publisher id

    let request = $.ajax({
        url: url,
        type: 'POST',
        data: {'csrfmiddlewaretoken': csrftoken,
               'id_publisher': id_publisher},
        dataType: 'json'
    });
    request.done(function(data){
        if(data.success){
            if ( $('#id_newPub_form').length ) {
                 $('#id_newPub_form').remove();
            }
            $('#id_publisher').append(data.html);
        }else{
            console.log(data.message)
        }
    });
    request.fail(function(jqXHR, textStatus){
        console.log( "Request failed: " + textStatus );
    });
});

/*
    Show images preview
*/
$(document).on('change', '#id_image', function(evt){
    // let f = evt.target.files[0]; --> only one file
    let files = evt.target.files; // FileList object
    for (let i = 0, f; f = files[i]; i++) {
        let reader = new FileReader();
        // Closure to capture the file information.
        reader.onload = (function(theFile) {
            return function(e) {
                $('#id_pre_view').append('<img class="element" src="' +
                    e.target.result +
                    '" title="' + escape(theFile.name) +
                    '" name="image" id="id_image"/>');
                $('#id_label_image').addClass('dn');
            };
        })(f);
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
            $('#id_newPub_form').remove();
            console.log('save');
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
