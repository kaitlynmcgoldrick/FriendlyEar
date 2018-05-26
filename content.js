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
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'https://192.34.78.218/api/inputUserData', true);
        // xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        // xhr.onreadystatechange = handler;
        xhr.send(JSON.stringify({
            "time": 3234234,
            "text": "fhdkfhsdkfj"
        })); 
        console.log(focused.value);

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