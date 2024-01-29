const books_container= document.getElementsByClassName("book_details_container");
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