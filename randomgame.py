import random
r=random.randint(0,100)
x=0
while 1:
    print ("guess a no")
    inv=int(input())
    if inv == r:
        break
    elif inv > r:
        print('you choose a larger no')
        x+=1
    elif inv < r:
        print("you choose a smaller no")
        x+=1

print("your points are " )
print(100-x)
