var timeout;

function logout() {
    window.location.href = urlLogout;
}

function resetTimer() {
    clearTimeout(timeout);
    timeout = setTimeout(logout, 3600000);
}

window.onload = resetTimer;
document.onclick = resetTimer;