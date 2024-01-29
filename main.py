import flask
import json
from flask import render_template , jsonify
from datetime import datetime
from pythonfiles.ForClass import createins
from pythonfiles.ForLoginMethods import *
from pythonfiles.ForBookMethods import  *
from pythonfiles.ForReadMethods import *
##working with a flask!!
app= flask.Flask("main")
#-----------------------------------------------------------------------------#           
##routing to main page
@app.route("/")
def gethomepage():
    return render_template("index.html")   
#-----------------------------------------------------------------------------#
## upload the temp json file to api/data route to make js read it
@app.route('/api/data', methods=['GET'])
def get_data():
    with open ("temp.json") as file:
          data=json.load(file)
          return jsonify(data)
#-----------------------------------------------------------------------------#
## routing to login page
@app.route("/login")
def getloginpage():
    return render_template("login.html") 

## login checkkk if the user is exist
@app.route("/logincheck")
def logincheck(): 
  email=flask.request.args.get("email")
  username=flask.request.args.get("username")
  password=flask.request.args.get("pass")
  ##check if the user didn't leave the text files or didn't add anything.
  if email!="" and username!="" and password!= "":
     if checkemailandpassword(email,username,password)== True:
        ##if the user already exist , go and add his email into temp json file and userbooks json file.
        accsessusername(email)
        #reading the books file into books page using jinja
        with open("books.json") as json_file:
           data=json.load(json_file) 
        booky=data["books"]
        return render_template("books.html",test=booky)
     else:
        return render_template("logincheck.html")
  else: return render_template("login.html") 

#-----------------------------------------------------------------------------#
##routing to signup!
@app.route("/signup")
def getsignuppage():
    return render_template("signup.html")

##sign up to create new account into json file.
@app.route("/signupcheck")
def signupadd():
    #the data user type in form
    addemail=flask.request.args.get("addemail:")
    addusername=flask.request.args.get("adduser:")
    addpassword=flask.request.args.get("addpass:")
    signcheck=True
    if addemail!= "" and addusername!="" and addpassword!="":
      signcheck= register(addemail,addusername,addpassword)
      ##if it's a new user go and add his email into userbook json file so he will have a to read list
      if signcheck==True:  
       accsessusername(addemail)
       ##displaying books data into books page using jinja
       with open("books.json") as json_file:
         data=json.load(json_file) 
       booky=data["books"]
       return render_template("books.html",test=booky)
      else:
          return render_template("userishere.html")
    else: return render_template("signup.html")
              
#-----------------------------------------------------------------------------#                    
##routing to books page
@app.route("/books")
def bookspage():
    #open the books json file to display all books using jinja
    with open("books.json") as json_file:
     data=json.load(json_file) 
     booky=data["books"]
     ##i sort the books by publish date (the new comes first)
     sorted_array = sorted(booky, key=lambda x: x["publish date"], reverse=True)
     return render_template("books.html",test=sorted_array)
      
#routing to create new admin        
@app.route("/newadmin")
def newadmin():
    return render_template("newadmin.html")    

#route to create new account into json file.
@app.route("/newadmincheck")
def create_new_admin():
    addemail=flask.request.args.get("addemail:")
    addusername=flask.request.args.get("adduser:")
    addpassword=flask.request.args.get("addpass:")
    signcheck=True
    if addemail!= "" and addusername!="" and addpassword!="":
      signcheck= add_admin(addemail,addusername,addpassword)
      ##if it's a new admin go and add his email into userbook json file so he will have a to read list
      if signcheck==True:  
       accsessusername(addemail)
      with open("books.json") as json_file:
         data=json.load(json_file) 
      booky=data["books"]       
      return render_template("books.html",test=booky)
    
##route for deleting a specific book    
@app.route("/books/delete/<name>/<author>")
def deletewholebook(name,author):
    ## i will add the functionality..
    delete_whole_book(name,author)
    with open("books.json") as json_file:
     data=json.load(json_file) 
    booky=data["books"]
     ##i sort the books by publish date (the new comes first)
    sorted_array = sorted(booky, key=lambda x: x["publish date"], reverse=True)
    return render_template("books.html",test=sorted_array)

##routing to book details page
@app.route("/books/details/<name>/<author>")
def bookdetails(name,author):
      ##opening the book details by selecting its name and author by filtering function.
      book= filtering(name,author)
      ##printing the book details using jinja
      return render_template("booksdetails.html",data=book)

## routing to book details page to add review on it
@app.route("/books/details/add reveiw/<name>/<author>")
def bookreveiw(name,author):
    reveiw=flask.request.args.get("reveiw")
    if reveiw!=None:
    ##add review by taking the name and author by selecting the book and with the review user add
        addreview(reveiw,name,author) 
    book= filtering(name,author)
    return render_template("/booksdetails.html",data=book)

##routing to search book page
@app.route("/books/search")
def searchpage():
    searchword=flask.request.args.get("search")
    ##check if the user enter a word in search text area
    if searchword != None:
        ##calling the searching function and return array of books
        output= searching(searchword) 
        ##if there is no books found
        if(output=="no books found" or output==[]):

                return render_template("nobook.html")
        else:   ##is there is a book found , sort the books displayed using jinja
                sortedoutput = sorted(output, key=lambda x: x["publish date"], reverse=True)
                return render_template("searchbook.html",test=sortedoutput)
        
##routing to add new book page
@app.route("/add_book")
def bookadd():
        ##opening the temp json file to make sure that the user that has an account only who can access this functionality
    with open("temp.json") as file:
        data=json.load(file)
        ##so there is a user who logged in already!
    if data["user"]!= None:   
         return render_template("addbook.html")
       ##the user is not logged in 
    else: return render_template("notuser.html")   

##confirm addition
@app.route("/confirm_book")
def bookadd_confirm():
       ##takes all information about a new book from form in html
       bookname=flask.request.args.get("bookname")
       bookauthor=flask.request.args.get("bookauthor")
       booktype=flask.request.args.get("booktype")
       bookdescription=flask.request.args.get("bookdescription")
       bookpublishdate=flask.request.args.get("bookpublishdate")
       bookimage= flask.request.args.get("imgurl")
       print("publish date")
       print(bookpublishdate)
       yeartime=""
       if bookpublishdate!=None:
           ##how many years thie book has been published
           yeartime=yearcalculating(bookpublishdate)
       review=[]
       ##value check to check if the book is already added before, it it's = false then tell the user that the book is already here
       valuecheck=True
       #if the user fill all text areas then
       if bookname and bookauthor and booktype and bookdescription and bookpublishdate !=None:
           valuecheck=createins(bookname,bookauthor,booktype,bookdescription,bookpublishdate,review,bookimage,yeartime)    
       if valuecheck==True:   
              with open("books.json") as json_file:
               data=json.load(json_file) 
              booky=data["books"]
     ##i sort the books by publish date (the new comes first)
              sorted_array = sorted(booky, key=lambda x: x["publish date"], reverse=True)
            #   return render_template("books.html",test=sorted_array)
              book= filtering(bookname,bookauthor)
      ##printing the book details using jinja
              return render_template("booksdetails.html",data=book)
       else:
          return render_template("bookishere.html")
#-----------------------------------------------------------------------------#      
# route to Add to read list page
@app.route("/addtoread/<name>/<author>")
def addtoist(name,author):
       ##open temp json file to read the name of the current user
       with open("temp.json") as file:
           data= json.load(file)
       ##if there is no user return not user page    
       if data["user"]== None:
           return render_template("notuser.html")
       else:  
          #if there is a user so add the book name into his to read list and redirect to add to read page
          selectingbook(name,author)
          return render_template("addtoread.html")

## routing to read list page
@app.route("/toread")
def toreadpage():
       ##take the user name from temp json file
       with open("temp.json") as json_file:
          temporary=json.load(json_file) 
       nowname=temporary["user"]
       ##if there is no user logged in , redirect to not user page 
       ## if there is a user take his name and open the userbook json file to read all his books and display it using jinja
       if nowname!=None:
          with open("userbook.json") as json_file:
              userdata=json.load(json_file) 
          datausers=userdata["users"]  
          bok=[]
          for item in datausers:
               if item["name"]==nowname:
                   bok=item["books"]
                 
          return render_template("toread.html",data=bok)
       else: return render_template("notuser.html")

## routing to remove any book from read list
@app.route("/toread/removefrom/<bookname>/<bookauthor>")
def delete(bookname,bookauthor):
    ## x is the name of the book then we go to deletebook function that take the book name and delete it from user books json file
    deletebookfrom_toread(bookname,bookauthor)
    return render_template("removing.html")
#-----------------------------------------------------------------------------#   
#routing to log out page (saying bye bye)
@app.route("/logout")
def logout():
    with open("temp.json") as file:
        data=json.load(file)
        ##while user is logging out , we will remove his name from temp json file
        ##if there in no current user so we will redirect to not user page
        if data["user"]!=None:
           data["user"]=None
           data["is_admin"]= False
           writinginto(data,"temp.json")
           return render_template("logout.html")
        else: return render_template("notuser.html")

#-----------------------------------------------------------------------------#



