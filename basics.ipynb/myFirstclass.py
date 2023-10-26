#class MSCDSB:

   # def __init__(self):#member function
        #DATA MEMBERS / PROPERTIES / ATTRIBUTES 
    #    self.name="MSCDSB"
   #     self.students=["A","B","C","D"]

  #  def printStudents(self):#member function
 #       for student in self.students:
#            print(student)

#obj=MSCDSB()
#print(obj.name,obj.students)
#obj.printStudents()

#------------------------------------------------------------------------------------------------------------

#class car:
   # def __init__(self,mfg,mdl,yer):
    #    self.Manufacturer=mfg
     #   self.Model=mdl
      #  self.Year=yer

  #  def __str__(self):
   #     return self.manufacturer

#G_Wagon=car("BENZ","G-class",2022)
#print(G_Wagon.Manufacturer,G_Wagon.Model,G_Wagon.Year)

#Ferrari=car("Ferrari","A-series",2023)
#print(Ferrari.Model,Ferrari.Manufacturer,Ferrari.Year)

#Porsche=car("Porsche","Caymen",2023)
#print(Porsche.Manufacturer,Porsche.Model,Porsche.Year)

#------------------------------------------------------------------------------------------------------------------------------

#CREATE A CLASS RESTAURANT THAT ACCEPTS
#ITEM AND QUANTITY AS INPUT
#INSIDE YOUR CLASS YOU ARE HAVING THE ITEM
#AND ITS COST (UNIT PRICE) AS A DICTIONARY
#AND ITS PRICE AS A DICTIONARY
#CREATE A FUNCTION TO CALCULATYE TOTAL COST
#THAT PRINTS ITEMNAME,QTY,AND TOTALCOST

# class restaurant():
#     def __init__(self,itemname,qty):
#         self.item=itemname
#         self.quantity=qty

#         self.menuItems = {
#             "Fried rice" : 250,
#             "Biriyani" : 300,
#             "Chapathi" : 130,
#             "Noodles" : 220,
#         }

#     def total_cost(self):
#         print("Total cost of the order:")
#         print("Item\t:",self.item)
#         print("Quantity\t:",self.quantity)
#         total=self.quantity * self.menuItems[self.item]
#         print("Total\t:",total)

# Order=restaurant("Chapathi",4)
# Order.total_cost()

#--------------------------------------------------------------------------------------------------------------------------------------

#DEFINE A CLASS EXPENSE TRACKER THAT STORES THE 
#EXPENSES AND INCOME IN A DICTIONARY
#IMPLEMENT THE METHOD TO
# - STORE THE TRANSACTION
# - VIEW TRANSACTION
# - CALCULATE THE TOTAL EXPENSE/INCOME

# class expense_tracker():
#     def __init__(self):

#         self.store_exp={
#             "Income" : [],
#             "Expense" : [],
#             }
        
#     def store_transactions(self,type,amt,category,date,details):
#         trans={
#             "Amount":amt,
#             "Category":category,
#             "Date":date,
#             "Details":details,
#         }
#         if type=="income":
#             self.store_exp['Income'].append(trans)
#         else:
#             self.store_exp['Expense'].append(trans)

#     def view_transaction(self):
#         print("Your Income:")
#         for item in self.store_exp['Income']:
#             print(item)
#         print("Your Expenses:")
#         for item in self.store_exp['Expense']:
#             print(item)

#     def calculate_transactions(self):
#         total_income = 0
#         for item in self.store_exp['Income']:
#             total_income += item["Amount"]
#         print("Total income \t:\t",total_income)

#         total_expense=0
#         for item in self.store_exp['Expense']:
#             total_expense += item["Amount"]
#         print("Total Expenses\t:\t",total_expense)

# #DEFINE A MENU THAT WILL LET USERS TO ENTER EXPENSE ,VIEW EXPENSES
# #OR INCOME,GET TOTALS IN EACH AND EXIT FROM THE PROGRAM
 
# def collectInput():
#     amt=int(input("Enter the amount:"))
#     category=input("Enter category:")
#     date=input("Enter the date (DD/MM/YYYY):")
#     details=input("Enter the description:")
#     return amt,category,date,details

# myexpense=expense_tracker()

# while True:
#     print("...MY EXPENSE TRACKER....")
#     print("1.Record Income")
#     print("2.Record Expense")
#     print("3.View Records")
#     print("4.View My Spendings")
#     print("5.Exit")

#     choice=input("Enter your choice:")

#     if choice==1:
#         print("Enter the details of income:")
#         amt,category


#----------------------------------------------------------------------------------------------------------------------------------

# define a class expense tracker that stores the
# expenses and income in a dictionary
# implement the method to
# - store the transaction;
# - view transactions;
# - calculate the total expense/income


class expenseTracker:
    def __init__(self):
        self.expenseDict = {
            "income": [],
            "expense": [],
        }

    def store_transactions(self, type, amt, category, date, details):
        trans = {
            "Amount": amt,
            "Category": category,
            "Date": date,
            "Details": details,
        }
        if type == "income":
            self.expenseDict['income'].append(trans)
        else:
            self.expenseDict['expense'].append(trans)

    def view_transactions(self):
        print("Your Income:")
        for item in self.expenseDict['income']:
            print(item)
        print("Your Expenses:")
        for item in self.expenseDict['expense']:
            print(item)

    def calculate_transactions(self):
        total_income = 0
        for item in self.expenseDict['income']:
            total_income += item["Amount"]
        print("Total Income\t:\t", total_income)

        total_expense = 0
        for item in self.expenseDict['expense']:
            total_expense += item["Amount"]
        print("Total Expenses\t:\t", total_expense)

# define a menu that will let users to enter expense, view expenses
# or income, get totals in each and exit from the program


def collectInput():
    amt = int(input("Enter the amout: "))
    category = input("Enter Category: ")
    date = input("Enter Date (DD/MM/YYYY): ")
    details = input("Enter description: ")
    return amt, category, date, details


myexpense = expenseTracker()

while True:
    print("...MY EXPENSE TRACKER...")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Records")
    print("4. View My Spendings")
    print("5. Exit")

    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        print("Enter the details of income")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        exit()
    else:
        print("In valid choice")


 #----------------------------------------------------------------------------------------------------------------------------------       
       





        
    





