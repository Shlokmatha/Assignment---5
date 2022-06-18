a=int(input("Enter first number of range: "))
b=int(input("Enter last number of range: "))
c=int(input("Enter the divisor : "))

for i in range(a,b):
    if i==0:
        pass
    elif i%c==0:
        print(i)
