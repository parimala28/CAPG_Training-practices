class Example:
    def __init__(self,name):
        print(f"First constructor : hello {name}")
    def __init__(self,age):
        print(f"second constructor : Age is {age}")
obj=Example(25)



#---------------------------------------

class Example:
    def __init__(self,*args):
        if len(args) == 1:
            print(f"Hello {args[0]}")
        elif len(args) == 2:
            print(f"hello {args[0]},you are {args[1]} year old.")

obj1=Example("Alice")
obj2=Example("bob",20)

#---------------------------------------------------


class Example:
    def __init__(self,studentname,**kwargs):
        self.studentname=studentname
        if "name" in kwargs and "age" in kwargs:
            print(f"Hello {kwargs['name']} , you are {kwargs['age']} years old.")
        elif "name" in kwargs:
            print(f"Hello {kwargs['name']}")
        self.xfield=kwargs['name']
obj1=Example(studentname="s1",name="Alice")
obj2=Example(studentname="s2",name="bob",age=20)


          
    
