import json

#-----------------------------------------------------------------------------# 
##dealing with json!!
#how to update your data into json file (replaces the data inside with this data!)
def writinginto(data,filename):
    with open(filename,"w") as s: 
        json.dump(data,s,indent=4)
#-----------------------------------------------------------------------------#
##this function is adding books into userbooks json file, which means it added books to user to read list 
# it check the name that exist in temp json file then take this name and search for it in userbooks json file, to add books to specific user               
def selectingbook(bookname,bookauthor):
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
                 for book in item["books"]:
                   if book["bookname"] ==bookname and book["bookauthor"]==bookauthor:
                      check=True
                 #the book isn't in user read list so we will add it     
                 if check==False:     
                    temp_book={"bookname": bookname , "bookauthor":bookauthor}
                    item['books'].append(temp_book)
           writinginto(data,"userbook.json")  

#-----------------------------------------------------------------------------#
#to delete any book from to read list if i finish it    
def deletebookfrom_toread(name,author):
    ##opend the temp json to find which user is here by selecting him name from temp json file
    print("in functions")
    with open("temp.json") as file:
        users= json.load(file)
    tempuser=users["user"]   
    ##we had the name so we will loop for it in userbook json file to retrieve the books and remove the book by book name  
    with open("userbook.json") as file:
        userbookdata= json.load(file)
    usersarr= userbookdata["users"]
    for item in usersarr:
        if item["name"] == tempuser:
            for book in item["books"]:
                if book["bookname"]== name and book["bookauthor"]== author:
                    item["books"].remove(book)   
    writinginto(userbookdata,"userbook.json")   
#-----------------------------------------------------------------------------#              