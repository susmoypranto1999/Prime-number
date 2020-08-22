import math
number= int(input("Test till:"))

def is_prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False

    return True
lists=[]
for  n in range(1,number+1):
    if is_prime(n):
        lists.append(n)
print(lists)