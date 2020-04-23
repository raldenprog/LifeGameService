function writeCompetitionInfo(id) {
    var obj = {
        id_event: id
    };

    var strObj = JSON.stringify(obj);

    var str = 'http://188.227.86.21:' + port + '/event?param=descr&data=' + strObj;

    console.log(str);


    var xhr = createCORSRequest('GET', str);
    xhr.send();

    xhr.onload = function () {
        var data = $.parseJSON(this.responseText);
        console.log(data);
        var description = data.Data[0].description;
        var name = data.Data[0].name;

        document.getElementById("competition-name").innerHTML = name;
        document.getElementById("competition-description").innerHTML = description;
        //var competitionName = data.Data.name;

    };
}