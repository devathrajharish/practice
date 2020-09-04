import random

def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b) #Recursive call

for i in range(10):
    a = random.randint(1, 200)
    b = random.randint(1, 200)
    gcd = GCD(a,b)
    print("GCD of {} and {} is: {}".format(a,b,gcd))