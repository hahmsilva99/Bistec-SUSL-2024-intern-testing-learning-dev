document.getElementById('send-button').addEventListener('click', function() {
    const inputText = document.getElementById('input-text').value;
    if (inputText.trim() === "") return;

    // Send skill or query to backend
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: inputText }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.candidates && data.candidates.length > 0) {
            // Populate candidate dropdown
            const selectElement = document.getElementById('candidate-select');
            selectElement.innerHTML = '';
            data.candidates.forEach(function(candidate) {
                const option = document.createElement('option');
                option.value = candidate;
                option.textContent = candidate;
                selectElement.appendChild(option);
            });
            document.getElementById('candidate-dropdown').style.display = 'block';
        } else {
            addBotMessage(data.response);
        }
    });
});

document.getElementById('details-button').addEventListener('click', function() {
    const selectedCandidate = document.getElementById('candidate-select').value;
    const selectedDetail = document.getElementById('details-select').value;

    // Fetch details of the selected candidate
    fetch('/details', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ candidate: selectedCandidate, detail: selectedDetail }),
    })
    .then(response => response.json())
    .then(data => {
        addBotMessage(data.response);
    });
});

function addBotMessage(message) {
    const botMessage = document.createElement('div');
    botMessage.className = 'message bot-message';
    botMessage.textContent = message;
    document.getElementById('chat-output').appendChild(botMessage);
    document.querySelector('.chat-window').scrollTop = document.querySelector('.chat-window').scrollHeight;
}
