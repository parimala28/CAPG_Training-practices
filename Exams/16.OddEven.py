def Even(n):          #odd and even pushing
    even, odd=[], []
    for a in n:
        if a%2==0:
            even.append(a)
        else:
            odd.append(a) 
    return even,odd
def main():
    n=list(map(int,input("Enter the List: ").split()))   #input
    even, odd=Even(n)
    print(f"The Even List: {even}")      #printing even and odd list
    print(f"The Odd List: {odd}")
main()    


