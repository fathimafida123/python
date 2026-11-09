#stack
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)
stack.pop()
print(stack)
top=[stack[-1]]
if stack:
    print("stack element:",top)
else:
    print("stack is empty")    
