const divweuse= document.getElementById("blo")
const bookname= document.getElementsByClassName("d1")
const bookauthor= document.getElementsByClassName("d2")
const toread_list= document.getElementById("toread");
const review_button= document.getElementById("reviewbtn");
const review_text= document.getElementById("reviewtxt");

review_text.hidden=true;

review_button.addEventListener("mouseover", ()=>{
    review_text.hidden= false;
})

fetch('/api/data')
.then(response => response.json())
.then(data => {
    let admin= data["is_admin"];
    let user= data["user"];
    if (admin == true){
        const deletebookbutton=document.createElement("button");
        deletebookbutton.innerText=" Delete Book"
        divweuse.appendChild(deletebookbutton)
        let bookname_value= bookname[0].innerText;
        let bookauthor_value=bookauthor[0].innerText;
        deletebookbutton.addEventListener("click", () => {
            window.location="/books/delete/" + bookname_value + "/" + bookauthor_value;
        });}

     if (user == null)
     {
        review_button.style.display="none"
        toread_list.style.display="none"
     }
    
})

