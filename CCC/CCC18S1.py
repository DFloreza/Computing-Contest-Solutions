# CCC' 18 S1 - Voronoi Villages
# Dexter Floreza

counter = 1
counter2 = 0

positionList = [] # store all the positions of the ith village
midpointListLefts = [] # store all the values of the left midpoints
midpointListRights = [] # store all the values of the right midpoints
VSizeList = [] # the size of the villages

N = eval(input()) # num villages

for x in range(N):
    positionEntry = eval(input())
    positionList.append(positionEntry)

positionList2 = sorted(positionList) # sort it from decreasing to increasing

for x in range(len(positionList2) - 2):
    # keep going until we're at the 2nd last village
    # and we are going to start at the 2nd village
    # so essentially we are starting at the 2nd village and ending our calculations
    # on the 2nd last village
    
    # calculate the midpoint of the village left to the village index
    midPointDifferenceLeft = positionList2[counter] - positionList2[counter-1]
    midPointValueLeft = midPointDifferenceLeft/2
    midpointListLefts.append(midPointValueLeft)

    # calculate the midpoint of the village right to the village index
    midPointDifferenceRight = positionList2[counter+1] - positionList2[counter]
    # SUBTRACT THE CURRENT NUMBER WE ARE AT FROM THE NUMBER AHEAD 
    midPointValueRight = midPointDifferenceRight/2
    midpointListRights.append(midPointValueRight)
        
    counter+= 1

for x in range(len(midpointListRights)):
    # now we will iterate through each midpoint list and add the su
    VillageSize = midpointListLefts[counter2] + midpointListRights[counter2]
    VSizeList.append(VillageSize)

    counter2 += 1

VSizeList2 = sorted(VSizeList) # remember to sort them out in the end

print(min(VSizeList2))
        

    
    
    


