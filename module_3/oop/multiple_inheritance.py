
class st1:

    sid=0
    snm=''

    def getdata(self):
        self.sid=input("enter id of student 1:")
        self.snm=input("enter name student 1:")


class st2:

    id=0
    nm=''

    def getdata1(self):
        self.id=input("enter id of student 2:")
        self.nm=input("enter name student 2:")

class tops(st1,st2):
    def printdata(self):
        print("-------------------student 1's detail---------------")
        print("id:",self.sid)
        print("name:",self.snm)
        print("-------------------student 2's detail---------------")
        print("id:",self.id)
        print("name:",self.nm)

t=tops()
t.getdata()
t.getdata1()
t.printdata() 