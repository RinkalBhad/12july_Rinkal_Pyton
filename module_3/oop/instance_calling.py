class student:
    id=1
    name="rinkal"

    def getdata(self):
        print(self.id)
        print(self.name)

'''c=student()
c.getdata()
c.id=100
c.name="bhad"
c.getdata()'''

# calling using instance

student().getdata()
student().id=30
student().name="bhad"
student().getdata()

