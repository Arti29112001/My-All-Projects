from mobile import Mobile
from mobileMgmt import MobileMgmt


def admin():
    ch = 0
    mob = MobileMgmt()
    while(ch != 6):
        print('''
        1. Add Mobile
        2. Search Mobile
        3. Edit Mobile
        4. Delete Mobile
        5. Show all mobiles
        6. Exit
        ''')
        ch = int(input("Enter your choice: "))
        if(ch == 1):
            id = int(input("Enter the id of mobile: "))
            mobnm = input("Enter the mobile name: ")
            price = float(input("Enter the price: "))
            qty = int(input("Enter the quantity of mobile: "))

            m = Mobile(id,mobnm, price, qty,)
            mob.addMob(m)

        elif(ch == 2):
            print("a. search mobile through id")
            print("b. search moble based on name")

            ans = input("Enter your choice (a or b): ")
            if(ans.lower() == "a"):
                id = int(input("Enter the id: "))
                mob.searchById(id)
            if(ans.lower() == "b"):
                nm = input("Enter the name of mobile you want to search: ")
                mob.searchByName(nm)

        elif(ch == 3):
            id = int(input("Enter the id of mobile to be edit: "))
            mob.editById(id)
            
        elif(ch == 4):
            id = int(input("Enter the id of mobile to be deleted: "))
            mob.deleteMob(id)
            
        elif(ch == 5):
            mob.displayMob()


        elif(ch == 6):
            print("Exist")

        else:
            print("invalid input")

        
