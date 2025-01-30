T1=()
print("An empty tuple",T1)

T2=(0,)
print("The one item tuple",T2)

T3=(0,'Ni',1.2,3)
print("The four item tuple",T3)

T4=0,'Ni',1.2,3
print("Another four item ",T4)

T5=('abc',('def','ghi'))
print("nested tuples",T5)

T6=tuple('spam')
print("tuple of items in an iterable",T6)


print("The tuples are:",T6[1])

print("the tuples of:",T5[1][1])

print("the ratio of tuples:",T4[1:3])

print("The length of tuple is",len(T6))