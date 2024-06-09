from abc import ABC, abstractmethod
from HRSGAME import Armor_module
from HRSGAME import Weapon_module


class Unit_class(ABC):
    name = ""
    health = 100
    attack = 20
    defence = 5
    life_status = True
    health_in_arena = None

    helmet = Armor_module.Helmet()
    bodyarmor = Armor_module.BodyArmor()
    boots = Armor_module.Boots()
    shield = Armor_module.Shield()

    weapon = Weapon_module.Weapon()

    # special abilities
    ability = ""
    ability_value = 0
    ability_cooldown = 0

    #effects
    magic_shield = False
    stunned = False
    poisoned_moves = 0
    poison_value = 0

    def hit_power(self):
        hit_power = self.attack
        return hit_power

    def defence_power(self):
        defence_power = self.defence + self.helmet.value + self.bodyarmor.value + self.boots.value + self.shield.value
        return defence_power

    def unit_info(self):
        return f"Name - {self.name}, health - {self.health}, attack - {self.attack}, defence - {self.defence}, ability - {self.ability}, magic shield - {self.magic_shield}, stunned - {self.stunned}, poisoned(moves) - {self.poisoned_moves}"

    @abstractmethod
    def use_ability(self, attacker, defender, attacker_team, defender_team):
        pass

    def has_magic_shield(self, enemy):
        if enemy.magic_shield == True:
            enemy.magic_shield = False
            print(f"{enemy.name} has magic shield. {self.name} is not able to hurt {enemy.name}")
            return True
        else:
            return False


    def hit(self, enemy):
        if not self.has_magic_shield(enemy):
            if enemy.defence_power() < self.hit_power():
                enemy.health_in_arena = enemy.health_in_arena + enemy.defence_power() - self.hit_power()
                print(f"{self.name} hit {enemy.name} by {self.hit_power()} points")

            if self.defence_power() < enemy.hit_power():
                self.health_in_arena = self.health_in_arena + self.defence_power() - enemy.hit_power()
                print(f"{enemy.name} responsed and hit {self.name} by {enemy.hit_power()} points")

    def is_stunned(self):
        if self.stunned == True:
            self.stunned = False
            print(f"{self.name} is stunned and cannot make move")
            return True
        else:
            return False

    def check_poison(self):
        if self.poisoned_moves > 0:
            self.health_in_arena -= self.poison_value
            self.poisoned_moves -= 1
            print(f"{self.name} has damaged by poisoning for {self.poison_value} HP")
