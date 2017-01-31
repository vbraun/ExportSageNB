'use strict';


function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


var exportSageNB = function(uniqueId) {
    console.log('Converting ' + uniqueId);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            document.location = 'http://' + document.location.host + xhttp.responseText;
        } else {
            document.querySelector('.error').innerText = xhttp.responseText;
        }
    };
    xhttp.open('POST', '/sagenb/export', true);
    xhttp.setRequestHeader('X-Xsrftoken', getCookie("_xsrf"));
    xhttp.send(uniqueId);
};
