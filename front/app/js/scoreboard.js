var tasks;

function getScoreboard() {
    var xhr = createCORSRequest('GET', 'http://90.189.132.25:13451/scoreboard');
    xhr.send();
    xhr.onload = function () {
        data = $.parseJSON(this.responseText);

        for (var i = 0; i < Math.ceil(data.data.length / 2); i++) {
            var str = "<tr><td>" + (i + 1) + ")</td><td>" + String(data.data[i].Login) + "</td><td>" + String(data.data[i].point) + "</td></tr>";
            $("#scoreboard-first-table").append(str);
        }

        for (var i = Math.ceil(i = data.data.length / 2); i < data.data.length; i++) {
            var str = "<tr><td>" + (i + 1) + ")</td><td>" + String(data.data[i].Login) + "</td><td>" + String(data.data[i].point) + "</td></tr>";
            $("#scoreboard-second-table").append(str);
        }
    }

    xhr.onerror = function () {
        //console.log('error ' + this.status);
    }
}

$(document).ready(function () {
    getScoreboard();
});
