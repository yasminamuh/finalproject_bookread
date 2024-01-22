
const localname = document.getElementById("username2");
const namebutton = document.getElementById("checkpass");
const localemail=document.getElementById("email");
const localpass=document.getElementById("password");
function saving()
{
    localStorage.setItem("user name:",localname.value);
}
namebutton.addEventListener("click",saving);



