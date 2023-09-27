class father:
    car=0
    bal=0

    def data(self):
        self.car=input("enter car:")
        self.bal=input("enter bank balance:")

class son(father):
    def printdata(self):
        print("car:",self.car)
        print("balance:",self.bal)


s=son()
s.data()
s.printdata()

