def is_prime(num):
    #Check if a number is prime.
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    #Print all prime numbers in the given range [start, end].
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# Input range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end} are:")
print_primes_in_range(start, end)




def is_prime(num):
    #Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    #Print all prime numbers in the given range [start, end] using a while loop."""
    num = start
    while num <= end:
        if is_prime(num):
            print(num, end=" ")
        num += 1

# Input range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end} are:")
print_primes_in_range(start, end)

