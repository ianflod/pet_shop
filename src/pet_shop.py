def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
     pet_shop["admin"]["total_cash"] += cash 

def add_or_remove_cash(pet_shop, cash):
     pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, sales):
    pet_shop["admin"]["pets_sold"] =+ sales


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breed_count = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_count.append(pet)
    return breed_count

def get_pets_by_breed(pet_shop, breed):
    breed_count = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_count.append(pet)
    return breed_count

def find_pet_by_name(pets_shop, name):
    for pet in pets_shop["pets"]:
        if pet["name"] == name:
            return pet

def find_pet_by_name(pets_shop, name):
    for pet in pets_shop["pets"]:
        if pet["name"] == name:
            return pet


def remove_pet_by_name(pet_shop, name):
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            del pets[pets.index(pet)]

def add_pet_to_stock(pet_shop, new_pet):
    new_pet = {
                    "name": "Felix",
                    "pet_type": "cat",
                    "breed": "Tabby",
                    "price": 100,
                }
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customers, new_pet):
    new_pet = [1]
    for customer in customers:
        return customers["pets"].append(new_pet)

        








            





            















    



