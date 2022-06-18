l=[]

n=int(input("Enter the number of elements in list:"))
for i in range(0,n):
    element=input()
    l.append(element)

print(l)
for i in l:
    print(f"{i} --> occured {l.count(i)} times")
    