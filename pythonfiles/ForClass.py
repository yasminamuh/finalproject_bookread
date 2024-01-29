import json

#-----------------------------------------------------------------------------# 
##dealing with json!!
#how to update your data into json file (replaces the data inside with this data!)
def class_writinginto(data,filename):
    with open(filename,"w") as s: 
        json.dump(data,s,indent=4)
#-----------------------------------------------------------------------------# 
## here when i need to create a new book and update it into books json file       
def update(name,author,type,description,publishdate,review,image_path,yeartime):
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
       temp={"name":name,"author":author,"type":type,"description":description,"publish date":publishdate,"reviews":review,"image":image_path,"years":yeartime}
       booky.append(temp)
       class_writinginto(data,"books.json")    
    return choice    

#-----------------------------------------------------------------------------# 
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
    def addyears(self,yeartime):
        self.yeartime=yeartime
        return yeartime
    def addimage(self,image_path):
        self.image_path=image_path
        return image_path
    ##this method to add all book properties into database
    def addthem(self):
        check=update(self.name,self.author,self.type,self.description,self.publishdate,self.review,self.image_path,self.yeartime)
        ##the check boolean variable is to check if the book is already in the data base so we don't need to add it
        ## or it's okay to add it, if check = true , then add it , if not don't add it
        if check==True:
            return True
        else:
            return False

#-----------------------------------------------------------------------------# 

##create instance from class book
def createins(bookname,bookauthor,booktype,bookdescription,bookpublishdate,review,image_path,yeartime):
    newbook= book(bookname)
    newbook.addname(bookname)
    newbook.addauthor(bookauthor)
    newbook.addtype(booktype)
    newbook.adddescription(bookdescription)
    newbook.addpublishdate(bookpublishdate)
    newbook.addreview(review)
    newbook.addimage(image_path)
    newbook.addyears(yeartime)
    check= newbook.addthem()  
    ##create instance and add it if check = true.
    if check==True:
        return True
    else:
        return False   
    
#-----------------------------------------------------------------------------# 
