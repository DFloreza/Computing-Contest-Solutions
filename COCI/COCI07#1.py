# COCI '07 CONTEST 5 # Tri
# Dexter Floreza

n1, n2, n3 = [int(x) for x in input().split()]

# we will have to brute force identify all the permutations of addition, sub.
# multiplication, and division unfortunately
print(n1,n2,n3)
# addition case 1: n1 + n2 = n3
if n1 + n2 == n3:
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    print(n1 + "+" + n2 + "=" + n3)
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

# addition case 2: n1 = n2 + n3
if n1 == n2 + n3:
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    print(n1 + "=" + n2 + "+" + n3)
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

# subtraction case 1: n1 - n2 = n3
if n1 - n2 == n3:
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    print(n1 + "-" + n2 + "=" + n3)
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

# subtraction case 2: n1 = n2 - n3
if n1 == n2 - n3:
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    print(n1 + "=" + n2 + "-" + n3)
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

if n1 * n2 == n3:
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    print(n1 + "*" + n2 + "=" + n3)
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

if n1 == n2 * n3:
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    print(n1 + "=" + n2 + "*" + n3)
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

if n2 * n3 == n1:
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    print(n1 + "/" + n2 + "=" + n3)
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

if n1 * n3 == n2:
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    print(n1 + "=" + n2 + "/" + n3)
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    



    









    
