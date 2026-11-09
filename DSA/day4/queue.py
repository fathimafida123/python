# #queue
# #list
# queue=[]
# queue.append(10)
# queue.append(20)
# queue.append(30)

# queue.pop(0)
# data=queue[0]
# print(queue)
# print(data)

#linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def Enqueue(self,data):
        new_node=Node(data)
        if self.rear is None:
            self.front=new_node
            self.rear=new_node
            return 
        self.rear.next=new_node
        self.rear=new_node
    def Dequeue(self):
        if self.front is None:
            print("list is empty")
            return
        removed=self.front.data
        self.front=self.front.next
        print(removed)
        if self.front is None:
            self.rear=None

    def display(self):
        current=self.front
        while current:
            print(current.data,end="->")
            current=current.next
        print(None)    
q=Queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Dequeue()
q.display()