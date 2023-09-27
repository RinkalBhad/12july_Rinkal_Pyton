class grand():
    
    gold=0
    house=0

    def getdata(self):
        self.gold=input("enter gold details:")
        self.house=input("enter house detail:")

class father(grand):
    car=0
    bal=0

    def g_getdata(self):
        self.car=input("enter car details:")
        self.bal=input("enter balace:")

class son(father):
    def h(self):
        print(self.gold)
        print(self.house)
        print(self.car)
        print(self.bal)

s=son()
s.getdata()
s.g_getdata()
s.h()