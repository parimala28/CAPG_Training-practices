# import pandas as pd
# data={
#     'name':["pari","bob","ravi"],
#     'age':[20,30,40],
#     'city':['hyd','chicago','new york']
# }
# df=pd.DataFrame(data)

# # df.to_csv('output.csv',index=False)                 #writing to csv files
# df=pd.read_csv('customers.csv')
# print(df)
# df.to_json('customers.json',index=False)  
# df.to_html('customers.html',index=False)                          #displaying csv files
# df1=df.sort_values(by='Country',ascending=False)
# print(df1)
# # df['Numeric']                                        #select single column
# # df.sort_values(by='',ascending=False)               #sorting by ascending




import pandas as pd
data={
    'name':["pari","bob","ravi"],
    'age':[20,30,40],
    'city':['hyd','chicago','new york'],
    'Year':[2021,2023,2034],
    
}
df=pd.DataFrame(data)
df.set_index(['age','Year','city'],inplace=True)
print(df)