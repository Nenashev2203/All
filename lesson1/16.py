import math
x=int(input("x= "))
y=int(input("y= "))

r1=2
r2=1

a = math.sqrt((x-1)**2+y**2);
b = math.sqrt((x-1)**2+y**2);

if a<=r1 and b>=r2 :
    print("yes", end=" ")
elif 2<=x<=6 and -1<=y<=3 :
    print("yes")
else:
    print("no")