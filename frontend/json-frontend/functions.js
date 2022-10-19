function makeGETRequest(url, cb) {
    if (!url) throw 'No GET url!';

    httpRequest = new XMLHttpRequest();
    if (!httpRequest) {
        alert('Ошибка!');
        console.log('Cannot create an XMLHTTP instance');
        return false;
    }
    httpRequest.withCredentials = true;
    httpRequest.onreadystatechange = () => {
        alertStatus(cb);
    };
    httpRequest.open('GET', url);
    httpRequest.send();
}

function makePOSTRequest(url, data, cb) {

    if (!url) throw 'No POST url!';
    if (!data) throw 'No data!';

    httpRequest = new XMLHttpRequest();
    if (!httpRequest) throw 'Cannot create an XMLHTTP instance'


    httpRequest.withCredentials = true;
    httpRequest.onreadystatechange = () => {
        alertStatus(cb);
    };
    httpRequest.open('POST', url);
    httpRequest.setRequestHeader('Content-Type', 'application/json');
    httpRequest.send(JSON.stringify(data));
}

function alertStatus(cb) {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
        if (httpRequest.status === 200) {
            if (cb) cb('success');
        } else {
            alert('Ошибка!');
            if (cb) cb('error');
        }
    }
}

function removeCookie(name) {
    document.cookie = name + '=; Max-Age=0;';
}

function logout(e) {
    e.preventDefault();
    removeCookie('sessionid');
    makeGETRequest('login.html', () => {
        window.location = 'login.html';
    });
}

window.makeGETRequest = makeGETRequest;
window.makePOSTRequest = makePOSTRequest;
