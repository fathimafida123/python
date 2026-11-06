#single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#create nodes
first=Node(10)
second=Node(20)
third=Node(30)


#connect nodes
first.next=second
second.next=third

#Head
Head=first

#get output

current=Head
while current is not None:
    print(current.data)
    current=current.next
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
print(head.data)
print(head.next.data)
print(head.next.next.data)        