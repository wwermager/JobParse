from db import insert,close
for x in range (1, 1000):
    insert(x,"test","test",111111111111,"test","test",1)
close()
