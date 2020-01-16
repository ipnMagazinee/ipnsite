
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
    $('#id_department').val('Department');
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
    $('#id_department').val(item);
    $('#id_department').attr('data-id', '' + $(this).attr('id') + '');
    $('section').removeClass('blur');
});

/*
    Send Sign Up form
 */
$(document).on('click', '#btn_signUp', function () {
   let url = $(this).data('url');
   let name = $('#id_name').val();
   let email = $('#id_email').val();
   let pwd = $('#id_password').val();
   let conf_pwd = $('#id_conf_password').val();
   let area = $('#id_area').val();
   let dep = $('#id_department').val();
   let progress_val= $('#id_progress').val();
   let form = $('#id_signUp_form');

   // Empty inputs validation
   let message = ''
   message += ValidateEmpty(name, 'Enter name.')
    if(email.length === 0){
        message += 'Enter email address.';
    }else{ // Email address validation
        let regex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
        if (!(regex.test(email))){
            message += 'The email address is incorrect.';
        }
    }
    message += ValidateEmpty(pwd, 'Enter password.');
    if (pwd.length !== 0){
        if(progress_val <= 30){
            message += 'Your password is very easy.';
        }
    }
    if(conf_pwd.length === 0){
        message +=  'Enter confirm password.';
    }
    else{
        if(pwd !== conf_pwd){ message += 'Passwords do not match.'; }
    }
    message += ValidateEmpty(area, 'Enter Area.');
    message += ValidateEmpty(dep, 'Enter Department.');

    if(message.length === 0){ // send form

        let request = $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: new FormData($(form)[0]),
            dataType: 'json',
            contentType: false,
            processData: false,
        });
        request.done(function (data) {
            if(data.success) {
                window.location = data.url; // Redirect to user profile
            }
            else {
                $('#id_message').addClass('msg-error');
                $('#id_message_text').html(data.message);
            }
        });
        request.fail(function( jqXHR, textStatus ) {
        console.log( "Request failed: " + textStatus );
    });
    }
    else{ // validation fail
        $('#id_message').addClass('msg-error');
        $('#id_message_text').html(message);
    }
});

function ValidateEmpty(value, message) {
    if(value.length === 0){
            return message + ' ';
    }
    else{
        return '';
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
                window.location = data.url;
            }else{
                $('#id_message').addClass('msg-error');
                $('#id_message_text').html(data.message);
            }
        });
    request.fail(function(rqHX, textStatus){
        console.log('Error ' + textStatus)
    });
});

/*
      password progress bar
*/
$('#id_password').keyup(function(e) {
    $('#id_progress').show();
     var strongRegex = new RegExp("^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
     var mediumRegex = new RegExp("^(?=.{7,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
     var enoughRegex = new RegExp("(?=.{6,}).*", "g");
     if (false == enoughRegex.test($(this).val())) {
        $('#id_progress').val(5);
     } else if (strongRegex.test($(this).val())) {
        $('#id_progress').val(100);
     } else if (mediumRegex.test($(this).val())) {
        $('#id_progress').val(85);
     } else {
        $('#id_progress').val(30);
     }
     if($(this).val() == '')
     {
        $('#id_progress').hide();
     }
     return true;
});