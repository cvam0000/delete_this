def cvam_fucvtion(a):
    big=0
    t=0
    for x,y in a.items():
        if big<= y:
            big=y
            t=x
    print("the man of the matc is ",t)
a={"sachin":100 ,"virat":45,"rohit":500}
cvam_fucvtion(a)
