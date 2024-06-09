
def display_welcome_board():
    return '''
    -------------------------------------------------------------------------

                      *********** GAME OF HEROES ***********

                          -- the game by unknown man --

    -------------------------------------------------------------------------
    '''


def get_player_name():
    return "Young hero, tell me your name --> "


def welcome_hero(player_name, all_arenas):
    return f'''
        Welcome young hero {player_name}!
        Take some money and create your own squad to fight in {all_arenas} arenas!
        Lets begin your own story!
    '''


def wow_you_have_a_squad(player_team):
    text = '''
    Wow! You have your squad from 4 heroes!
    '''
    for unit in player_team:
        text += "\n" + unit.unit_info()
    return text


def arena_is_cleared(rewarded, arena_num, gold):
    return f'''\n \n
    Take {rewarded} gold for successful battle in {arena_num} Arena.
    Now you have {gold} gold in your bag.
    Let us prepare to the next battle and go to shop
    to recruit new teammates and items for them.
    \n\n
    Press ENTER to continue --->
    '''


def arena_is_lost():
    return '''
    You lose this arena, but you can recruit new units.
        
    Press ENTER to return to shop --->
    '''


def display_arena_board(player_t, comp_t, arena_counter):
    return f'''
        -------------------------------------------------------------------------
                         ***** ARENA №{arena_counter} BOARD *****
        -------------------------------------------------------------------------
                                Welcome to the arena!!
         {player_t.name}                  vs                       {comp_t.name}
    '''


def display_arena_results(arena_counter):
    return f'''
            -------------------------------------------------------------------------
                          ***** ARENA №{arena_counter} RESULTS *****
            -------------------------------------------------------------------------
    '''


def choose_unit_for_fight(fight_counter):
    return f'''
            -------------------------------------------------------------------------
                           CHOOSE UNIT FOR FIGHT #{fight_counter}!
    '''


def display_fight_board(attacker, defender, fight_counter):
    return f'''
            -------------------------------------------------------------------------
                           ***** FIGHT #{fight_counter} BOARD *****
            -------------------------------------------------------------------------
            Attacker                         vs                        Defender
            {attacker.name}                                            {defender.name}
            
            Attacker - {attacker.unit_info()}
            Defender - {defender.unit_info()}
'''


def display_fight_result(attacker, defender):
    return f'''           
            {attacker.name} status: {attacker.life_status}; health: {attacker.health_in_arena}
            {defender.name} status: {defender.life_status}; health: {defender.health_in_arena}
'''


def game_won(name, all_arenas):
    return f'''
    Young hero {name}, you`ve won all {all_arenas} battles!!
    
    Now you will become the most famous hero and people will tell legends about you.
    Now you can go and rest with your teammates. 
    But all those who died in your adventure won`t be forgotten.
    
                    R.I.P. to all fallen
    '''


def game_lost(name):
    return f'''
    Young hero {name}, you made a good way to achieve your dreams.
    But your enemies was stronger and smarter.
    
    Go and rest in your home to become stronger.
    
                    R.I.P. to all fallen
    '''
