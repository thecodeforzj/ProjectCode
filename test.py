'''
class Employee:
    empcount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1
    def displayCount(self):
        print('Total Employee {}'.format(self.empcount))
    def displayEmployee(self):
        print('Name ',self.name,'Salary ',self.salary)

em1 = Employee('Tom',20000)
em1.displayCount()
em1.displayEmployee()
em2 = Employee('Jary',50000)

em2.displayEmployee()
em2.displayCount()
'''
class Parent:
    ParentAttr = 100
    def __init__(self):
        print('父类的构造函数！！！')
    def ParentMothd(self):
        print("调用父类函数！！！")
    def MothdChange(self):
        print("父类的函数！！！")

    def setParentAttr(self,attr):
        self.ParentAttr = attr 
    def getParentAttr(self):
        print(self.ParentAttr)

class child(Parent):
    def __init__(self):
        print('调用子类的构造函数！！！')
    def childMothd(self):
        print('调用子类函数！！')
    def MothdChange(self):
        print('子类重写了父类函数！！！')

ch = child()
ch.childMothd()
ch.getParentAttr()
ch.MothdChange()
ch.ParentMothd()
ch.setParentAttr(200)
ch.getParentAttr()










































































































































































































































































































































































