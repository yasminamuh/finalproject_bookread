
const localname = document.getElementsByClassName("username");
const namebutton = document.getElementsByClassName("save");
const localemail=document.getElementsByClassName("email");

//Set username to local storage
function saving()
{
    for (let i =0; i<localname.length; i++)
    {
    localStorage.setItem("user name:",localname[i].value);
    }
}
for(let i=0; i<namebutton.length ; i++){
    namebutton[i].addEventListener("click",saving);

}



