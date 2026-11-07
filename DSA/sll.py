class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)

node1.next=node2
node2.next=node3

head=node1
current=head

while current is not None:
    print(current.data,end="->")
    current=current.next

#insert at beginning

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def add(self,head,data):
        new_data=Node(data)
        new_data.next=head
        head=new_data
    def display(self):
        current=head
        while current is not None:
            print(current.data,end="->")
            current=current.next
head=Node(10)         
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)

ll=LinkedList()
ll.add(head,60)
ll.display()


#insert at end

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def add(self,head,data):
        new_data=Node(data)
        if head is None:
            head=new_data
            return head
        current=head
        while current.next is not None:
           current=current.next
        current.next=new_data
        return head
    def display(self,head):
        current=head
        while current:
            print(current.data,end="->")
            current=current.next
ll=LinkedList()
head=None
head = ll.add(head, 10)
head = ll.add(head, 20)
head = ll.add(head, 30)
head = ll.add(head, 40)
head = ll.add(head, 50)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:        
    def add(self,head,data):
        new_data=Node(data)
        if head is None:
            head=new_data
            return head
        current=head
        while current.next is not None:
            current=current.next
        current.next=new_data
        self.display(head)
        return head
    def display(self,head):
        current=head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")    
ll=LinkedList()
head=None
head=ll.add(head,10)
head=ll.add(head,20)
head=ll.add(head,30)
head=ll.add(head,40)
head=ll.add(head,50)

ll.display(head)        
                