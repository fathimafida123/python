# numbers=[1,2,3,4,5]
# target=3
# for i in range(len(numbers)):
#     if numbers[i]==target:
#         print("elment found at index",i)
#         break
#binary search

# def binary_search(num,target):
#     low=0
#     high=len(num)-1
#     mid=(low+high)//2
#     while low<=high:
#         if num[mid]==target:
#             return mid
#         elif num[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# number=[1,2,3,4,5,6]
# print(binary_search(numbers,3))


#bubble sort

# num=[1,3,6,2,9,5]
# n=len(num)
# for i in range(n):
#     for j in range(n-i-1):
#         if num[j]>num[j+1]:
#             num[j+1],num[j]=num[j],num[j+1]
#     print(num)            

def binary_search(numbers,target):
    low=0
    high=len(numbers)-1
    while low<=high:
        mid=(low+high)//2
        if numbers[mid]==target:
            return mid
        elif numbers[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

num=[1,2,3,4,5,6,7]
print(binary_search(num,1))           

num=[1,3,2,4,6,5,7,9,8]
n=len(num)
for i in range(n):
    for j in range(n-i-1):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
print(num)            

#selection sort

num=[64,25,12,22,11]
n=len(num)

for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if num[min_index]>num[j]:
            min_index=j
        num[i],num[min_index]=num[min_index],num[i]
print(num)         

