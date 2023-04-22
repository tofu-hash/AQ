function showNotification(text) {
    let notification = document.getElementById('notification');
    let n_text = document.getElementById('notification-text');

    n_text.innerHTML = text;

    notification.style.left = '30px';
}

function closeNotification() {
    let notification = document.getElementById('notification');
    let n_text = document.getElementById('notification-text');

    n_text.innerHTML = '';

    notification.style.left = '-500px';
}
