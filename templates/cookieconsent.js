// static/js/cookieconsent.js
function acceptCookies() {
    document.getElementById('cookieConsent').style.display = 'none';
    localStorage.setItem('cookiesAccepted', 'true');
}

window.onload = function() {
    if (!localStorage.getItem('cookiesAccepted')) {
        document.getElementById('cookieConsent').style.display = 'block';
    }
}

