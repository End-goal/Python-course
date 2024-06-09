from .Unit import Unit_class


class Barbarian_class(Unit_class):
    name = "Barbarian"

    ability = "Stun all enemy units for the next move"

    def use_ability(self, attacker, defender, attacker_team, defender_team):
        for unit in defender_team.alive_team_arena:
            unit.stunned = True
