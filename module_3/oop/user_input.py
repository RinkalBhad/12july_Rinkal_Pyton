class student:
    sid=0
    snm=""
  
    def data(self):
        
          self.sid=input("enter id:")
          self.snm=input("enter name:")

    def printdata(self):
        
         print("id:",self.sid)
         print("name:",self.snm)


s=student()
s.data()
s.printdata()     



'''class student:
    sid=0
    snm=""
    n=0
    def data(self):
        self.n=int(input("enterr n:"))
        for i in range(self.n):
          self.sid=input("enter id:")
          self.snm=input("enter name:")

    def printdata(self):
        for i in range(self.n):
         print("id:",self.sid)
         print("name:",self.snm)


s=student()
s.data()
s.printdata()     

'''