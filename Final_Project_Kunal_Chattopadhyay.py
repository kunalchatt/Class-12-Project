#importing mysql connector module and creating database if it does not exist
import pickle
import mysql.connector
try:
    ab = mysql.connector.connect(host="localhost", user="root", password="",port=3306,database="kunal_inventory")
    if ab.is_connected():
        print("Connected to MySQL Database")
except:
    ab = mysql.connector.connect(host='localhost', user='root', password='', port=3306)
    xyz=ab.cursor()
    b="create database kunal_inventory"
    xyz.execute(b)
    xyz.execute("use kunal_inventory")
    c="create table users (id integer, name varchar(25), username varchar(20), password integer)"
    xyz.execute(c)
    print("successful in creating database and table")
    xyz.execute("insert into users values (1 ,'Kunal','kunalc',9999)") 
    
d=ab.cursor()
d.execute("use kunal_inventory")

#converting data from database into list

def dataext():
    xy=ab.cursor()
    s = "select * from users"
    xy.execute(s)
    r = xy.fetchall()
    userdata=[]
    for i in r:
        userdata=userdata+[list(i)]
    
    return userdata

print("Welcome to Grocery Manager")
print()

#Login and Register system

def register():
    global customer
    name=input("Enter your name:")
    count2=0
    usernamelist=[]
    for i in dataext():
        
        usernamelist.append(i[2])
    while count2==0:
        username=input("Enter Unique Username: ")
        if username not in usernamelist:
            count2=1
        else:
            print("That username is taken, please try another")
            print()
    count5=0
    while count5==0:
        password=input("Enter your password (in numbers): ")
        confirmpassword=input("Confirm your password: ")
        if confirmpassword == password:
            count5=1
            password=int(password)
    ids=len(dataext())+1
    d=ab.cursor()
    d.execute("insert into users values(%s,%s,%s,%s)",(ids,name,username,password))
    customerid=len(dataext())
    customer=(ids,name,username,password)
    

def login():
    global customer
    check1=0
    username=input("Enter your username: ")
    password=int(input("Enter your password: "))
    for i in dataext():
    
        
        if username==i[2] and password==i[3]:
            customerid=i[0]
            customer=i
            print("Successfully logged in")
            check1=1
            break
    if check1!=1:
            print("Username or password does not exist")
            print("You do not have an account, please register")
            register()
che=0
while che==0:
    choice=input("Enter r to register, or enter l to login: ")
    if choice=="r":
        register()
        che=1
    elif choice == "l":
        login()
        che=1
    else:
        print("Wrong input given, please try again")

#Add, Remove, and modify data system

try:
    stock_file=open("stock.dat","rb")
    try:
        while True:
            stock=pickle.load(stock_file)
            
    except EOFError:
         print()
    stock_file.close()



except:
    stock_file=open("stock.dat","wb")
    pickle.dump({1:100,2:250,3:500},stock_file)
    stock_file.close()
    stock_file=open("stock.dat","rb")
    try:
        while True:
            stock=pickle.load(stock_file)
            
    except EOFError:
         print()
    stock_file.close()



try:
    unit_price_file=open("unit_price.dat","rb")
    try:
        while True:
            unit_price=pickle.load(unit_price_file)
            
    except EOFError:
         print()
    unit_price_file.close()



except:
    unit_price_file=open("unit_price.dat","wb")
    pickle.dump({1:1200,2:300,3:50},unit_price_file)
    unit_price_file.close()
    unit_price_file=open("unit_price.dat","rb")
    try:
        while True:
            unit_price=pickle.load(unit_price_file)
            
    except EOFError:
         print()
    unit_price_file.close()



try:
    description_file=open("description.dat","rb")
    try:
        while True:
            description=pickle.load(description_file)
            
    except EOFError:
         print()
    description_file.close()



except:
    description_file=open("description.dat","wb")
    pickle.dump({1:"rice",2:"shampoo",3:"oreo biscuit"},description_file)
    description_file.close()
    description_file=open("description.dat","rb")
    try:
        while True:
            description=pickle.load(description_file)
            
    except EOFError:
         print()
    description_file.close()




c="y"
print("To add an item - a")
print("To remove an item - r")
print("To modify and edit the stock information of an item - e")
print("To show the list all items - l")
print("To know informaton of an item - i")
print("To quit the grocery stock manager - q")
print("To see all the commands again - help")
print()


while(c!= "q" or c!= "Q"):
    
    c=input("What would you like to do? ")
    
    if(c=="q" or c=="Q"):
        break
        
    elif(c=="A" or c=="a"): #to add a new item
        uid = int(input("Enter Unique item ID: "))
        price = float(input("Enter item's price: "))
        desc = input("Enter the item's description: ")
        stockamt = int(input("Enter the item's stock: "))
        
        m=0
        for i in range(0,len(unit_price)):
            if(uid in unit_price):
                uid+=1 #adding +1 to UID if already exists
                m=1
        if(m==1):
            print()
            print("That item with the Unique Id already exists, the value will be changed to: ",uid)


               
        unit_price.update({uid: price})
        description.update({uid: desc})
        if(stockamt > -1):
            stock.update({uid: stockamt})
        else:
            stockamt = 0
            stock.update({uid: stockamt})
            print("The stock of an item cannot be negative, the stock has been set to 0.")
        description_file=open("description.dat","wb")
        pickle.dump(description,description_file)
        description_file.close()

        stock_file=open("stock.dat","wb")
        pickle.dump(stock,stock_file)
        stock_file.close()

        unit_price_file=open(" unit_price.dat","wb")
        pickle.dump( unit_price, unit_price_file)
        unit_price_file.close()
        print()
        print("Item number: ",uid," Description: ",description.get(uid)," Price: ",
              unit_price.get(uid)," Stock: ",stock.get(uid))
        print("Item was added successfully!")
        print()
        
    elif(c=="E" or c=="e"): #to edit the information of an existing item
        print()
        uid = int(input("Enter item number: "))
        if(uid in unit_price):
            price = float(input("Enter item price: "))
            desc = input("Enter item description: ")
            stockamt = int(input("Enter item stock: "))
                
            unit_price.update({uid: price})
            description.update({uid: desc})
            stock.update({uid: stockamt})
            
        else:
            print("That item does not exist, to add an item use a")
        print()
        description_file=open("description.dat","wb")
        pickle.dump(description,description_file)
        description_file.close()

        stock_file=open("stock.dat","wb")
        pickle.dump(stock,stock_file)
        stock_file.close()

        unit_price_file=open(" unit_price.dat","wb")
        pickle.dump( unit_price, unit_price_file)
        unit_price_file.close()
            
    elif(c=="R" or c=="r"): #to completely remove an item
        print()
        uid = int(input("Enter item number: "))
        if(uid in unit_price):
            verify = input("Are you sure you want to remove that item (y/n)? ")
            if(verify=="y" or verify=="Y"):
                unit_price.pop(uid)
                description.pop(uid)
                stock.pop(uid)
                print("Item successfully removed!")
            print()
        else:
            print("Sorry, we don't have such an item!")
            print()

        description_file=open("description.dat","wb")
        pickle.dump(description,description_file)
        description_file.close()

        stock_file=open("stock.dat","wb")
        pickle.dump(stock,stock_file)
        stock_file.close()

        unit_price_file=open(" unit_price.dat","wb")
        pickle.dump( unit_price, unit_price_file)
        unit_price_file.close()
        
    elif(c=="L" or c=="l"): #to show the information of all the items
        print()
        print("Item and their prices: ",unit_price)
        print("Descriptions: ",description)
        print("Stock left of Item: ",stock)
        print()

    elif(c=="I" or c=="i"):
        print()
        uid=int(input("Enter Item Number: "))
        if(uid in unit_price):
            print()
            print("Item number: ",uid," Description: ",description.get(uid)," Price: "
                  ,unit_price.get(uid)," Stock: ",stock.get(uid))
        else:
            print("Sorry we don't have such an item!")
            print()
        
        
    elif(c=="help"): #help menu
        print("To add an item - a")
        print("To remove an item - r")
        print("To modify and edit the stock info of an item - e")
        print("To show the list all items - l")
        print("To know informaton of an item - i")
        print("To quit the grocery stock manager - q")
        print("To see all the commands again - help")
        print()
        
        
    else:
        print()
        print("You have entered wrong input, please enter a valid value and try again")
        print()


print("Thank you for using Inventory Management System")


    
    













        
