function logout() {
    deleteCookie('UUID');
    $(location).attr('href', "/login");
}


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

$(document).ready(function () {
    if ($.cookie('UUID') != null) {

    }
    maybeScroll ();

    $("#account-info-switch").click(function () {
        //$(".header__account-info-container").classList;
        document.getElementById("header-account-info-container").classList.toggle("disabled-block");
        //console.log(document.getElementById("header-account-info-container"));

        console.log("switch");
    });

});
