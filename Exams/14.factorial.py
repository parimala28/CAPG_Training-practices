def negative():
        return "ivalid! The number is negative"

def factorial(n):      #factorial printing 
    fact=1
    for i in range(1,n+1):
        
        fact*=i
    return fact
def main():
    try:
        n=int(input("Enter any num: "))     #input
        if n<0:                                      #checking factorial
               negative()
        else:
             res=factorial(n)
             print(f"The value {res}")
    except ValueError:                         #error print
       print("The value is invalid")

main()         
                   
          

