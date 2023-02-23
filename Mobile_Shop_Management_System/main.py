from admin import admin
from user import user

if(__name__=="__main__"):
    print('''
    ______________________________________________________________________

                     *  *  *  *  *  *  *  *  *  *  *  *  *
                     *                                   *
                     *   Mobile Shop Management System   *
                     *                                   *
                     *  *  *  *  *  *  *  *  *  *  *  *  *
                     
    _______________________________________________________________________
    ''')
    print('''
    1. Admin
    2. User
    ''')

    ch = 0
    ch = int(input("Enter your choice:  "))

    try:
        if(ch==1):      
            usernm = input("Enter your username: ")
            pwd = input("Enter your password: ")
            if(usernm.lower() == "arti" and pwd.lower() == "1234"):
                admin()
            else:
                print("please enter valid username and password")
    
        elif(ch==2):
            user()
        
        else:
            print("somthing went wrong, enter valid input")
    except:
        print("Enter valid credentials")
