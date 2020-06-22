import database
import data_generator
import matplotlib.pyplot as plt

def graphics(db):
    stats = ["country", "company_name", "price", "product_name", "type"]

    for i in range(0, len(stats)):
        print("{}) {} ".format(i, stats[i]))

    x = int(input())
    y = int(input())

    plt.xlabel(stats[x])
    plt.ylabel(stats[y])

    data = data_generator.get_data(x=x, y=y, stats=stats, db=db)
    plt.plot(data[0], data[1], 'o')
    plt.show()

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
5) delete all
6) Exit
'''

    print(opts + "->: ")
    index = input()

    if index == '0':
        db.save(get_file_path())
    elif index == '1':
        db.load(get_file_path())
    elif index == '2':
        print("How much to generate: ")
        num = int(input())
        for i in range (0, num):
            db.insert(data_generator.generate())
    elif index == '3':
        graphics(db)
    elif index == '4':
        data_generator.print_raw(db)
    elif index == '5':
        db.base.smembers(db.DATA_ID)
        return
    elif index == '6':
        return

    menu()
