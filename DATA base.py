import sqlite3


# dtbs = sqlite3.connect("car-price.db")


# def db_tables():
#     dtbs = sqlite3.connect("car-price.db")
#     crsr = dtbs.cursor()
#
#     crsr.execute('''CREATE TABLE IF NOT EXISTS cars_brands(
#         brand_id INTEGER,
#         name TEXT
#
#     ) ''')
#
#     crsr.execute('''CREATE TABLE IF NOT EXISTS models(
#         model_id INTEGER,
#         name TEXT,
#         brand_id INTEGER
#
#     ) ''')
#
#     crsr.execute('''CREATE TABLE IF NOT EXISTS prices(
#         price_id INTEGER,
#         price INTEGER,
#         model_id INTEGER
#
#     ) ''')
#
#     dtbs.commit()
#
#     dtbs.close()
#
# def db_insert():
#     dtbs = sqlite3.connect("car-price.db")
#     crsr = dtbs.cursor()
#
#     crsr.execute("INSERT INTO cars_brands VALUES (1, 'Toyota') ")
#     crsr.execute("INSERT INTO cars_brands VALUES (2, 'Volkswagen') ")
#     crsr.execute("INSERT INTO cars_brands VALUES (3, 'Ford') ")
#
#     crsr.execute("INSERT INTO models VALUES (1, 'Corolla', 1) ")
#     crsr.execute("INSERT INTO models VALUES (2, 'Rav4', 1) ")
#     crsr.execute("INSERT INTO models VALUES (3, 'Land Cruiser', 1) ")
#     crsr.execute("INSERT INTO models VALUES (4, 'Touareg', 2) ")
#     crsr.execute("INSERT INTO models VALUES (5, 'Tiguan', 2) ")
#     crsr.execute("INSERT INTO models VALUES (6, 'Golf', 2) ")
#     crsr.execute("INSERT INTO models VALUES (7, 'Ranger', 3) ")
#     crsr.execute("INSERT INTO models VALUES (8, 'Kuga', 3) ")
#     crsr.execute("INSERT INTO models VALUES (9, 'Mustang', 3) ")
#
#     crsr.execute("INSERT INTO prices VALUES (1, '34000', 1) ")
#     crsr.execute("INSERT INTO prices VALUES (2, '27700', 2) ")
#     crsr.execute("INSERT INTO prices VALUES (3, '85230', 3) ")
#     crsr.execute("INSERT INTO prices VALUES (4, '70600', 4) ")
#     crsr.execute("INSERT INTO prices VALUES (5, '40052', 5) ")
#     crsr.execute("INSERT INTO prices VALUES (6, '32320', 6) ")
#     crsr.execute("INSERT INTO prices VALUES (7, '61760', 7) ")
#     crsr.execute("INSERT INTO prices VALUES (8, '31290', 8) ")
#     crsr.execute("INSERT INTO prices VALUES (9, '53100', 9) ")
#
#     dtbs.commit()
#
#     dtbs.close()
#
# def db_extract():
#     dtbs = sqlite3.connect("car-price.db")
#     crsr = dtbs.cursor()
#
#     crsr.execute("SELECT * FROM prices")
#     data=crsr.fetchall()
#     print(data)
#
#     crsr.execute('''SELECT prices.price, models.name, cars_brands.name
#             FROM prices
#             JOIN models ON prices.model_id = models.model_id
#             JOIN cars_brands ON models.brand_id = cars_brands.brand_id
#             ''')
#     data = crsr.fetchall()
#     print(data)
#
#     dtbs.close()

def main_prog():
     dtbs = sqlite3.connect("car-price.db")
     crsr = dtbs.cursor()

     print("Select brand")

     crsr.execute("SELECT * FROM cars_brands")
     data = crsr.fetchall()

     brands = []
     x=0

     for item in data:
          brands.append(item[1])
          print(f"{x}. {brands[-1]}")
          x += 1

     while True:
          u_inp = input("Enter number --> ")
          try:
               brand=brands[int(u_inp)]
               break
          except:
               continue

     print()

     crsr.execute(f"SELECT * FROM models WHERE brand_id = (SELECT brand_id FROM cars_brands WHERE name = '{brand}')")
     data = crsr.fetchall()

     models = []
     x=0
     for item in data:
          models.append(item[1])
          print(f"{x}. {models[-1]}")
          x += 1

     while True:
          u_inp = input("Enter number --> ")
          try:
               model=models[int(u_inp)]
               break
          except:
               continue

     crsr.execute(f"SELECT price FROM prices WHERE model_id = (SELECT model_id FROM models WHERE name = '{model}')")
     data = crsr.fetchall()
     price = data[0][0]
     print(f"{brand} {model} costs {price} dollars")


     dtbs.close()


main_prog()