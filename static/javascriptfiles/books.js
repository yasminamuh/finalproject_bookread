
const logoutbutton= document.getElementById("logout");
const content= document.getElementById("content");
const New_admin= document.getElementById("addnewadmin");

const toread_button= document.getElementById("gotoread");
 const forbuttons= document.getElementById("forbuttons");

fetch('/api/data')
.then(response => response.json())
.then(data =>
{
    let admin= data["is_admin"];
    let user= data["user"];
    if (admin == true){
        const addbutton=document.createElement("button");
        // const editbookbutton= document.createElement("button");
        // const deletebookbutton=document.createElement("button");
        addbutton.innerText="Add a new book"
        forbuttons.appendChild(addbutton)
        addbutton.addEventListener("click", () => {
            window.location="/add_book";
        });
        const addadmin= document.createElement("button");
        addadmin.innerText="Add new admin"
        New_admin.appendChild(addadmin)
        addadmin.addEventListener("click", () => {
            window.location="/newadmin";
        });

    }

    if (user == null){
        logoutbutton.style.display="none";
        toread_button.style.display="none";
        const login=document.createElement("button");
        login.innerText="Login"
        const signup=document.createElement("button");
        signup.innerText="Sign up"
        forbuttons.appendChild(login)
        forbuttons.appendChild(signup)
        login.addEventListener("click", () => {
            window.location="/login";
        });
        signup.addEventListener("click", () => {
            window.location="/signup";
        });



    }
    // else {
    //     logoutbutton.style.display="inline_block";
    // }

}
)




logoutbutton.addEventListener("click", () => {
    localStorage.clear();
    window.location="/logout";
});
varo=localStorage.getItem("user name:");
if (varo!=null){
    content.innerText="welcome "+ varo;
}
else{ content.innerText="welcome "}

const divvat= document.getElementsByClassName("ji");
const namess=document.getElementsByClassName("d1");
const authorss=document.getElementsByClassName("d2");

for (let i=0;i<divvat.length;i++)
{
    divvat[i].addEventListener("click",()=>{
        let namevalue= namess[i].innerText;
        let authorvalue=authorss[i].innerText;
        window.location="/books/details/" + namevalue + "/" + authorvalue;

    })
}
