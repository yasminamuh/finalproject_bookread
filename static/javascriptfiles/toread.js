const logoutbutton= document.getElementById("logout2");

logoutbutton.addEventListener("click", () => {
    localStorage.clear();
    window.location="/logout";
});