function saveScrollPosition() {
    sessionStorage.setItem('scrollPosition', window.pageYOffset);
}

function restoreScrollPosition() {
    var scrollPosition = sessionStorage.getItem('scrollPosition');
    if (scrollPosition !== null) {
        window.scrollTo(0, scrollPosition);
        sessionStorage.removeItem('scrollPosition');
    }
}
window.addEventListener('beforeunload', saveScrollPosition);
window.addEventListener('load', restoreScrollPosition);
