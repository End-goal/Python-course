from .Unit import Unit_class


class Knight_class(Unit_class):
    name = "Knight"

    ability_value = 0.5
    ability = f"Hits all enemy squad by {ability_value * 100}% of own attack"

    def use_ability(self, attacker, defender, attacker_team, defender_team):
        for unit in defender_team.alive_team_arena:
            if not self.has_magic_shield(defender):
                unit.health_in_arena = unit.health_in_arena + defender.defence_power() - self.ability_value * self.hit_power()
                print(f"{self.name} hits {unit.name} by {self.ability_value * self.hit_power()} points")
