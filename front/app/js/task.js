var tasks;



function getTasks() {
    var categories = new Array();
    var active;
    var obj = {
        id_event: 7
    };

    var data = JSON.stringify(obj);

    var str = 'http://90.189.132.25:13451/task?data=' + data;
    var xhr = createCORSRequest('GET', str);

    console.log(str);

    xhr.send();
    xhr.onload = function () {
        tasks = $.parseJSON(this.responseText);

        console.log("answer");
        console.log(tasks);
        console.log(tasks.Data.length);

        var categoiesContainer = document.getElementById("tasks__category-container");


        for (var i = 0; i < tasks.Data.length; i++) {

            var alreadyExists = false;

            for (var j = 0; j < categories.length; j++) {
                if (tasks.Data[i].task_category === categories[j]) {
                    alreadyExists = true;
                    break;
                }
            }

            if (!alreadyExists) {
                var str = '<div active-category="true"  category-name="' + tasks.Data[i].task_category + '" class="tasks__category">' + tasks.Data[i].task_category + '</div>';

                categoiesContainer.innerHTML += str;
                categories[categories.length] = tasks.Data[i].task_category;
            }
        }

        console.log($("[active-category=true]"));
        console.log($("#tasks__category-container").attr("class"));

        console.log($("[active-category=true]").attr("category-name"));
        var active = $("[active-category=true]").attr("category-name");



        for (var i = 0; i < tasks.Data.length; i++) {
            if (tasks.Data[i].task_category === active) { // ВЫВОД НА ЭКРАН
                str = '<div class="tasks__one-task">';
                str += '<div class="tasks__task-name">' + tasks.Data[i].task_name + '</div>';
                str += '<div class="tasks__form-container"><div class="tasks__task-description">' + tasks.Data[i].task_description +'</div> ';
                str += '<form onsubmit="submitTask(' + tasks.Data[i].id_task + ');" class="tasks__tasks-form" action="">';
                str += '<div class="tasks__task-flag-input"><input type="text">';
                str += '<div class="tasks__task-flag-input-done" style="display: none;"></div></div>';
                str += '<div class="tasks__task-submit-button" onclick="submitTask(' + tasks.Data[i].task_id + ')">Отправить</div></form></div></div>';
                document.getElementById("tasks-list-container").innerHTML += str;
            }
        }
    };

    xhr.onerror = function () {
        console.log('error ' + this.status);
    }
}

function submitTask(task) {
    alert(task);

    var flag = "c0c7c76d30bd3dcaefc96f40275bdc0a";

    var obj = {
        Task_id: 148,
        Task_flag: "CTF{test}",
        UUID: "0fc1d179-1b23-47dc-b83a-b3270b544c3d",
        id_event: 7
    };

    var data = JSON.stringify(obj);

    var str = 'http://90.189.132.25:13451/task?param=check&data=' + data;
    var xhr = createCORSRequest('GET', str);
    xhr.send();
    xhr.onload = function () {
        console.log(this.responseText);
        data = $.parseJSON(this.responseText);
        console.log(data);
        if (data.Answer === "Success") {
            console.log("Флаг правильный");
            //location.reload();
        } else { alert("Неправильный флаг"); }
    };

    xhr.onerror = function () {
        alert("Неверный флаг");
    }
}

function closeDescription() {
    $(".task-description").remove();
}

function openTask(task) {
    for (i = 0; i < tasks.Data.length; i++) {
        if (tasks.Data[i].Task_name === task) {
            var str = "<div class=\"task-description\">" +
                "<div class=\"task-description-container\">" +
                "<div class=\"task-description__close\" onclick=\"closeDescription()\">X</div>" +
                "<div class=\"task-description__title\">" + tasks.Data[i].Task_name + "</div>" +
                "<div class=\"task-description__description maybescroll\">" + tasks.Data[i].Task_description + "</div>";
            if (tasks.Data[i].Task_hint) {
                str = str + "<div class=\"task-description__description maybescroll\">Подсказка: " + tasks.Data[i].Task_hint + "</div>"
            }
            if (!tasks.Data[i].Close) {
                if (tasks.Data[i].Task_link) {
                    str = str + "<a href='" + tasks.Data[i].Task_link + "' class=\"task-description__link\">Link</a>";
                }
                str = str + "<form class=\"task-description-send-container\" action='javascript:submitTask('"+ task +"');'>" +
                    "<input class=\"task-description__flag\" type=\"text\" name=\"flag\" placeholder=\"FLAG\" " +
                    "id=\"flag\"></input> " +
                    "<button type=\"submit\" class=\"task-description__enter\" id=\"submit-task\" onclick=\"submitTask('" + task + "')\"></button>";
            }
            str = str + "</div></div>";
            $(".tasks-page").prepend(str);
            break;
        }
    }

    maybeScroll ();
}

$(document).ready(function () {
    //getTasks();
});
