function writeCompetitionInfo(id) {
    var obj = {
        id_event: id
    };

    var strObj = JSON.stringify(obj);

    if (typeof(port) == "undefined") {
        var port = "13451";
    }

    var str = 'http://192.168.1.3:' + port + '/event?param=descr&data=' + strObj;

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