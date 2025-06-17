from sqlalchemy import create_engine
from abc import ABC, abstractmethod
from app.mods.create import Creator, create_database
from app.mods.inserter import Inserter
from app.mods.selector import Selector
from app.mods.updator import Updator
from app.mods.dropper import Dropper

class Kernel(ABC):
    def __init__(self, name, command):

        self.command = command
        self.name = name

    @abstractmethod
    def logic(self):
        pass

class Tc(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)
        

    def logic(self, name: str, dct: dict):

        columns = list(dct.keys())
        types = list(dct.values())

        values_string = ''
        for i in range(len(types)):
            if (i+1) == len(types): 
                values_string += f'{columns[i]} {types[i]}'
            else:
                values_string += f'{columns[i]} {types[i]}, '

        command = f"CREATE TABLE IF NOT EXISTS {name} ({values_string});"

        kernel = Creator(self.name, command)
        kernel.create_table()

        signature = f'{name} ({values_string})'
        del kernel
        return [signature, len(columns)]
    
        

        
class Db(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)
    
    def logic(self):
        create_database(self.name)

class In(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)

    def logic(self, signature, lst):
         
        string = ''
        for i in range(len(lst)):
            if (i+1) == len(lst):
                string += f"'{lst[i]}'"

            else:
                string += f"'{lst[i]}', "

        command = f"INSERT INTO {signature} VALUES ({string});"

        kernel = Inserter(command, self.name)
        kernel.insert()

        del kernel
    
    

class Se(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)

    def logic_int(self, where_state, table_name, column):

        command = f"SELECT * FROM {table_name} WHERE {column}={where_state};"
        kernel = Selector(self.name, command)
        return kernel.select_where()
    
    def logic_string(self, where_state, table_name, column):

        command = f"SELECT * FROM {table_name} WHERE {column}='{where_state}'"
        kernel = Selector(self.name, command)
        return kernel.select_where()
    
    def logic(self):
        return super().logic()
    
class U(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)

    def logic(self, columns_dct: dict, table_name, set_dct: dict, where_state: dict, where_type):

        columns = list(set_dct.keys())
        values = list(set_dct.values())

        cloumnsw = list(where_state.keys())
        valuesw = list(where_state.values())
        
        

        string = ''
        for i in range(len(columns)):
            
            if columns_dct[columns[i]] == "TEXT":

                if i+1 == len(columns):
                    string += f"{columns[i]} = '{values[i]}'"
                else:
                    string += f"{columns[i]} = '{values[i]}', "
            
            else:

                if i+1 == len(columns):
                    string += f"{columns[i]} = {values[i]}"
                else:
                    string += f"{columns[i]} = {values[i]}, "

        
            
        if where_type == "TEXT":
            string2 = ''
            for n in range(len(cloumnsw)):
                if n+1 == len(valuesw):
                    string2 += f"{cloumnsw[n]} = '{valuesw[n]}'"
                else:
                    string2 += f"{cloumnsw[n]} = '{valuesw[n]}', "
        else:
            string2 = ''
            for n in range(len(cloumnsw)):
                if n+1 == len(valuesw):
                    string2 += f"{cloumnsw[n]} = {valuesw[n]}"
                else:
                    string2 += f"{cloumnsw[n]} = {valuesw[n]}, "

        


        command = f"UPDATE {table_name} SET {string} WHERE {string2};"
        print(command)
        kernel = Updator(command, self.name)
        kernel.update()

class Al(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)

    def logic(self, table_name):
        
        command = f"SELECT * FROM {table_name};"
        kernel = Selector(self.name, command)

        return kernel.select_all()

class Md(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)
    
    def logic(self, table_name):

        command = f"DELETE FROM {table_name};"
        kernel = Dropper(self.name, command)
        kernel.delete()

class Dy(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)

    def logic(self, table_name):
        
        command = f"DROP TABLE {table_name}"
        kernel = Dropper(self.name, command)
        kernel.delete()

class W(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)

    def logic(self):
        
        import os
        os.remove(self.name)

class Ds(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)
    
    def logic(self, struct: dict, where_statement: dict, table_name):

        columns = list(where_statement.keys())
        values = list(where_statement.values())

        string = ''
        for i in range(len(columns)):

            type_ = struct[columns[i]]
            if type_ == "TEXT":
                if i+1 == len(columns):
                    string += f"{columns[i]} = '{values[i]}'"
                else:
                    string += f"{columns[i]} = '{values[i]}', "
            else:
                if i+1 == len(columns):
                    string += f"{columns[i]} = {values[i]}"
                else:
                    string += f"{columns[i]} = {values[i]}, "

        command = f"DELETE FROM {table_name} WHERE {string};"
        kernel = Dropper(self.name, command)
        kernel.delete()


class Cs(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)

    def logic(self, table):
        command = f"PRAGMA table_info({table});"
        kernel = Selector(self.name, command)
        return [row[1] for row in kernel.select_all()]

class Te(Kernel):

    def __init__(self, name, command):
        super().__init__(name, command)
    
    def logic(self):
        
        command = "SELECT name FROM sqlite_master WHERE type='table';"
        kernel = Selector(self.name, command)
        return kernel.select_all()