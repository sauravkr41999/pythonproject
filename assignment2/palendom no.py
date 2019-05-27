print("enter the no")
a=int(input())
x=a
c=0
while(a>0):
    b=a%10
    a=a//10
    c=c*10+b
if c==x:
    print("given no is palendom")
else:
    print("given no is not palendom")
    
