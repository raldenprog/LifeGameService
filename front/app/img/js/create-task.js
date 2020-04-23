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
        task_category: 'crypto',
        task_name: 'test_task_crypto101',
        task_flag: 'CTF{test}',
        task_description: 'test',
        task_point: 100,
        task_hint: 'test',
        task_solve: 0,
        task_link: 'http:test',
        status: 0,
        public_status: 0,
        id_event: 7
    };

    var data = JSON.stringify(str);

    str = 'http://90.189.132.25:13451/registration?data=' + data;
    var xhr = createCORSRequest('GET', str);
    xhr.send();

    xhr.onload = function () {

    };

    xhr.onerror = function () {
        alert('error ' + this.status);
    }
}

$(document).ready(function() {



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