function createTask(category, name, flag, description, point, hint, link, eventId, public_status) {
    var obj = {
        task_category: category,
        task_name: name,
        task_flag: flag,
        task_description: description,
        task_point: point,
        task_hint: hint,
        task_solve: 0,
        task_link: link,
        status: 1,
        public_status : 1,
        id_event: eventId
    };

    var strObj = JSON.stringify(obj);

    str = 'http://217.23.13.145:' + port + '/task?param=create&data=' + strObj;

    var xhr = createCORSRequest('GET', str);
    xhr.send();

    xhr.onload = function () {
        var data = $.parseJSON(this.responseText);
        if (data.Answer.toLowerCase() === 'success') {
            alert("Таск добавлен");
        } else {
            alert('Ошибка. Проверьте правильно ли введены данные');
        }
    };

    xhr.onerror = function () {
        alert('request error ' + this.status);
    };
}

$(document).ready(function() {
    if (typeof(port) == "undefined") {
        var port = "13451";
    }

    $("#create-task-button").click(function(){	// Событие клика на кнопку "Зарегистрироваться"
        var category = $("#task-category").val();
        var name = $("#task-name").val();
        var flag = $("#task-flag").val();
        var description = $("#task-description").val();
        var point = $("#task-point").val();
        var hint = $("#task-hint").val();
        var link = $("#task-link").val();
        var eventId = $("#task-event-id").val();
        var public_status = $("#task-public-status").val();

        console.log(category);
        console.log(name);
        console.log(flag);
        console.log(description);
        console.log(point);
        console.log(eventId);

        if (category  && name && flag && description && point && eventId) {
            createTask(category, name, flag, description, point, hint, link, eventId, public_status);
        } else {
            alert("Введите корректно необходимые данные");
            var stars = $(".authorization__star");
            $(stars).show();

/*            $("#login").addClass("authorization__input--warning");
            $("#email").addClass("authorization__input--warning");
            $("#pass").addClass("authorization__input--warning");
            $("#pass-check").addClass("authorization__input--warning");*/
        }
    });

    /*$("#login").change(function () { $("#login").removeClass("authorization__input--warning") });
    $("#email").change(function () { $("#email").removeClass("authorization__input--warning"); });
    $("#pass").change(function () { $("#pass").removeClass("authorization__input--warning"); });
    $("#pass-check").change(function () { $("#pass-check").removeClass("authorization__input--warning"); });*/
});
