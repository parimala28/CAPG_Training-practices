import random


def display(message):  #display function
    print(message)


def game():
    num = random.randint(1, 100)  # Generate a random number between 1 and 100
    a = 0
    while True:
        g = input("Guess a number between 1 and 100: ")
        if g.isdigit():  # Check if the input is a valid number
            g = int(g)
            a += 1
            if g < num:
                display("Too Low!")
            elif g > num:
                display("Too High!")
            else:
                display(f"You've guessed the number {num} in {a} attempts.")
                break  # Exit the loop when the correct number is guessed
        else:
            display("Please enter a valid integer.")

# Main function to start the game and replay option
def main():
    display("Welcome to the Number Guessing Game!")
    game()
    

main()
