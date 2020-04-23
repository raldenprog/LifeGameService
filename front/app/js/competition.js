function writeCompetitionName(id) {
    var obj = {
        id_event: id
    };

    var strObj = JSON.stringify(obj);

    var str = 'http://188.227.86.21:' + port + '/event?param=info_event&data=' + strObj;

    console.log(str);


    var xhr = createCORSRequest('GET', str);
    xhr.send();

    xhr.onload = function () {
        var data = $.parseJSON(this.responseText);
        var competitionName = data.Data.name;
        console.log(competitionName);
        var competitionNameElements = document.getElementsByClassName('js-competition-set-name');
        console.log(competitionNameElements);
        [].forEach.call(competitionNameElements, function(element) {
            element.innerHTML = competitionName;
        });
    };
}