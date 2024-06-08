import random
from classes.monster import Monster
from services.data_store import DataStore
import curses
import copy


class MonsterService:

    @staticmethod
    def spawn_monster_by_difficulty(difficulty) -> Monster:
        datastore = DataStore()
        monsters = datastore.find_monsters()

        monster = random.choice(monsters)

        if difficulty == 1: 
            monster.level = random.randint(1, 5)
        elif difficulty == 2: 
            monster.level = random.randint(6, 10)
        elif difficulty == 3: 
            monster.level = random.randint(11, 30)

        return monster
    

    @staticmethod
    def spawn_monster(difficulty,monster_pool) -> Monster:
        monster = random.choice(monster_pool)

        if difficulty == 1: 
            monster.level = random.randint(1, 5)
        elif difficulty == 2: 
            monster.level = random.randint(6, 10)
        elif difficulty == 3: 
            monster.level = random.randint(11, 30)

        return copy.deepcopy(monster)
    
    @staticmethod
    def display_monster_hud(monster):
        health_bar = '\033[31m' + '█' * int(monster.health / 10) + '\033[0m'
        mana_bar = '\033[34m' + '█' * int(monster.mana / 10) + '\033[0m'
        stamina_bar = '\033[32m' + '█' * int(monster.stamina / 10) + '\033[0m'

        stdscr = curses.initscr()
        _, term_width = stdscr.getmaxyx()
        curses.endwin()

        print(f"\033[31mHealth: {monster.health}\033[0m [{health_bar:<10}]".rjust(term_width))
        print("")
        print(f"\033[34mMana: {monster.mana}\033[0m [{mana_bar:<10}]".rjust(term_width))
        print("")
        print(f"\033[32mStamina: {monster.stamina}\033[0m [{stamina_bar:<10}]".rjust(term_width))