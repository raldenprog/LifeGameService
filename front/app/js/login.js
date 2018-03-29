if (typeof(port) == "undefined") {
    var port = "13451";
}

function authorisation(login, pass) {
    var str = {
        Login: login,
        Password: pass
    };

    var data = JSON.stringify(str);
    console.log(data);

    str = 'http://90.189.132.25:'  + port +  '/auth?data=' + data;
    var xhr = createCORSRequest('GET', str);
    xhr.send();


    xhr.onload = function () {
        id = $.parseJSON(this.responseText);

        console.log(id);
        if(id.Answer === "Success") {
            //$.cookie('UUID', id.Data.UUID);
            setCookie('UUID', id.Data.UUID, {path: '/'});

            if ($.cookie('UUID')) {
                $(location).attr('href', "/competitions-list");
            } else { alert("coockie error"); }


        } else {
            console.log("Некорректные данные");

            $("#pass-field").addClass('authorization__input-text--wrong');
            $("#login-field").addClass('authorization__input-text--wrong');

            setTimeout(function(){
                $("#pass-field").removeClass('authorization__input-text--wrong');
                $("#login-field").removeClass('authorization__input-text--wrong');
            }, 2000);
        }
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

});