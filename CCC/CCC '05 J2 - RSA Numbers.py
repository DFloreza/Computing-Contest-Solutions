# CCC '05 J2 - RSA Numbers
# Dexter Floreza


def main():
    N1 = eval(input())
    N2 = eval(input())
    currentNumber = N1
    RSACounter = 0

    factor_finder(N1, N2, currentNumber, RSACounter)

# identify all the numbers in that range that have four divisors
def factor_finder(N1, N2,currentNumber, RSACounter):
    for x in range(N1-1, N2):
        factorCounter = 0
        factorList = [] # reset the factor list
        for i in range(1, currentNumber+1):
            # go through each number from 1 to the current number
           if currentNumber % i == 0:
               factorList.append(i)
               # if it works print it works then add to the list

        if len(factorList) == 4: 
            RSACounter += 1

        currentNumber += 1 # add to the currentNumber counter

    print("The number of RSA numbers between", N1, "and", N2, "is", RSACounter)

main()
