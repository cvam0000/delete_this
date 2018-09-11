y=int(input( ) )
stack=[]
for i in range(y):
    a=int(input())
    stack.append(a)
p=0
for b in range(y):
    print(stack)
    stack.pop(p)

print("poping all the elements one by one in FIFO manner")
