#print("Hello World")
#first_name=input("what is your first name?")
#last_name=input("What is your last name?")
#street=input("what is your street name?")
#city=input("what is your city name?")
#pincode=int(input("pincode of your city?"))

#first_name="pari"
#last_name="chindam"
#print(f"Hello {first_name} {last_name},how are you?")

#first=int(input("enter a number:"))
#second=int(input("enter a number:"))
#sum=first+second
#print(f"The sum is {sum}")
#sum=float(first)+float(second)

#n=255
#ans1=n/10*10
#ans=n//10*10
#print(ans1,ans)


#import random
#num=random.random()
#print(num)

#a=float(input("Length:"))
#b=float(input("width:"))
#c=float(input("Height:"))
#a1
# 2
# rea=int(length)*int(width)
#print(area)

#q,q1=(-b + ((b**2 - 4*a*c)**0.5))/(2*a) , (-b - ((b**2 - 4*a*c)**0.5))/(2*a)
#print(q,q1)


import math
def prime(n):
    if(n<=1):
        return False
    if(n==2):
        return True
    if(n%2==0):
        return False

    i=3
    while(i<=math.sqrt(n)):
        if(n%i==0):
            return False
        i+=2
        return False
    def main():
        n=int(input("any num: "))
        if(prime(n)):
            return "The num is prime"
        else:
            return "The num is not prime"

    main()

