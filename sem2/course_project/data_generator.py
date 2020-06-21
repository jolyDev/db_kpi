import database
import json
import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

countries = ["USA", "England", "Canada", "Germany", "Poland", "Italy", "Ukraine", "China"]
types = ["A+", "A", "B", "C", "D", "E"]

def get_company(country_id):
    if country_id == 0:
        return ["surgeArms", "ortho-proto", "USA brand masters"][random.randint(0, 2)]
    elif country_id == 1:
        return ["mech rotate", "evolve"][random.randint(0, 1)]
    elif country_id == 2:
        return "g&X"
    elif country_id == 3:
        return "Danke"
    elif country_id == 4:
        return ["PoliArms", "Edu"][random.randint(0, 1)]
    elif country_id == 5:
        return "Sycily"
    elif country_id == 6:
        return "Dobroboot"
    elif country_id == 7:
        return ["Chi go youghn", "Mech Tech"][random.randint(0, 1)]


def generate() -> []:
    countries_count = 7
    country_id = random.randint(0, countries_count)
    country = countries[country_id]
    price = ((countries_count + 3) - country_id) * random.randint(20, 25)

    types_count = 4
    type_id = random.randint(0, types_count)
    price = (price + (types_count + 10) - type_id) * random.randint(10, 35)

    return {
        "country": country,
        "company_name": get_company(country_id),
        "price": price,
        "product_name": randomString(random.randint(3, 5)),
        "type":types[type_id]
    }

def print_raw(db):
    i = 0
    el = db.base.hget(db.DATA_ID, "0")

    while el is not None:
        print(el)
        i=i+1
        el = db.base.hget(db.DATA_ID, str(i))

def get_data(x, y, stats, db):
    y_val=[]
    x_val=[]

    i = 0
    el = db.base.hget(db.DATA_ID, "0")

    while el is not None:
        y_val.insert(0,json.loads(el)[stats[y]])
        x_val.insert(0, json.loads(el)[stats[x]])
        i=i+1
        el = db.base.hget(db.DATA_ID, str(i))

    result = [x_val, y_val]
    return result


