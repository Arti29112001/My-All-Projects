
from userMgmt import UserMgmt
from mobileMgmt import MobileMgmt

def user():
    usermgmt = UserMgmt()
    mobilemgmt = MobileMgmt()
    ch = 0
    while (ch != 6):
        print('''
        1. Show list of all mobiles
        2. Search mobile
        3. Add to cart
        4. Buy Mobile, Make Payment-show bill
        5. show cart items
        6. Exit

        ''')
        ch = int(input("Enter your choice: "))

        if(ch == 1):
            mobilemgmt.displayMob()

       
        elif(ch == 2):
            print("a. search mobile through id")
            print("b. search moble based on name")

            ans = input("Enter your choice (a or b): ")
            if(ans.lower() == "a"):
                id = int(input("Enter the id: "))
                mobilemgmt.searchById(id)
            if(ans.lower() == "b"):
                nm = input("Enter the name of mobile you want to search: ")
                mobilemgmt.searchByName(nm)

        elif(ch == 3):  
            id = int(input("Enter id of mobile: "))
            usermgmt.addToCart(id)
            

        elif(ch == 4):
            usermgmt.buyMob()

        elif(ch==5):
            usermgmt.showCart()
              

        elif(ch==6):
            print("Exist")
        else:
            print("Invalid input")
