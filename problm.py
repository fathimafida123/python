# # nums=[10, 10, 20, 8, 5]
# # largest=float("-inf")
# # second=float("-inf")
# # for n in nums:
# #     if n>largest:
# #         second=largest
# #         largest=n
# #     elif second<n and largest>n:
# #         second=n

# # print(second)            

# # str="programming"
# # dic={}
# # for i in str:
# #     if i not in dic:
# #         dic[i]=1
# #     else:
# #         dic[i]+=1
# # print(dic)        


# # nums = [1, 2, 4, 5]
# # for i in range(len(nums)):
# #     if i not in nums:
# #       print(i)

# # text = "aabbcde"
# # dic={}
# # for i in text:
# #     if i not in dic:
# #         dic[i]=1
# #     else:
# #         dic[i]+=1            
# # for key,value in dic.items():
# #     if value==1:
# #         print(key)
# #         break

# # num=int(input("enter a number"))
# # count=0
# # for i in range(1,num+1):
# #     if num%i==0:
# #         count+=1
# # if count==2:
# #     print("prime")
# # else:
# #     print("not a prime")    
    
 
# # n=4
# # for i in range(2,n):
# #     if n%i==0:
# #         print("not prime")
# #     else:
# #         print("prime")

# # nums = [4, 2, 7, 2, 5, 4]
# # store=[]
# # for i in nums:
# #     if i not in store:
# #         store.append(i)
# #     else:
# #         print(i)  
# #         break  

# # nums = [0, 3, 0, 5, 2, 0, 7]
# # data=[]
# # data2=[]
# # for i in nums:
# #     if i!=0:
# #         data.append(i)
# #     else:
# #         data2.append(i)
# # print(data+data2)            
    
# # text = "aabbbccccdd"
# # data={}
# # large=float("-inf")
# # second=float("-inf")
# # for i in text:
# #     if i not in data:
# #         data[i]=1
# #     else:
# #         data[i]+=1
# # print(data)     
# # for key,value in data.items():
# #     if large<value:
# #         second=large
# #         large=value
# #     elif second<value <large:
# #         second=value     
# # print(second)

# # text1 = "listen"
# # text2 = "silent"

# # data=sorted(text1)
# # data2=sorted(text2)
# # if data==data2:
# #     print(True)
# # else:
# #     print(False)    

# # nums = [1, 3, 2, 3, 4, 3, 2, 2, 2]
# # num=max(nums,key=nums.count)#key ennu parayunnathu max() enthine base cheythu compare cheyyanam ennu parayan aanu
# # print(num)


# # list1 = [1, 2, 3, 4, 5]
# # list2 = [3, 4, 5, 6, 7]
# # data=[]
# # for i in list1:
# #     if i in list2 and i not in data:
# #         data.append(i)
# # print(data)         

# # list1 = [1, 2, 3, 4, 5]
# # list2 = [3, 4, 5, 6, 7]
# # data=[]
# # for i in list1:
# #     if i not in data and i not in list2:
# #         data.append(i)
# # print(data)        


# def nums(*args):
#     large=float("-inf")  
#     second=float("-inf")
#     for i in args:
#         if i>large:
#             second=large
#             large=i
#             print(second)            
# nums(10, 5, 20, 8, 20)


# class BankAccount():
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#         else:
#             print("the amount we cant deposit")
#     def withdraw(self,amount):
#         if amount>0 and amount<self.__balance:
#             self.__balance-=amount
#         else:
#             print("the amout tou cant withdraw")
#     def get_balance(self):
#         return self.__balance
# b=BankAccount(5000)
# print(b.deposit(7000))
# print(b.withdraw(4000))
# print(b.get_balance())    
                            

# def decorator(fun):
#     def wrapper(name):
#         fun(name.upper())
#     return wrapper
# @decorator
# def greet(name):
#     print(name)
# greet("fida")    

# day=3
# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case _:
#         print("invalid day")            

# a=10
# b=8
# print(a is not b)        

# a=10
# b=a
# print(a is b)

# import copy

# a = [[1, 2], [3, 4]]
# b = a.copy()

# b[0].append(99)

# print(a)
# print(b)

# x = [1, 2]
# y = x
# print(x is y)
# y = y + [3]

# print(x)
# print(y)
# print(x is y)

# #global vs nonlocal
# x=10
# def data():
#     x=5
# data()
# print(x)    

# x=10
# def data():
#     global x
#     x=5
# data()
# print(x)  

# def outer():
#     count=3

#     def inner():
#         nonlocal count
#         count+=5
#     inner()
#     print(count)
# outer()

# def multiplier(n):
#     def calculate(x):
#        return x*n
#     return calculate
# double=multiplier(5)
# print(double(6))

# def data(*args,**kwargs):
#     print(kwargs)
#     print(args)
# data(10,29,name="fida",age=18)

# data=[x*2 for x in range(1,9)]
# print(data)

# str= "i have a car"
# s=str.split(" ")
# rev=""
# print(s)
# for i in s:
#     rev=i+" "+rev
# print(rev)

# str="programming"
# store={}
# for i in str:
#     if i not in store:
#         store[i]=1
#     else:
#         store[i]+=1
# print(store)            

# def decorator(fun):
#     def wrapper(*args):
#         print("start")
#         fun(*args)
#         print("finish")
#     return wrapper    
# @decorator
# def greet(a,b):
#     print(a+b)
# greet(2,8)            

# class Student():
#   school="Abc school" #class
#   def sound(self):
#       name="fida" #instance

# def play():
#     game="football" #lcoal
#     return Student.school
  
# s=Student()
# print(play()) 
      
# # def fun(n):
# #     if n==0:
# #        return
# #     print(n)
# #     fun(n-1)
# # fun(5)    

# # def fun(n):
# #     if n==5:
# #         return
# #     print(n)
# #     fun(n+1)
# # fun(1)     

# # def factorial(n):
# #     if n==0 or n==1:
# #         return 1
# #     return n*factorial(n-1)
# # print(factorial(5))

# # def fibonacci(n):
# #     if n==0:
# #         return 0
# #     if n==1:
# #         return 1
# #     return fibonacci(n-1)+fibonacci(n-2)
# # print(fibonacci(3))     

# def demo():
#     x = yield 10
#     print(x)
#     yield 20

# g = demo()

# print(next(g))
# print(g.send(50))

# def demo():
#     x=yield 1
#     # print("received: ",x)
#     yield x
#     yield 3
# d=demo()
# print(next(d))
# print(d.send(2))    
# print(next(d))

# class cal:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self, other):
#         return self.a+other.a
# c1=cal(5)
# c2=cal(7)
# print(c1+c2)

# class Encapsulation:
#     def __init__(self,balance):
#         self.__balance=balance
#     @property
#     def get_balance(self):
#         return self.__balance     
#     def withdraw(self,amount):
#         if self.__balance >amount >0:
#             self.__balance-=amount
#             return self.__balance
#         else:
#             return "you cant withdraw amount"
# e=Encapsulation(1000)
# print(e.get_balance)
# print(e.withdraw(300))
# print(e.get_balance)
          
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"name is  {self.name}")
# class Student(Person):
#     def __init__(self,name,cource):
#         super().__init__(name)
#         self.cource=cource
#     def display(self):
#         print(f"name is {self.name} and cource is {self.cource}")

# p=Student("fida","python")
# p.display()
     

# class Animal:
#     pass
# class Cat(Animal):
#     def sound(self):
#         print("meow")
# class Dog(Animal):
#     def sound(self):
#         print("bark")
# c=Cat()
# c.sound()
# d=Dog()
# d.sound()

# from abc import ABC,abstractmethod
# class Abstract(ABC):
#     @abstractmethod
#     def withdraw(self):
#         pass
#     @abstractmethod
#     def deposit(self):
#         pass
# class ATM(Abstract):
#     def __init__(self,balance):
#         self.__balance=balance
#     def withdraw(self,amount):
#         if self.__balance>amount:
#             self.__balance-=amount
#             return self.__balance
#         else:
#             return "you cant withdarw this amount"
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             return self.__balance
#         else:
#             return "you cant deposit this amount"
# a=ATM(10000)
# print(a.withdraw(1000))
# print(a.deposit(700))



# def demo():
#     x=yield 1
#     print("received: ",x)
#     # yield x
#     yield 3
# d=demo()
# print(next(d))
# print(d.send(2))    
# # print(next(d))

# try:
#     a=10
#     b=0
#     res=a/b
# except ZeroDivisionError:
#     print("you cant devide by zero")
# else:
#     print("result: ",res)   
# finally:
#     print("finished")     


# i=1
# while(i<=5):
#     print(i)
#     i+=1

# data=[1,2,3]
# data.extend([4,5])
# print(data)    
# data.insert(1,7)
# print(data)
# data.pop(3)
# print(data)
# data.reverse()
# print(data)
# print(len(data))
# print(data)
# print(data[1:2])


# data=(1,2,3)
# print(data[0])
# change=list(data)
# change[1]=4
# print(tuple(change))
# print(data.count(2))

# data={1,3,6,5,3}
# print(data)
# data.update([2,7,9,0])
# print(data)
# data.remove(9)
# print(data)

# data={x:x*x for x in range(2,10) if x%2==0}
# print(data)
# num1={"name":"fida","age":18}
# num2={"cource":'python',"place":"vkd"}
# num1.update(num2)
# print(num1)

students = {
    "student1": {
        "name": "Fida",
        "age": 20,
        "marks": {
            "Python": 90,
            "SQL": 85
        }
    },
    "student2": {
        "name": "Rahul",
        "age": 21,
        "marks": {
            "Python": 95,
            "SQL": 80
        }
    }
}
data=students["student1"]["age"]=20
print(students["student1"])
students["student2"]["marks"]["HTML"]=80
print(students["student2"]["marks"]["HTML"])
print(len(students))

for key,value in students.items():
    print(value["name"])
   
for key,value in students.items():
    print(value["name"],value["marks"]["Python"])

for key,value in students.items():
    if value["marks"]["Python"]>80:
        print(value["name"]) 
total=0           
for key,value in students.items():
    for sub,mark in value["marks"].items():
        total+=mark
print(total)    

highest=0
for key,value  in students.items():
    for sub,mark in value["marks"].items():
        if highest<mark:
            highest=mark
print(highest)            

