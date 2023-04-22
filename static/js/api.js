async function createUser() {
    let name = document.getElementById('name-register').value;
    let password = document.getElementById('password-register').value;

    let response = await fetch('/api/v1/accounts/register/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'username': name,
            'password': password
        })
    });
    let status = response.status;
    let result = await response.json();

    if (status === 201) {
        window.location.href = '/accounts/login/';
    } else {
        let responseMessage = '';
        for (let item in result) {
            responseMessage += result[item][0] + ' (' + item + ')<br>';
        }
        showNotification(responseMessage);
    }
}


async function loginUser() {
    let name = document.getElementById('name-login').value;
    let password = document.getElementById('password-login').value;

    let response = await fetch('/api/v1/accounts/login/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'username': name,
            'password': password
        })
    });
    let status = response.status;
    let result = await response.json();

    if (status === 200) {
        window.location.href = '/profile/';
    } else {
        showNotification(result['message']);
    }
}


async function logoutUser() {
    let response = await fetch('/api/v1/accounts/logout/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    });
    let status = response.status;
    let result = await response.json();

    if (status === 200) {
        window.location.href = '/';
    } else {
        showNotification(result['message']);
    }
}


async function createQuestion() {
    let title = document.getElementById('title').value;
    let description = document.getElementById('description').value;
    let themes = document.getElementById('themes').value;

    let response = await fetch('/api/v1/questions/create/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'title': title,
            'description': description,
            'themes': themes
        })
    });
    let status = response.status;
    let result = await response.json();

    if (status === 201) {
        window.location.href = '/profile/';
    } else {
        let responseMessage = '';
        for (let item in result) {
            responseMessage += result[item][0] + ' (' + item + ')<br>';
        }
        showNotification(responseMessage);
    }
}


async function getCurrentUserQuestions() {
    let response = await fetch('/api/v1/questions/current/get/', {
        method: 'GET'
    });
    let status = response.status;
    let result = await response.json();

    if (status === 201) {

    } else {
        let responseMessage = '';
        for (let item in result) {
            responseMessage += result[item][0] + ' (' + item + ')<br>';
        }
        showNotification(responseMessage);
    }
}
