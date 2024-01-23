const divweuse= document.getElementById("blo")
const bookname= document.getElementsByClassName("d1")
const bookauthor= document.getElementsByClassName("d2")

console.log(bookname[0].innerText)
fetch('/api/data')
.then(response => response.json())
.then(data => {
    let admin= data["is_admin"];
    let user= data["user"];
    if (admin == true){
        console.log("okay")
        const editbutton=document.createElement("button");
        const deletebookbutton=document.createElement("button");
        editbutton.innerText="Edit book"
        deletebookbutton.innerText=" Delete Book"
        divweuse.appendChild(editbutton)
        divweuse.appendChild(deletebookbutton)
        let bookname_value= bookname[0].innerText;
        console.log(bookname_value)
        let bookauthor_value= bookauthor[0].innerText;
        editbutton.addEventListener("click", () => {
            window.location="/books/edit/" + bookname_value + "/" + bookauthor_value;
        });
        deletebookbutton.addEventListener("click", () => {
            window.location="/books/delete/" + bookname_value + "/" + bookauthor_value;
        });

    }
    // Use the data as needed in your JavaScript code
})