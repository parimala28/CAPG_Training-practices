def display(data):
    print(f"The max number is {data}")
def g_input():
    a=int(input("A: "))
    b=int(input("B: "))
    c=int(input("C: "))
    d=int(input("D: "))
    ans=0
    return (a,b,c,d)

    

def max_num(a,b,c,d):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

        
        
def main():
    (a,b,c)=g_input()   
    max=max_num(a,b,c)
    display(max)
main()    
    
