const logoutbutton= document.getElementById("logout");

logoutbutton.addEventListener("click", () => {
    localStorage.clear();
    window.location="/logout";
});
const content= document.getElementById("content");
varo=localStorage.getItem("user name:");
if (varo!=null){
    content.innerText="welcome "+ varo;
}
else{ content.innerText="welcome "}

