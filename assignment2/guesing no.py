print("enter the value between 1 to 15")
import random
a=random.randint(1,15)
c=0
d=3
for i in range (3):
    b=int(input())
    if a==b:
        c=c+1
        break
    else:
        print("your entered value does not match")
        d-=1
        print("attempts left are"+str(d))
if c==1:
    print("you won")
else:
    print("you lost")
    print("value of a is"+str(a))

