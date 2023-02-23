from mobile import Mobile
import os

class UserMgmt():

    def addToCart(self, id):
        allMob = []
        found = False
        try:
            with open("mobiles.txt", "r") as fp:
                for line in fp:
                    try:
                        line.index(str(id), 0,4)
                        print("found: ", line)
                        with open("cart.txt", "a") as fp:
                            pass
                    except:
                        pass
                    else:
                        found = True                      
                        line = line.split(",")
                        qty = input("Enter quantity of mobile you want buy: ")
                        a = int(line[3])
                        line[3] = qty                      
                        line += "\n"
                        line = ",".join(line)                       
                        allMob.append(line)
            if (found):
                if(a >= int(qty)):
                    with open("cart.txt", "a") as fp:
                        for mo in allMob:
                            fp.write(mo)
                        print("item added in Add to Cart successfully...")
                elif(a == 0):
                    print("Item is not available in stock")
                else:
                    print("Quantity of this mobile is",a, "- add only available quantity of mobiles")
            else:
                print("id is not found")
        except:
            print("File is not present")






    def showCart(self):
        try:
            with open("cart.txt", "r") as fp:
                print(fp.read())
        except:
            print("file does not exist")




    def buyMob(self):
        mobiles= []
        allmob = []
        sum = 0
        try:
            with open("cart.txt", "r") as fp:
                for line in fp:
                    line = line.split(",")
                    mobiles.append(line)
                    bill = float(line[2]) * int(line[3])
                    allmob.append(bill)
                
                for x in allmob:
                    sum = sum + x

            try:
                os.remove("cart.txt")
            except:
                print("file not found")
            
            else:
                
                for i in mobiles:
                    print("\t",i[1],i[2])
                print("Amount: ",sum)
                print()
                print("\t __________________________________________")
                gst = sum * (18/100)
                print("\t| Total GST(18%)            : ",gst,"Rs  |")
                cgst = sum * 9/100
                print("\t| SGST(9%)                  : ",cgst,"Rs  |")
                sgst = sum * 9/100
                print("\t| CGST (9%)                 : ",sgst,"Rs  |")
                total = sum + gst
                print("\t| Bill Amount (Inclued GST) : ",total,"Rs |")
                print("\t|_________________________________________|")
                print()
                buy = input("Payment done (Y/N): ")
                print()
                if(buy.lower() == "y"):
                    print(".....Thank You For Visiting Us.....")
                    totalmo = []
                    with open("mobiles.txt","r") as fp:
                        for line in fp:
                            line = line.split(",")
                            for x in mobiles:
                                if(x[0] == line[0]):
                                    line[3] = str(int(line[3])-int(x[3]))
                                    line[3] += "\n"
                            line = ",".join(line)
                            totalmo.append(line)
                        
                    with open("mobiles.txt","w") as fp:
                        for j in totalmo:
                            fp.write(j)
                
                else:
                    print("Cancel Order")
                
        except:
            print("File does not exist")




        



                

           