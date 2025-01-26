# Function to add an item to the cart
def item(cart):
    item = input("Enter the item name: ")
    p = float(input("Enter the item price: "))
    cart.append((item, p))  
    print(f"Added {item} to the cart.")

# Function to view cart items
def cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item, p in cart:
            print(f"{item} - ${p:.2f}")

# Function to calculate the total price
def calculate_total(cart):
    total = sum(p for _, p in cart)  # Sum up the prices
    print(f"The total price of items in the cart is: ${total:.2f}")

# Main function to manage the shopping cart
def main():
    cart = []  # Initialize an empty cart

    while True:
        print("\nShopping Cart Menu:")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Calculate Total")
        print("4. Exit")

        n = input("Enter your choice (1-4): ")

        if n == "1":
            item(cart)  # Add item to cart
        elif n == "2":
            cart(cart)  # View items in cart
        elif n == "3":
            calculate_total(cart)  # Calculate the total price
        elif n == "4":
            print("Exit")
            break  # Exit the loop and program
        else:
            print("Invalid choice.")  

# Start the program
if __name__ == "__main__":
    main()
