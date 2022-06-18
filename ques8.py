num1=int(input("Enter 1st number :"))
num2=int(input("Enter 2nd number :"))
num3=int(input("Enter 3rd number :"))
num4=int(input("Enter 4th number :"))
num5=int(input("Enter 5th number :"))
num6=int(input("Enter 6th number :"))
num7=int(input("Enter 7th number :"))
num8=int(input("Enter 8th number :"))
num9=int(input("Enter 9th number :"))
num10=int(input("Enter 10th number :"))

a=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]

# part 1
print("positive number are")
for i in a:
    
    if i>0:
        print( i)
# part 2
print("negative numbers are")
for i in a:
    
    if i <0:
        print( i)
# part 3

print("odd numbers are")
for i in a:
    if i%2!=0:
        print(i)
# part 4 
print("even numbers are")
for i in a:
    
    if i%2==0:
        print(i)
# part 5
for i in a:
    print(f"{i}--> occured {a.count(i)} times")