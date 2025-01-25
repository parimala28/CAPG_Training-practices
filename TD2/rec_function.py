#display function
def display(data):
    print(f"The area is {data}")
def get_input():
    received_length=input("Length: ")
    received_width=input("Width: ")
    return (received_length,received_width)
def compute_area (length,width):
    area=int(length)*int(width)
    return area
def main():
    (length,width)=get_input()
    area=compute_area(length,width)
    display(area)
main()  


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
        return True
    def main():
        n=int(input("any num: "))
        if(prime(n)):
            return "The num is prime"
        else:
            return "The num is not prime"

    main()


    

    