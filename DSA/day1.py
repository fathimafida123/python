#linearithmic
n = 8

for i in range(n):
    j = n

    while j > 1:
        j = j // 2
        print(i, j)

#TASK
def find_max(num):
    maximum=num[0]
    for i in num:
        if i>maximum:
            maximum=i
    print(maximum)    

find_max([41,22,23,14,54,16])                

