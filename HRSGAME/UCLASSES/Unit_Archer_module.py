from .Unit import Unit_class


class Archer_class(Unit_class):
    name = "Archer"

    ability = "Triple hit to 1 enemy unit"

    def use_ability(self, defender, attacker_team, defender_team):
        if not self.has_magic_shield(defender):
            defender.health_in_arena = defender.health_in_arena + defender.defence_power() - 3 * self.hit_power()
            print(f"{self.name} hits {defender.name} by {3 * self.hit_power()} points")
