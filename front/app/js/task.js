function getTasks() {
    str = "http://90.189.132.25:13451/task?session=" + $.cookie('UUID');
    var xhr = createCORSRequest('GET', str);
    xhr.send();
    xhr.onload = function () {
        tasks = $.parseJSON(this.responseText);
        console.log(this.responseText);

        for (i = 0; i < tasks.Data.length; i++) {
            //data.Data[i].Task_hint  если пустой, то не выводить
            //data.Data[i].Task_description
            //data.Data[i].Task_name
            //data.Data[i].Task_link  если null то не выводить на экран
            //data.Data[i].Close      сдан таск или нет
            //data.Data[i].Task_category
            //data.Data[i].Task_point
            //data.Data[i].Task_point

            //console.log(tasks.Data[i].Task_category);
            //console.log("____");
            var str = '<a href="#" class="tasks__link';
            if (tasks.Data[i].Close === true) {
                str = str + ' tasks__link--done'
            }
            str = str + '" id="' + tasks.Data[i].Task_name + '" onclick="openTask(\'' + String(tasks.Data[i].Task_name) + '\')">' + tasks.Data[i].Task_point + '</a>';

            category = '#' + tasks.Data[i].Task_category;
            $(category).append(str);
        }
    }

    xhr.onerror = function () {
        //console.log('error ' + this.status);
    }
}

function submitTask(task) {
    var str = 'http://90.189.132.25:13451/task?session=' + $.cookie('UUID') + '&Task_name=' + task + '&Task_flag=' + $("#flag").val();
    var xhr = createCORSRequest('GET', str);
    xhr.send();
    xhr.onload = function () {
        data = $.parseJSON(this.responseText);
        if (data.Data) {
            location.reload();
        } else { alert("Неправильный флаг"); }
    }

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
    getTasks();
});
