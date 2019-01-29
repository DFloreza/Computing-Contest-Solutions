# COCI '06 Contest 4 #1 Sibice
import math

matchList = []
counter = 0

N, W, H = [int(x) for x in input().split()]
# N is number of matches
# W - width
# H - Height

add = (W ** 2) + (H ** 2) # before finding the square root
hypotenuse = int(math.sqrt(add)) # hypotenuse of the diagonal


for x in range(N):
    match = eval(input())
    matchList.append(match)

for x in range(len(matchList)):
    if matchList[counter] <= H:
        print("DA")
    elif matchList[counter] > H:
        if matchList[counter] <= hypotenuse:
            print("DA")
        else:
            print("NE")
    counter += 1
    
