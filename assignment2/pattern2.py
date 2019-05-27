for i in range(5):
    for j in range(9):
        if j==i:
            print("*",end="")
        elif i==0:
            print("*",end="")
        elif j==8-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
           
