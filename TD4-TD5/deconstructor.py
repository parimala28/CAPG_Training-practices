class DestructorExample:
    def __init__(self,name):
        print(f"object {self.name} is created.")
    def __init__(self):
        print(f"object {self.name} is destroyed.")

obj=DestructorExample("sample")
del obj  