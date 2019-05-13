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

            //Login:"new_user2",
            /*Password:"new_password",
            Name:"new_name",
            Surname:"new_surname",
            Email:"new_email",
            City:"new_city",
            Educational:"new_ed",
            Logo_name:"new_logo_name",
            Logo:"new_logo",
            Sex:"Man"*/
        };

        var data = JSON.stringify(str);


        str = 'http://90.189.168.29:13451/registration?data=' + data;
        var xhr = createCORSRequest('GET', str);
        xhr.send();

        xhr.onload = function () {
            alert("успешная регистрация");
            alert(this.responseText);
            console.log(this.responseText);
            //console.log($.parseJSON(this.responseText));
            var answ = $.parseJSON(this.responseText);
            console.log(answ.Answer);
            if (answ.Answer === 'Success') {
                $.cookie('UUID', answ.Data.UUID);
                console.log("cookie set");
                console.log($.cookie('UUID'));
            }

            if ($.cookie('UUID') != null) {
                $(location).attr('href', "personal-page.html");

            }
        };

        xhr.onerror = function () {
            alert('error ' + this.status);
        }
    }


    $("#reg-btn").click(function(){	// Событие клика на кнопку "Зарегистрироваться"
        var login = $("#login").val();
        var email = $("#email").val();
        var pass = $("#pass").val();
        var pass_check = $("#pass-check").val();
        var name = $("#name").val();
        var sname = $("#sname").val();
        var gender = $("#gender").val();
        var city = $("#city").val();
        var educational = $("#educational").val();
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