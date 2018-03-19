$(document).ready(function () {
    if ($.cookie('UUID')) {
        var obj = {
            //Login: $.cookie('UUID')
            UUID: "0fc1d179-1b23-47dc-b83a-b3270b544c3d"
        };


        var data = JSON.stringify(obj);

        var str = 'http://90.189.132.25:13451/cabinet?data=' + data;
        var xhr = createCORSRequest('GET', str);
        xhr.send();

        xhr.onload = function () {
            console.log(this.responseText);

            id = $.parseJSON(this.responseText);

            if(id.Answer === 'Success') {
                console.log("success");
            } else { alert('Произошла ошибка');}
        };

        xhr.onerror = function () {
            //alert('error ' + this.status);
            console.log(str);
        };



        //$(location).attr('href', "login.html");
        console.log("ВЫ не авторизованы, вас перенаправляет на страницу авторизации");
    }

    $("#logout-link").click(function () {
        logout();
    })
});