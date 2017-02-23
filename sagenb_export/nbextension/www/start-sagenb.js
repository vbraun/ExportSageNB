'use strict';


var startSageNB = function() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var url = xhttp.responseText;

            window.location.replace(url);
        } else {
            document.querySelector('.error').innerText = xhttp.responseText;
        }
    };
    xhttp.open('GET', '/sagenb/start', false);
    xhttp.send();
};
