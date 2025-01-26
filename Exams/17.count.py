def word(sent):
    words=sent.split()
    w_c={}
    for word in words:             #condition for word count
        if word in w_c:
            w_c[word]+1
        else:
            w_c[word]=1  
    return w_c
def main():
    sent=input("Enetr a sentence: ")       #input
    counts=word(sent)
    print("The count")
    for word,count in counts.items():
        print(f"{word} : {count}")


main()  #main function

