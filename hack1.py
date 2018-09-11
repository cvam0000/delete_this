physics=[]
a=int(input())
for b in range(a):
    name=str(input())
    marks=float(input())
    na=[]
    ma=[]
    na.append(name)
    ma.append(marks)
    new=[]
    new.extend(na)
    new.extend(ma)
    physics.append(new)
    del na,ma,new
print(physics)
manku=0
rama=[]
for tatti in range(a):
    rama.append(physics[manku][1])
    manku+=1

for bharti in range(a):
    
