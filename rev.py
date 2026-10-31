#COMPOSITION
#it means one class contains obj of another class to use its functionality

# class Engine:
#     def start(self):
#         print("Engine started")
# class  Car:
#     def __init__(self):
#         self.engine=Engine()
#     def start_car(self):
#         self.engine.start()    
# c=Car()
# c.start_car()       

#== , is

# a=[1,2,3]
# b=[1,2,3]
# c=b
# print(a==b)
# print(a is b)
# print(a is c)

# a=[1,2,3]
# b=a
# b.append(30)
# print(a)
# print(b)
# a=[1,2,3]
# b=a.copy()
# b.append(4)
# print(a)
# print(b)
# a=[[1,2],[3,4]]
# b=a.copy()
# b[0][0]=0
# a[0].append(99)
# b[0]=9
# print(b)
# print(a)

# import copy
# a=[[1, 2], [3, 4]]
# b=copy.deepcopy(a)
# b[0].append(99)
# print(a)
# print(b)

#LIST

# fruits=["apple","mango"]
# fruits.insert(1,"banana")
# fruits.insert(5,"orange")
# print(fruits)

# a=[1,2,4]
# b=[3,5,6]
# a.extend(b)
# print(a)

# #Removing Items
# fruits=["apple","banana","mango"]
# fruits.remove("apple")
# print(fruits)
# x=fruits.pop(1)
# print(fruits)
# print(x)

# numbers = [5, 10, 15, 20]

# x = numbers.pop()

# print(numbers)
# print(x)


# numbers = [5, 10, 15, 20, 25]
# del numbers[-1]
# print(numbers)
# del numbers

# i=1

# while i<=5:
#     print(i)
#     i+=1
# x=1    
# while x<=10:
#     print(x)
#     if x==3:
#         break
#     x+=2
# print("loop finished")    

# x=0
# while x<10:
#     x+=1
#     if x==3:
#         continue
#     print(x)    

# i=1
# while i<=2:
#     j=1

#     while j<=2:
#         print(j,i)
#         j+=1
#     i+=1    

# i=1
# total=0

# while i<=4:
#     total=total+i
#     i=i+1
# print(total)    

# i=1
# while i<=4:
#     print(i)
#     i+=1
# else:
#     print("done")    

# i=2
# while i<=6:
#     print(i)
#     if i==3:
#         break
#     i+=1
# else:
#      print("done")       

# a = (5)
# b = (5,)
# c = 5,

# print(type(a))
# print(type(b))
# print(type(c))

# student="fida",18,"python"
# print(student)

# student=("fida",18,"python")
# name,age,cource=student
# print(name)
# print(age)
# print(cource)
# print(student[:2:])
# print(student[::-1])

# print("fida" in student)

# fruits = {"apple", "banana"}
# fruits.add("mango")
# print(fruits)
# fruits.remove("apple")
# print(fruits)
# fruits.discard("orange")
# print(fruits)

# student = {
#     "name": "Fida",
#     "age": 21,
#     "cource": "Python"
# }
# student["name"]="finu"
# print(student)
# student["age"]=18
# del student["cource"]
# print(student)

# if "email" in student:
#     print("found")
# else:
#     print("not found")    

# person = {
#     "name": "Anu",
#     "age": 22,
#     "city": "Kochi",
#     "course": "Python"
# }
# count=0
# for i in person:
#     count+=1
# print(count)

# for key,value in person.items():
#     print(f"{key}:{value}")

# products = {
#     "pen": 10,
#     "book": 50,
#     "bag": 500,
#     "pencil": 5
# }
# total=0
# for i in products.values():
#     total+=i
# print(total)    

# numbers = [5, 10, 15, 20, 25]
# data={x:x for x in numbers if x>10}
# print(data)

# numbers = [1, 2, 3, 4, 5]
# data={x:x*x for x in numbers}
# print(data)

# marks = {
#     "Anu": 75,
#     "Fida": 92,
#     "Riya": 85,
#     "Maya": 68
# }
# name=""
# mark=0
# for key,value in marks.items():
#     if value>mark:
#         name=key
#         mark=value
# print(name)
# print(mark)    

# marks = {
#     "Anu": 75,
#     "Fida": 92,
#     "Riya": 85,
#     "Maya": 68,
#     "Sara": 95
# }
# for key,value in marks.items():
#     if value>80:
#         print(key,value)

#STRING

# text="HELLO WORLD"
# words=text.split('L')
# print(words)
# words = ["Python", "is", "easy"]
# result="-".join(words)
# print(result)

# text = input("Enter names separated by commas: ")
# words=text.split(",")
# print(words)
# data=[word.strip() for word in words]
# data=sorted(data)
# join=",".join(data)
# print(join)

# text=input("enter a long text : ")
# text=text.strip()
# s=text.split()
# count=0
# for i in s:
#     count+=1
# print(f"word count:{count}")
# print(text.upper())
# if "python" in text.lower():
#     print("true")
# else:
#     print("false")        
# vow="aeiou"
# count=0
# for i in text:
#     for j in vow:
#         if i==j:
#             count+=1 
# print(f"voewls: {count}")            


# data = {"a": 10, "b": 20}
# x=data.setdefault("a",30)
# y=data.setdefault("c",40)
# print(data)

# data.update({"d":50,"c":60})
# print(data)
# x=data.pop("e",0)
# print(x)
# print(data)
# x=data.popitem()
# print(x)

# keys=["name","age","cource"]
# student=dict.fromkeys(keys,"unknown")
# print(student)

# keys=["a","b","c"]
# data=dict.fromkeys(keys,0)
# print(data)

# numbers=[1,2,3,4,5]
# result={}
# for num in numbers:
#     result[num]=num*2
# print(result)

# result={num:num*2 for num in numbers}
# print(result)

# res={num:num for num in range(1,10) if num%2==0}
# print(res)

# res={n:"even" if n%2==0 else "odd" for n in range(1,10)}
# print(res)

# numbers = [10, 15, 20, 25, 30]
# res={n:"big" if n>20 else "small" for n in numbers}
# print(res)

# text="banana"
# frequency={}
# for i in text:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency[i]=1
# print(frequency)            

# products = {
#     "pen": 10,
#     "book": 60,
#     "bag": 500,
#     "pencil": 5
# }
# new_dict={}
# for key,value in products.items():
#     if value>50:
#         new_dict[key]=value
# print(new_dict)        

# stock1 = {
#     "apple": 10,
#     "banana": 5
# }

# stock2 = {
#     "banana": 7,
#     "orange": 4
# }
# new_dict=stock1.copy()

# for key,value in stock2.items():
#     if key in new_dict:
#         new_dict[key]+=value
#     else:
#         new_dict[key]=value
# print(new_dict)                
     
# numbers=[1,2,3,4,5]
# def double(num):
#     return num*2
# res=map(double,numbers)
# print(list(res))        

# res=list(map(lambda num:num*2,numbers))
# print(res)

# from functools import reduce
# names = ["Anu", "Fida", "Riya", "Maya", "Sara"]

# marks = [75, 92, 48, 85, 60]

# result=list(zip(names,marks))
# print(result)
# def assign_grade(mark):
#     if mark>=90:
#         return "A"
#     elif mark>=80:
#         return "B"
#     elif mark>=70:
#         return "C"
#     elif mark>=50:
#         return "D"
#     else:
#         return "F"
# res=list(map(assign_grade,marks))
# print(res)
# res=list(zip(names,marks,res))
# print(res)

# passStud=list(filter(lambda student:student[1]>=50,res))
# print(passStud)
# data=list(map(lambda student:student[0],passStud))
# print(data)

# total=reduce(lambda a,b:a+b,marks,0)
# average=total/len(marks)
# print(f"\nTotal marks: {total}")
# print(f"Average marks: {average}")

# #CLOSURE

# def outer():
#     number=10
#     def inner():
#         print(number+5)
#     return inner
# rs=outer()
# rs()        

# def outer():
#     count=0
#     def inner():
#         nonlocal count
#         count+=1
#         print(count)
#     inner()
#     inner()
# outer()        


# def outer():
#     x = 10

#     def inner():
#         nonlocal x
#         x = 20
        
#     inner()
#     print(x)

# outer()

# def decorator(fun):
#     def wrapper():
#         print("hyyy")
#         fun()
#         print("fidaa")
#     return wrapper    

# @decorator
# def greet():
#     print("hello")

# greet()

# def decorator(fun):
#     def wrapper(name):
#         print("hello")
#         fun(name.upper())
#         print("hyy")
#     return wrapper    
# @decorator
# def greet(name):
#     print(name)
# greet("fidaa")    

# def decorator(fun):
#     def wrapper(*args):
#         print("started")
#         result=fun(*args)
#         print("finished")
#         return result
#     return wrapper
# @decorator        
# def add(a,b):
#     return a+b

# @decorator
# def mul(a,b):
#     return a*b
# print(add(3,4))
# print(mul(4,5))    

# def prefix_decorator(prefix):
#     def decorator(fun):
#         def wrapper(name):
#             return f"{prefix},{fun(name)}"
#         return wrapper
#     return decorator    
# @prefix_decorator("hello")
# def greet(name):
#     return name
# print(greet("fidaa"))    

# def decorator(fun):
#     def wrapper():
#         print("welcome")
#         fun()
#         print("thank you")
#     return wrapper    
# @decorator        
# def greet():
#     print("hello fidaa")   

# greet()

# def decorator(fun):
#     def wrapper():
#         print("welcome")
#         fun()
#         print("thank you")
#     return wrapper    
# def greet():
#     print("fidaa")
# greet=decorator(greet)
# greet()    

# def decorator(fun):
#     def wrapper(*args):
#         print("calculation")
#         res=fun(*args)
#         print("finished")
#         return res
#     return wrapper 
# @decorator   
# def add(a,b):
#     print(a+b)
# add(4,8)    

# def decorator(fun):
#     def wrapper(*args):
#         print("calculation")
#         res=fun(*args)
#         print("finished")
#         return res
#     return wrapper 
# def add(a,b):
#     print(a+b)
# add=decorator(add)
# add(4,8)  

# def decorator(fun):
#     def wrapper(n):
#         if n>0:
#             return fun(n)
#         else:
#             print("invalid number")
#     return wrapper
# @decorator
# def square(n):
#     print(n*n)
# square(9)
# square(-7)
# square(0)

# def decorator(fun):
#     def wrapper(age):
#         if age>=18:
#             return fun(age)
#         else:
#             print("acces denied")
#     return wrapper
# @decorator
# def greet(age):
#     print("access granted")
# greet(12)
# greet(19)
# greet(18)

# def message_decorator(message):
#     def decorator(fun):
#         def wrapper():
#             print(message)
#             fun()
#         return wrapper 
#     return decorator
# @message_decorator("hyyy")
# def greet():
#     print("hello")
# greet()    

# def message_decorator(message):
#     def decorator(fun):
#         def wrapper():
#             print(message)
#             fun()
#         return wrapper
#     return decorator

# decorator_fn=message_decorator("hello")
# wrapper_fn=decorator_fn(greet)
# wrapper_fn()    

# #MAGIC METHODS

# class Student():
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name

# s=Student("fida")
# print(s)        

# class Laptop():
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __str__(self):
#         return f"{self.name} costs ₹{self.price}"    
# s=Laptop("laptop",50000)
# print(s)    

# class Laptop():
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __repr__(self):
#         return f"laptops({self.name} costs ₹{self.price})"    
# s=Laptop("laptop",50000)
# print(repr(s))    

# class Team:
#     def  __init__(self,members):
#         self.members=members
#     def __len__(self):
#         return len(self.members)
# team=Team(["fida","shamna","rinsha","hiba"])
# print(len(team))        

# class Team:
#     def  __init__(self,members):
#         self.members=members
#     def __len__(self):
#         return len(self.members)
# team=Team("fidaa")
# print(len(team))     

# class Number:
#     def __init__(self,value):
#         self.value=value
#     def __add__(self,other):
#         return self.value+other.value
# n1=Number(10)
# n2=Number(15)
# print(n1+n2)            

# class Student:
#     def __init__(self,name):
#         self.name=name
#     def __eq__(self,other):
#         return self.name==other.name
# s1=Student("fidaa")
# s2=Student("fidaa")
# s3=Student("shamna")
# print(s1==s2)
# print(s2==s3)            

# class Student:
#     def __init__(self,marks):
#         self.marks=marks
#     def __lt__(self,other):
#         return self.marks< other.marks
# s1=Student(96)
# s2=Student(90)
# print(s1>s2)

# numbers=[1,2,3]
# it=iter(numbers)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) #raises StopIteration

# class Number:
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num>=10:
#             raise StopIteration
#         value=self.num
#         self.num+=1
#         return value
# n=Number()
# print(n)
# print(next(n))    
# print(next(n))  
# for i in n:
#     print(i)       

# class Number:
#     def __init__(self):
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         value=self.num   
#         self.num+=1
#         return value
# n=Number()
# print(next(n))     
# print(next(n))  
# for i in n:
#     print(i)


# def numbers():
#     yield 1
#     yield 2
#     yield 3
# # for num in numbers():
# #     print(num)   
# n=numbers()
# print(next(n))


# # nums=(x for x in range(1,6))
# # print(next(nums))

# nums=(x**2 for x in range(1,8)) 
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))


# nums=[x*2 for x in range(1,9)]
# print(nums)

# nums = (x ** 2 for x in range(1, 5))

# print(next(nums))
# print(next(nums))
# print(next(nums))

# def numbers():
#     yield from [10,20,30]
# gen=numbers()
# print(next(gen))
# print(next(gen))
# print(next(gen))    

# def fruits():
#     data=["apple","mango","orange"]
#     yield from data
# gen=fruits()
# print(next(gen))    


# def fruits():
#     fruits=yield "apple"
#     yield fruits
# gen=fruits()
# print(next(gen))    
# print(gen.send("banana"))
    
# def fruits():
#     fruits1=yield "ready"
#     print("first received: ",fruits1)

#     fruits2=yield "next"
#     print("second received: ",fruits2)
#     yield "done"
# gen=fruits()

# print(next(gen))
# print(gen.send("banana"))
# print(gen.send("mango"))

# def fruits():
#     data=[10,20,30] 
#     yield from data
# gen=fruits()
# print(next(gen))
# print(next(gen))
# gen.close()
# # print(next(gen))


# class Numbers:
#     def generate(Self):
#         for num in range(1,8):
#             yield num
# obj=Numbers()
# gen=obj.generate()

# print(next(gen))

# class Number:
#     def generate(self):
#         for num in range(1,7):
#             if num%2==0:
#                 yield num
# c=Number()
# obj=c.generate()
# print(next(obj))                
# print(next(obj))                
# print(next(obj))                
# # print(next(obj))                

# class Student:
#     def greet(self):
#         print("helloo")
# def new_greet(self):
#     print("hyyy")
# Student.greet=new_greet
# s=Student()
# s.greet()                

# def number(num):
#     num=10
# n=4
# number(n)
# print(n)

# def change(items):
#     items.append(4)
# numbers=[1,2,3]
# change(numbers)
# print(numbers)     

# def countdown(n):
#     if n==0:
#         print("done")
#         return
#     print(n)
#     countdown(n-1)

# countdown(3)        

# def countdown(n):
#     if n==5:
#         print(n)
#         return
#     print(n)
#     countdown(n+1)
# countdown(1)    


# file=open("student.txt","w")
# file.write("fidaa\n")
# file.write("finuu")
# file.close()
# file=open("student.txt","r")
# data=file.read()
# print(data)

# with open("student.txt","r") as file:
#     data=file.readlines()
#     print(data)
# with open("student.txt","a") as file:
#     file.write("fideeyy")
# with open("student.txt","r")as file:
#     data=file.read()
# print(data)        

# with open("data.txt","w") as file:
#     file.write("hello fida")
# with open("data.txt","r") as file:
#     data=file.read()
# print(data)    

# with open("data.txt","r+") as file:
#     file.write("hi")
#     # file.seek(0)
#     data=file.read()

# print(data)    

# with open("datas.txt","w")as file:
#     file.write("hello fida")
# with open("datas.txt","w+")as file:
#     file.write("python")
#     file.seek(0)
#     data=file.read()
# print(data)    

# with open("dataa.txt","w") as file:
#     file.write("hyy")
# with open("dataa.txt","a+") as file:
#     file.write("fidaa")
#     file.seek(0)
#     print(file.read())    

# try:
#     a=int(input("enter a number: "))
#     b=int(input("enter a number: "))
#     print(a / b)
# except ZeroDivisionError:
#     print("you cannot devide number with zero")
# finally:
#     print("finished")

# try:
#     age=int("hello")
# except ValueError:
#     print("Please enter a valid number")

# try:
#     result = 10 / 2

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# else:
#     print("Result:", result)

# finally:
#     print("Program finished")   



# try:
#     number = int(input("Enter a number: "))
#     print(100 / number)

# except ValueError:
#     print("Enter numbers only")

# except ZeroDivisionError:
#     print("Number cannot be zero")     


# try:
#     number1=int(input("enter 1st number: "))
#     number2=int(input("enter 2nd number: "))

#     result=number1/number2
# except ValueError:
#     print("enter number only")
# except ZeroDivisionError:
#     print("number cannot devide by zero") 
# else:
#     print("result",result)
# finally:
#     print("calculation finished")               


# try:
#     age=-5
#     if age<0:
#         raise ValueError("age cannot be negative")
#     print("your age is",age)
# except ValueError as error:
#     print("error:",error)
# print("program completed")        


age = -5

if age < 0:
    raise ValueError("Age cannot be negative")

print("Program completed")