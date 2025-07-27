document.querySelectorAll('.subtask-circle').forEach(circle => {
    circle.addEventListener('click', function () {
        const subtaskId = this.dataset.id;
        fetch(`/subtasks/${subtaskId}/toggle/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCSRFToken(),
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.completed) {
                this.classList.add('checked');
            } else {
                this.classList.remove('checked');
            }
        });
    });
});

function getCSRFToken() {
    const name = 'csrftoken=';
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookies = decodedCookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let c = cookies[i].trim();
        if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
    }
    return '';
}
