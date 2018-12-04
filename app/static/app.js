var suit = -1;
var qs = -1;
$('#chat-form').on('submit', function(event){
    event.preventDefault();
    console.log( $('#chat-msg').val() );
    $.ajax({
        url : '/post/',
        type : 'POST',
        data : {
            msgbox : $('#chat-msg').val(),
            suit : suit,
            qs : qs,
        },

        success : function(json){
            $('#chat-msg').val('');
            $('#msg-list').append('<li class="text-left query list-group-item">' + json.query + '</li>');
            $('#msg-list').append('<li class="text-left response list-group-item">' + json.response + '</li>');
            suit = json.suit;
            qs = json.qs;
            if(qs == 4){
                $('#send').attr('disabled','disabled');
            }
        },
        failure: function(data) {
            alert('Got an error dude, ajax not get back!');
        }
    });
});

$(document).ready(function() {
    $('#send').attr('disabled','disabled');
    $('#chat-msg').keyup(function() {
       if($(this).val() != '' && qs != 4) {
          $('#send').removeAttr('disabled');
       }
       else {
       $('#send').attr('disabled','disabled');
       }
    });
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});