from .Unit import Unit_class

class Wizard_class(Unit_class):
    name = "Wizard"

    ability = "Creates shield for all allies to protect them from 1 enemy attack"

    def use_ability(self, attacker, defender, attacker_team, defender_team):
        for unit in attacker_team.alive_team_arena:
            unit.magic_shield = True
            print(f"{self.name} gave {unit.name} magic shield for 1 defence")
