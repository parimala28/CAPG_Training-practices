# convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# convert Celsius to Kelvin
def celsius_to_kelvin(c):
    return c + 273.15

# convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

# convert Kelvin to Celsius
def kelvin_to_celsius(k):
    return k - 273.15

# convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def main():
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    
    n = int(input("Enter the convertion number: "))
    
    if n == 1:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
    elif n == 2:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celsius_to_kelvin(c)}K")
    elif n == 3:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f)}°C")
    elif n == 4:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_kelvin(f)}K")
    elif n == 5:
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k}K = {kelvin_to_celsius(k)}°C")
    elif n == 6:
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k}K = {kelvin_to_fahrenheit(k)}°F")
    else:
        print("Invalid choice, please enter a valid option.")

# Calling the main function 
main()
