var port = '13451';
//var port = '8000';

/*var username = "";*/

function User() {
    this.username = "";
}

User.prototype.setUsername = function (username) {
  this.username = username;
};

User.prototype.writeUsername = function () {
    var usernameElements = document.getElementsByClassName("header__element--name");

    [].forEach.call(usernameElements, function(element) {
        element.innerHTML = user.username;
    });
};

function logout() {
    deleteCookie('UUID');
    $(location).attr('href', "/login");
}

// /auth?param=get_user_name&data={"UUID":"0fc1d179-1b23-47dc-b83a-b3270b544c3d"}
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

function maybeScroll () {
    if ($(".maybescroll").outerHeight() > 399 && $(window).width() > '1500') {
        $(".maybescroll").addClass("container-scroll-y");
    } else {
        if ($(".maybescroll").outerHeight() > 199){
            $(".maybescroll").addClass("container-scroll-y");
        };
    }
}

function setUsername() {
    var obj = {
        UUID: $.cookie('UUID')
    };

    var strObj = JSON.stringify(obj);

    var str = 'http://90.189.132.25:'  + port +  '/auth?param=get_user_name&data=' + strObj;
    console.log(str);

    var xhr = createCORSRequest('GET', str);
    xhr.send();

    xhr.onload = function () {
        console.log(this.responseText);
        var data = $.parseJSON(this.responseText);

        console.log(data.Answer);

        if (data.Answer === 'Success') {
            console.log('main success');
            var username = data.Data.name;
            //console.log("asda");
            console.log(username);
            if (username != "") {
                console.log(username);

                user.setUsername(username);
                user.writeUsername();
                
            }

        } else {
            //return false;
        }


    };


    //return username();
}

var user = new User();

var isName = 0;
var timerId = setInterval(function() {
    if (isName != 0) {
        alert ("okey");
    }
}, 2000);



var username = setUsername();
console.log(username);

$(document).ready(function () {
    if ($.cookie('UUID') != null) {
        //setUsername();
    }
    maybeScroll ();

    /*$("#account-info-switch").click(function () {
        //$(".header__account-info-container").classList;
        document.getElementById("header-account-info-container").classList.toggle("disabled-block");
        //console.log(document.getElementById("header-account-info-container"));

        console.log("switch");
    });*/

});
