import database
import data_generator

def graphics():
    a = 0

def get_file_path():
    print("\n enter filename")
    return input() + ".json"



db = database.database()

def menu():
    opts = '''
0) Save
1) Load
2) Gather Info
3) Show Graphics
4) print_raw
5) Exit
'''

    print(opts + "->: ")
    index = input()

    if index == '0':
        db.save(get_file_path())
    elif index == '1':
        db.load(get_file_path())
    elif index == '2':
        for i in range (0, 1):
            db.insert(data_generator.generate())
    elif index == '3':
        graphics()
    elif index == '4':
        data_generator.print_raw(db)
    elif index == '5':
        return

    menu()

