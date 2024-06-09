import random
import UCLASSES


class Team_class():
    alive_team = []
    dead_team = []
    alive_team_arena = []
    dead_team_arena = []
    name = ""

    def create_team_for_p1(self, player_name):
        self.alive_team = [UCLASSES.Archer_class(),
                           UCLASSES.Shaman_class(),
                           UCLASSES.Knight_class(),
                           UCLASSES.Healer_class()]
        self.name = f"{player_name}`s team"

    def create_comp_team_for_arena(self):
        comp_team = []

        list = [UCLASSES.Wizard_class(),
                UCLASSES.Healer_class(),
                UCLASSES.Knight_class(),
                UCLASSES.Shaman_class(),
                UCLASSES.Archer_class(),
                UCLASSES.Barbarian_class()]
        name_list = ["Monster`s squad",
                     "Crocodiles",
                     "Supermen",
                     "WoW warriors",
                     "BlaBla squad",
                     "Pink ponys"]
        for i in range(5):
            rand_index = random.randint(0, len(list)-1)
            rand_char = list.pop(rand_index)
            comp_team.append(rand_char)
        self.alive_team_arena = comp_team

        self.name = random.choice(name_list)

    def display_team_info(self,):
        print(self.alive_team_arena)
        x = 0
        for unit in self.alive_team_arena:
            print(f'{x}) {unit.unit_info()}')
            x += 1

    def check_alive(self):
        for unit in self.alive_team_arena:
            if unit.health_in_arena > 0:
                return True
        return False

    def p_choose_unit(self):
        self.display_team_info()

        while True:
            answer = input("Choose your unit for attack ---> ")

            if len(answer) == 0:
                print("Write smth")
                continue

            try:
                answer = int(answer)
            except:
                print("Please, write a number")
                continue

            try:
                unit = self.alive_team_arena[answer]
            except:
                print("Enter correct number of unit")
                continue

            if unit.life_status != True:
                print("Choose alive unit")
                continue

            return unit

    def comp_choose_unit(self):
        while True:
            unit = random.choice(self.alive_team_arena)
            if unit.life_status == True:
                return unit

    def check_dead_alive(self):
        lst = []
        for unit in self.alive_team_arena:
            if unit.life_status == True:
                lst.append(unit)
            else:
                self.dead_team.append(unit)
            self.alive_team_arena = lst

    def team_info_shop(self):
        x = 0
        for unit in self.alive_team:
            armor = ""
            if unit.helmet.value > 0:
                armor+=f"{unit.helmet.name}({unit.helmet.value}),"
            if unit.bodyarmor.value > 0:
                armor+=f"{unit.bodyarmor.name}({unit.bodyarmor.value}),"
            if unit.boots.value > 0:
                armor+=f"{unit.boots.name}({unit.boots.value}),"
            if unit.shield.value > 0:
                armor+=f"{unit.shield.name}({unit.shield.value})"
            if unit.weapon.value > 0:
                weapon = f"{unit.weapon.name}({unit.weapon.value})"
            else:
                weapon = ""
            if unit.ability_value > 0:
                ability = f"{unit.ability}({unit.ability_value})"
            else:
                ability = ""
            print(f"{x}. {unit.name}; armor - {armor}; weapon - {weapon}; ability - {ability}")
            x += 1
