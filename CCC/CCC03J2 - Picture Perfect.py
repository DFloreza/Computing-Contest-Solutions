# CCC '03 J2 - Picture Perfect
counter = 0
areaCounter = 0
areaList = []

area = eval(input())

while area != 0:
    areaList.append(area)
    area = eval(input()) # enter again

for x in range(len(areaList)):
    removalCounter = 0
    counter2 = 0
    perimeterList = [] # for storing the perimeters
    # identify all the factors, then pair the factors
    factorList = []

    
    for i in range(1, areaList[counter]+1):
        # for loop that identifies all the factors
        if areaList[counter] % i == 0:
            factorList.append(i)

    # find the pairing factor to calculate the perimeter for this area
    for x in range(len(factorList)):
        # divide the arealist[counter] number by the factorlist[counter]
        # to list out all the possible perimeters
        numerator = areaList[areaCounter]
        denominator = factorList[counter2]
        secondFactor = numerator/denominator
        
        perimeter = (2*secondFactor)+(2*factorList[counter2])
        perimeterList.append(perimeter)

        counter2 += 1
        

    # since there will be a time where the perimeters will be increasing then
    # decreasing due to the repetition, we will simply just identify the minimum
    # of the list and identify its corresponding factors with its index

    desiredperimeter = min(perimeterList)
    while desiredperimeter.is_integer() == False:
        # can't have decimals with our desired perimeter, keep removing until
        # we got one without decimals
        perimeterList.remove(desiredperimeter)
        removalCounter += 1 # create a removal Counter to count the removals
        desiredperimeter = min(perimeterList)
        
    # now find the dimensions of that perimeter given its value
    # method 1: subtract 2*w from perimeter and then divide by l

    # index of the desired perimeter will be equal to the index of the width
    # width is equal to (desired perimeter - 2w) / 2
    dispensableIndex = perimeterList.index(desiredperimeter)

    # we must also consider if the width and length are equal
    w = factorList[dispensableIndex]
    l = (desiredperimeter - (2 * w))/ 2
    

    print("Minimum perimeter is", int(desiredperimeter), "with dimensions", w, "x", int(l))

    areaCounter += 1

    counter += 1



    

    

    
    
    
