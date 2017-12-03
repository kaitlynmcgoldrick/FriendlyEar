showHide();

function showHide() {
    var el = document.getElementById("comments");
    if( el && el.style.display == 'none')
        el.style.display = 'block';
    else if( el )
        el.style.display = 'none';
}
