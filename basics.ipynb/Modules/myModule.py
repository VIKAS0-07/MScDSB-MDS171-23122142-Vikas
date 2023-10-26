# class student:
#     def __init__(self,name,phone):
#         self.name = name
#         self.phone = phone

#     def print_student(self):
#         print(self.name,self.phone)
        
class petstore:
    def __init__(self):
        self.pets={
            "DOGS" : [ {"Labrador" : 10000,
                       "Rotweiller" : 20000,
                       "Doberman" : 30000,
                       "Pitbull" : 40000,
                       } ],
            "CATS" : [ {"Persian" : 13000,
                      "Siamese" : 23000,
                      "Himalayan" : 30000,
                      "American Bobtail" : 45000,
                      } ],
            "FISHES" : [ {"Fighter" : 150,
                        "Koi" : 120,
                        "Flowerhorn" : 2500,
                        "Goldfish" : 400,
                        } ],
            "PARROT" : [ {"Macaw" : 200000,
                         "Cockateil" : 6500,
                         "Green Parrot" : 8500,
                         "African Parrot" : 45000,
                         } ]
        }
        print(self.pets)
        
    def store_pets(self,name):
        self.name= {"Horse": [{"Black Horse" : 4002456,"White Horse" : 4561444, "Grey Horse" : 5020010, "Brown Horse" : 7800141}]}
        self.name.update(self.pets)
        print(self.pets)

    def search_pets(self):
        self.search = input("Enter the pet name to be searched:").strip().upper()
        flag=0
        for i in self.pets:
            if i==self.search:
                flag=1
        if flag==1:
            print("This pet is available in the store")
        else:
            print("This pet is not available in the store")
        
    def sell_pet(self):
        self.sell_cust=input("Enter the pet name that the customer wants:")
        for items in self.Lst_pets:
            if items==self.sell_cust:
                self.Lst_pets -= self.sell_cust
        print("The pet is sold successfully")

    def list_allpets(self):
        self.display = self.Lst_pets
        print("The available pets in the list are:",self.display)

pets=petstore() 
pets.search_pets()








