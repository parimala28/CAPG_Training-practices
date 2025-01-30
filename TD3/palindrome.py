def palindrome(p):
    L=list(p.lower())
    return L == L[::-1]
def main():
    p=input("Enter any things: ")
    if palindrome(p):
        return "plaindrone"
    else:
        return "not palindrome"
main()        