# heron's formula  (s(s-a)(s-b)(s-c))**1/2 
# where s is semiperimeter, s=(a+b+c)/2 and a,b,c are sides of triangle

a=int(input("Enter 1st side of triangle:"))
b=int(input("Enter 2nd side of triangle:"))
c=int(input("Enter 3rd side of triangle:"))

sum1=a+b
sum2=b+c
sum3=a+c

if (a or b or c) <=0:
    print("input side greater than zero")
else:
    pass

if c<sum1 and a<sum2 and c<sum3 :
    print("triangle is possible")
else:
    print("triangle not possible")

def area():
    s=(a+b+c)/2
    print("area of triangel is" , (s*(s-a)*(s-b)*(s-c))**0.5 )

area()