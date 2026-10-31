# fruits=["apple","banana","mango"]
# print(fruits[2])
# change=fruits[1]="grapes"
# print(change)
# add=fruits.append("orange")
# print(fruits)
# fruits.remove("mango")
# print(len(fruits))

# for i in fruits:
#     print(i)

# student = {"name": "Fida", "age": 16, "mark": 90}
# print(student["mark"])

# numbers = [2, 4, 6, 8]
# print(sum(numbers))

# a={1,2,3,5,4,3}
# b={3,8,6,9,3}
# print(a|b)
# print(a-b)
# print(a&b)

# student = {"name": "Fida", "age": 16, "mark": 90}
# student["name"]="shamna"
# print(student["name"])
# student.update({"cource":"python"})
# student.pop("name")
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name","not available"))

# data={n:n*n for n in range(1,6)}
# print(data)

# word="fidaa"
# print(word[2])
# print(word[-2])
# print(word[1:3])
# print(word)
# word="heloo fidaaa"
# new=word.replace( "fidaaa","finuu")
# print(new)
# print(word.capitalize())
# print(word.title())
# text = "apple,mango,banana"
# print(text.split(","))
# words = ["Python", "is", "easy"]
# print("-".join(words))

# numbers=[12,3,54,67,8]
# print(max(numbers))

# class Student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def __str__(self):
#         return f"student name ={self.name} student mark={self.mark}"    
# s1=Student("fida",18)
# s2=Student("shamna",20)
# print(s1)
# print(s2)
# class BankAccount:
#    def __init__(self,name,balance):
#     self.name=name
#     self.balance=balance
#    def deposit(self,amount):
#         self.balance = self.balance+amount
#         return self.balance
# s1=BankAccount("fida",100000)
# res=s1.deposit(50000)
# print(res)

# #INHERITANCE
# class Vehicle:
#     def start(self):
#         print("vehicle is starting")
# class Car(Vehicle):
#     pass
# c=Car()
# c.start()    

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(self.name)
# class Student(Person):
#     pass
# s=Student("fida")
# s.display()    

# class Employee:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(self.name)    
# class Manager(Employee):
#     def __init__(self,name,department):
#         super().__init__(name)
#         self.department=department
# m=Manager("fida","HR")
# m.display()
# print(m.department)        

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def show_name(self):
#         print(self.name)    
# class Employee(Person):
#     def __init__(self,salary,name):
#         super().__init__(name)
#         self.salary=salary
#     def show_salary(self):
#         self.salary
# class Manager(Employee):
#     def __init__(self,salary,name,department):
#         super().__init__(salary,name)
#         self.department=department
#     def show_department(self):
#             print(self.department)
# c=Manager(40000,"fida","HR")
# c.show_department()
# c.show_name()
# c.show_salary()                       


# class Camera:
#     def take_photo(self):
#         print("taking photo")
# class Phone():
#     def  make_call(self):
#         print("making a call")      
# class Smartphone(Camera,Phone):
#     pass
# c=Smartphone()
# c.take_photo()
# c.make_call()            

# class Shape:
#     def display(self):
#         print("this is a shape")
# class Circle(Shape):
#     pass
# class Rectangle(Shape):
#     pass 
# class Triangle(Shape):
#     pass
# c1=Triangle()
# c2=Rectangle()
# c3=Circle()
# c1.display()
# c2.display()
# c3.display()

# class Animal:
#     def sound(self):
#         print("animal sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog sound")
# c=Dog()
# c.sound()              

# class Calculator:
#     def add(self,a,b,c=0):
#         return a+b+c
# c=Calculator()
# res=c.add(2,5,6) 
# print(res) 
# res=c.add(3,8,6) 
# print(res)

# class Calculator:
#     def add(self,*args):
#         result=0
#         for i in args:
#             result=result+i
#         return result
# c=Calculator()
# print(c.add(1,4,2,6))            

# class Number:
#     def __init__(self,value):
#         self.value=value
#     def __add__(self,other):
#        return self.value+ other.value
# a=Number(10)
# b=Number(20)           
# print(a+b)
# print("hi"+"hello")

# # class Student:
# #     def __init__(self,marks):
# #         self.marks=marks
# #     def get_marks(self):
# #         return self.marks
# #     def set_marks(self,value):
# #         if 0<=va        

# from abc import ABC,abstractmethod
# class ATM:
#     @abstractmethod
#     def withdraw(self,amount):
#         pass
# class my_Atm(ATM):
#     def __init__(self):
#         self.balance=5000
#     def withdraw(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#             print("withdrawal successfull")     
#             print(f"remaining balance={self.balance}")
#         else:
#             print("this is not successull")
# w=my_Atm()
# w.withdraw(2000)

# #Shape Area Calculator

# class Shape(ABC):
#     @abstractmethod
#     def area(self,*args):
#         pass
# class Circle(Shape):
#     def area(self,radius):
#         return 3.14*radius*radius
# class Rectangle(Shape):
#     def area(self,length,width):
#         return length*width
# c1=Rectangle()
# c2=Circle()   
# print(c1.area(6,7))
# print(c2.area(6))   

# class Employee:
#     @abstractmethod
#     def calculate_salary(self,amount):
#         pass
# class FULL_Time(Employee):
#     def salary(self,amount):
#         print(f"full_time salary={amount}")
# class PART_TIME(Employee):
#     def salary(self,amount,hours):
#         print(f"part-time salary ={hours*amount}")
# f=FULL_Time()                
# p=PART_TIME()

# p.salary(200,6)
# f.salary(30000)

# class Notification(ABC):
#     @abstractmethod
#     def send(self):
#         pass
# class  EmailNotification(Notification):
#     def __init__(self,message):
#         self.message=message
#     def send(self):
#         print(f"Email sent : {self.message}") 
# class SMSNotification(Notification):
#     def __init__(self,message):
#         self.message=message
#     def send(self):
#         print(f"SMS sent : {self.message}")
# S=SMSNotification("hellooo welcom")
# E=EmailNotification("hyyyy elcome")
# S.send()
# E.send()

# class BankAccount:
#     def __init__(self,amount):
#         self.amount=amount
#         print(f"deposited:{self.amount}")
#     def deposit(self,amount):
#         self.amount+=amount 
#     def withdraw(self,amount):
#         if self.amount>=amount:
#             self.amount-=amount
#             return self.amount     
# c=BankAccount(2000)
# c.deposit(3000)
# print(c.withdraw(1000))

# class Employee:
#     def __init__(self,name,basicsalary,bonus):
#         self.name=name
#         self.basicsalary=basicsalary
#         self.bonus=bonus
#     def total(self):
#          self.basicsalary+=self.basicsalary+self.bonus
#          return self.basicsalary
# c=Employee("fida",40000,9000)
# print(c.total())    

# #INHERITENCE

# class Vehicle:
#         def __init__(self,rent,days):
#             self.rent=rent
#             self.days=days
#         def calculate_rent(self):
#                    self.rent*=self.days
#                    return self.rent
# class Car(Vehicle):
#         pass
        
# class Bike(Vehicle):
#         pass
        
# c=Car(2000,3)
# b=Bike(500,3)  
# print(c.calculate_rent())  
# print(b.calculate_rent())

# class Animal:
#     def sound(self):
#         print("animal sound")
# class Cat(Animal):        
#     def sound(self):
#         print("cat sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog sound")
# c=Cat()
# c.sound()
# D=Dog()
# D.sound()

# class Shape:
#     def area(self):
#         print("area created")
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#             return self.length * self.width
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#             return 3.14 * self.r*self.r       
# C=Circle(6)
# R=Rectangle(3,6)
# print(C.area())
# print(R.area())

# class ATM:
#     def __init__(self,balance):
#         self.__balance=balance
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amount):
#         self.__balance=amount
#     def  deposit(self,amount):
#         self.__balance+=amount
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#         else:
#             print("inufficient balance")
# a=ATM(5000)
# a.deposit(1000)
# print(a.get_balance())
# a.withdraw(3000)
# print("balance:",a.get_balance())

# class Student:
#     def __init__(self,mark):
#         self.__mark=mark
#     def get_mark(self):
#         return self.__mark
#     def set_mark(self,newMark):
#         if 0<newMark and 100>=newMark:
#             self.__mark = newMark
#         else:
#             print("invalid marks")      
# c=Student(50)
# print(c.get_mark())
# c.set_mark(100)
# print(c.get_mark())


# data=[1,3,8,7,2,5,6,4]
# even=[]
# for i in data:
#     if i%2==0:
#         even.append(i)
# even.sort()
# print(even)
# j=0
# for i in range(len(data)):
#     if data[i]%2==0:
#         data[i]=even[j]
#         j+=1
# print(data)          

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print(f"name is {self.name} marks is{self.marks}")
# c=Student("fida",97)
# c.display()

# from abc import ABC ,abstractmethod
# class BankAccount(ABC):
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#     @abstractmethod    
#     def withdraw(self,amount):
#         pass
# class Person(BankAccount):
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print( self.balance )
#         else:
#             print("invalid amount")
# p=Person("fida",3000)
# p.withdraw(5000)

# num="12345"
# for i in range(len(num)-1,-1,-1):
#   print(num[i],end="")

# num=12345
# count=0
# for i in str(num):
#   count+=1
# print(count)

# num=1234
# sum=0
# for i in str(num):
#     sum+=int(i)
# print(sum)    

# num=[2,4,35,8,6,9]
# even=[]
# for i in num:
#     if i%2==0:
#         even.append(i)
# print(even)        

# str="education"
# count=0
# vow="aeiou"
# for i in str:
#     for j in vow:
#         if i==j:
#             count+=1
# print(count)            

# num=[12,45,7,89,23]
# largest=num[0]
# for i in num:
#     if i>largest:
#         largest=i
# print(largest)        

# str="madam"
# rev=""
# for i in str:
#     rev=i+rev
# if rev==str:
#     print("palindrome")
# else:
#     print("not a palindrome")    

# str="programming"
# data=""
# for i in str:
#     if i not in data:
#         data+=i
# print(data)        

# num=[10,25,8,40,30]
# data=[]
# for i in num:
#     data.append(i)
#     res=sorted(data,reverse=True)
# print(res[1])

# num=[10,25,8,40,30]
# data=[]
# for i in num:
#     data.append(i)
#     res=sorted(data)
# print(res[-2])  

# num = [10, 25, 8, 40, 30]

# data = sorted(num)
# print(data[-2])

num=7
count=0
for i in range(1,num+1):
    if num % i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")                

# word="hello"
# data={}
# count=1
# for i in word:
#     if i not in data:
#         data[i]=1
#     else:
#         data[i]+=1
# print(data)           

# #Two Sum

# nums=[2,7,11,15]
# target=9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#            print([i,j])


# data=[1,2,3,4,1,2]
# res=[]
# class Solution:
#     def  RemoveDuplicates(self,nums):
#         for i in data:
#            if i not in res:
#                res.append(i)
#         return len(res),res
# c=Solution()
# data=[1,2,3,4,1,2]
# k,result=c.RemoveDuplicates(data)  
# print(k)
# print(result)          

    
# class Number:
#     def palindrome(self,number):
#         rev=""
#         for i in str(number):
#             rev=i+rev
#         if rev==str(number):
#             print("palindrome")            
#         else:
#             print("this not a palindrome")
# obj=Number()
# num=121
# obj.palindrome(num)        

# class Number:
#     def largest(self,num):
#         first=float('-inf') #to give infinity negative value 
#         second=float('-inf')
#         for i in num:
#             if i>first:
#                 second=first
#                 first=i
#             elif i<first and i>second:
#                 second=i
#         if second==float('-inf'):
#             return "No second-largest distinct number"     
#         return second            

# obj=Number()
# number=[2,3,1,4,6]
# print(obj.largest(number))

# number=[0, 1, 0, 3, 12]
# list1=[]
# list2=[]
# for i in number:
#     if i==0:
#         list1.append(i)
#     else:
#         list2.append(i)
# res=list2+list1
# print(res)            

# number=[3, 0, 1]
# large=len(number)
# for i in range(large+1):
#     if i not in number:
#         print(i)


# class Student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.__mark=mark
#     def set_mark(self,marks):
#         if 0<marks and 100>=marks:
#             self.__mark=marks
#         else:
#             print("invalid marks")    
#     def show_marks(self):
#         return self.__mark
# s=Student("fida",55)
# s.set_mark(99)
# print(s.show_marks())
# s.set_mark(101)
# print(s.show_marks())


# class Employee:
#     def __init__(self,amount):
#         self.__amount=amount
#     def update_salary(self,salary):
#         if salary>0 :
#             self.__amount=salary
#         else:
#             print("invalid")       
#     def show_salary(self):
#         self.__amount
# s1=Employee(400)
# s1.update_salary(600)
# print(s1.show_salary())
# s2=Employee(500)
# s2.update_salary(0)
# print(s2.show_salary())   