import Texts_module


class Fight_class():

    def __init__(self, init_player_unit, init_comp_unit, init_fight_counter, init_player_team, init_comp_team):
        self.p_un = init_player_unit
        self.comp_un = init_comp_unit
        self.fight_count = init_fight_counter
        self.p_team = init_player_team
        self.comp_team = init_comp_team

    def display_fight_board(self):
        if self.fight_count % 2 != 0:
            print(Texts_module.display_fight_board(attacker = self.p_un,
                                                   defender = self.comp_un,
                                                   fight_counter = self.fight_count))
        else:
            print(Texts_module.display_fight_board(attacker=self.comp_un,
                                                   defender=self.p_un,
                                                   fight_counter = self.fight_count))

    def check_ability_player(self):
        if self.p_un.ability_cooldown == 0:
            print(f"{self.p_un.name} is ready to use his ability ({self.p_un.ability})")

            u_inp = ""
            while len(u_inp) == 0 or \
                   u_inp[0].lower() not in ["y", "n"]:
                u_inp = input(" do you wanna use this ability now?(Y/N) ---> ")
                if u_inp[0].lower() == "y":
                    self.p_un.ability_cooldown = 3
                    return True
                else:
                    self.p_un.ability_cooldown = 0
                    return False
            else:
                self.p_un.ability_cooldown -= 1
                return False

    def check_ability_computer(self):
        if self.comp_un.ability_cooldown == 0:
            self.comp_un.ability_cooldown = 3
            return True
        else:
            self.comp_un.ability_cooldown -= 1
            return False

    def attack(self):
        pass

    def fight(self):
        self.display_fight_board()

        if self.fight_count % 2 != 0 and not self.p_un.is_stunned():
            if self.check_ability_player():
                self.p_un.use_ability(attacker=self.p_un,
                                      defender=self.comp_un,
                                      attacker_team=self.p_team,
                                      defender_team=self.comp_team)
            else:
                self.p_un.hit(self.comp_un)
                attacker = self.p_un
                defender = self.comp_un
        elif self.fight_count % 2 == 0 and not self.comp_un.is_stunned():
            if self.check_ability_computer():
                self.comp_un.use_ability(attacker=self.p_un,
                                         defender=self.p_un,
                                         attacker_team=self.comp_team,
                                         defender_team=self.p_team)
            else:
                self.comp_un.hit(self.p_un)
                attacker = self.comp_un
                defender = self.p_un



        for team in [self.p_team,
                     self.comp_team]:
            print(f"{team.name}")
            for unit in team.alive_team_arena:
                unit.check_poison()
                print()

        print(Texts_module.display_fight_result(attacker, defender))

        for team in [self.p_team,
                     self.comp_team]:
            team.check_dead_alive()
