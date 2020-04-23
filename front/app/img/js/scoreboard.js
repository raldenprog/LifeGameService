var tasks;

function getScoreboard(id_event) {

    var obj = {
      id_event: id_event
    };

    var str = JSON.stringify(obj);

    var str = 'http://188.227.86.21:13451/scoreboard?data=' + str;

    console.log(str);


    var xhr = createCORSRequest('GET', str);
    xhr.send();

    xhr.onload = function () {
        console.log(this.responseText);

        var scores = $.parseJSON(this.responseText);

        if (scores.Answer === 'Success') {
            console.log(scores);

            for (var i = 0; i < scores.Data.length; i++) {
                var str = '<tr>\n' +
                    '<td><div class="scoreboard__table-cell scoreboard__table-cell--border-right">' + (i+1) + '</div></td>' +
                    '<td><div class="scoreboard__table-cell scoreboard__table-cell--border-right">' + scores.Data[i].name + '</div></td>' +
                    '<td><div class="scoreboard__table-cell">crypto</div></td>' +
                    '<td><div class="scoreboard__table-cell">joy</div></td>' +
                    '<td><div class="scoreboard__table-cell">ppc</div></td>' +
                    '<td><div class="scoreboard__table-cell">recon</div></td>' +
                    '<td><div class="scoreboard__table-cell">stego</div></td>' +
                    '<td><div class="scoreboard__table-cell">web</div></td>' +
                    '<td><div class="scoreboard__table-cell scoreboard__table-cell--result">' + scores.Data[i].point + '</div></td></tr>';
                document.getElementById('scoreboard-table').innerHTML += str;
            }
        } else {
            alert('load score failed');
        }

    };

    xhr.onerror = function () {
        console.log('error ' + this.status);
    }
}