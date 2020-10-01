a = [1, 11, 23, 44, 54, 76, 9, 76, 32, 4, 565, 87, 545]

A=[]
B=[]
for i in a:
    if(i%2==0):
        A.append(i)
    else:
        B.append(i)
print("A",A)
print("B",B)