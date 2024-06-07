document.addEventListener('DOMContentLoaded', function() {
          const chatForm = document.getElementById('message-form');
          const userInput = document.getElementById('user-input');
          const chatBox = document.getElementById('chat-box');
      
          chatForm.addEventListener('submit', function(event) {
              event.preventDefault();
              
              const message = userInput.value.trim();
              if (!message) return;
      
              appendMessage('user', message);
              sendMessageToBot(message);
              userInput.value = '';
          });
      
          function appendMessage(sender, message) {
              const messageElement = document.createElement('div');
              messageElement.classList.add('message', sender);
              messageElement.innerText = message;
              chatBox.appendChild(messageElement);
              chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
          }
      
          async function sendMessageToBot(message) {
              try {
                  const response = await fetch('http://localhost:5005/webhooks/rest/webhook', {
                      method: 'POST',
                      headers: {
                          'Content-Type': 'application/json'
                      },
                      body: JSON.stringify({
                          message: message
                      })
                  });
                  
                  const responseData = await response.json();
                  if (responseData && responseData.length > 0) {
                      const botMessage = responseData[0].text;
                      appendMessage('bot', botMessage);
                  }
              } catch (error) {
                  console.error('Error sending message to bot:', error);
              }
          }
      });