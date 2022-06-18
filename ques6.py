lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  

print ("The Prime Numbers in the input range are: ") 
for i in range(lower_value,upper_value + 1): 
    if i > 1:  
        for j in range (2, i):  
            if (i % j) == 0:  
                break  
        else:  
            print (i)