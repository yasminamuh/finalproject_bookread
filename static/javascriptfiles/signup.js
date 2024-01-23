const addname = document.getElementById("adduser");
const namebutton = document.getElementById("save");
function saving()
{
    localStorage.setItem("user name:",addname.value);
}
namebutton.addEventListener("click",saving);

