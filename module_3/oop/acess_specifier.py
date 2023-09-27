class student:
    #private
    __id=101
    __name="rinkal"

    def __data(self):
        print(self.__id)
        print(self.__name)

    def  hh(self):
        self.__data()

s=student()
s.hh()

'''class student:

    #private
    __id=0
    __name=""

    def __data(self):
        self.__id=input("enter id:")
        self.__name=input("enter name:")
    
        print("this is private function")

    def printdata(self):
      
        self.__data()
        print(self.__id)
        print(self.__name)

s=student()
s.printdata()
'''