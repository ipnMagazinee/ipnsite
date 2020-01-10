

// Initializes a new instance of the StringBuilder class
// and appends the given value if supplied
function StringBuilder(value){
    this.strings = new Array("");
    this.append(value);
}

// Appends the given value to the end of this instance.
StringBuilder.prototype.append = function (value){
    if (value){
        this.strings.push(value);
    }
};

// Clears the string buffer
StringBuilder.prototype.clear = function () {
    this.strings.length = 1;
};

// Converts this instance to a String.
StringBuilder.prototype.toString = function () {
    return this.strings.join(" ");
};



// Hide user options
$(document).on('click', function(evt){
    if($(window).width() <= 480){ // Phone
        id = evt.target.id;
        switch (id) {
            case 'id_user_data':
                if($('#id_user_options').is(':visible')){
                    $('#id_user_options').removeClass('dfc jc');
                    $('#id_user_options').addClass('dn');
                    $('#id_logo').show();
                }else{
                    $('#id_user_options').addClass('dfc jc');
                    $('#id_logo').hide();
                }
                break;
            case 'id_user_options':
                // do nothing
                break;
            default:
                $('#id_user_options').removeClass('dfc jc');
                $('#id_user_options').addClass('dn');
                $('#id_logo').show();
                break;
        }
    }else{ // PC
        id = evt.target.id;
        switch (id) {
            case 'id_user_data':
                if($('#id_user_options').is(':visible')){
                    $('#id_user_options').removeClass('dfc jc');
                    $('#id_user_options').addClass('dn');
                    $('#id_logo').css({'width': '85%'});
                }else{ // do not visible
                    $('#id_logo').css({'width': '70%'});
                    $('#id_user_options').css({'width': '15%'})
                    $('#id_user_options').removeClass('dn');
                    $('#id_user_options').addClass('dfc jc');
                }
                break;
            case 'id_user_options':
                // do nothing
                break;
            default:
                $('#id_user_options').removeClass('dfc jc');
                $('#id_user_options').addClass('dn');
                $('#id_logo').css({'width': '85%'});
                break;
        }
    }
});