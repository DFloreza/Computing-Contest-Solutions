H = int(input())
c = 1
highestValueReached = False

#if H % 2 != 0:
    
for x in range(H):
    Whitespace = " "*((H*2) -(c*2))
    
    if c < H and highestValueReached == False:
        print(("*"*c) + Whitespace + ("*"*c))
        c += 2
        
    elif highestValueReached == True:
        print(("*"*c) + Whitespace + ("*"*c))
        c -= 2
    
    elif c == H and highestValueReached != True:
        print(("*"*c) + Whitespace + ("*"*c))
        highestValueReached = True
        c -= 2
    
        
        
        
        
# keep going until number of loops is equivalent to H:
# Calculate whitespace
# if counter is less than H, then print the stars and add more to conuter
# if counter equals H, switch highestValueReached variable to true
# if highestValueReached variable is true, then subtract from the counter then print and keep going
    
