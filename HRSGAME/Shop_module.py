import sqlite3
import Team_module
import UCLASSES
import Armor_module
import time
import Weapon_module


class Shop_class():
    def __init__(self, init_p_team=None, init_gold=0):
        self.p_team = init_p_team
        self.gold = init_gold

    def unit_shop(self):
        db = sqlite3.connect("Db_shop.db")
        crsr = db.cursor()
        crsr.execute("SELECT unit_name, unit_price FROM units")
        data = crsr.fetchall()
        print(f'''
        -------------
          BUY UNITS
        -------------
        Gold = {self.gold}
        ''')

        for x in range(len(data)):
            print(f"        {x}. {data[x][0]} - {data[x][1]} Gold.")
        print(f"        {len(data)}. Show your team with all unit's items to analise.")
        print(f"        {len(data)+1}. Return to previous page.")
        while True:
            answer = input("Input your choice here ---> ")
            try:
                answer = int(answer)
            except:
                continue

            if answer > len(data)+1 or answer < 0:
                continue

            if answer == len(data)+1:
                self.item_categories()
            if answer == len(data):
                self.p_team.team_info_shop()
                continue
            else:
                choise = data[answer][0]
                self.gold = self.gold - crsr.execute(f"SELECT unit_price FROM units WHERE unit_name = '{choise}'").fetchone()[0]
                library = [
                    UCLASSES.Wizard_class(),
                    UCLASSES.Archer_class(),
                    UCLASSES.Shaman_class(),
                    UCLASSES.Knight_class(),
                    UCLASSES.Healer_class(),
                    UCLASSES.Barbarian_class()
                ]
                for unit in library:
                    if unit.name.lower() == choise:
                        self.p_team.alive_team.append(unit)
                        print(f"        {unit.name} joined your team!")
                        self.item_categories()
                break

    def armor_shop(self):
        db = sqlite3.connect("Db_shop.db")
        crsr = db.cursor()
        crsr.execute("SELECT armor_name, value, price, armor_type_id FROM armor")
        data = crsr.fetchall()

        print(f'''
            ---------------
               BUY ARMOR
            ---------------
            Gold = {self.gold}
            ''')

        for x in range(len(data)):
            print(f"        {x}. {data[x][0]} ({data[x][1]} power) - {data[x][2]} Gold")
        print(f"        {len(data)}. Show your team with all unit's items to analise.")
        print(f"        {len(data)+1}. Return to previous page.")

        while True:
            answer = input("Input your choice here ---> ")
            try:
                answer = int(answer)
            except:
                continue

            if answer > len(data)+1 or answer < 0:
                continue

            if answer == len(data)+1:
                self.item_categories()
            if answer == len(data):
                self.p_team.team_info_shop()
                continue
            else:
                armor_name = data[answer][0]
                armor_value = data[answer][1]
                armor_price = data[answer][2]
                armor_type = data[answer][3]
                if armor_price > self.gold:
                    print("You can't afford to buy this. Choose something cheaper.")
                    continue
                break
        print(f"\n Which unit will get this item?")
        self.p_team.team_info_shop()
        while True:
            answer = input("Input your choice here ---> ")
            try:
                answer = int(answer)
            except:
                continue

            if answer > len(self.p_team.alive_team)-1 or answer < 0:
                continue

            unit = self.p_team.alive_team[answer]
            break
        crsr.execute(f"SELECT armor_type_name FROM armor_types WHERE armor_type_id ='{armor_type}'")
        armor_type = crsr.fetchone()[0]

        if armor_type == "helmet":
            unit.helmet = Armor_module.Helmet(armor_name,armor_value)
        if armor_type == "bodyarmor":
            unit.bodyarmor = Armor_module.BodyArmor(armor_name,armor_value)
        if armor_type == "boots":
            unit.boots = Armor_module.Boots(armor_name,armor_value)
        if armor_type == "shield":
            unit.shield = Armor_module.Shield(armor_name,armor_value)
        self.p_team.team_info_shop()
        self.gold = self.gold - armor_price
        print(f"You have bought {armor_name} for your {unit.name} for {armor_price} gold.")
        time.sleep(1)
        db.close()
        self.item_categories()
        return

    def weapon_shop(self):
        db = sqlite3.connect("Db_shop.db")
        crsr = db.cursor()
        crsr.execute("SELECT weapon_name, value, price, usable_for_unit FROM weapons")
        data = crsr.fetchall()

        print(f'''
            ----------------
               BUY WEAPON
            ----------------
            Gold = {self.gold}
            ''')
        print(f"\n Which unit will get new item?")
        self.p_team.team_info_shop()
        while True:
            answer = input("Input your choice here ---> ")
            try:
                answer = int(answer)
            except:
                continue

            if answer > len(self.p_team.alive_team) - 1 or answer < 0:
                continue

            unit = self.p_team.alive_team[answer]
            break

        crsr.execute(f"SELECT unit_id FROM units WHERE unit_name = '{unit.name.lower()}'")
        unit_id = crsr.fetchone()[0]
        crsr.execute(f"SELECT weapon_name, value, price FROM weapons WHERE usable_for_unit = '{unit_id}'")
        data = crsr.fetchall()
        weapon_name = data[0]
        weapon_value = data[1]
        weapon_price = data[2]
        print()

        for x in range(len(data)):
            print(f"        {x}. {data[x][0]} ({data[x][1]} power) - {data[x][2]} Gold")
        print(f"        {len(data)}. Show your team with all unit's items to analise.")
        print(f"        {len(data)+1}. Return to previous page.")

        while True:
            answer = input("Input your choice here ---> ")
            try:
                answer = int(answer)
            except:
                continue

            if answer > len(data) + 1 or answer < 0:
                continue
            if answer == len(data)+1:
                self.item_categories()
                break
            if answer == len(data):
                self.p_team.team_info_shop()
                continue

            weapon_name = data[answer][0]
            weapon_value = data[answer][1]
            weapon_price = data[answer][2]

            if weapon_price > self.gold:
                print("You can't afford to buy this. Choose something cheaper.")
                continue
            break
        unit.weapon = Weapon_module.Weapon(weapon_name, weapon_value)
        print(f"{unit.name} got new {unit.weapon.name} with {unit.weapon.value} power points for {weapon_price} gold!")
        self.gold -= weapon_price
        print()
        time.sleep(1)
        self.item_categories()
        db.close()

    def ability_shop(self):
        db = sqlite3.connect("Db_shop.db")
        crsr = db.cursor()

        print(f'''
            -----------------
               BUY ABILITY
            -----------------
            Gold = {self.gold}
            ''')
        print(f"\n Which unit will get new item?")
        self.p_team.team_info_shop()

        while True:
            answer = input("Input your choice here ---> ")
            try:
                answer = int(answer)
            except:
                continue

            if answer > len(self.p_team.alive_team) - 1 or answer < 0:
                continue

            unit = self.p_team.alive_team[answer]
            break

        crsr.execute(f"SELECT unit_id FROM units WHERE unit_name = '{unit.name.lower()}'")
        unit_id = crsr.fetchone()[0]
        crsr.execute(f"SELECT ability_name, value, price FROM abilities WHERE usable_for_unit = '{unit_id}'")
        data = crsr.fetchall()
        ability_name = data[0]
        ability_value = data[1]
        ability_price = data[2]
        print()

        for x in range(len(data)):
            print(f"        {x}. {data[x][0]} ({data[x][1]} power) - {data[x][2]} Gold")
        print(f"        {len(data)}. Show your team with all unit's items to analise.")
        print(f"        {len(data) + 1}. Return to previous page.")

        while True:
            answer = input("Input your choice here ---> ")
            try:
                answer = int(answer)
            except:
                continue

            if answer > len(data) + 1 or answer < 0:
                continue
            if answer == len(data)+1:
                self.item_categories()
                break
            if answer == len(data):
                self.p_team.team_info_shop()
                continue

            ability_name = data[answer][0]
            ability_value = data[answer][1]
            ability_price = data[answer][2]

            if ability_price > self.gold:
                print("You can't afford to buy this. Choose something cheaper.")
                continue
            break
        unit.ability = ability_name
        unit.ability_value = ability_value

        print(f"{unit.name} got new {unit.ability} with {unit.ability_value} power points for {ability_price} gold!")
        self.gold -= ability_price
        print()
        time.sleep(1)
        self.item_categories()
        db.close()

    def item_categories(self):
        print(f'''
        ---------------------
           ITEM CATEGORIES
        ---------------------
        Gold = {self.gold}
        
            0. Buy units.
            1. Buy armor.
            2. Buy weapon.
            3. Buy ability.
            4. Show your team with all unit's items to analise.
            5. Return to previous page.
        ''')

        while True:
            answer = input("Input your choice here ---> ")
            if answer not in ["0", "1", "2", "3", "4", "5"]:
                continue
            if answer in ["1", "2", "3"] and len(self.p_team.alive_team) < 5:
                print("You need full team before buying another items")
                continue

            if answer == "0":
                if len(self.p_team.alive_team) == 5:
                    print("\nYour team is full, I won't allow you to recruit new ally")
                    continue
                else:
                    self.unit_shop()
            elif answer == "1":
                self.armor_shop()
                break
            elif answer == "2":
                self.weapon_shop()
                break
            elif answer == "3":
                self.ability_shop()
                break
            elif answer == "4":
                self.p_team.team_info_shop()
                continue
            elif answer == "5":
                self.main()
            break

    def main(self):
        print(f'''
        ----------------------------
            WELCOME TO GAME SHOP
        ----------------------------
        Gold = {self.gold}
        ''')
        print(f'''
        Please, choose what would you like to by here
            0. See all item categories
            1. Look at your team with all unit's items to analise
            2. Exit the shop
        ''')

        while True:
            answer = input("Input your choice here ---> ")
            if answer not in ["0", "1", "2"]:
                continue
            elif answer == "0":
                self.item_categories()
                break
            elif answer == "1":
                self.p_team.team_info_shop()
                continue
            elif answer == "2":
                if len(self.p_team.alive_team) < 5:
                    print("You need full team before buying another items")
                    continue
                print("\n See you next time! Good luck!")
                break
        return