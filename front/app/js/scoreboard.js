var tasks;

function getScoreboard() {
    var xhr = createCORSRequest('GET', 'http://87.103.243.110:13451/scoreboard');
    xhr.send();
    xhr.onload = function () {
        data = $.parseJSON(this.responseText);
        for (i = 0; i < data.data.length / 2; i++) {
            var str = "<tr><td>" + (i + 1) + ")</td><td>" + String(data.data[i].Login) + "</td><td>" + String(data.data[i].point) + "</td></tr>";
            $("#scoreboard-first-table").append(str);
        }

        for (i = data.data.length / 2; i < data.data.length; i++) {
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
