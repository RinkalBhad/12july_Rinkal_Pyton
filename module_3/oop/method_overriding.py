'''class student:
    def getdata(self,id,name):
        print(id)
        print(name)


class otherst(student):
    def getdata(self, id, name):
        return super().getdata(id, name)
    

st=student()
st.getdata(1,"rinkal")

o=otherst()
o.getdata(2,"bhad")
'''

class st1:
    id=0
    name=''

    def data(self):
        self.id=input("enter id:")
        self.name=input("Enter name:")
        print(self.id)
        print(self.name)

class st2(st1):
    def data(self):
        return super().data()          #class alg alg hoy and mehod na name same hoy
    

s=st1()
s.data()

s1=st2()
s1.data()