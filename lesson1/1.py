room=int(input())
room1= (room%8)
entrance=(room//8)+1
if (room % 8) == 0:
    room1=8
    entrance=(room//8)
print (room1, entrance)