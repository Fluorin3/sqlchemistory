from interface import Interface
import os


interface = Interface()
try:
    interface.init()
    print("Everything has been inited")
except:
    try:
        a = interface.init_db()
        if a != '':
            print("Database only has been inited")
        else:
            print("Nothing has been inited")
    except:
        print("Nothing has been inited")

while True:
    term = input("Input command: ")

    if term == "Db":
        name = input("Input name: ")
        interface.define_database(name)

    elif term == "Tc":
        interface.tc(term)
        interface.init()
    
    elif term == "In":
        try:
            interface.inn(term)
        except:
            print("Error when creating table. Check types of columns")

    elif term == "Se":
        try:
            print(interface.se(term))
        except:
            print("")
    
    elif term == "Al":
        try:
            print(interface.al(term))
        except:
            print("Cannot found any table in session. To fix this use command 'Cs'")
    
    elif term == "Er":
        break

    elif term == "U":
        try:
            interface.u(term)
        except:
            print("Cannot found table or columns")

    elif term == "Ds":
        interface.ds(term)

    elif term == "Dy":
        interface.dy(term)
        try:
            interface.init()
        except:
            interface.init_db()

    elif term == "Md":
        interface.md(term)
    
    elif term == "Cs":
        try:
            name = input("Input table's name: ")
            interface.cs(term, name)
            interface.init()
        except:
            print("Table not found. Check command 'Te'")
    
    elif term == "I":
        try:
            interface.init()
        except:
            try:
                interface.init_db()
            except:
                print("There is nothing to init")
    
    elif term == 'Sn':
        interface.sn(term)

    elif term == 'Tm':
        print(interface.tm(term))

    elif term == "Cn":
        print(interface.cn(term))
    elif term == "Te":
        print(interface.te(term))
    elif term == "Cl":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Element not found.")