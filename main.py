import flask
import json
from flask import render_template, request , flash , url_for ,redirect
from werkzeug.utils import secure_filename
##working with a flask!!
app= flask.Flask("main")

#-----------------------------------------------------------------------------#
##dealing with json!!
#how to update your data into json file (replaces the data inside with this data!)
def writinginto(data,filename):
    with open(filename,"w") as s: 
        json.dump(data,s,indent=4)

#-----------------------------------------------------------------------------#           
##routing to main page
@app.route("/")
def gethomepage():
    return render_template("index.html")   
#-----------------------------------------------------------------------------#

#start working in login!
#-----------------------------------------------------------------------------#
##check email and passwords..
#returns true if the user is exist and false if there is no user with this email,name and password!
def checkemailandpassword(email,name,password):
        with open("login.json") as json_file:
           data=json.load(json_file)
        arr=data["users"]
        choice= False
        for item in arr:
             #check if this data is exist in login json.
             if item["email"]== email and item["password"] == password and item["username"] == name:
                  choice= True                  
  
        return choice   

## writing into userbook json file

#this function is adding user name to file userbook json just to save the user name and books he added to read list
# it added the email of the user( because it's unique) , when the user login
#it also added the email into a temo json file(which is temporary file that contain only one user)
def accsessusername(name):
    with open("userbook.json") as json_file:
           data=json.load(json_file)
    arr=data["users"]
    choice=True
    for item in arr:
        #check if the user email already exist or not to avoid overriding
        if item["name"] == name:
            choice=False
    #adding a user email into userbook json file        
    if choice==True:
        temp={"name":name,"books":[]}
        arr.append(temp)
        writinginto(data,"userbook.json")
    #adding a user email into temp json file    
    with open("temp.json") as json_file:
           datatemp=json.load(json_file)  
           datatemp["user"] = name
           writinginto(datatemp,"temp.json")
 #-----------------------------------------------------------------------------#

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
#all done with login  
#-----------------------------------------------------------------------------#
  
#start working in sign up!
#-----------------------------------------------------------------------------#  
##here when i need to register and create a new username into login json file "same logic as update!"
def register(email,name,password):
    ##open login json file to update it with the new user data!
    with open("login.json") as json_file:
      data=json.load(json_file) 
      users=data["users"]
      choice=True
      for item in users:
          #check if this email is exist to stop creating new account
          if item["email"]==email:
              choice=False
      #this is a new account so we will add it into our file        
      if choice==True:        
           tempuser={"email": email,"username": name, "password": password}
           #we append the users array with this object
           users.append(tempuser)
           writinginto(data,"login.json")
      return choice       
#------------------------------------------------
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
#all done with sign up 
#-----------------------------------------------------------------------------#   
    
# start working in books!
#-----------------------------------------------------------------------------#        
## here when i need to create a new book and update it into books json file       
def update(name,author,type,description,publishdate,review,image_path):
    with open("books.json") as json_file:
     data=json.load(json_file) 
     booky=data["books"]
     choice=True
    for item in booky:
        ##i check if the book is already here 
         if item["name"]==name and item["author"] == author:
             choice=False
    if choice==True:        
     #this book isn't in database so i will add it 
       temp={"name":name,"author":author,"type":type,"description":description,"publish date":publishdate,"reviews":review,"image":image_path}
       booky.append(temp)
       writinginto(data,"books.json")    
    return choice    


##creating first class: BOOK CLASS
class book:
    def __init__(self,name):
        self.name=name
        
    def addname(self,name):
        self.name=name
        return name
    def addauthor(self,author):
        self.author=author
        return author
    def addtype(self,type):
        self.type=type
        return type
    def adddescription(self,description):
        self.description=description
        return description
    def addpublishdate(self,publishdate):
        self.publishdate=publishdate
        return publishdate   
    def addreview(self,review):
        self.review= review
        return review
    def addimage(self,image_path):
        self.image_path=image_path
        return image_path
    ##this method to add all book properties into database
    def addthem(self):
        check=update(self.name,self.author,self.type,self.description,self.publishdate,self.review,self.image_path)
        ##the check boolean variable is to check if the book is already in the data base so we don't need to add it
        ## or it's okay to add it, if check = true , then add it , if not don't add it
        if check==True:
            return True
        else:
            return False


##create instance from class book
def createins(bookname,bookauthor,booktype,bookdescription,bookpublishdate,review,image_path):
    newbook= book(bookname)
    newbook.addname(bookname)
    newbook.addauthor(bookauthor)
    newbook.addtype(booktype)
    newbook.adddescription(bookdescription)
    newbook.addpublishdate(bookpublishdate)
    newbook.addreview(review)
    newbook.addimage(image_path)
    check= newbook.addthem()  
    ##create instance and add it if check = true.
    if check==True:
        return True
    else:
        return False   

## searching for a book by name of a book and an author 
    
def searching(word):
        with open("books.json") as json_file:
          data=json.load(json_file) 
          arr=data["books"]
          ##an empty array to fill with found books!
          bookexist=[]
          ## not to check in books json if the word is null
          if(word!=""):
             #looping for each object in our books json file, when found the book by name or author 
             #we will add this book to bookexist array to return it
             for item in arr:
                  if item["name"].lower().find(word.lower())!=-1 or item["author"].lower().find(word.lower())!=-1:
                       bookexist.append(item)
             return bookexist
          else: return ("no books found")        

          
#filtering(similar to search!) but it only return one item and i don't check if it's already in the data base
#cause i will call this function when i select the book already with the existing name and author            
def filtering(name,author):
      with open("books.json") as json_file:
          data=json.load(json_file) 
          arr=data["books"]
          boit=[]
          for item in arr:
               if item["name"].find(name)!= -1 and item["author"].find(author)!=-1:
                       boit.append(item)           
      return boit  


# add review functionality 
## calling filtering function to retrieve array of one book selected by the user and add review into it
#by searching for it in books json file by name and  updating it's review property
def addreview(review,name,author):   
    mybooks = filtering(name,author)
    ##to accsess the book name
    namebook= mybooks[0]["name"]
    # Read existing data
    with open("books.json") as json_file:
            data = json.load(json_file)
    booky=data["books"] 
    for item in booky:
        #when i select the book add reviews on it
        if item["name"]==namebook and item["author"]==author:
             item["reviews"].append(review)
             writinginto(data,"books.json")     
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
    ##add review by taking the name and author by selecting the book and with the review user add
    addreview(reveiw,name,author)
    ##display all books sorted using jinja
    with open("books.json") as json_file:
     data=json.load(json_file) 
     booky=data["books"]
     sorted_array = sorted(booky, key=lambda x: x["publish date"], reverse=True)
     return render_template("books.html",test=sorted_array)    

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
       ##takes all information about a new book from form in html
       bookname=flask.request.args.get("bookname")
       bookauthor=flask.request.args.get("bookauthor")
       booktype=flask.request.args.get("booktype")
       bookdescription=flask.request.args.get("bookdescription")
       bookpublishdate=flask.request.args.get("bookpublishdate")
       bookimage= flask.request.args.get("imgurl")
       review=[]
       ##value check to check if the book is already added before, it it's = false then tell the user that the book is already here
       valuecheck=True
       #if the user fill all text areas then
       if bookname and bookauthor and booktype and bookdescription and bookpublishdate !=None:
           valuecheck=createins(bookname,bookauthor,booktype,bookdescription,bookpublishdate,review,bookimage)    
       if valuecheck==True:   
          return render_template("addbook.html")
       else:
          return render_template("bookishere.html")
     ##if the user didn't login or sign up we redirect him to not user page   
    else: return render_template("notuser.html")   



#-----------------------------------------------------------------------------#
##all done with books page !
#-----------------------------------------------------------------------------#

#handle to read list!
    
##this function is adding books into userbooks json file, which means it added books to user to read list 
# it check the name that exist in temp json file then take this name and search for it in userbooks json file, to add books to specific user               
def selectingbook(bookname):
    print(bookname)
    ## it opens temp json file to take the user name 
    with open("temp.json") as json_file:
           temp=json.load(json_file) 
           name=temp["user"]
    check=False
    ## it opens userbook json file to add books into a user name
    with open("userbook.json") as json_file:
           data=json.load(json_file)
           arr=data["users"] 
           for item in arr:
               #reach the specific user
               if item["name"] == name:
                 #check if the user already added this book to his to read list or not to avoid overriding
                 for r in item["books"]:
                   if r ==bookname:
                      check=True
                 #the book isn't in user read list so we will add it     
                 if check==False:     
                    item['books'].append(bookname)
           writinginto(data,"userbook.json")  


#to delete any book from to read list if i finish it    
def deletebook(name):
    ##opend the temp json to find which user is here by selecting him name from temp json file
    with open("temp.json") as file:
        users= json.load(file)
    tempuser=users["user"]   
    ##we had the name so we will loop for it in userbook json file to retrieve the books and remove the book by book name  
    with open("userbook.json") as file:
        userbookdata= json.load(file)
    usersarr= userbookdata["users"]
    for item in usersarr:
        if item["name"] == tempuser:
            item["books"].remove(name)
    writinginto(userbookdata,"userbook.json")      
#-----------------------------------------------------------------------------#
#route to read list !
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
          selectingbook(name)
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

  

## to remove any book from read list
@app.route("/toread/removefrom/<x>")
def delete(x):
    ## x is the name of the book then we go to deletebook function that take the book name and delete it from user books json file
    deletebook(x)
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
           writinginto(data,"temp.json")
           return render_template("logout.html")
        else: return render_template("notuser.html")