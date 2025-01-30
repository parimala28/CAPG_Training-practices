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

print(f"Prime numbers between {start} and {end} are:")
print("The largest:",)
   #start and end 
prime(start, end)





def is_prime(num):
    
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_list(start, end):
   
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Input values
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Generate the list of prime numbers
primes = prime_list(start, end)

# Display the results
if primes:
    print(f"Prime numbers between {start} and {end} are: {primes}")
    print(f"The smallest prime number is: {primes[0]}")
    print(f"The largest prime number is: {primes[-1]}")
else:
    print(f"There are no prime numbers between {start} and {end}.")

 