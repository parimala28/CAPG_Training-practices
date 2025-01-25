
import math
def prime(n):
    if(n<=1):
        return False
    if(n==2):
        return True
    if(n%2==0) :
        return False

    i=3
    while(i<=math.sqrt(n)):
        if(n%i==0):
            return False
        i+=2
        return True
    def main():
        n=int(input("any num: "))
        if(prime(n)):
            return "The num is prime"
        else:
            return "The num is not prime"

    main()



