function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    const chatbox = document.getElementById('chatbox');

    // Display user message with timestamp
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'user-message';
    userMessageDiv.innerHTML = `You: ${userInput} <span class="timestamp">(${new Date().toLocaleTimeString()})</span>`;
    chatbox.appendChild(userMessageDiv);
    
    document.getElementById('userInput').value = '';

    // Send message to the server
    fetch('/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot response with timestamp
        const botMessageDiv = document.createElement('div');
        botMessageDiv.className = 'bot-message';
        botMessageDiv.innerHTML = `Bot: ${data.response} <span class="timestamp">(${new Date().toLocaleTimeString()})</span>`;
        chatbox.appendChild(botMessageDiv);
        
        chatbox.scrollTop = chatbox.scrollHeight; // Scroll to the bottom
    });
}