document.getElementById('send-button').addEventListener('click', function() {
    const inputText = document.getElementById('input-text').value;
    if (inputText.trim() === "") return;

    // Display user message
    const userMessage = document.createElement('div');
    userMessage.className = 'message user-message';
    userMessage.textContent = inputText;
    document.getElementById('chat-output').appendChild(userMessage);

    // Send to backend and display bot response
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: inputText }),
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement('div');
        botMessage.className = 'message bot-message';
        botMessage.textContent = data.response;
        document.getElementById('chat-output').appendChild(botMessage);
        
        // Scroll to the latest message
        document.querySelector('.chat-window').scrollTop = document.querySelector('.chat-window').scrollHeight;
    });

    // Clear the input field
    document.getElementById('input-text').value = '';
});
