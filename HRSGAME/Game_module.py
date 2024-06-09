import time

import Texts_module
import UCLASSES
from Arena_module import ArenaClass
import Team_module
import Shop_module
import sqlite3

class Game_class():
    player_name = ""
    player_gold = 1000
    all_arenas = 5
    arena_counter = 0
    win_status = None
    base_reward = 100

    def game_continue(self):
        if self.arena_counter < 5:
            return True
        if len(self.player_team.alive_team) < 5:
            unit_needed = 5 - len(self.player_team.alive_team)
            db = sqlite3.connect("Db_shop.db")
            crsc = db.cursor()
            crsc.execute("SELECT unit_price FROM units")
            dt = crsc.fetchall()
            db.close()
            lst = []
            for price in dt:
                lst.append(price[0])
            min_price = min(lst)
            min_budget = unit_needed * min_price
            if self.player_gold > min_budget:
                return True
        else:
            return False

    def calculate_reward(self):
        rew = self.base_reward
        for arena_num in range(self.arena_counter):
            rew = rew * 1.5
        return rew


    def play(self):
        self.arena_counter = 0

        print(Texts_module.display_welcome_board())
        self.player_name = input(Texts_module.get_player_name())
        print(Texts_module.welcome_hero(self.player_name, self.all_arenas))
        time.sleep(1)
        self.player_team = Team_module.Team_class()
        self.player_team.create_team_for_p1(self.player_name)

        print(Texts_module.wow_you_have_a_squad(self.player_team.alive_team))
        time.sleep(4)


        while self.game_continue():

            shop = Shop_module.Shop_class(self.player_team, self.player_gold)
            shop.main()

            arena = ArenaClass(self.player_team, self.arena_counter)
            arena.create_comp_team()
            arena.display_arena_board()
            arena.arena_fight()
            arena.display_arena_results()

            arena_results = arena.arena_results()
            self.player_team.alive_team = arena_results[0]
            self.player_team.dead_team.append(arena_results[1])

            if self.player_team.alive_team:
                arena_rew = self.calculate_reward()
                self.player_gold += arena_rew
                print(Texts_module.arena_is_cleared(arena_rew, self.arena_counter, self.player_gold))
                input()
                self.arena_counter += 1
            elif self.game_continue():
                print(Texts_module.arena_is_lost())
                input()
            else:
                self.win_status = False
                break

        if self.win_status == True:
            print(Texts_module.game_won(self.player_name, self.all_arenas))
        else:
            print(Texts_module.game_lost(self.player_name))

        u_inp = None
        while u_inp not in ["y", "n"]:
            u_inp = input("Want to take revenge? (Y/N) - ").lower()
            if u_inp == "y":
                self.play()
            elif u_inp == "n":
                break


game = Game_class()
game.play()