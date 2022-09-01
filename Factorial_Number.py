product=1
N=int(input("Enter a number= "))
for i in range(N,0,-1):
    product*=N
print(N,"*",i,"=",product)
