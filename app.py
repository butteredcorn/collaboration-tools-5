class Dog ():
    #note: if you do not specify an initializer
    # python will use a default one
    def bark(self):
        print("bark")

    def talk(self):
        print(f"bark, my name is {self.name}")

doggo = Dog()
doggo.bark()

#other languages won't let you bind things like this
doggo.name = "Doggo"
doggo.talk()


class Student ():
    university = "BCIT" #shared with every student that will be created

    def __init__ (self, name, age):
        self.name = name
        self.age = age

joe = Student("Joe", "26")

#add property after the fact
joe.school = "bcit"
print(f"{joe.school}")



class Employee:
    def __init__(self, name, salary):
        #no concept of private
        #python developers just use an underscore to signify that something should not be changed
        # _name is a protected attribute (again by convention only)
        self._name = name 
        self.__salary = salary

    def setSalary(self, salary):
        if type(salary) is not int:
            raise ValueError ("no good")
        self.__salary = salary

    def getSalary(self):
        return self.__salary

    #note: there IS an order for this function... getter first, setter second
    #can look up fget and fset to see more.
    salary = property(getSalary, setSalary)

kiran = Employee("Kiran", 1000)

#kiran._salary = 2000

print(kiran.getSalary())

#note, using two underscores will have vs.code hide __name

#single underscore is protected
#double underscore is private... nothing outside the class can use double udnerscore

#print(kiran.__name) #this will throw: AttributeError: 'Employee' object has no attribute '__name'

"""
note one other thing. Python has a concept called 'Name Mangling'
This means that even thought you define a private variable .__salary
you could do something like kiran.__salary = 7000 still
kiran.__salary during initialization actually gets renamed automatically by Python!
kiran.__salary gets renamed to 'kiran._Employee__salary'

"""
kiran.__salary = 8000
print(kiran._Employee__salary)
print(kiran.__dict__)

kiran.setSalary(10000)
print(kiran.getSalary())

#in python3 we can map each setter and getter to a property!!
kiran.salary = 2500
print(kiran.salary)

#however, the best is to use decorators. 

class Person:
    def __init__(self):
        self.__name=''

    # def getName(self):
    #     return self.__name

    # def setName(self, value):
    #     self.__name=value

    # #decorator syntax automates the property function
    # name = property(getName, setName)


    #this is the ideal way to write OOP in python*
    #under decorator syntax, both setter and getter must have same name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name=value

p = Person()
p.name = 'Steve Jobs'
print(p.name)