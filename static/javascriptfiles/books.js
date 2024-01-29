const content= document.getElementById("content");
const New_admin= document.getElementById("addnewadmin");
const toread_button= document.getElementById("gotoread");
const forbuttons= document.getElementById("forbuttons");
// reading temp json data to check if there is a user and if its admin or not!!
fetch('/api/data')
.then(response => response.json())
.then(data =>
{
    let admin= data["is_admin"];
    let user= data["user"];
    //when the user is admin, create add a new book button and create new admin button
    if (admin == true){
        const addbutton=document.createElement("button");
        addbutton.id="addabook"
        addbutton.innerText="Add a new book"
        forbuttons.appendChild(addbutton)
        addbutton.addEventListener("click", () => {
            window.location="/add_book";
        });
        const addadmin= document.createElement("button");
        addadmin.innerText="Create new admin"
        New_admin.appendChild(addadmin)
        addadmin.addEventListener("click", () => {
            window.location="/newadmin";
        });

    }
    // when there is no user has logged in, hide the log out button and to read button
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
}
)
// reading the user name from local storage and print it in a welcome div
let username=localStorage.getItem("user name:");
if (username!=null){
    content.innerText="Welcome "+ username;
}
else{ content.innerText="Welcome "}

//clear what is written in local storage while logging out
const logoutbutton= document.getElementById("logout");
logoutbutton.addEventListener("click", () => {
    localStorage.clear();
});

const books_container= document.getElementsByClassName("books_div");
const namess=document.getElementsByClassName("d1");
const authorss=document.getElementsByClassName("d2");

// make the book div to link to book details page
for (let i=0;i<books_container.length;i++)
{
    books_container[i].addEventListener("click",()=>{
        let namevalue= namess[i].innerText;
        let authorvalue=authorss[i].innerText;
        window.location="/books/details/" + namevalue + "/" + authorvalue;

    })
}
