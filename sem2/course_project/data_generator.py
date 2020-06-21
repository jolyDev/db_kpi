import database
import json

class prosthesis:
    def __init__(self, country, company_name, price, product_name, type):
        self.country = country
        self.company_name = company_name
        self.price = price
        self.product_name = product_name
        self.type = type

def generate() -> []:
    return {
        "country":"england",
        "company_name": "ortho-proto",
        "price":250,
        "product_name":"dency",
        "type":"A+"
    }

def print_raw(db):
    i = 0
    el = db.base.hget(db.DATA_ID, "0")

    while el is not None:
        print(el)
        i=i+1
        el = db.base.hget(db.DATA_ID, str(i))

