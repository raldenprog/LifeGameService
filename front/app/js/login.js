function authorisation(login, pass) {
    var str = {
        //Login: login,
        Login: "test_user15",
        //Password: pass
        Password: "new_password"
    };

    var data = JSON.stringify(str);
    console.log(data);

    str = 'http://90.189.132.25:13451/auth?data=' + data;
    var xhr = createCORSRequest('GET', str);
    xhr.send();


    xhr.onload = function () {
        id = $.parseJSON(this.responseText);

        console.log(id);
        if(id.Answer === "Success") {
            $.cookie('UUID', id);

            if ($.cookie('UUID')) {
                $(location).attr('href', "personal-page.html");
                console.log("Вы авторизованы");
            } else { alert("coockie error"); }
        } else { console.log('Введены некорректные данные');}
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
        $(location).attr('href', "personal-page.html");

        console.log("ВЫ авторизованы, вас перенаправляет на чето");
    }
});