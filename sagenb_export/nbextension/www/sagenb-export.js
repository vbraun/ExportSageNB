'use strict';

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
    xhttp.send(uniqueId);
};
