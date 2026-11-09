
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def add_start(self,data):
        newnode=Node(data)
        if self.head is not None:
            newnode.next=self.head
            self.head.prev=newnode
        self.head=newnode
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return 
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=newnode
        newnode.prev=current
    def add_position(self,data,position):
        newnode=Node(data)
        current=self.head
        for i in range(position-1):
            current=current.next
        newnode.next=current.next
        newnode.prev=current
        current.next.prev=newnode
        current.next=newnode
    def delete_first(self):
        self.head=self.head.next 
        self.head.prev=None
    def delete_end(self):
        current=self.head
        while current.next is not None:
            current=current.next
        current.prev.next=None
        current.prev=None
    def delete_position(self,position):
        current=self.head
        for i in range(position-1):
            current=current.next
        current.next=current.next.next
        if current.next is not None:
            current.next.prev=current
        
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" <-> ")
            current=current.next
        print("NONE")
dll=DoublyLinkedList()
dll.add_start(50)
dll.add_start(40)
dll.add_start(30)
dll.add_start(20)
dll.add_start(10)
dll.add_end(60)
dll.add_position(25,2)
dll.delete_first()
dll.delete_end()
dll.delete_position(1)
dll.display()

