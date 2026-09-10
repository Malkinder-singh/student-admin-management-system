
import csv

class manage:
    isLogginadmin = False
    isLogginStudent = False
    isLogginUser =[]
    
    def __init__(self,username,password,role): 
        self.username = username
        self.password = password
        self.role = role
    
    
    def addDB(self):
        if self.role == "student":
            
           with open("student.csv" , "a" , newline="\n") as file:
               writer = csv.writer(file)
               
               if file.tell() == 0:
                   writer.writerow(["username","password","age","course","role"])
                  
                   
               writer.writerow([self.username, self.password , self.age , self.course , self.role  ])
               print("\n" + "=" * 50 + "\n        STUDENT REGISTERED SUCCESSFULLY\n" + "=" * 50 + "\n")
        else:
            with open("admin.csv" , "a" , newline="\n") as file:
                        writer = csv.writer(file)
                        
                        if file.tell() == 0:
                            writer.writerow(["username","password","role"])
                        writer.writerow([ self.username , self.password , self.role ])
                    
            print("\n" + "=" * 50 + "\n          ADMIN REGISTERED SUCCESSFULLY\n" + "=" * 50 + "\n")
    
    @classmethod
    def login(self , username , password , role):
        print("\n" + "-" * 50 + f"\n              {role.upper()} LOGIN\n" + "-" * 50)
        if role == "admin":
          with open('admin.csv', mode='r', encoding='utf-8') as file:
             csv_reader = csv.reader(file)
             
             found = False
  
             for row in csv_reader:
               if row[0] == username and row[1] == password:
                    
                    manage.isLogginadmin = True
                    manage.isLogginUser = row
                    
                    print("\n" + "=" * 55 + f"\n  Welcome Back, {username}!\n  You can now manage student records.\n" + "=" * 55 + "\n")
                    found = True
               
                   
             if found == False:
                   print("\n[ERROR] Admin not found. Please register first.\n") 
             return found
        elif role == "student":
           
            with open('student.csv', mode='r', encoding='utf-8') as file:
                     csv_reader = csv.reader(file)
                     
                     found = False
          
                     for row in csv_reader:
                       print("  ", row)
                       if row[0] == username and row[1] == password:
                           
                           manage.isLogginUser = row
                           manage.isLogginStudent = True                            
                            
                           print("\n" + "=" * 55 + f"\n  Welcome Back, {username}!\n  You can now update your details.\n" + "=" * 55 + "\n")
                           found = True
                        
                       if found == False:
                           print("\n[ERROR] Student not found. Please register first.\n") 
                     return found   
     
            
               
        
class student(manage):
    def __init__(self , username , password , age , course):
        super().__init__(username , password , role = "student")
        self.age = age
        self.course = course
        
    @classmethod
    def updateStudent( cls , username = None , password = None , age = None):
        print("\n" + "-" * 50 + "\n             UPDATE PROCESS\n" + "-" * 50)
        print("[Updating username]", username)
        print("[Current user]", manage.isLogginUser)
        newData = []
        with open('student.csv', mode='r', encoding='utf-8') as file:
                            csv_reader = csv.reader(file)
                  
                            for row in csv_reader:
                               print("  ", row)
                               
                               if len(row) > 0 and   row[0] == manage.isLogginUser[0] and row[1] == manage.isLogginUser[1]:
                                    row[0] = username
                                    row[1] = password
                                    row[2] = age
                                    newData.append(row)
                               else:
                                    newData.append(row)    
                                 
        with open("student.csv", mode="w", newline="\n", encoding="utf-8") as file:
               writer = csv.writer(file)
               writer.writerows(newData)
        
           

        
    
       
class admin(manage):
    studentFound = None;
    def showAllStudents():        
        with open('student.csv', mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
        
            print("\n" + "=" * 60 + "\n                 STUDENT DETAILS\n" + "=" * 60)
            
            for row in csv_reader:
                s = ' , '.join(row)
                print(s)
    
    @classmethod
    def updatestd(cls):
         with open('student.csv', mode='r', encoding='utf-8') as file:
             csv_reader = csv.reader(file)
             
             username = input("\nEnter student username: ")
             age = input("Enter student age: ")
             
             for row in csv_reader:
                if len(row) > 0 and row[0] == username and row[2] == age:
                    print("\n[✓] STUDENT FOUND\n" + "-" * 40)
                    s = ' , '.join(row)
                    print(s)
                    admin.studentFound = row
             return admin.studentFound
    @classmethod        
    def updateNow(cls , data):
                newData = []
                with open('student.csv', mode='r', encoding='utf-8') as file:
                                     csv_reader = csv.reader(file)
                           
                                     for row in csv_reader:
                                        print("  ", row)
                                        
                                        if len(row) > 0 and   row[0] == admin.studentFound[0] and row[1] == admin.studentFound[2]:
                                             row[0] = data[0]
                                             row[2] = data[1]
                                             row[3] = data[2]
                                             newData.append(row)
                                        else:
                                             newData.append(row)    
                                          
                with open("student.csv", mode="w", newline="\n", encoding="utf-8") as file:
                        writer = csv.writer(file)
                        writer.writerows(newData)
                        admin.showAllStudents()

    @classmethod                    
    def deleteSTD(cls):
       newData = []

       with open('student.csv', mode='r', encoding='utf-8') as file:
           csv_reader = csv.reader(file)
        
           username = input("\nEnter student username: ")
           age = input("Enter student age: ")
        
           for row in csv_reader:
              if len(row) > 0 and row[0] == username and row[2] == age:
                print("\n[✓] STUDENT FOUND\n" + "-" * 40)
                s = ' , '.join(row)
                print(s)
              else:
                newData.append(row)

       with open("student.csv", mode="w", newline="\n", encoding="utf-8") as file:
          writer = csv.writer(file)
          writer.writerows(newData)

       print("\n" + "=" * 50 + "\n          STUDENT DELETED SUCCESSFULLY\n" + "=" * 50 + "\n")

    @classmethod
    def addStudent(cls):
       username = input("Enter student username: ")

       with open("student.csv", mode="r", encoding="utf-8") as file:
           csv_reader = csv.reader(file)

           for row in csv_reader:
               if len(row) > 0 and row[0] == username:
                  print("\n[ERROR] Username already exists.\n")
                  return

       password = input("Enter student password: ")
       age = input("Enter student age: ")
       course = input("Enter student course: ")

       with open("student.csv", mode="a", newline="\n", encoding="utf-8") as file:
           writer = csv.writer(file)

           writer.writerow([username, password, age, course, "student"])

       print("\n" + "=" * 50 + "\n          STUDENT REGISTERED SUCCESSFULLY\n" + "=" * 50 + "\n")
                 
                              
         
        
           
    


option = None
checkRole = None
secretKey = "admin123"
user = None
loggedInUser = None
def loginPage(role):
   username = input("Enter your username: ")
   password = input("Enter your password: ")
   result = manage.login(username , password , role)
   if result and role == "student":
       loggedInUser = student(username , password , role)
   else:
       loggedInUser = admin(username , password , role)
       
       
def updatePage():
    
    print("\n" + "=" * 60 + "\n                 UPDATE DETAILS\n" + "=" * 60 + "\nPress Enter to skip a field.\n")
    username =  input(f"your currrnt entusername - {manage.isLogginUser[0]} fill new one --- ")
    password = input(f"your current password - {manage.isLogginUser[1]} fill new one ---  ")
    age = input(f"your current  age - {manage.isLogginUser[2]} fill new one ---  ")
    student.updateStudent(username , password , age  )
    

             
            
            
    

   
   
while True:
    print("\n" + "=" * 60 + "\n             STUDENT & ADMIN SYSTEM\n" + "=" * 60)
    print("  1. Register")
    print("  2. Login")
    print("  3. Exit")
    if manage.isLogginadmin:
        print("  4. Enter Admin Panel")
    elif manage.isLogginStudent:
        print(f"  4. Update details ({manage.isLogginUser[0]})")
        print("  5. View your details")
    
    option = int(input("\nSelect an option: "))
    
    if option == 1:
        
       checkRole = int(input("\n  1. Admin\n  2. Student\n\nSelect role: "))
       if checkRole == 1:
           key = input("Enter admin secret key: ")
           if key == secretKey:
               username = input("Enter your name: ")
               password = input("enter your password :")
               user = admin(username , password , role = "admin")
               user.addDB()
               user = None
               checkRole = None

           else :
               print("\n[ERROR] Invalid secret key.\n")
       elif checkRole == 2:
            username = input("Enter your name: ")
            password = input("Enter your password: ")
            age = input("Enter your age: ")
            course = input("Enter your course: ")
            user = student(username,password,age,course)
            user.addDB()
            user = None
            checkRole = None
       else:
            print("\n[ERROR] Invalid option.\n")
            
            
    
    elif option == 2:
        checkRole = int(input("\n  1. Admin\n  2. Student\n\nSelect role: "))
        print("\nSelected role:", checkRole)
        if checkRole == 1:
          loginPage("admin")
        else:
          loginPage("student")  
    
    elif option == 4:
        
        if manage.isLogginStudent:
            updatePage()
        
        else:
            print("\n" + "=" * 60 + "\n                 ADMIN PANEL\n" + "=" * 60)
            adminOption = None
            print("  1. Show All Students")
            print("  2. Update Student")
            print("  3. Delete Student")
            print("  4. Add Student")
            
            adminOption = int(input("\nSelect admin option: "))
            
            
            
            if adminOption == 1:
                admin.showAllStudents()
                
            elif adminOption == 2:
                
              found = admin.updatestd()
              if found == None:
                  print("\n[ERROR] Student not found.")
              else :
                 username = input("Enter new name: ")
                 age = input("Enter new age: ")
                 course = input("Enter new course: ")
                 data = [username , age , course]
                 
                 admin.updateNow(data)
                 
            elif adminOption == 3:
                 admin.deleteSTD()

            elif adminOption ==4:
                 admin.addStudent()
                  
       
    

   
   
   





            
            