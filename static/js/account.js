
/*
    Get Areas
 */

$(document).on('click', '.area', function () {
    let url = $(this).data('url');
    let request = $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',

    });
    request.done(function( data ) {
        if(data.success){
            $('section').addClass('blur');
            $('body').append(data.html);
        }
    });
    request.fail(function( jqXHR, textStatus ) {
        console.log( "Request failed: " + textStatus );
        $('section').removeClass('blur');
    });
});

/*
    Select area: hide the list and show the item selected in the input: area
 */
$(document).on('click','.item_area', function () {
    let item = $(this).text();
    $('#list_area').remove();
    $('#id_area').val(item);
    $('#id_dep').val('Department');
    $('#id_area').attr('data-id', '' + $(this).attr('id') + '');
    $('section').removeClass('blur');

    // refresh
});

/*s
    Get Departments
 */
$(document).on('click', '.dept', function () {
    let area = $('#id_area').val();
    if(id_area !== 'Area'){
        let url = '/account/getDep/' + area + '/';
        let request = $.ajax({
            url: url,
            type: 'GET'
        });
        request.done(function (data) {
            if (data.success){
                $('body').append(data.html);
                $('section').addClass('blur');
            } else {
                console.log(data.message);
                $('section').removeClass('blur');
            }
        });

    } // end if
});

/*
    Select area: hide the list and show the item selected in the input: departem
 */
$(document).on('click', '.item_dep', function () {
    let item = $(this).text();
    $('#list_dep').remove();
    $('#id_dep').val(item);
    $('#id_dep').attr('data-id', '' + $(this).attr('id') + '');
    $('section').removeClass('blur');
});

/*
    Send Sign Up form
 */
$(document).on('click', '#btn_signUp', function () {
   let csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
   let url = $(this).data('url');
   let name = $('#id_name').val();
   let email = $('#id_email').val();
   let pwd = $('#id_password').val();
   let conf_pwd = $('#id_conf_password').val();
   let id_area = $('#id_area').data('id');
   let id_dep = $('#id_dep').data('id');

   // Empty inputs validation
    let msgBuilder = new StringBuilder();
    if(name.length === 0){
        msgBuilder.append('Enter name.');
    }
    if(email.length === 0){
        msgBuilder.append('Enter email address.');
    }else{ // Email address validation
        let regex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
        if (!(regex.test(email))){
            msgBuilder.append('The email address is incorrect.');
        }
    }
    if(pwd.length === 0 ){
        msgBuilder.append('Enter password.');
    }
    if(conf_pwd.length === 0){
        msgBuilder.append('Enter confirm password.');
    }else{
        if(pwd !== conf_pwd){ msgBuilder.append('Passwords do not match') }
    }
    if(id_area === 0){
        msgBuilder.append('Enter Area.');
    }
    if(id_dep === 0){
        msgBuilder.append('Enter Department.');
    }
    if(msgBuilder.toString().length === 0){ // send form

        let request = $.ajax({
            url: url,
            type: 'POST',
            data: {'csrfmiddlewaretoken': csrftoken,
                'name': name,
                'email': email,
                'password': pwd,
                'id_area': parseInt(id_area),
                'id_dep': parseInt(id_dep)},
            dataType: 'json'
        });
        request.done(function (data) {
           if(data.success) {
                $('#id_message').addClass('msg-success');
                $('#id_message_text').html(data.message);
           }else {
               $('#id_message').addClass('msg-error');
                $('#id_message_text').html(data.message);
           }
        });
        request.fail(function( jqXHR, textStatus ) {
            console.log( "Request failed: " + textStatus );
        });

    }else{ // validation fail
        $('#id_message').addClass('msg-error');
        $('#id_message_text').html(msgBuilder.toString());
    }
});

function Validate(value, message) {
    let msgBuilder = StringBuilder();
    if (isNaN(value)) { // Not a Number!'
        if(value.length === 0){
            msgBuilder.append(message);
        }
    }
    if(value === 0){
        msgBuilder.append(message);
    }
}

/*
    Send Login Form
* */
$(document).on('click', '#btn_login', function () {
    let form = $('#id_login_form');
    request = $.ajax({
        url: form.attr('action'),
        type: form.attr('method'),
        data: new FormData($(form)[0]),
        dataType: 'json',
        contentType: false,
        processData: false,
    });
    request.done(function(data){
            if(data.success){
                windows.open(data.url);
            }else{
                $('#id_message').addClass('msg-error');
                $('#id_message_text').html(data.message);
            }
        });
    request.fail(function(rqHX, textStatus){
        console.log('Error ' + textStatus)
    });
});