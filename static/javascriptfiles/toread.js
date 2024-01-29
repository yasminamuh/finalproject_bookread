const logoutbutton= document.getElementById("logout2");

logoutbutton.addEventListener("click", () => {
    localStorage.clear();
    window.location="/logout";
});

const book_div= document.getElementsByClassName("bookadded");
const namess=document.getElementsByClassName("namebooks");
const authorss=document.getElementsByClassName("authorbooks");

for (let i=0;i<book_div.length;i++)
{
    book_div[i].addEventListener("click",()=>{
        let namevalue= namess[i].innerText;
        let authorvalue=authorss[i].innerText;
        window.location="/books/details/" + namevalue + "/" + authorvalue;

    })
}
