#function to print prime number using loop
def prime(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")    

start = int(input("1st num: "))   #input values
end = int(input("2nd num: "))

print(f"Prime numbers between {start} and {end} are:")     #start and end 
prime(start, end)
