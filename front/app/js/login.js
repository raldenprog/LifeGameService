function authorisation(login, pass) {
    var str = {
        Login: login,
        Password: pass
    };

    var data = JSON.stringify({Data: str});
    var xhr = createCORSRequest('POST', 'http://90.189.132.25:13451/auth');
    xhr.setRequestHeader(
        'X-Custom-Header', 'value');
    xhr.setRequestHeader(
        'Content-Type', 'application/json; charset=utf-8');
    xhr.setRequestHeader(
        'Access-Control-Allow-Origin', '*');
    xhr.send(data);

    xhr.onload = function () {
        id = $.parseJSON(this.responseText);
        if(id.Answer === 'Success') {
            $.cookie('UUID', String(id.Data.UUID));
            if ($.cookie('UUID')) {
                $(location).attr('href', "index.html");
            } else { alert("cookie error"); }
        } else { alert('Введены некорректные данные');}
    }

    xhr.onerror = function () {
        alert('error ' + this.status);
    }
}

function authorisationSubmit() {
    if($("#pass-field").val() && $("#pass-field").val()){
        authorisation($("#login-field").val(), $("#pass-field").val());
    } else { alert("Введите данные"); }
}

$(document).ready(function() {
    if ($.cookie('UUID')) {
        $(location).attr('href', "index.html");
    }
});