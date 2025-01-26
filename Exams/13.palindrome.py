def is_palindrome(p):
    p=str(p)
    return p == p[::-1]       #palindrome  condition
def main():                 #main function
    while True:
        p = input("Enter any no or string:")    # input
        if p.lower() == "stop":
            print("exit")
            break

        if(is_palindrome(p)):            #printing  yes or not
            print("palindrome")
        else:
            return "Not palindrome"

if __name__ == "__main__":          
     main()            
