from mobile import Mobile 


class MobileMgmt():

    def addMob(self, m):
        with open("mobiles.txt", "a") as fp:
            fp.write(str(m)+ "\n")



    def searchById(self, id):
        try:
            with open("mobiles.txt", "r") as fp:
                for line in fp:
                    try:
                        line.index(str(id),0,4)
                        print("mobile is found:  ", line)
                        break
                    except:
                        pass

                else:
                    print("mobile is not found")
        except:
            print("file does not exist")



    def searchByName(self,nm):
        try:
            with open("mobiles.txt", "r") as fp:
                for line in fp:
                    if(nm.lower() in line.lower()):
                        print("Found: ", line)
                        break
                else:
                    print("Name is not found")
        except:
            pass



    def editById(self, id):
        allMob = []
        found = False
        try:
            with open("mobiles.txt", "r") as fp:
                for line in fp:
                    try:
                        line.index(str(id), 0,4)
                    except:
                        pass
                    else:
                        found = True
                        line = line.split(",")
                        print(line)
                        print("a. You want to edit name of mobile")
                        print("b. You want to edit price of mobile")
                        ans = input("Enter your choice(a or b): ")
                        if(ans.lower() == "a"):
                            line[1] = input("Enter a new name: ")
                        elif(ans.lower() == "b"):
                            line[2] = input("Enter the new price of mobile: ")
                        else:
                            print("invalid input")
                        line = ",".join(line)
                    finally:
                        allMob.append(line)              
            if(found):
                with open("mobiles.txt", "w") as fp:
                    for mob in allMob:
                        fp.write(mob)
            else:
                print("id is not found")
        except:
            print("File is not present")



    def deleteMob(self, id):
        allMob = []
        found = False
        try:
            with open("mobiles.txt", "r") as fp:
                for line in fp:
                    try:
                        line.index(str(id), 0,4)
                    except:
                        allMob.append(line)
                    else:
                        found = True
            if(found):
                with open("mobiles.txt", "w") as fp:
                    for mob in allMob:
                        fp.write(mob)
            else:
                print("id is not found")
        except:
            print("File is not present")



    def displayMob(self):
        with open("mobiles.txt", "r") as fp:
            print(fp.read())


    
    


    