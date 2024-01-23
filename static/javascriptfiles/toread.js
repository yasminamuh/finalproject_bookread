const logoutbutton= document.getElementById("logout2");

logoutbutton.addEventListener("click", () => {
    localStorage.clear();
    window.location="/logout";
});

const divvat= document.getElementsByClassName("bookadded");
const namess=document.getElementsByClassName("namebooks");
const authorss=document.getElementsByClassName("authorbooks");

for (let i=0;i<divvat.length;i++)
{
    divvat[i].addEventListener("click",()=>{
        let namevalue= namess[i].innerText;
        let authorvalue=authorss[i].innerText;
        window.location="/books/details/" + namevalue + "/" + authorvalue;

    })
}
