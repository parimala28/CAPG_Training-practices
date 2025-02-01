file=open("sample.txt" ,"w")
file.write("Hello, this is a sample text with the sample words")
file.close()

# with open("sample.txt" , "w") as file:
#     file.write("Hello world")           #file closes automatically
    

#reading the entire file
with open("sample.txt" ,"r") as file:
    content=file.read()
    print(content)    

#reading line by line
    with open("sample.txt" , "r") as file:
        for line in file:
            print(line.strip())
