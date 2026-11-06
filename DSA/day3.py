# #single linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# #create nodes
# first=Node(10)
# second=Node(20)
# third=Node(30)


# #connect nodes
# first.next=second
# second.next=third

# #Head
# Head=first

# #get output

# current=Head
# while current is not None:
#     print(current.data)
#     current=current.next
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# head=Node(10)
# head.next=Node(20)
# head.next.next=Node(30)
# print(head.data)
# print(head.next.data)
# print(head.next.next.data)     

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# node1=Node(10)
# node2=node1
# print(node2.data)        

# node1=Node(20)
# node2=Node(30)
# node1.next=node2
# print(node1.next.data)

# # list to linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def list_link(number):
#     head=None
#     current=None
#     for value in number:
#         new_value=Node(value)
#         if head is None:
#            head=new_value
#            current=new_value
#         else:
#             current.next=new_value
#             current=new_value
#     return head              
# data=[10,20,30,40]
# print(list_link(data))
 
# result=list_link(data)
# current=result
# res=[]
# while current is not None:
#     res.append(current.data)
#     current=current.next
# print(res)    
    
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def link_list(numbers):
#     head=None
#     current=None
#     for value in numbers:
#         new_value=Node(value)
#         if head is None:
#             head=new_value
#             current=new_value
#         else:
#             current.next=new_value
#             current=new_value
#     return head

# data=[10,20,30,40]
# result=link_list(data)
# current=result
# while current is not None:
#     print(current.data,end=" -> ")
#     current=current.next


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
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" -> ") 
            current=current.next
        print("None")
ll=LinkedList()
ll.add(10)
ll.add(20)
ll.display()


            
             
        
        

        

            
                