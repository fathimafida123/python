#DUCK TYPING

# class Cat:
#     def sound(self):
#         print("meow")
#     def name(self):
#         print("pupy")    
# class Dog:
#     def sound(self):
#         print("boww")
#     def name(self):
#         print("kittu")   

# def make_sound(animal):  #this is norml fn 
#     animal.sound()

# make_sound(Dog())
# make_sound(Cat())

#without using duck method
# class Cat:
#     def sound(self):
#         print("meow")
#     def name(self):
#         print("pupy")    
# class Dog:
#     def sound(self):
#         print("boww")
#     def name(self):
#         print("kittu")   

# animal=[Cat(),Dog()]
# for animals in animal:
#     animals.sound()

# make_sound(Dog())
# make_sound(Cat())

#abstractmethod
# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("baww")
   
# class Cat(Animal):
#     def sound(self):
#         print("meow")                
# dog=Dog()   
# dog.sound()    
# cat=Cat()
# cat.sound()

# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog():
#     def run(self):
#         print("runn")
   
# class Cat(Animal):
#     def sound(self):
#         print("meow")                
# dog=Dog()   
# dog.run()    
# cat=Cat()
# cat.sound()        

# from abc import ABC,abstractmethod

# class vehicles(ABC):
#     @abstractmethod
#     def start():
#         pass
#     @abstractmethod
#     def stop():
#         pass    
# class Car(vehicles):
#     def start(self):
#         print('car is started')
#     def stop(self):
#         print("car is stoped")    
# car=Car()
# car.start()       
# car.stop()

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

#     def fuel(self):
#         print("Vehicle needs fuel")


# class Car(Vehicle):

#     def start(self):
#         print("Car starts")


# car = Car()
# car.start()
# # car.fuel()

# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass

#     def show_message(self):
#         print("Payment system started")


# class UPI(Payment):

#     def pay(self, amount):
#         print(f"Paid ₹{amount} using UPI")


# class Card(Payment):

#     def pay(self, amount):
#         print(f"Paid ₹{amount} using Card")


# p1 = UPI()
# p2 = Card()

# p1.show_message()
# p1.pay(500)

# p2.show_message()
# p2.pay(1000)
# print(Payment.__abstractmethods__)

# from abc import ABC,abstractmethod
# class Car:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     @abstractmethod
#     def start_engin(self):
#         pass
# class BMW(Car):
#     def start_engin(self):
#         print(f"i have a car the car name is {self.name} the color is {self.color} ")
# class Toyota(Car):
#     def start_engin(self):
#           print(f"i have a car the car name is {self.name} the color is {self.color} ")
# bmw=BMW("BMW","black")
# toyota=Toyota("Toyota","black")
# bmw.start_engin()
# toyota.start_engin()

# from abc import ABC,abstractmethod
# class Animal(ABC):
#     def __init__(self,name):
#         self.name=name
#         print("parent")
#     @abstractmethod
#     def sound(self):
#          pass
# class Dog(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#         print("child")
#     def sound(self):
#         print(f"the dog name is {self.name} is age is {self.age}")
# dog=Dog("puppy",4)
# dog.sound()
# super().__init__(name) use cheyyumbol parent
#  class-ile constructor call cheyyum. Athu name store cheyyum. Child constructor age
#   store cheyyum. Angane parent-ileyum child-ileyum attributes initialize cheyyam.


# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass


# class Pet(Animal):

#     def play(self):
#         print("Pet is playing")


# class Dog(Pet):

#     def sound(self):
#         print("Dog is barking")


# d = Dog()
# d.sound()
# d.play()

#ENCAPSULATION

# class Student:
#     def __init__(self):
#         self.__marks=0
#     def update(self,marks):
#         if 0<= marks <=100:
#             self.__marks=marks    
#         else:
#             print("invalid mark")
#     def show(self):
#         print(self.__marks)
# s1=Student()
# s1.update(100)
# s1.show()        

#PUBLIC,PRIVATE,PROTECTED DATA

# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self._age=age
#         self.__marks=marks
#     def update(self):
#         self.name="fidaa"
#         self._age=19
#         self.__marks=70    
# class Child(Student):
#     def change(self):
#         self.name="finu"
#         self._age=10
#         self._Student__marks=19
# c=Child("fideey",18,90)
# print(c.name) 
# print(c._age)
# print(c._Student__marks)  
# c.update()
# print(c.name) 
# print(c._age) 
# print(c._Student__marks)  

# c.change()
# print(c.name) 
# print(c._age) 
# print(c._Student__marks)  

# class Student:
#     def __init__(self, marks):
#         self.__marks = marks

#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid marks")

#     def get_marks(self):
#         return self.__marks


# s1 = Student(80)

# s1.set_marks(95)
# print(s1.get_marks())

#@PROPERTY

class Student:
    def __init__(self,marks):
        self.__marks=marks
    @property
    def mark(self):
       return self.__marks   
    @mark.setter
    def mark(self,value):
        if 0<= value <=100:
            self.__marks=value
s1=Student(40)
print(s1.mark)   
s1.mark=99
print(s1.mark)            

# class Student:
#     def __init__(self,mark):
#         self.__mark=mark
#     @property
#     def data(self):
#         return self.__mark    
# s1=Student(99)
# print(s1.data)

# class Student:
#     def __init__(self, marks):
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks


# class Child(Student):
#     def show(self):
#         print(self.get_marks())


# c1 = Child(80)
# c1.show()

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Invalid amount")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance or invalid amount")

#     def show_balance(self):
#         print(self.__balance)


# account = BankAccount(1000)

# account.deposit(500)
# account.withdraw(200)
# account.show_balance()

#ITERATOR AND GENERATOR

# nums=[1,2,3]
# it=iter(nums)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# class Count:
#     def __init__(self):
#         self.num = 5

#     def __next__(self):
#         value = self.num
#         self.num += 1
#         return value

# c = Count()

# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# class Numbers:
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=3:
#             value=self.num
#             self.num+=1
#             return value
#         else:
#             raise StopIteration     

# n=Numbers()
# for i in n:
#     print(i)


# class Numbers:
#     def __init__(self,num):
#         self.num = num

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.num <= 10:
#             value = self.num
#             self.num += 1
#             return value
#         else:
#             raise StopIteration


# n1 = Numbers(4)
# n2=Numbers(2)

# iterator1 = iter(n1)
# iterator2=iter(n2)
# print(next(iterator2))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator2))

# class Numbers:
#     def __init__(self, start):
#         self.num = start

#     def __next__(self):
#         if self.num <= 3:
#             value = self.num
#             self.num += 1
#             return value
#         raise StopIteration


# n1 = Numbers(1)
# n2 = Numbers(1)

# print(next(n1))
# print(next(n1))
# print(next(n2))
# #Here, we use next() directly. The __iter__() method is not defined.

# #GENERATOR
# def num():
#     yield 10
#     yield 20
#     yield 30
# n=num()
# # print(next(n))    
# for i in n:
#     print(i)

# class Numbers:
#     def num(self):
#         yield 10
#         yield 20
#         yield 30

# n = Numbers()

# g = n.num()

# print(next(g))
# print(next(g))
# print(next(g))    

#GENERATOR EXPRESSSION

# class Numbers:
#     def generate(self):
#         return (x for x in range(10) if x % 2==0)
# n=Numbers()
# # g=n.generate()
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# n = Numbers()

# for x in n.generate():
#     print(x)

# def Number():
#     number =yield 10 
#     yield number
# g=Number()
# print(next(g))   
# print(g.send(50))

# def Number():
#     while True:
#         number = yield
#         print("Received:", number)

# g = Number()

# next(g)          # Start the generator
# g.send(10)
# g.send(20)
# g.send(30)
# g.send(40)
# while True keeps the generator running.
# number = yield pauses the generator and waits for a value.
# g.send(10) sends 10 into the generator.
# number stores 10, and print() displays it.
# The loop repeats, allowing the next number to be sent.

#YIELD FORM

# def numbers():
#     yield from [10,20,30]
# for x in numbers():
#     print(x)    

# def numbers():
#     yield from range(1,5)
# for x in numbers():
#     print(x)        

# #yield from with another generator
# def first():
#     yield 10
#     yield 20
# def second():
#     yield from first()
#     yield 30
# for x in second():
#     print(x)            

#yield from inside a class
# class Numbers:
#     def generate(self):
#         yield from [5,10,15]
# n = Numbers()

# for x in n.generate():
#     print(x)            

# def numbers():
#     values = [10, 20, 30]

#     for x in values:
#         yield x  

# def numbers():
#     values = [10, 20, 30, 40, 50]
#     yield from values

# for n in numbers():
#     print(n)        


# def numbers():
#     yield from [10, 20, 30]
#     yield from [40, 50, 60]

# for x in numbers():
#     print(x)

#CLOSE

# def numbers():
#     yield 10
#     yield 20
#     yield 30
# g=numbers()
# print(next(g))    
# g.close()
# print(next(g))   

class Numbers:
    def generate(self):
        yield 10
        yield 20
        yield 30

n = Numbers()
g = n.generate()

print(next(g))
g.close()