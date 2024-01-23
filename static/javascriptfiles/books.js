const addbook_button= document.getElementById("addabook");

const logoutbutton= document.getElementById("logout");

const toread_button= document.getElementById("gotoread");


fetch('/api/data')
.then(response => response.json())
.then(data =>
{
    let admin= data["is admin"];
    let user= data["user"];
    if (admin == false){
        addbook_button.style.display= "none";
    }
    else {
        addbook_button.style.display= "inline_block";
    }
    if (user == null){
        logoutbutton.style.display="none";
        addbook_button.style.display= "none";
        toread_button.style.display="none";

    }
    else {
        logoutbutton.style.display="inline_block";
    }

}
)




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

