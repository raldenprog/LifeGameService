var tasks;
var id_event;

if (typeof(port) == "undefined") {
    var port = "13451";
}

function Competition() {

}

Competition.prototype.changeCategory = function (category) {
    var containers = $('.competition__category-list-container');
    for (var i = 0; i < containers.length; i++) {
        containers.eq(i).hide();
    }
    $("#" + category + "-tasks-container").show();

    var categories = $('.competition__category');
    for (var i = 0; i < categories.length; i++) {

        if (categories.eq(i).attr('name') === category) {
            categories.eq(i).addClass('competition__category--active');
        } else {
            categories.eq(i).removeClass('competition__category--active');
        }
    }

    this.activeCategory = category.toLowerCase();
};


var competition = new Competition();

function addCategoryContainer(tasks) {
    var container = "";
    for (var i = 0; i < tasks.Data.length; i++) {
        /*var container = document.CreateElement("div", {
            "class": "competition__category-list-container",
            "id": tasks.Data[i].task_category.toLowerCase() + "wtf-tasks-container",
            "style": "display: none;"
        });*/
        if (tasks.Data[i].task_category === competition.activeCategory) {
            container += '<div class="competition__category-list-container" id="' + tasks.Data[i].task_category.toLowerCase() + '-tasks-container"></div>';
        } else {
            container += '<div class="competition__category-list-container" id="' + tasks.Data[i].task_category.toLowerCase() + '-tasks-container" style="display: none"></div>';
        }

    }
    document.getElementById("tasks-container").innerHTML += container;
    //tasks.Data[i].task_category.toLowerCase();
}

function getTasks(competitionId) {
    id_event = competitionId;

    var categories = new Array();
    var active;

    var obj = {
        id_event: id_event,
        UUID: $.cookie('UUID')
    };

    var data = JSON.stringify(obj);

    var str = 'http://192.168.0.7:' + port + '/task?data=' + data;
    var xhr = createCORSRequest('GET', str);

    xhr.send();
    xhr.onload = function () {
        tasks = $.parseJSON(this.responseText);

        competition.activeCategory = tasks.Data[0].task_category;
        competition.categoryArray = new Array();

        console.log("answer");
        console.log(tasks);
        console.log(tasks.Data.length);

        var categoiesContainer = document.getElementById("tasks-category-container");

        // Добавление категорий в контейнер
        for (var i = 0; i < tasks.Data.length; i++) {
            var alreadyExists = false;
            for (var j = 0; j < categories.length; j++) {
                if (tasks.Data[i].task_category === categories[j]) {
                    alreadyExists = true;
                    break;
                }
            }

            if (!alreadyExists) {
                if (tasks.Data[i].task_category === competition.activeCategory) {
                    var str = '<div name="' + tasks.Data[i].task_category.toLowerCase() + '" onclick="competition.changeCategory(\'' + tasks.Data[i].task_category.toLowerCase() + '\')"  class="competition__category competition__category--active">' + tasks.Data[i].task_category + '</div>';
                } else {
                    var str = '<div name="' + tasks.Data[i].task_category.toLowerCase() + '" onclick="competition.changeCategory(\'' + tasks.Data[i].task_category.toLowerCase() + '\')"  class="competition__category">' + tasks.Data[i].task_category + '</div>';
                }

                categoiesContainer.innerHTML += str;
                categories[categories.length] = tasks.Data[i].task_category; //добавляем элемент в массив категорий
            }
        }

        addCategoryContainer(tasks);

        var str = "";
        for (var i = 0; i < tasks.Data.length; i++) {


            if (tasks.Data[i].close) {
                str = '<div class="competition__one-task competition__one-task--done" id="one-task-container-' + tasks.Data[i].id_task + '">';
            } else {
                str = '<div class="competition__one-task" id="one-task-container-' + tasks.Data[i].id_task + '">';
            }

            str += '<div class="competition__task-name">' + tasks.Data[i].task_name + '<br>' +
                tasks.Data[i].task_point + '<br><a href="' + tasks.Data[i].task_link + '">link</a></div>';
            str += '<div class="competition__form-container"><div class="competition__task-description">' + tasks.Data[i].task_description + '</div>';
            str += '<div onsubmit="submitTask(' + tasks.Data[i].id_task + ');" class="competition__tasks-form" action="">';

            if (tasks.Data[i].close) {
                str += '<div class="competition__task-flag-input" ><input style="display: none;" type="text">';
                str += '<div class="competition__task-flag-input-done">Решено</div></div>';
            } else {
                str += '<div class="competition__task-flag-input"><input class="competition__task-field" type="text" id="task-input-' + tasks.Data[i].id_task + '">';
                str += '<div class="competition__task-flag-input-done" style="display: none;" id="task-input-stub-' + tasks.Data[i].id_task + '">Решено</div></div>';
            }

            if (!tasks.Data[i].close) {
                str += '<button class="competition__task-submit-button" id="task-submit-button-' + tasks.Data[i].id_task + '" onclick="submitTask(' + tasks.Data[i].id_task + ')">Отправить</button></div></div></div>';
            }

            if (document.getElementById(tasks.Data[i].task_category.toLowerCase() + "-tasks-container")) {

                document.getElementById(tasks.Data[i].task_category.toLowerCase() + "-tasks-container").innerHTML += str;

            }
        }
    };

    xhr.onerror = function () {
        console.log('error ' + this.status);
    };
}

function submitTask(taskId) {
    console.log(this);
    var flag = $("#task-input-" + taskId).val();

    var obj = {
        Task_id: taskId,
        Task_flag: flag,
        UUID: $.cookie('UUID'),
        id_event: id_event
    };

    var data = JSON.stringify(obj);

    var str = 'http://192.168.0.7:' + port + '/task?param=check&data=' + data;
    console.log(str);
    var xhr = createCORSRequest('GET', str);
    xhr.send();
    xhr.onload = function () {
        data = $.parseJSON(this.responseText);
        console.log(data);


        if (data.Answer.toLowerCase() === "success") {
            $("#one-task-container-" + taskId).addClass("competition__one-task--done");
            $("#task-input-" + taskId).hide();
            $("#task-input-stub-" + taskId).show();
            $("#task-submit-button-" + taskId).hide();
        } else {
            $("#task-input-" + taskId).addClass('competition__task-field--wrong');
            setTimeout(function(){
                $("#task-input-" + taskId).removeClass('competition__task-field--wrong');
            }, 2000);
        }
    };

    xhr.onerror = function () {
        console.log("Проблемы с запросом");
    };
}

function closeDescription() {
    $(".task-description").remove();
}

function openTask(task) {
    for (i = 0; i < competition.Data.length; i++) {
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
