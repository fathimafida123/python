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

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=node1
print(node2.data)        

node1=Node(20)
node2=Node(30)
node1.next=node2
print(node1.next.data)