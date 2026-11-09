# #stack
# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
# stack.append(40)
# print(stack)
# stack.pop()
# print(stack)
# top=[stack[-1]]
# if stack:
#     print("stack element:",top)
# else:
#     print("stack is empty")    

#stack using linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.top is None:
            print("list is empty")
            return
        removed=self.top.data
        self.top=self.top.next
        print(removed,"removed")
    def peek(self):
        if self.top is  None:
            print("list is empty")
        else:
            print("element:",self.top.data) 
    def display(self):
        current=self.top
        while current is not None:
            print(current.data) 
            current=current.next


s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.peek()                