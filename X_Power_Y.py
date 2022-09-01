x=int(input("Enter a number for base x : "))
y=int(input("Enter a number for index y : "))
power=1
for count in range(1,y+1):
    power*=x
print(x,"^",y,"=",power)
      
