# dict

# stu={
#     "name":"fida",
#     "age":18,
#     "place":"vazhakkad",

# }

# stu["name"]="fathima fida"
# stu.update({"cource":"python"})
# print(stu.get("city","not available"))
# print(stu.pop("age"))
# print(stu)
# stu.clear()
# print(stu)
# stu["name"]="fida"
# print(stu.keys())
# print(stu.values())
# print(stu.items())
# student={}
# student["name"]="fida"
# print(student)

# person = dict(name="Amina", age=20)
# print(person)

marks={
    "maths":99,
    "physics":86,
    "biology":90
}

for i in marks.keys():
    print(i)
for i in marks.values():
    print(i)
for i in marks.items(): #it stores data inside tuple
    print(i)    
for sub,mark in marks.items(): #it store in seperate variable
    print(sub,mark)
# students={
#     "student1":{"name":"fida",
#     "age":18,
#     "course":"python"},
#     "student2":{
#         "name":"shamna",
#         "age":17,
#         "cource":"react"
#     }
# }
# print(students["student1"]["name"])
# print(students["student2"]["name"])

# student = {
#     "name": "Amina",
#     "age": 20,
#     "course": "Python"
# }
# for stu,det in student.items():
#     print(stu,det)
# # Comprehension
# data={}
# for i in range(1,4):
#     data[i]=i*i
# print(data)

# data={i:i*i for i in range(1,4)}
# print(data)

# data={i:i*2 for i in range(1,6)}
# print(data)

# data={i:i*i for i in range(1,12)if i%2==0}
# print(data)

# data={i:i**3 for i in range(1,8) if i>5}
# print(data)


        

# marks = {
#     "Amina": 85,
#     "Rahul": 35,
#     "Fathima": 92,
#     "Arun": 28
# }
# data={name:mark for name,mark in marks.items() if mark>50 }
# print(data)

# prices = {
#     "Food": 200,
#     "Toy": 150,
#     "Bed": 800
# }

# data={name:price+50 for name,price in prices.items()}
# print(data)

# stu={
#     "name":"fida",
#     "name":"finu"
# }
# print(stu)

# del stu
# print(stu)

# copy()
# students={
#     "name":"fida",
#     "name":"shamna"
# }
# new_student=students.copy() #it creates seperate shallow copy
# new_student["name"]="rinsha"
# new_student["age"]=18
# print(students)
# print(new_student)

# setdefault()

# students={
#     "name":"fida",
#     "age":20
# }
# print(students)
# res=students.setdefault('age',25)
# print(res)
# #The "age" key already exists, so setdefault() returns its current value, 20. It does not replace it with 25.

# students={
#     "name":"fida",
#     "age":20
# }
# print(students)
# res=students.setdefault("city","malappuram")
# print(students)
# print(res)

# #nested dict
# student={
#     "student1":{
#     "name":"fida",
#     "age":18
#     },
#     "student2":{
#     "name":"shamna",
#     "age":17
#     }
# }
# # print(student["student1"])
# # student["student2"]["age"]=18
# # print(student["student2"]["age"])
# student["student3"]={
#     "name":"rinsha",
#     "age":18
# }
# # print(student["student3"])
# # print(student)
#  #remove items
# student["student1"].clear()
# print(student)
# rem=student["student2"].pop("age")
# print(rem)
# print(student)

# # student.clear()
# # print(student)

# student["student3"].popitem()
# print(student)

# # looping 
# for i in student.items():
#     print(i)  #it  returns data inside tuple the key and value stored inside i

# for key,item student.items():
#     print(key,item)     #it seperate key ,value 

# students={
#     "student1":{
#        "name":"fida",
#        "age":18
#     },
#     "student2":{
#         "name":"shamna",
#          "age":17
#     }
# }

# for i in students.values():
#     print(i["name"])

# numbers=[10,4,7,5]
# result={}
# for n in numbers:
#     if n>8:
#         result[n]="yes"
#     else:
#         result[n]="no"
# print(result)        

# #comprehension

# result={n:"yes" if n>7 else "no" for n in numbers}
# print(result)

# numbers=[-1,2,0]
# result={n:"positive" if n>0 else "zero" if n==0 else "negative" for n in numbers}
# print(result)

# deepcopy and shallowcopy
# import copy
# a={
#     "cource":"python",
#     "student1":{
#         "name":"fida"
#     }
# }
# b=a.copy()
# b["student1"]["name"]="shamna"
# b["cource"]="react"
# print(a)
# print(b)

# deepcopy

# b=copy.deepcopy(a)
# b["cource"]="react"
# b["student1"]["name"]="shamna"
# print(a)
# print(b)

# problms

# numbers = [1, 2, 2, 3, 3, 3, 4]
# count={}
# for n in numbers:
#     if n in count:
#         count[n]+=1
#     else:
#         count[n]=1
# print(count)        

# marks = {
#     "Fida": 85,
#     "Anu": 92,
#     "Shamna": 78,
#     "Riya": 95
# }
# highestname=""
# highestmark=0
# for name,mark in marks.items():
#     if mark>highestmark:
#         highestmark=mark
#         highestname=name
# print(highestname)        
# print(highestmark)           

# STRINGS

# def square(n):
#     """Returns the square of a number."""
#     return n * n
# print(square(5))
# print(square.__doc__)

# word="fidaa"
# print(word[1:3])
# print(word[::2])
# print(word[::-1])

# word="python programming"
# print(word.upper())
# word="banana"
# print(word.count("a"))
# word="  Hello World  "
# print(word)
# print(word.strip())
# word="I like apple"
# print(word.replace("apple","orange"))
# word="hi"
# print(word.center(10,"*"))
# letter="1234"
# print(letter.isdigit())
# word="python"
# res=word[::-1]
# print(res)

# word="programming"
# count=0
# for i in word:
#     if i in "aeiou":
#         count+=1
# print(count)    

# word="madam"
# rev=word[::-1]
# if word==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

# text = "banana"
# result=""
# for i in text:
#     if i not in result:
#         result+=i
# print(result)        

# text = "Python is easy to learn"
# spl=text.split(" ")
# print(len(spl))

# text = "banana"
# maxcount=0
# maxchar=""
# for i in text:
#     c=text.count(i)
#     if c>maxcount:
#         maxchar=i
#         maxcount=c
       
# print(maxchar)   
# print(maxcount)

# # f-string
# name="fida"
# print(f"hello {name}") #F-strings are especially useful when a sentence contains several variables
# print("helllo", name)   

# a=10
# b=5
# print(f"total={a+b}")

# # Using f-strings with decimal numbers
# price = 99.5678

# print(f"Price: {price:.2f}") #:.2f means display two digits after the decimal point.

