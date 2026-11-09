numbers=[1,2,3,4,5]
target=3
for i in range(len(numbers)):
    if numbers[i]==target:
        print("elment found at index",i)
        break
#binary search

def binary_search(num,target):
    low=0
    high=len(num)-1
    mid=(low+high)//2
    while low<=high:
        if num[mid]==target:
            return mid
        elif num[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
number=[1,2,3,4,5,6]
print(binary_search(numbers,3))


#bubble sort

num=[1,3,6,2,9,5]
n=len(num)
for i in range(n):
    for j in range(n-i-1):
        if num[j]>num[j+1]:
            num[j+1],num[j]=num[j],num[j+1]
print(num)            