a=0
for i in range(4,-1,-1):
    for j in range(9):
        if j==i:
            print("*",end="")
        elif i==0:
            print("*",end="")
        elif j==i+a:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    a=a+2
 
