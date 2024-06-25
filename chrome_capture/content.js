function sendToBackground( message, type) {
    console.log("Sent to background")
    chrome.runtime.sendMessage({
      type: type,
      message: message,
      timestamp: new Date().toISOString()
    });
  }    

document.addEventListener('click', (event) => {
  console.log(`Element clicked: ${event.target}`);
  sendToBackground("click",`${event.target}`);
});


document.addEventListener('submit', (event) => {
  console.log(`Form submitted: ${event.target}`);
  sendToBackground("submit", `${event.target}`);
  
});

console.log(`Page visited: ${window.location.href}`);
sendToBackground("access", `${window.location.href}`);