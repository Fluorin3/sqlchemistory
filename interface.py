from app.insearch import *
import json
import ast
from prettytable import PrettyTable

class Interface():

    def __init__(self):
        self.session_db = ''
        self.signature = ''
        self.dct = {}
        self.table_name = ''
        self.const = 0

    def init_db(self):
        with open('session.txt', 'r') as f:
            self.session_db = f.readline().replace('\n', '')
        return self.session_db

    def init(self):
        with open('session.txt', 'r') as f:
            lst = f.readlines()
            
            self.session_db = lst[0].replace('\n', '')
            
            self.signature = lst[1].replace('\n', '')
            
            self.const = int(lst[2].replace('\n', ''))
            
            self.dct = ast.literal_eval(lst[3].replace('\n', ''))
            
            self.table_name = lst[4].replace('\n', '')
            
            

    def define_database(self, name):

        d = Db(name, '')
        d.logic()
        self.session_db = name
        with open('session.txt', 'w') as f:
            f.write(self.session_db+'\n')
        

    def tc(self, command):
        io = Tc(self.session_db, command)
        name = input("input name of table: ")
        if name == 'Eu':
            return 0
        count = int(input("Input count of columns: "))
        if count == 'Eu':
            return 0
        dction = {}
        for i in range(count):
            a = input(f"Input name of column number {i+1}: ")
            if a == 'Eu':
                return 0
            b = input("Input type of column: ")
            if b == 'Eu':
                return 0
            dction[a] = b
            print('\n')

        res = io.logic(name, dction)
        sig = str(res[0])
        cons = res[1]
        dc = dction
        tab_name = name

        string = f'{self.session_db}\n{sig}\n{cons}\n{dc}\n{tab_name}'
        with open('session.txt', 'w') as f:
            f.write(string)

        with open(f'tables_{self.session_db}.txt', 'a') as f:
            f.write(f'{dc}$ {sig}'+'\n')
    

    
    def inn(self, command):
        nlst = []
        io = In(self.session_db, command)
        types = list(self.dct.values())
        columns = list(self.dct.keys())
        for i in range(self.const):
            n = input(f"Input data in column '{columns[i]}': ")
            if n == 'Eu':
                return 0
            nlst.append(n)

        io.logic(self.signature.replace("TEXT", '').replace("INTEGER", ''), nlst)

    def se(self, command):
        io = Se(self.session_db, command)

        col = input("Input name of column: ")
        if col == 'Eu':
            return 0
            
        if col in self.dct.keys():
            type_ = self.dct[col]
            if type_ == "INTEGER":
                where = input("Input value from selected column: ")
                if where == 'Eu':
                    return 0

                res = io.logic_int(where, self.table_name, col)
            else:
                where = input("Input value from selected column: ")
                if where == 'Eu':
                    return 0

                res = io.logic_string(where, self.table_name, col)
            return res
        else:
            return "No."
    
    def u(self, command):

        io = U(self.session_db, command)

        send_dct_col = {}
        send_dct_where = {}
        type_where = ''

        count_of_columns_str = input("Input count of columns to change: ")
        if count_of_columns_str == "Eu":
            return 0
        count_of_columns = int(count_of_columns_str)

        columns_from = list(self.dct.keys())
        types_from = list(self.dct.values())

        for ii in range(count_of_columns):
            print('\n')
            col_inp = input("Input column name: ")
            if col_inp == "Eu":
                return 0
            inp = input(f"Input change of column '{col_inp}': ")
            if inp == "Eu":
                return 0
            send_dct_col[col_inp] = inp
        
        where_count = int(input("Input count of conditions: "))

        print('\n')
        print('Condtions')
        print('\n')

        for i in range(where_count):
            
            column_name = input("Input column's name: ")
            if column_name == 'Eu':
                return 0
            type_column = self.dct[column_name]
            type_where = type_column
            condition = input("Input value of column: ")
            if condition == 'Eu':
                return 0
            send_dct_where[column_name] = condition


        io.logic(self.dct, self.table_name, send_dct_col, send_dct_where, type_where)
    
    def al(self, command):
        
        io = Al(self.session_db, command)

        names = list(self.dct.keys())

        table_ = PrettyTable()
        table_.field_names = names

        for i in io.logic(self.table_name):

            table_.add_row(i)

        return table_
    
    def cn(self, command):

        return self.dct

    def w(self, command):
        sure = input("Are you sure (c - confirm, d - deny): ")
        if sure == 'c':
            db = input("Enter database name (D - default): ")
            if db == "D":
                io = W(self.session_db, command)

            else:
                io = W(db, command)
    
            io.logic()
        else:
            pass
    
    def dy(self, command):
        io = Dy(self.session_db, command)
        sure = input("Are you sure (c - confirm, d - deny): ")
        if sure == "c":
            table = input("Enter table's name (D - default): ")
            if table == "D":
                io.logic(self.table_name)
            else:
                io.logic(table)
            
            last = self.session_db
            
            with open("session.txt", 'w') as f:
                f.write(last+'\n')

            with open(f'tables_{last}.txt') as f:
                lst = f.readlines()
                for i in lst:
                    if table in i:
                        ind = lst.index(i)
                        print("key has been founded!")
                        lst.remove(lst[ind])
                        for row in lst:
                            f.write(str(row+'\n'))
                        break
                    else:
                        continue
               
        else:
            pass

    def md(self, command):
        io = Md(self.session_db, command)
        sure = input("Are you sure (c - confirm, d - deny): ")
        if sure == "c":
            table = input("Enter table's name (D - default): ")
            if table == "D":
                io.logic(self.table_name)
            else:
                io.logic(table)
        else:
            pass
    
    def ds(self, command):
        io = Ds(self.session_db, command)
        sure = input("Are you sure (c - confirm, d - deny): ")
        if sure == "c":
            table = input("Enter table's name (D - default): ")
            if table == "D":
                send_dct_where = {}
                count_where = int(input("Input count of columns for check conditions: "))
                for i in range(count_where):
                    column = input("Input column name: ")
                    value = input("Input value from column: ")
                    send_dct_where[column] = value

                io.logic(self.dct, send_dct_where, self.table_name)
            else:
                send_dct_where = {}
                count_where = int(input("Input count of columns for check conditions: "))
                for i in range(count_where):
                    column = input("Input column name: ")
                    value = input("Input value from column: ")
                    send_dct_where[column] = value

                io.logic(self.dct, send_dct_where, table)
        else:
            pass
    
    def cs(self, command, table_name):

        

        io = Cs(self.session_db, command)
        column_lst = io.logic(table_name)

        
        with open(f'tables_{self.session_db}.txt', 'r') as f:
            lst = f.readlines()
            
        
        for dct in lst:
            dct.replace("\n", '')
            for sym in dct:
                if sym == '$':
                    sig = dct[dct.index('$')+2::]
                    ab = dct[:dct.index('$'):]
                    absolute = ast.literal_eval(ab)
                    
                    # dct_lst.append(absolute)
                    columns = list(absolute.keys())
                    
                    c = 0
                    for i in range(len(columns)):
                        try:
                            if column_lst[i] == columns[i]:
                                c += 1
                            else:
                                pass
                        except:
                            pass
                    
                    if c == len(column_lst):
                        session_string = f'{self.session_db}\n{sig}{c}\n{absolute}\n{table_name}'
                        
                        with open('session.txt', 'w') as f:
                            f.write(session_string)
                    
                        break

                    
                else:
                    continue
            
    
    def te(self, command):
        io = Te(self.session_db, command)

        return io.logic()
    
    def sn(self, command):
        db_name = input("Enter database's name: ")
        if db_name == 'Eu':
            return 0
        self.session_db = db_name
        with open("session.txt", 'w') as f:
            f.write(db_name+'\n')
    
    def tm(self, command):
        return 'Current database: '+self.session_db+', table: '+self.table_name