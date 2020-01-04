
/*
    Send form
*/

$(document).on('click', '#btn_save', function(){
    let form = $('#id_review_form');
    request = $.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: new FormData($(form)[0]),
        dataType: 'json',
        contentType: false,
        processData: false
    });
    request.done(function(data){
        if(data.success){ window.location = data.url; }
    });
    request.fail(function(jqXHR, textStatus){
        console.log(textStatus );
    });
});

/*
    Change the name of the file to upload
*/
$(document).on('change', '#id_file', function(evt){
    $('#id_file_name').html(evt.target.files[0].name);
});
