def alp_print():
    row=int(input("Enter the number of rows"))
    n=0
    for i in range(0,row+1):
        for j in range(i):
            if n==26:
                n=0
            else:
                pass
            y=chr(65+n)    
            print(y,end="")
            n+=1
        
        print("")

alp_print()