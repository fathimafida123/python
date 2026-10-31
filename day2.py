# list

# number=[10,60,80,40]
# number.append(50)
# print(number)
# number.remove(10)
# print(number)
# number.pop(2)
# print(number)
# number.sort()
# print(number)
# print(len(number))
# print(number[1:2]) #slice
 
# #  change tuple value by converting into list
# number=(1,2,3,5)
# data=list(number)
# data[3]=4
# changed=tuple(data)
# print(changed)

# fruits=("apple","mango","orange")
# # for fruit in fruits:
# #     print(fruit)
# for i in range(len(fruits)):
#     print(i,fruits[i])

# fruits = {"apple", "mango", "orange"}

# # for fruit in fruits:
# #     print(fruit)
# print("apple" not in fruits)

# setMethods & operations

# a={1,2,3,4}
# b={3,4,5,7}
# print(a&b)
# print(a-b)
# print(a|b)

# number=[10,15,8,20]
# for num in number:
#     if num>10:
#         print(num)

#       print even numbers
# numbers=[10,22,33,40,55]  
# for i in numbers:
#     if i%2==0:
#         print("even: ",i)
#     else:
#         print("odd: ",i)     

# numbers=[-1,3,-5,6,8]
# for i in numbers:
#     if i>0:
#         print(i)

# numbers = [5, 12, 20, 30, 18, 25]
# for i in numbers:
#     if i>10 and i<25:
#         print(i)

# numbers = [12, -4, 7, 8, -6, 10, 3, 0]
# for i in numbers:
#     if i>0 and i%2==0:
#         print(i)

# numbers = [12, 5, 8, 3, 10, 7, 4]

# oddcount = 0
# evencount = 0

# for i in numbers:
#     if i % 2 == 0:
#         evencount += 1
#     else:
#         oddcount += 1

# print("Even numbers:", evencount)
# print("Odd numbers:", oddcount)  

# a=20
# b=40
# c=10
# if a>b and a>c:
#     print("a is largest")
# elif b>c:
#     print("b is largest")
# else:
#     print("c is largest")        

# sort
# list

# numbers=[1,9,4,5,8]
# # numbers.sort()
# result=sorted(numbers)
# print(numbers)
# print(result)
 
#  tuple

#  sort  in tuple we can't use sort bcz its immutable
#  we can use sorted it returns new sorted list. but it return in a list
# numbers=(1,4,2,3,7)
#  numbers.sort()
# result=sorted(numbers)
# print(numbers)
# print(result)
# result=tuple(sorted(numbers))
# print(result)

# set
# Sets do not have a .sort() method because they are unordered collections.
# numbers={1,4,2,6,4,7}
# result=sorted(numbers)
# print(result)
# print(set(result))

# Q1. Change a list item
# Create a list [10, 20, 30] and change 20 to 50.

# number=[10, 20, 30]
# number[1]=50
# print(number)

# # Create name = "Python". Try changing the first character to "J". Observe the result and explain why.

# name="python"
# # name[0]="J"
# # print(name) #string is immutable we cant change

# name="J"+name[1:]
# print(name)

# List vs tuple

# datal=[1,2,3]
# datat=(1,2,3)
# datal[1]=4
# print(datal)
# change=list(datat)
# change[1]=4

# print(tuple(change))

# fruits = ["apple", "banana"]
# fruits.append("mango")
# print(fruits)

# numbers = [10, 20, 30, 40]
# numbers[2]=35
# print(numbers)

# numbers=[1, 2, 2, 3, 3, 4]

# unique=[]
# for i in numbers:
#       if i not in unique:
#             unique.append(i)
 
# print(unique)

# number=[10, 20, 30, 40]
# total=0
# for i in number:
#       total+=i
# print(total)      
