a=0
b=1
c=2
for i in range(10):
    d=a+b+c
    a=b
    b=c
    c=d
    print(d)
