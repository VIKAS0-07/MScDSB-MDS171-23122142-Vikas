class sportMart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def createOrder(self,OrderID,ItemName,Quantity,Price):
        temp={
            "orderid" : OrderID,
            "itemName" : ItemName,
            "quantity" : Quantity,
            "price" : Price
        }
        self.orders[OrderID]=temp

    def createInventoryItem(self,ProductId,ProductName,Quantity,Price):
        temp={
            "Product Id" : ProductId,
            "Product_Name" : ProductName,
            "quantity" : Quantity,
            "price" : Price
        }
        self.inventory[ProductId] = temp

    def printOrders(self):
        print(self.orders)

    def PrintInventory(self):
        print(self.inventory)

    def Update_Orders(self,OrderID,ItemName,Quantity,Price):
        temp={
            "orderid" : OrderID,
            "itemName" : ItemName,
            "quantity" : Quantity,
            "price" : Price
        }         #Create a menudriven program # Create new orders and update inventory #Export the final data to the fil
        a=input("Enter the order id:")
        b=input("Enter the item name:")
        c=int(input("Enter the quantity:"))
        d=int(input("Enter the price of the item:"))
        temp["orderid"]=a
        temp["itemname"]=b
        temp["quantity"]=c
        temp["price"]=d
        temp.update(self.inventory)
        print(self.inventory)

        
trinity = sportMart()
orders = open("customer_order.csv","r+")
orders_header=orders.readline()
orders_orders=orders.readlines()
for item in orders_orders:
    temp=item.strip().split(',')
    trinity.createOrder(temp[0],temp[1],temp[2],temp[3])
trinity.printOrders()

while True:
    choice=int(input("Enter your choice:"))

    if choice==1:
        print("1.Add order")
        trinity.Update_Orders()
    elif choice==2:
        exit()

    


