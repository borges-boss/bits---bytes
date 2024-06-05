import random
from classes.monster import Monster
from services.data_store import DataStore


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

        return monster