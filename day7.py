# f = open("student.txt", "w")
# f.write("My name is Fida \n")
# f.write("I am learning Python\n")
# f.write("File handling is easy")
# f.close()

# f=open("student.txt","r")
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# f=open("student.txt","w")
# f.write("apple ")
# f.write("mango ")
# f.write("banana ")
# f.close()
# f=open("student.txt","r")
# print(f.readlines())
#it show the \n inside list to avoid this we can use strip

# f=open("student.txt","w")
# f.write("apple \n")
# f.write("mango \n")
# f.write("banana \n")
# f.close()
# f=open("student.txt","r")
# data=f.readlines()
# print(data[0].strip())
# print(data[1].strip())
# print(data[2].strip())
# f.close()
#if i have loats of data this method felt very difficult

# f=open("student.txt","w")
# f.write("apple \n")
# f.write("mango \n")
# f.write("banana \n")
# f.close()
# f=open("student.txt","r")
# data=f.readlines()
# print(type(data))
# for line in data:
#     print(line.strip())
# f.close()

# #APPEND

# f=open("student.txt","w")
# f.write("apple \n")
# f.write("mango \n")
# f.write("banana \n")
# f.close()
# f=open("student.txt","w")
# f.write("orange \n")
# f.close()
# f=open("student.txt","a")
# f.write("grapes \n")
# f.close()

# f=open("student.txt","r")
# data=f.readlines()
# print(type(data))
# for line in data:
#     print(line.strip())
# f.close()

# with open("student.txt","w") as f:
#     f.write("banana\n")
#     f.write("apple")
# with open("student.txt","r")as f:
#     print(f.tell())
#     print(f.read(6))
#     print(f.tell())
#     print(f.read(6))
#     print(f.tell())
#     f.seek(3)
#     print(f.read())
#     f.seek(7,2)
#     print(read())

#MAP
# def double(n):
#     return n*2
# numbers=[1,2,3,4]
# result=map(double,numbers)
# print(list(result))    

# def square(n):
#     return n*n
# numbers=[5,4,3,8]
# result=map(square,numbers)
# print(list(result))    

# numbers=["10","30","60"]
# result=map(int,numbers)
# print(list(result))

# names=["apple","mango","banana"]
# result=map(str.upper,names)
# print(list(result))

# names=["apple","Mango","banana"]
# result=map(str.lower,names)
# print(list(result))

# numbers=[1,2,3,4]
# result=map(str,numbers)
# print(list(result))

# #FILTER
# numbers=[1,2,3,5,6]
# result=filter(lambda n:n<5,numbers)
# print(list(result))


# def num(n):
#     return n<5
# numbers=[1,2,3,5,6]
# result=filter(num,numbers)
# print(list(result))

# #REDUCE
# from functools import reduce
# numbers=[1,2,3,4,6]
# result=reduce(lambda a,b:a+b,numbers)
# print(result)

# numbers=[1,4,5,7,9]
# result=reduce(lambda a,b:a*b,numbers)
# print(result)

# #ZIP()

# names=["fida","finu","moluse"]
# nums=[1,2,3,4,6]
# result=zip(names,nums)
# print(list(result))

# def outer():
#     message="hello"
#     def inner():
#         print(message)
#     return inner
# result=outer()
# result()        

# #DECORATOR

# def my_decorator(fun):
#     def wrapper():
#         print("before fn")
#         fun()
#         print("after fn")
#     return wrapper
# def greet():
#     print("hello")
# greet=my_decorator(greet)
# greet()            

# def decorator(func):
#     def wrapper():
#         print("start")
#         func()
#         print("end")
#     return wrapper    
# def greet():
#     print("hello")
# result=decorator(greet)
# result()    

#@DECORATOR
# def my_decorator(func):
#     def wrapper():
#         print("start")
#         func()
#         print("end")
#     return wrapper
# @my_decorator   
# def greet():
    # print("hello")

# greet()
# #The decorator returns the wrapper function.Python assigns that returned function to the name greet. thats why we use the greet()
# import time

# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print("Time taken:", end - start, "seconds")
#     return wrapper

# @timer
# def greet():
#     print("Hello!")

# greet()
class Student:
    def __str__(self):
        return "Hello Fida"

s1 = Student()

print(s1)     

class Student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "hello "+self.name    
s1=Student("fida")
print(s1)

class Student:
    def __str__(self):
       return "fidaa"

s=Student()
print(s)        

class Student:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f"Student('{self.name}')"    
s=Student("fida")
print(repr(s))


class Student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"student name:{self.name}" 
    def __repr__(self):
        return f"Student({self.name})"      
s=Student("fidaa")
print(s)
print(repr(s))

class Student:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        return len(self.name)    
c=Student("fidaaa")
print(len(c))   

class Student:
    def __init__(self):
        self.names=["fida","finu","shamna"]
    def __len__(self):
        return len(self.names)
c=Student()
print(len(c))        

class Number:
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        return self.value+other.value 
a=Number(5)
b=Number(4)
print(a+b)           

class Number:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value

a = Number(10)
b = Number(4)

print(a - b)

class Number:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        return self.value / other.value

a = Number(20)
b = Number(4)

print(a / b)

#CALL BY VLAUE AND REFERENCE
def change(x):
    x=10
a=3
change(a)    
print(a)

def change(items):
    items[1]=99
data=[10,20,30]    
change(data)
print(data)

def change(item):
    items=[4,5,6]
data=[2,3,1]
change(data)
print(data)    

def change(item):
    item.append(4)
data=[1,2,3]
change(data)
print(data)    

class Animal:
    def sound(self):
        print("original sound")
def new_sound(self):
    print("new sound")
Animal.sound=new_sound

a=Animal()
a.sound()