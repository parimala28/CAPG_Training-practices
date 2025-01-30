def space(p):
    words=[]
    word=" "
    for ch in p:
        if ch!=" ":
            word+=ch
        else:
            if word:
                words.append(word)
                word=""
            if word:
                words.append(word)
                return words
p=input("Enter any words:")
res=space(p)
print(res)
