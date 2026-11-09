# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node(10)
# node2=Node(20)
# node3=Node(30)

# node1.next=node2
# node2.next=node3

# head=node1
# current=head

# while current is not None:
#     print(current.data,end="->")
#     current=current.next

# #insert at beginning

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def add(self,head,data):
#         new_data=Node(data)
#         new_data.next=head
#         head=new_data
#     def display(self):
#         current=head
#         while current is not None:
#             print(current.data,end="->")
#             current=current.next
# head=Node(10)         
# head.next=Node(20)
# head.next.next=Node(30)
# head.next.next.next=Node(40)
# head.next.next.next.next=Node(50)

# ll=LinkedList()
# ll.add(head,60)
# ll.display()


# #insert at end

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def add(self,head,data):
#         new_data=Node(data)
#         if head is None:
#             head=new_data
#             return head
#         current=head
#         while current.next is not None:
#            current=current.next
#         current.next=new_data
#         return head
#     def display(self,head):
#         current=head
#         while current:
#             print(current.data,end="->")
#             current=current.next
# ll=LinkedList()
# head=None
# head = ll.add(head, 10)
# head = ll.add(head, 20)
# head = ll.add(head, 30)
# head = ll.add(head, 40)
# head = ll.add(head, 50)

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:        
#     def add(self,head,data):
#         new_data=Node(data)
#         if head is None:
#             head=new_data
#             return head
#         current=head
#         while current.next is not None:
#             current=current.next
#         current.next=new_data
#         self.display(head)
#         return head
#     def display(self,head):
#         current=head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("None")    
# ll=LinkedList()
# head=None
# head=ll.add(head,10)
# head=ll.add(head,20)
# head=ll.add(head,30)
# head=ll.add(head,40)
# head=ll.add(head,50)

# ll.display(head)        
                


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
# # insert at the beginning
#     def add_first(self,data):
#         newnode=Node(data)
#         newnode.next=self.head
#         self.head=newnode
   
# # # insertion at the end
#     def add_end(self,data):
#         newnode=Node(data)
#         if self.head is None:
#             self.head=newnode
#             return
#         current=self.head
#         while current.next is not None:
#             current=current.next
#         current.next=newnode
   
# # insertion at a specific position
#     def add_position(self,data,position):
#         newnode=Node(data)
#         if position == 0:
#             newnode.next=self.head
#             self.head=newnode
#             return
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         newnode.next=current.next
#         current.next=newnode
  
#     def delete_first(self):
#         if self.head is None:
#             print("listis empty")
#             return
#         self.head=self.head.next
#     def delete_end(self):
#         if self.head is None:
#               print("list is empty")
#               return
#         current=self.head
#         while current.next is not None:
#              current=current.next
#         current.next=None
#     def delete_position(self,position):
#         if self.head is None:
#             print("the list is empty")
#             return
#         current=self.head
#         for i in range(position-1):
#             current=current.next
#         current.next=current.next.next

#     def display(self):
#             current=self.head
#             while current is not None:
#                 print(current.data,end=" -> ")
#                 current=current.next
#             print("None")



# l1=Linkedlist()
# l1.add_first(10)
# l1.add_first(20)
# l1.add_first(30) 
# l1.add_first(40)
# l1.add_first(50)

# l1.add_end(5)

# l1.add_position(25,3)

# l1.delete_first()

# l1.delete_end()
# l1.delete_position(2)


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node
    def add_position(self,data,position):
        new_node=Node(data)    
        if position==0:
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        for i in range(position-1):
            current=current.next
        new_node.next=current.next
        current.next=new_node
    def delete_first(self):
        if self.head is None:
            print("head is empty")
            return
        self.head=self.head.next  
    def delete_end(self):
        if self.head is None:
            print("list is empty")
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=None 
    def delete_position(self,position):
        current=self.head
        for i in range(position-1):
            current=current.next
        current.next=current.next.next        
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end="->")
            current=current.next
ll=LinkedList()
ll.add(10)       
ll.add(20) 
ll.add(30) 
ll.add(40)    
ll.add_end(80)  
ll.add_position(60,3)
ll.delete_end()
ll.delete_first()
ll.delete_position(2)
ll.display()



                