showHide();

function showHide() {
    window.addEventListener("keyup", () => {
        console.log("listening")
    })


    
    var el = document.getElementById("comments");
    if( el && el.style.display == 'none')
        el.style.display = 'block';
    else if( el )
        el.style.display = 'none';
}
