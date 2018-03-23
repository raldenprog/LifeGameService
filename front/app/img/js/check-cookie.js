if ($.cookie('UUID') === null && !$("div").is(".authorization")) {
    $(location).attr('href', "login.html");
}