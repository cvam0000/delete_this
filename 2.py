x=int(input())
cvam_list=[]
for i in  range(0,x):
    f=float(input())
    cvam_list.append(f)
print(cvam_list)
a=0
b=0
for v in cvam_list:
    if v>=a:
        b=a
        a=v
    elif v<=a:
                if v>=b:
                    b=v
print(int(b))
