
# import pandas as pd
# n=int(input("Enetr number of records:"))
# with open("data.csv","w") as file:
#     file.write("id,name,age\n")
#     for i in range(n):
#         id=int(input(f"Enter a id number{i+1}:"))
#         name=input(f"Enetr a name{i+1}:")
#         age=int(input(f"Enter a age{i+1}:"))
#         file.write(f"{id},{name},{age}\n")
# print(f"{'data.csv'}")      
# df=pd.read_csv("data.csv")
# print(df)        



import pandas as pd
n = int(input("Enter the number of records: "))
data = []
for i in range(n):
    id = input(f"Enter ID for record {i+1}: ")
    name = input(f"Enter Name for record {i+1}: ")
    age = input(f"Enter Age for record {i+1}: ")
    data.append({"id": id, "name": name, "age": age})
df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)
df_read = pd.read_csv("output.csv")
print(df_read)
