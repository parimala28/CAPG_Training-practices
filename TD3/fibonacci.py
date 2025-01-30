def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n<0:
        return (-1) ** (-n + 1)
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
fib=[fibonacci(i)
for i in range(-1,11)]
print(fib)  
    
    
        

