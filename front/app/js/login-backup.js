function authorisation(login, pass) {
    var str = {
       //Login: login,
        "Login": "test_user15",
        //Password: pass
        "Password": "new_password"
    };

    var data = JSON.stringify({Data: str});
    var xhr = createCORSRequest('POST', 'http://188.227.86.21:' + port + '/auth?data=');
    xhr.setRequestHeader(
        'X-Custom-Header', 'value');
    xhr.setRequestHeader(
        'Content-Type', 'application/json; charset=utf-8');
    xhr.setRequestHeader(
        'Access-Control-Allow-Origin', '*');
    xhr.send();

    xhr.onload = function () {
        alert("onload");
        console.log(this.responseText);

        id = $.parseJSON(this.responseText);
        if(id.Answer === 'Success') {
            $.cookie('UUID', String(id.Data.UUID));
            if ($.cookie('UUID')) {
                $(location).attr('href', "index.html");
            } else { alert("cookie error"); }
        } else { alert('Введены некорректные данные');}
    }

    xhr.onerror = function () {
        //alert('error ' + this.status);
        console.log(str);

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