d={}
print(d)

d1={'spam':2,'eggs':3}
print("The values",d1)
  
d2={'food':{'ham':1,'egg':2}}
print("The key value pairs",d2)
print(d2['food'])

d3=dict(name='bon',age=20)
print(d3)

d4=dict(zip(['p','a','o','s'],[1,3,4,5]))
print(d4)

d5=dict.fromkeys(['a','b'])
print(d5)

d6={'a':1,'b':2,'c':3}
print(d6['a'])

d7={'apple':10,'banana':20,'grapes':30}
print("give the key elements:",d7.keys())
print("give the value elements:",d7.values())
print("give the items in dic",d7.items())
print("",d7.get('app','not in dic'))

d7=d6.copy()
print