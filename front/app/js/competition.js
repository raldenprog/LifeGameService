function writeCompetitionName(id) {
    var obj = {
        id_event: id
    };

    var strObj = JSON.stringify(obj);

    if (typeof(port) == "undefined") {
        var port = "13451";
    }

    var str = 'http://217.23.13.145:' + port + '/event?param=info_event&data=' + strObj;

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