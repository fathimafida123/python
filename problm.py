# nums=[10, 10, 20, 8, 5]
# largest=float("-inf")
# second=float("-inf")
# for n in nums:
#     if n>largest:
#         second=largest
#         largest=n
#     elif second<n and largest>n:
#         second=n

# print(second)            

# str="programming"
# dic={}
# for i in str:
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]+=1
# print(dic)        


# nums = [1, 2, 4, 5]
# for i in range(len(nums)):
#     if i not in nums:
#       print(i)

# text = "aabbcde"
# dic={}
# for i in text:
#     if i not in dic:
#         dic[i]=1
#     else:
#         dic[i]+=1            
# for key,value in dic.items():
#     if value==1:
#         print(key)
#         break

# num=int(input("enter a number"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("not a prime")    
    
 
# n=4
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#     else:
#         print("prime")

# nums = [4, 2, 7, 2, 5, 4]
# store=[]
# for i in nums:
#     if i not in store:
#         store.append(i)
#     else:
#         print(i)  
#         break  

# nums = [0, 3, 0, 5, 2, 0, 7]
# data=[]
# data2=[]
# for i in nums:
#     if i!=0:
#         data.append(i)
#     else:
#         data2.append(i)
# print(data+data2)            
    
# text = "aabbbccccdd"
# data={}
# large=float("-inf")
# second=float("-inf")
# for i in text:
#     if i not in data:
#         data[i]=1
#     else:
#         data[i]+=1
# print(data)     
# for key,value in data.items():
#     if large<value:
#         second=large
#         large=value
#     elif second<value <large:
#         second=value     
# print(second)

# text1 = "listen"
# text2 = "silent"

# data=sorted(text1)
# data2=sorted(text2)
# if data==data2:
#     print(True)
# else:
#     print(False)    

# nums = [1, 3, 2, 3, 4, 3, 2, 2, 2]
# num=max(nums,key=nums.count)#key ennu parayunnathu max() enthine base cheythu compare cheyyanam ennu parayan aanu
# print(num)


# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# data=[]
# for i in list1:
#     if i in list2 and i not in data:
#         data.append(i)
# print(data)         

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# data=[]
# for i in list1:
#     if i not in data and i not in list2:
#         data.append(i)
# print(data)        


def nums(*args):
    large=float("-inf")  
    second=float("-inf")
    for i in args:
        if i>large:
            second=large
            large=i
            print(second)            
nums(10, 5, 20, 8, 20)


class BankAccount():
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("the amount we cant deposit")
    def withdraw(self,amount):
        if amount>0 and amount<self.__balance:
            self.__balance-=amount
        else:
            print("the amout tou cant withdraw")
    def get_balance(self):
        return self.__balance
b=BankAccount(5000)
print(b.deposit(7000))
print(b.withdraw(4000))
print(b.get_balance())    
                            

def decorator(fun):
    def wrapper(name):
        fun(name.upper())
    return wrapper
@decorator
def greet(name):
    print(name)
greet("fida")    

day=3
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case _:
        print("invalid day")            

a=10
b=8
print(a is not b)        

a=10
b=a
print(a is b)

