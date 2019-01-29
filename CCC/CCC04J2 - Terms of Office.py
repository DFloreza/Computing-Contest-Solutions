# CCC '04 J2 - Terms of Office


X = eval(input()) # current year, lower bound
Y = eval(input()) # future year, upper bound

currentYear = X

for eachNumber in range(X, Y+1):
    factorList = []
    trCond = False
    cpCond = False
    myrCond = False
    dcrCond = False
    
    # reset all conditions and the factor list

    # identify if it follows the criteria for an unusual year
    d = currentYear - X
  
    if d % 2 == 0:
        trCond = True
    if d % 3 == 0:
        cpCond = True
    if d % 4 == 0:
        myrCond = True
    if d % 5 == 0:
        dcrCond = True

    if (trCond == True) and (cpCond == True) and (myrCond == True) and (dcrCond == True):
        print("All positions change in year", currentYear)

    currentYear += 1

