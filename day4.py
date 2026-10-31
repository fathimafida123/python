# function

# def calculate_total(price,quantity):
#     total=price*quantity
#     print(f"total price:₹{total}")

# calculate_total(100,200)   
# calculate_total(950,455) 

# def square(a):
#     square=a*a
#     print(f"square of {a}:{square}")
# square(5)

# def x(a,b):
#     return a+b

# def y(a,b):
#     print(a+b)    
# result=x(3,6)
# print(result)    

# res=y(5,8)
# print(res)

#DEFAULT PARAMETER
# def greet(name="fidaaa"):
#     print(f"hello,{name}")
# greet()
# greet("finuuu")    

#POSITIONAL AND KEYWORD ARGUMNET

# def greet(age,name):
#     print("name:",name,"age:",age)
# greet("fida",18)
# greet(age=18, name="fidaa")

#*ARGS

# def numbers(*args):
#     total=0
#     for i in args:
#          total+=i
#     print(total)

# numbers(1,4,8,3,9,2)

# def calculate(*numbers):
#     ans=(numbers[0]+numbers[2])*numbers[2]
#     print(ans)        
# calculate(5,3,8)    

#**KWARGS

# def student_details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")
# student_details(name="Fathima", age=20, course="Python", place="Malappuram")

# def calculate_marks(**kwargs):
#     total=0
#     for key,value in kwargs.items():
#         total+=value
#     print(total)
# calculate_marks(Maths=80, English=75, Science=90)

#RECURSION

# def fun(n):
#     if n==1:
#         return 1
#     print(n)
#     fun(n-1)
# fun(5)

#FACTORIAL

# def fun(n):
#     if n==1:
#         return 1
#     return n*fun(n-1)    
# print(fun(3))

#FIBONACCI
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     return fibonacci(n - 1) + fibonacci(n - 2)

# for i in range(7):
#     print(fibonacci(i), end=" ")

#LAMBDA
add=lambda a,b:a+b
print(add(10,20))

check=lambda n:"even" if n%2==0 else "odd"
print(check(4))

big=lambda a,b:f"{a} is bigger" if a>b else f"{b} is bigger"
print(big(2,6))

square=lambda a:a*a
print(square(6))

sub=lambda a,b:a-b
print(sub(50,20))

num=lambda n: "positive" if n>0 else "negative" if n<0 else "zero"
print(num(0))

#map

# num=[1,2,3,4]
# res=list(map(lambda n:n*2,num))
# print(res)

# #filter

# num=[3,5,6,7,8]
# res=list(filter(lambda n:n%2==0,num))
# print(res)

#EXCEPTION HANDLING
try:
    a=10
    b=2
    print(a/b)
except ZeroDivisionError:
    print("error occured")
else:
    print("there is no error")
finally:
    print("finished")        

try:
    print(int("name"))    
except ValueError:
    print("invalid input")    
else:
    print("valid input")    
finally:
    print("finished")    