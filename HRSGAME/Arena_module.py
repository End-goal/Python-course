import Team_module
import Texts_module
import Fight_module

class ArenaClass():

    def __init__(self, init_player_team, init_counter_arena):
        self.player_team = init_player_team
        self.player_team.alive_team_arena = self.player_team.alive_team
        self.player_team.dead_team_arena = []
        self.fight_counter = 0
        self.counter_arena = init_counter_arena

    def create_comp_team(self):
        self.comp_team = Team_module.Team_class()
        self.comp_team.create_comp_team_for_arena()

    def display_arena_board(self):
        print(Texts_module.display_arena_board(self.player_team, self.comp_team, self.counter_arena))
        print()
        print(self.player_team.name)
        print(self.player_team.display_team_info())
        print()
        print(self.comp_team.name)
        print(self.comp_team.display_team_info())

    def arena_fight(self):
        for team in [self.player_team, self.comp_team]:
            for unit in team.alive_team_arena:
                unit.health_in_arena = unit.health
                
        while self.player_team.check_alive and self.comp_team.check_alive:
            self.fight_counter += 1
            print(Texts_module.choose_unit_for_fight(self.fight_counter))
            
            if self.fight_counter%2 != 0:
                print("Player chooses his unit for attack")
                player_unit = self.player_team.p_choose_unit()
                print(f"player chosed {player_unit.name}")
                print()
                print("Player chooses unit to attack")
                comp_unit = self.comp_team.p_choose_unit()
                print(f"Player chosed {comp_unit.name}")
            else:
                print("Computer chooses it`s unit for attack")
                comp_unit = self.comp_team.comp_choose_unit()
                print(f"Computer chosed {comp_unit.name}")
                print()
                print("Computer chooses unit to attack")
                player_unit = self.player_team.comp_choose_unit()
                print(f"Computer chosed {player_unit}")

            fight = Fight_module.Fight_class(player_unit,
                                             comp_unit,
                                             self.fight_counter,
                                             self.player_team,
                                             self.comp_team)
            fight.fight()

    def display_arena_results(self):
        print(Texts_module.display_arena_results(self.counter_arena))
        ...

    def arena_results(self):
        return [[self.player_team.alive_team_arena],
                [self.player_team.dead_team_arena]]
