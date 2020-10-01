a = [1, 2, "George", "32", 32, "64", 128]

A=[]
B=[]
for i in a:
    if isinstance(i, int):
        A.append(i)
    else:
        B.append(i)
print("A",A)
print("B",B)