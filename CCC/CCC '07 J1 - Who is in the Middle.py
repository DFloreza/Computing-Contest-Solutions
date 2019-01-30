n1 = eval(input())
n2 = eval(input())
n3 = eval(input())

isbnorig = 9*1+7*3+8*1+0*3+9*1+2*3+1*1+4*3+1*1+8*3

isbnsum = isbnorig + (n1 * 1) + (n2 * 3) + (n3 * 1)
print("The 1-3-sum is", isbnsum)
