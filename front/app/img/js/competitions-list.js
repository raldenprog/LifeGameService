var select_event_id = -1;

function selectCompetition(id) {
    select_event_id = id;

    $('#select-registration-type-popup').show();
}

function regForCompetition(official) {

    var obj = {
        UUID: $.cookie('UUID'),
        id_event: select_event_id,
        official: official
    };
    var strObj = JSON.stringify(obj);

    var str = 'http://217.23.13.145:13451/event?param=reg_user&data=' + strObj;
    var xhr = createCORSRequest('GET', str);
    xhr.send();

    xhr.onload = function () {
        data = $.parseJSON(this.responseText);
        console.log(data);

        if (data.Answer.toLowerCase() === 'success') {
            console.log("yes success");
            $(location).attr('href', '/competition/' + select_event_id + '/info/');
        }
    };

    xhr.onerror = function () {
        console.log(str);
    };
}

function closePopup(id) {
    $('#' + id).hide();
}

$(document).ready(function () {
    var obj = {
        Name: 'Mostevent',
        Page: 0
    };

    var strObj = JSON.stringify(obj);

    var str = 'http://217.23.13.145:13451/event?data=' + strObj;
    var xhr = createCORSRequest('GET', str);
    xhr.send();

    console.log(str);

    xhr.onload = function () {
        data = $.parseJSON(this.responseText);

        var id_event = 7;

        if (data.Answer === 'Success') {
            for (var i = 0; i < data.Data.length; i++) {
                var str = '<tr><td><div class="competitions__table-cell-block"><div>' + data.Data[i].name + '</div></div></td>';
                str += '<td><div class="competitions__table-cell-block"><div>хз, кто авторы</div></div></td>';
                str += '<td><div class="competitions__table-cell-block"><div>' + data.Data[i].date_start + '</div></div></td>';
                str += '<td><div class="competitions__table-cell-block"><div>' + data.Data[i].date_end + '</div></div></td>';
                str += '<td><div class="competitions__table-cell-block"><div>Длительность</div></div></td>';


                if (data.Data[i].status === 1) {
                    str += '<td><div class="competitions__table-cell-block competitions__table-cell-block--transparent"><div><button class="competitions__button" onclick="selectCompetition(' + id_event + ');">принять участие</button></div></div></td>';
                } else {
                    str += '<td><div class="competitions__table-cell-block competitions__table-cell-block--transparent"><div><button class="competitions__button competitions__button--no-active" onclick="selectCompetition(' + id_event + ');">принять участие</button></div></div></td>';
                }

                str += '<td><div class="competitions__table-cell-block"><div><a href="/competition/7/rating" class="competitions__button">Просмотр</a></div></div></td>';
                str += '<td><div class="competitions__table-cell-block"><div>' + 50 + '</div></div></td>';


                document.getElementById('competitions-table').innerHTML += str;
            }

            str += '<tr><td><div class="table-default__last-cell-block"><div></div></div>' +
                '</td><td><div class="table-default__last-cell-block"><div></div></div></td><td>' +
                '<div class="table-default__last-cell-block"><div></div></div></td><td></td><td>' +
                '<div class="table-default__last-cell-block"><div></div></div></td><td></td><td>' +
                '<div class="table-default__last-cell-block"><div></div></div></td><td>' +
                '<div class="table-default__last-cell-block"><div></div></div></td></tr>';


            document.getElementById('competitions-table').innerHTML += str;


        } else { alert('Произошла ошибка');}

    };

    xhr.onerror = function () {
        console.log(str);
    };

    //$(location).attr('href', "login.html");

    $("#logout-link").click(function () {
        logout();
    });
});

