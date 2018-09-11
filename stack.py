y=int(input( ) )
stack=[]
for i in range(y):
    a=int(input())
    stack.append(a)
for n in stack:
    print(stack)
    stack.pop()
    print(stack)
print("poping all the elements one by one in LIFO manner")
