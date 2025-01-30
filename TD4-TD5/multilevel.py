class School():
    
        def display_school(self):
            print("This is school.")

class Ug(School):
    def display_ug(self):
        print("The school is updated to UG")

class Pg(Ug):
    def display_pg(self):
        print("The Ug is now updated to PG")
p=Pg()
p.display_school()
p.display_ug()
p.display_pg()
