#method 1................

'''from mymodule import*
hi()
sum(10,20)
even(5)'''

#method 2................

'''import mymodule
mymodule.hi()
mymodule.even(7)
mymodule.sum(10,40)'''

#method 3................

'''import mymodule as m
m.hi()
m.even(7)
m.sum(10,40)'''

#method 4................

from mymodule import hi,even
hi()
even(8)


