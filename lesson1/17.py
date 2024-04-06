x = input()
a = list (x)
l=a[0]
m=int(a[1])
if l == "a":
    c = 1
elif l == "b":
    c = 2
elif l == "c":
    c = 3
elif l == "d":
    c = 4
elif l == "e":
    c = 5
elif l == "f":
    c = 6
elif l == "g":
    c = 7
elif l == "h":
    c = 8
if (c+m)%2 == 0:
    print ("black")
else:
   print ("white")