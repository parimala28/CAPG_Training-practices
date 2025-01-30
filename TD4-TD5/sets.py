empty_set=set()
fruits={"apple","banana","cherry"}

print("empty_set",empty_set)
print("set of frits",fruits)
 
fruits.add("grapes")
fruits.remove("apple")
print("set of fruits",fruits)

set1={"a","b","c","d"}
set2={"A","B","c","D"}
print("the union",set1|set2)
print("the intersection",set1&set2)
print("the difference",set1-set2)
print("the symetric difference",set1^set2)

