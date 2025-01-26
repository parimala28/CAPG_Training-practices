def second_largest():
    num=list(map(int,input("Enter a number list: ").split()))  #input values
    if len(num)<2:
        print(num)
    else: 
        first=second=float('-inf')  #condition to get second largest number
        for n in num:
            if n>first:
                first,second=n,first
            elif n>second and n!=first:
                second=n
        if second==float('-inf'):
            print("The list not have largest.")
        else:
            print(f"The second largest number is: {second}")


def main():
   
   
    second_largest()
main()    