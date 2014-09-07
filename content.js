showHide();

function showHide() {
    var el = document.getElementById("watch-discussion");
    if( el && el.style.display == 'none')
        el.style.display = 'block';
    else if( el )
        el.style.display = 'none';
}
