from abc import ABC , abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass
        

    @abstractmethod
    def update(self):
        pass
        

    @abstractmethod
    def delete(self):
        pass
           


class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("insert the values into SQLdatabase.")

    def update(self):
        print("update the values into SQLdatabase.")

    def delete(self):
        print("delete the values in SQLdatabase.") 


class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("insert the values into NoSQLdatabase.")

    def update(self):
        print("update the values into NoSQLdatabase.")

    def delete(self):
        print("delete the values in NoSQLdatabase.") 

nosql=NoSQLDatabase()
nosql.insert()
nosql.update()
nosql.delete()
sql=SQLDatabase()
sql.insert()
sql.update()
sql.delete()        

        