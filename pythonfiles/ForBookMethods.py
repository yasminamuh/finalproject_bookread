import json
from datetime import datetime


#-----------------------------------------------------------------------------#
##dealing with json!!
#how to update your data into json file (replaces the data inside with this data!)
def writinginto(data,filename):
    with open(filename,"w") as s: 
        json.dump(data,s,indent=4)


 
# start with books
           
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
    if review!="":
        with open("books.json") as json_file:
            data = json.load(json_file)
        booky=data["books"] 
        for item in booky:
        #when i select the book add reviews on it
           if item["name"]==namebook and item["author"]==author:
               item["reviews"].append(review)
               writinginto(data,"books.json")     
## calcualte how many years and months this book has been published 
# using book publish date               
def yearcalculating(bookpublishdate):
        #convert it into date time
        input_date = datetime.strptime(bookpublishdate, '%Y-%m-%d')
        current_date = datetime.now()
        yeartime=""
        years_difference = current_date.year - input_date.year
        months_difference = current_date.month - input_date.month

        if current_date.day < input_date.day:
                 months_difference -= 1

        if months_difference < 0:
                  years_difference -= 1
                  months_difference += 12
 
        if years_difference ==0:
                 if months_difference !=0:
                      yeartime= str(months_difference) +" months "
                 else:  yeartime="this month"
        else: 
                 yeartime = str(years_difference) + " years " 
        return yeartime         

#create new admin 
## adding new admin    
##has same functionality to register
def add_admin(email,name,password):
    ##open login json file to update it with the new user data!
    with open("login.json") as json_file:
      data=json.load(json_file) 
      admins=data["admins"]
      choice=True
      for item in admins:
          #check if this email is exist to stop creating new account
          if item["email"]==email:
              choice=False
      #this is a new account so we will add it into our file        
      if choice==True:        
           tempuser={"email": email,"username": name, "password": password}
           #we append the users array with this object
           admins.append(tempuser)
           writinginto(data,"login.json")
      return choice       

## deleting the book functionality    
def delete_whole_book(name,author):
    ##here we delete it from books.json based on it's name and author 
    with open("books.json")as books_file:
        books_data=json.load(books_file)
    books=books_data["books"]
    for item in books:
         if item["name"] == name and item["author"] == author:
             books.remove(item)
    writinginto(books_data,"books.json") 
    ##here we delete it from toread list for any user (userbook json file)                
    with open("userbook.json")as books_file:
        userbooks_data=json.load(books_file)
    books=userbooks_data["users"]   
    for item in books:
            for book in item["books"]:
                if book["bookname"]== name and book["bookauthor"]== author:
                    item["books"].remove(book)          
    writinginto(userbooks_data,"userbook.json")                    
#-----------------------------------------------------------------------------#  