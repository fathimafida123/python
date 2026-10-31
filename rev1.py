# try:
#     a=int(input("enter a number: "))
#     b=int(input("enter a number: "))
#     res=a/b
# except ZeroDivisionError:
#     print("number canot devided by zero")
# else:
#     print("result: ",res) 
# finally:
#     print("done")       

# with open("employees.txt","w")as file:
#     file.write(str(1)+","+"anu"+","+str(30000)+"\n")
#     file.write(str(2)+","+"rahul"+","+str(40000)+"\n")
#     file.write(str(3)+","+"fathima"+","+str(50000)+"\n")
# with open("employees.txt","a") as file:
#     file.write(str(4)+","+"meera"+","+str(20000)+"\n")
# with open("employees.txt","r")as file:
#     data=file.read()
# print(data)        

# class Company():
#     company="Tech solution"
#     @classmethod
#     def Change(cls,new_nm):
#         cls.company=new_nm
# c=Company()
# c.Change("bridgeon solution")   
# print(c.company)     

# class Animal():
#     name="cat"
#     @classmethod
#     def change(cls,new_nm):
#         cls.name=new_nm
# a=Animal()
# a.change("dog")
# print(a.name)        

# class Number():
#     @staticmethod
#     def add():
#         print(10+20)

# n=Number()
# n.add()

# class Animal():
#     def cat(self):
#         print("cat")
# a=Animal()
# a.cat()        

# class Employee():
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print(f"employee name is {self.name} salary is {self.salary} ") 
# class Developer(Employee):
#     def display(self,role):
#         print(f"employee name is {self.name} salary is {self.salary} role is {role} ")
# e=Employee("fida",3000)
# d=Developer("anu",35000)
# d.display("developer")
  


# class Student():
#     def data(self):
#         print("student")
# c1=Student()
# c1.data()

# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#          print(f"name: {self.name} age: {self.age}")
# s1=Student("fida",18)
# s1.display()             

# class Company():
#     company_name="Tech Solutions"
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"{self.name} work in {Company.company_name}")
#     @classmethod
#     def Change(cls):
#         cls.company_name="Bridgeon solution"
# c1=Company("fida")
# c2=Company("shamna")
# c1.display()
# Company.Change()
# c1.display()
# c2.display()

# class Student():
#     def stu(self):
#         message="hyy"
#         print(message)
# s1=Student()
# s1.stu()       

# class Calculator():
#     def add(self,a,b):
#         result=a+b
#         print(result)
# c=Calculator()
# c.add(10,20)

# class Animal():
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(self.name)    
# a=Animal("cat")
# a.display()       

# class Animal():
#     name="Dog"
#     @classmethod
#     def change(cls,new_name):
#         name=new_name
# c=Animal()
# c.change("cat")

# class Calculator():
#     @staticmethod
#     def add(a,b):
#         print(a+b)
# c=Calculator()
# c.add(3,5)        

# class Student():
#     @staticmethod
#     def adult(age):
#        return age>18
# c=Student()
# print(c.adult(7))

# class BankAccount():
#     bank_name="ABC Bank"
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#     def display(self):
#         print(f"name {self.owner} bank name  {BankAccount.bank_name}  balance {self.balance}")
#     @classmethod
#     def change(cls,new_value):
#         cls.bank_name=new_value
#     @staticmethod
#     def is_valid_amount(amount):
#         return amount>0
# b=BankAccount("fida",800000)
# b.display()      
# BankAccount.change("ABCD Bank")
# b.display()          
# print(b.is_valid_amount(-900))

# class Animal():
#     def sound(self):
#         print("animal sound")
# class Cat(Animal):
#     pass
# class Dog(Animal):
#     pass
# c=Cat()
# d=Dog()
# c.sound()
# d.sound()


# class Father():
#     def family(self):
#         print("iam father of raju")
# class Mother():
#     def family(self):
#         super().family()
#         print("iam mother of raju")
# class Raju(Mother,Father):
#     def family(self):
#         super().family()
#         print("iam raju")
# r=Raju()
# r.family()
# # Father.family(r)

# class Grandfather():
#     def __init__(self,name):
#         self.name=name
#     def skill(self):
#         print("driving")
# class Father(Grandfather):
#     def hobby(self):
#         print("football")
# class Child(Father):
#     pass
# c=Child("fida")
# c.hobby() 
# c.skill() 
# print(c.name)                        

# class Animal():
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         print("animal sound")
# class Cat(Animal):
#     def __init__(self,name,age):
#         self.age=age
#         super().__init__(name)
#     def sound(self):
#         print("mweoww")
# class Dog(Cat):
#     def __init__(self,name,age,place):
#          self.place=place
#          super().__init__(name,age)
#     def sound(self):
#         print("bark")
# d=Dog("billy",3,"mundumuzhi")            
# print(d.name)
# print(d.age)

# class Parent():
#     def skill(self):
#         print("cooking")
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# c1=Child1()
# c1.skill()

# class Animal:
#     def eat(self):
#         print("Eating")
# class Dog(Animal):
#     def bark(self):
#         print("Barking")
#     def play(self):
#             print(" dog Playing")
# class Cat(Animal):
#     def meow(self):
#         print("Meowing")
#     def play(self):
#             super().play()
#             print("cat Playing")
# class Puppy(Dog, Cat):
#     def play(self):
#         super().play()
#         print("Playing")

# p = Puppy()
# p.eat()
# p.bark()
# p.meow()
# p.play()        

# class Calculator:
#     def add(self,a,b,c=0):
#         return a+b+c
# cal=Calculator()
# print(cal.add(2,3,4))
# print(cal.add(1,3))        

# class Cat():
#     def sound(self):
#         print("meow")
# class Dog():
#     def sound(self):
#         print("bark")
# def make_sound(Animal):
#     Animal.sound()

# c=Cat()
# d=Dog()
# make_sound(d)
# make_sound(c)

# class Animal():
#     def sound(self):
#         print("animal sound")
# class Cat(Animal):
#     def sound(self):
#         print("cat sound")
# c=Cat()
# c.sound()                

# from abc import ABC,abstractmethod
# class withdraw(ABC):
#     @abstractmethod
#     def withdraw(self,amount):
#         pass
#     @abstractmethod
#     def deposit(self,amount):
#         pass
# class Payment(withdraw):
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         if  amount>0:
#             self.balance+=amount
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             return self.balance
# p=Payment(500)
# p.deposit(3000)
# print(p.withdraw(600))


# class BankAccount():
#     def __init__(self,balance):
#         self.__balance=balance
#     def withdraw(self,amount):
#         if self.__balance>amount:
#             self.__balance-=amount
#         else:
#             return "the amount is not avilable in your account"    
#     def get_balance(self):
#         return self.__balance
# b=BankAccount(1000)
# print(b.withdraw(4000))
# print(b.get_balance())

                
# class Number():
#     def __init__(self,num):
#         self.num=num
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=4:
#             value=self.num
#             self.num+=1
#             return value
#         raise StopIteration
# n=Number(1)
# for i in n:
#     print(i)    

# class Number():
#     def fn(self):
#        yield 1
#        yield 2
#        yield 3
# n=Number()
# i=n.fn()
# print(next(i))     
# print(next(i))  
# print(next(i))  

class Number():
    def fn(self):
        for i in range(1,8):
            yield i
obj=Number()
for num in obj.fn():
    if num%2==0:
        print(num)         

              
class Numbers():
    def __iter__(self):
        for i in range(1,8):
            yield i
obj=Numbers()
for i in obj:
    print(i)            

square=lambda x:x*2
print(square(6))

nums=[1,2,3,4,5,6,2]
squares=[n*n for n  in nums]
print(squares)

even=[n for n in nums if n%2==0]
print(even)    
num=[1,2,3,4,3,1]
squares={n*n for n in num}
print(squares)
dic={x:x*x for x in range(1,8)}

print(dic)

res=lambda x,y:x+y
print(res(4,7))

res=lambda x,y: x if x>y else y
print(res(4,7))

nums=[1,2,3,4,5]
res=list(map(lambda x:x*x ,nums))
print(res)

res=list(filter(lambda x:x%2==0,nums))
print(res)

marks = {
    "Anu": 75,
    "Fida": 90,
    "Miya": 85
}
res=dict(filter(lambda item:item[1]>=80,marks.items()))
print(res)

prices = {
    "pen": 10,
    "book": 100,
    "bag": 800,
    "pencil": 5
}
res=dict(filter(lambda i:i[1]>=50,prices.items()))
print(res)

ans=lambda x:x*x
print(ans(7))

nums=[1,2,3,5]
data=list(map(lambda x:x%2==0,nums))
print(data)
names=["fida","finu","moluse"]
data=list(map(lambda x:x.upper(),names))
print(data)

list1=[1,2,3]
list2=[4,5,6]
data=list(map(lambda x,y:x+y,list1,list2))
print(data)

nums=[-5, 8, -2, 10, 0, 3]
data=list(filter(lambda n:n>0 ,nums))
print(data)

data=["cat", "elephant", "dog", "tiger"]
res=list(filter(lambda n:len(n)>3,data))
print(res)

from functools import reduce
numbers=[1,3,4,5]
res=reduce(lambda x,y:x+y,numbers)
print(res)

name=["fida","finu","moluse"]
mark=[90,60,70]
for name,mark in zip(name,mark):
    print(name,mark)
# data=list(zip(name,mark))
# print(data)

data={"anu":1,"riya":3}
data2={"raju":1,"priya":3}


names=["anu","riya","sara"]
marks=[80,50,20]
res=dict(zip(names,marks))
print(res)

a=[1,2,3]
b=["a","b","c"]
res=list(zip(a,b,strict=True))
print(res)

a=[1,2,3]
b=["a","b","c"]
res=zip(a,b,strict=True)
print(next(res))
print(next(res))

nums=[1,2,3]
let=["a","b","d"]
try:
    print(list(zip(nums,let,strict=True)))
except ValueError:
    print("lenght do not match")


dict1={"fida":12,"finu":13,"shamna":29}
dict2={"fideey":14,"moluse":6}
dict1.update(dict2)
print(dict1)

res={**dict1,**dict2}
print(res)

data={"apple":0}
a=data.get("banana",0)
b=data.setdefault("orange",0)
print(b)
print(a)
print(data)

student = {"name": "Anu", "age": 21}
print("name" in student)
print("anu" in student.values())

employee = {
    "name": "Rahul",
    "salary": 25000,
    "department": "IT"
}
print(employee["salary"])
print(employee.get("age","not available"))
print(employee.keys())
print(employee.values())
print(employee.items())
print("department" in employee)
employee.clear()
print(employee)

keys = ["x", "y", "z"]
data = dict.fromkeys(keys, 5)

data["y"] = 20
data["w"] = 30

print(data)
keys = ["x", "y", "z"]
data=dict.fromkeys(data,[])
print(data)
data["x"].append(8) #= use cheyyumbol "a"-yude reference maathram change aakunnu. append() use cheyyumbol randu keys share cheyyunna same list aanu modify cheyyunnathu. Athukondaanu randilum value varunnathu.
print(data)
data["x"]=[20]
print(data)
data["A"]=[3]
print(data)

data={x:x**2 for x in range(1,10) if x%3==0}
print(data)

data = {"a": "hello", "b": "python", "c": "world"}
res={x:y.upper() for x,y in data.items()}
print(res)