from .Unit import Unit_class


class Healer_class(Unit_class):
    name = "Healer"

    ability = "Heals all teammates by 50"
    ability_value = 50

    def use_ability(self, attacker, defender, attacker_team, defender_team):
        for unit in attacker_team.alive_team_arena:
            if unit.life_status == True:
                unit.health_in_arena += self.ability_value
                if unit.health_in_arena > unit.health:
                    unit.health_in_arena = unit.health
                print(f"{self.name} heals {unit.name} by {self.ability_value} HP")
