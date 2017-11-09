function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr) {
        xhr.open(method, url, true);
    } else if (typeof XDomainRequest != "undefined") {
        xhr = new XDomainRequest();
        xhr.open(method, url);
    } else {
        xhr = null;
    }
    return xhr;
}

function setJson(action, path) {
    var data = JSON.stringify({Data: action});
    var xhr = createCORSRequest('POST', path);
    xhr.setRequestHeader(
        'X-Custom-Header', 'value');
    xhr.setRequestHeader(
        'Content-Type', 'application/json; charset=utf-8');
    xhr.setRequestHeader(
        'Access-Control-Allow-Origin', '*');
    xhr.send(data);

    xhr.onload = function () {
        alert(this.responseText);
        return(this.responseText);
    }

    xhr.onerror = function () {
        alert('error ' + this.status);
        return(this.status);
    }
}