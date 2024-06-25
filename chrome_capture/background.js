chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log('Received message:', request);
    if (request.type && request.message) {
      fetch('http://localhost:8000/log', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          type: request.type,
          message: request.message,
          timestamp: request.timestamp
        })
      }).then(response => {
        if (response.ok) {
          console.log('Log sent to server successfully.');
        } else {
          console.error('Error sending log to server:', response.statusText);
        }
      }).catch(error => console.error('Error sending log to server:', error));
    }
    sendResponse({ status: 'success' });
  });
  