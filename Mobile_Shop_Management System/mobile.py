
class Mobile:
    def __init__(self,id,mobnm, price, qty):
        self.id = id
        self.mobnm = mobnm
        self.price = price
        self.qty = qty
        
    
    def __str__(self):
        data = str(self.id)+ "," + self.mobnm + "," + str(self.price)+ "," + str(self.qty)
        return data


if(__name__=="__main__"):
    m = Mobile(1,"vivo", 15000, 2)
    print(m)