class student:
        def __init__(self):
                self.stddet={}
                
        def add_detail(self):
                for i in range(0,2,1):
                        self.dict={
                        "Name" : [],
                        "Age" : [],
                        "Register Number" : []
                        } 
                        a=input("Enter the name of the student:")
                        b=input("Enter the Age of the student:")
                        c=input("Enter the register number of the student:")
                        self.dict["Name"]=a
                        self.dict["Age"]=b
                        self.dict["Register Number"]=c
                        self.stddet[c]=self.dict  #Since reg number is unique we assign it as akey in thje dictionary
                print(self.stddet)

        def print_Student(self):
                print(self.stddet)

        def search_details(self):
                res=input("Enter the register number of the student")
                flag=0
                for items in self.stddet:
                        if items==res:
                                flag=1
                if flag==1:     
                        print("The name is found",self.stddet[res]["Name"])
                else:
                        print("Invalid Register Number")
                        print("The name is not found")


        def create_file(self):
                file=open("Student.csv(2py1)","w+")
                file.write("Name,Age,Register Number\n")  #Header of the file
                for i in self.stddet:
                        file.write(self.stddet[i]["Name"]+","+self.stddet[i]["Age"]+","+self.stddet[i]["Register Number"]+"\n")
                file.close()

        def update_file(self,reg_no,edit_age):
                self.stddet[reg_no]["Age"]=edit_age
                self.create_file()
                


stud=student()

while True:

        print("******STUDENT DETAILS********")
        print("1.Add the student details")
        print("2.Print the student details:")
        print("3.Enter the element to be searched:")
        print("4.Add the elements to a csv file")
        print("5.Update Values")
        print("6.Exit")
        
        choice=int(input("Enter your choice:"))



        if choice==1:
                print("Enter the details of two students")
                stud.add_detail()
        if choice==2:
                print("The students details are:")
                stud.print_Student()
        if choice==3:
                print("Enter the ellement to be searched:")
                stud.search_details

        if choice==4:
                print("The file has been created successfully")
                stud.create_file()
        if choice==5:
                reg_no=input("Enter the register of the student:")
                edit_age=input("Enter the age to be edited")
                stud.update_file(reg_no,edit_age)

        if choice==6:
                exit()