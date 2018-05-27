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
        console.log("done typing");
        let focused = document.activeElement
        // let myValue = document.querySelector('input').value;

        var data = JSON.stringify({
            "time": 3234234,
            "text": "fhdkfhsdkfj"
          });
          
          var xhr = new XMLHttpRequest();
        //   xhr.withCredentials = true;
          
          xhr.addEventListener("readystatechange", function () {
            if (this.readyState === 4) {
              console.log(this.responseText);
            }
          });
          
          xhr.open("POST", "http://192.34.78.218/api/inputUserData");
          xhr.setRequestHeader("Content-Type", "application/json");
        //   xhr.setRequestHeader("Cache-Control", "no-cache");
        //   xhr.setRequestHeader("Postman-Token", "b32a78ce-5b83-5703-da70-06e30913a7ac");
          
          xhr.send(data);

        // var request = makeHttpObject();
        // request.open('POST', 'https://192.34.78.218/api/inputUserData', false);
        // request.send(JSON.stringify({}));
        // print(request.responseText);
      }
    
    var el = document.getElementById("comments");
    if( el && el.style.display == 'none')
        el.style.display = 'block';
    else if( el )
        el.style.display = 'none';
}