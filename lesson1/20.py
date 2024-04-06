x=float(input())
n=-1
a=0.00000001
rez=1
s=0
while abs(rez)>a:
    n += 1
    rez = (((-1)**(n))*(x**(n+1))/(n+1)
    s += rez

print(round(s, 8))