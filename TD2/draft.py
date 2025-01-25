import dis
def display(data):
    print(f"The avg is {data}")  #display the output

def g_input():
    a=int(input("A:"))
    b=int(input("B:"))
    c=int(input("C:"))
    d=int(input("D:"))
    return(a,b,c,d)     #input values

def sum_num(a,b,c,d):
    sum=(a+b+c+d)
    return sum       #sum the values

def avg_num(sum):
     p=sum/4
     return p        #avg the values

def main():
        (a,b,c,d)=g_input()
        sum=sum_num(a,b,c,d)
        p=avg_num(sum)
        dis.dis(display(p))
main()         