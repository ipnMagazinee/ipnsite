
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
            if ( $('#id_new_pub').length ) {
                $('#id_new_pub').remove();
            }
            $('section').append(data.html);
        }else{
            console.log(data.message)
        }
    });
    request.fail(function(jqXHR, textStatus){
        console.log( "Request failed: " + textStatus );
    });
});