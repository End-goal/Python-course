from .Unit import Unit_class


class Shaman_class(Unit_class):
    name = "Shaman"

    ability_value = 10
    poisoned_moves_default = 2
    ability = f"Poisons all enemy units for next 2 moves by {ability_value}"

    def use_ability(self, attacker, defender, attacker_team, defender_team):
        for unit in defender_team.alive_team_arena:
            if not self.has_magic_shield(defender):
                defender.poisoned = True
                defender.poisoned_moves = self.poisoned_moves_default
                defender.poison_value = self.ability_value
                print(f"{defender.name} has been poisoned by {self.name} for {self.poisoned_moves}")
