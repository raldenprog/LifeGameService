$(document).ready(function() {
    var steps = $("form").children(".step");

    function createCORSRequest(method, url) {
        var xhr = new XMLHttpRequest();
        if ("withCredentials" in xhr) {
            xhr.open(method, url, true);
        } else if (typeof XDomainRequest != "undefined") {
            xhr = new XDomainRequest();
            xhr.open(method, url);
        } else {
            xhr = null;
        }
        return xhr;
    }

    function registration(login, email, pass, name, sname, gender, city, educational) {
        var str = {
            Login: login,
            Password: pass,
            Name: name,
            Surname: sname,
            Email: email,
            Sex: gender,
            City: city,
            Educational: educational,
            Logo_name: '8',
            Logo: '9'
        };

        setJson(str, 'http://90.189.132.25:13451/registration');

        var data = JSON.stringify({Data: str});
        var xhr = createCORSRequest('POST', 'http://90.189.132.25:13451/registration');
        xhr.setRequestHeader(
            'X-Custom-Header', 'value');
        xhr.setRequestHeader(
            'Content-Type', 'application/json; charset=utf-8');
        xhr.setRequestHeader(
            'Access-Control-Allow-Origin', '*');
        xhr.send(data);

        xhr.onload = function () {
            alert("успешная регистрация");
            alert(this.responseText);
        }

        xhr.onerror = function () {
            alert('error ' + this.status);
        }
    }

    $("#reg-btn").click(function(){	// Событие клика на кнопку "Зарегистрироваться"
        login = $("#login").val();
        email = $("#email").val();
        pass = $("#pass").val();
        pass_check = $("#pass-check").val();
        name = $("#name").val();
        sname = $("#sname").val();
        gender = $("#gender").val();
        city = $("#city").val();
        educational = $("#educational").val();
/*
        console.log(login);
        console.log(email);
        console.log(pass);
        console.log(pass_check);
        console.log(name);
        console.log(sname);
        console.log(gender);
        console.log(city);
        console.log(educational);*/

        if (login  && email && pass && pass === pass_check) {
            registration(login, email, pass, name, sname, gender, city, educational);
        } else {
            alert("Введите корректно необходимые данные");
            $(steps).hide(); // скрываем все шаги
            $(steps[0]).show();
            var stars = $(".authorization__star");
            $(stars).show();

            $("#login").addClass("authorization__input--warning");
            $("#email").addClass("authorization__input--warning");
            $("#pass").addClass("authorization__input--warning");
            $("#pass-check").addClass("authorization__input--warning");
        }
    });

    $("#login").change(function () { $("#login").removeClass("authorization__input--warning") })
    $("#email").change(function () { $("#email").removeClass("authorization__input--warning"); })
    $("#pass").change(function () { $("#pass").removeClass("authorization__input--warning"); })
    $("#pass-check").change(function () { $("#pass-check").removeClass("authorization__input--warning"); })
});