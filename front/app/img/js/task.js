var tasks;
var id_event;

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

    this.activeCategory = category.toLowerCase()
};


var competition = new Competition();

function getTasks(competitionId) {
    id_event = competitionId;

    var categories = new Array();
    var active;

    var obj = {
        id_event: id_event,
        UUID: $.cookie('UUID')
    };

    var data = JSON.stringify(obj);

    var str = 'http://90.189.168.29:13451/task?data=' + data;
    var xhr = createCORSRequest('GET', str);

    xhr.send();
    xhr.onload = function () {
        tasks = $.parseJSON(this.responseText);

        console.log("answer");
        console.log(tasks);
        console.log(tasks.Data.length);

        var categoiesContainer = document.getElementById("tasks-category-container");


        for (var i = 0; i < tasks.Data.length; i++) {

            var alreadyExists = false;

            for (var j = 0; j < categories.length; j++) {
                if (tasks.Data[i].task_category === categories[j]) {
                    alreadyExists = true;
                    break;
                }
            }

            if (!alreadyExists) {
                var str = '<div name="' + tasks.Data[i].task_category.toLowerCase() + '" onclick="competition.changeCategory(\'' + tasks.Data[i].task_category.toLowerCase() + '\')"  class="competition__category">' + tasks.Data[i].task_category + '</div>';

                categoiesContainer.innerHTML += str;
                categories[categories.length] = tasks.Data[i].task_category;
            }
        }

        console.log($("[active-category=true]"));
        console.log($("#tasks-category-container").attr("class"));

        console.log($("[active-category=true]").attr("category-name"));
        var active = $("[active-category=true]").attr("category-name");


        competition.activeCategory = tasks.Data[0].task_category;
        competition.categoryArray = new Array();



       /*
       // Здесь будут добавляться контейнеры под категории

        var str = "";
        for (var i = 0; i < tasks.Data.length; i++) {
            //Добавление контейнера, если такой категории нет
            if (competition.categoryArray.indexOf(tasks.Data[i].task_category) === -1) {
                competition.categoryArray[competition.categoryArray.length] = tasks.Data[i].task_category;


                if (tasks.Data[i].task_category === competition.activeCategory) {
                    str += '<div id="' + tasks.Data[i].task_category + '-list-container"></div>';
                } else {
                    str += '<div id="' + tasks.Data[i].task_category + '-list-container" style="display: none;"></div>';
                }
            }
        }
        document.getElementById('tasks-container').innerHTML += str;
*/

        var str = "";
        for (var i = 0; i < tasks.Data.length; i++) {


            if (tasks.Data[i].close) {
                str = '<div class="competition__one-task competition__one-task--done">';
            } else {
                str = '<div class="competition__one-task">';
            }

            str += '<div class="competition__task-name">' + tasks.Data[i].task_name + '</div>';
            str += '<div class="competition__form-container"><div class="competition__task-description">' + tasks.Data[i].task_description + '</div>';
            str += '<div onsubmit="submitTask(' + tasks.Data[i].id_task + ');" class="competition__tasks-form" action="">';

            if (tasks.Data[i].close) {
                str += '<div class="competition__task-flag-input" ><input style="display: none;" type="text">';
                str += '<div class="competition__task-flag-input-done">Решено</div></div>';
            } else {
                str += '<div class="competition__task-flag-input"><input type="text" id="task-input-' + tasks.Data[i].id_task + '">';
                str += '<div class="competition__task-flag-input-done" style="display: none;">Решено</div></div>';
            }

            str += '<button class="competition__task-submit-button" onclick="submitTask(' + tasks.Data[i].id_task + ')">Отправить</button></div></div></div>';

            document.getElementById(tasks.Data[i].task_category.toLowerCase() + "-tasks-container").innerHTML += str;
        }
    };

    xhr.onerror = function () {
        console.log('error ' + this.status);
    };
}

function submitTask(taskId) {

    var flag = $("#task-input-" + taskId).val();

    var obj = {
        Task_id: taskId,
        Task_flag: flag,
        UUID: $.cookie('UUID'),
        id_event: id_event
    };

    var data = JSON.stringify(obj);

    var str = 'http://90.189.168.29:13451/task?param=check&data=' + data;
    console.log(str);
    var xhr = createCORSRequest('GET', str);
    xhr.send();
    xhr.onload = function () {
        data = $.parseJSON(this.responseText);
        if (data.Data) {
            console.log("Флаг правильный");
            location.reload();
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
