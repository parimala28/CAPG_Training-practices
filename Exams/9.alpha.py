def analyze(input_string):
   
    vowels="aeiouAEIOU"   
    vowel_count=0
    consonant_count=0
    digit_count=0
    special_count=0

    for ch in input_string:        #ondition for vowels,consonant,digit counts
        if ch in vowels:
            vowel_count += 1
        elif ch.isalpha():
            consonant_count += 1
        elif ch.isdigit():
            digit_count += 1
        else:
            special_count += 1

    reversed = input_string[::-1]    #reverse the string

    print("\nAnalysis Results:")
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Digits: {digit_count}")
    print(f"Special Characters: {special_count}")
    print(f"Reversed String: {reversed}")

def main():                            #main function
    
    print("String Analysis Tool")
    input_string = input("Enter a string to analyze: ")
    analyze(input_string)

if __name__ == "__main__":
    main()
