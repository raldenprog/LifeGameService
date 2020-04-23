var data;

function writeAccountPageData(data) {
    console.log(data);

    document.getElementById('login').innerHTML = data.Data[0].name;
    document.getElementById('team').innerHTML = "";
    document.getElementById('rating').innerHTML = ""; // Пока что рейтинга нет
}

$(document).ready(function () {
    var obj = {
        UUID: $.cookie('UUID')
    };

    var data = JSON.stringify(obj);


    var str = 'http://90.189.132.25:'  + port +  '/cabinet?data=' + data;
    var xhr = createCORSRequest('GET', str);
    xhr.send();

    xhr.onload = function () {
        //console.log(this.responseText);

        var data = $.parseJSON(this.responseText);

        if (data.Answer === 'Success') {
            console.log("success");
        } else {
            alert('Произошла ошибка');
        }

        writeAccountPageData(data);
    };

    xhr.onerror = function () {
        //alert('error ' + this.status);
        console.log(str);
    };

    //$(location).attr('href', "login.html");
    console.log("ВЫ не авторизованы, вас перенаправляет на страницу авторизации");

    $("#logout-link").click(function () {
        logout();
    })
});