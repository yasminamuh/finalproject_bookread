import json

#-----------------------------------------------------------------------------#
##dealing with json!!
#how to update your data into json file (replaces the data inside with this data!)
def writinginto(data,filename):
    with open(filename,"w") as s: 
        json.dump(data,s,indent=4)
#-----------------------------------------------------------------------------# 
##check email and passwords..
#returns true if the user is exist and false if there is no user with this email,name and password!
def checkemailandpassword(email,name,password):
        with open("login.json") as json_file:
           data=json.load(json_file)
        arr=data["users"]
        adminarr= data["admins"]
        choice= False
        for item in arr:
             #check if this data is exist in login json.
             if item["email"]== email and item["password"] == password and item["username"] == name:
                  choice= True         
        for item in adminarr:
             #check if this data is exist in login json.
             if item["email"]== email and item["password"] == password and item["username"] == name:
                  choice= True    
        return choice          



#-----------------------------------------------------------------------------# 

#this function is adding user name to file userbook json just to save the user name and books he added to read list
# it added the email of the user( because it's unique) , when the user login
#it also added the email into a temo json file(which is temporary file that contain only one user)
def accsessusername(name):
    isadmin=False
    with open("login.json") as login_file:
        logins=json.load(login_file)
        admins=logins["admins"]
        for admin in admins:
            if admin["email"]==name:
                isadmin=True

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
           datatemp["is_admin"]= isadmin
           writinginto(datatemp,"temp.json")

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
    #-----------------------------------------------------------------------------# 
