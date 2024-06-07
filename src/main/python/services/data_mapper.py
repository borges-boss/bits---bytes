from base.ability import Ability
from base.quest import Quest
from classes.consumable_item import ConsumableItem
from classes.damage_item import DamageItem
from classes.inn import Inn
from classes.monster import Monster
from classes.npc import Npc
from classes.open_fields import OpenFields
from classes.shop import Shop
from classes.tavern import Tavern
from classes.wearable_item import WearableItem
from constants.constants import ITEM_TYPE_CONSUMABLE, ITEM_TYPE_DAMAGE, ITEM_TYPE_WEARABLE, STRUCTURE_TYPE_CAVE, STRUCTURE_TYPE_DUNGEON, STRUCTURE_TYPE_INN, STRUCTURE_TYPE_OPEN_FIELD, STRUCTURE_TYPE_SHOP, STRUCTURE_TYPE_TAVERN
from classes.city import City
from classes.cave import Cave
from classes.dungeon import Dungeon


class DataMapper:


    @staticmethod
    def map_city_to_class_object(city_dict):
        city = City(city_dict['width'], city_dict['height'], city_dict['name'], 
                        city_dict['description'],[DataMapper.map_structures_to_class_object(structure) for structure in city_dict.get('structures', [])] )
        return city


    @staticmethod
    def map_structures_to_class_object(dict_structure):
        structure = None

        if dict_structure['type'] == STRUCTURE_TYPE_INN:
            structure = DataMapper.map_dict_to_good_structure(dict_structure)
        elif dict_structure['type'] == STRUCTURE_TYPE_TAVERN:
            structure = DataMapper.map_dict_to_good_structure(dict_structure)
        elif dict_structure['type'] == STRUCTURE_TYPE_OPEN_FIELD or dict_structure['type'] == STRUCTURE_TYPE_DUNGEON or dict_structure['type'] == STRUCTURE_TYPE_CAVE:
            structure = DataMapper.map_dict_to_dangerous_structure(dict_structure)
        elif dict_structure['type'] == STRUCTURE_TYPE_SHOP:
            structure = DataMapper.map_dict_to_good_structure(dict_structure)
        else:
            print(f"Unknown structure type: {dict_structure['type']}")

        return structure
    
    @staticmethod
    def map_dict_to_item(item_dict):
        type = item_dict.get('type')
        if type == ITEM_TYPE_WEARABLE:
            return WearableItem(
                name=item_dict.get('name'),
                type=item_dict.get('type'),
                rarity=item_dict.get('rarity'),
                weight=item_dict.get('weight'),
                enchantments=item_dict.get('enchantments', []),
                defence=item_dict.get('defence', 0.0),
                wearable_type=item_dict.get('wearable_type', "")
            )
        elif type == ITEM_TYPE_DAMAGE:
            return DamageItem(
                name=item_dict.get('name'),
                type=item_dict.get('type'),
                rarity=item_dict.get('rarity'),
                weight=item_dict.get('weight'),
                enchantments=item_dict.get('enchantments', []),
                damage=item_dict.get('damage', 0.0)
            )
        elif type == ITEM_TYPE_CONSUMABLE:
            return ConsumableItem(
                name=item_dict.get('name'),
                type=item_dict.get('type'),
                rarity=item_dict.get('rarity'),
                weight=item_dict.get('weight'),
                consumable_type=item_dict.get('consumable_type'),
                effect_value=item_dict.get('effect_value'),
                effect_type=item_dict.get('effect_type')
            )
        else:
            raise ValueError(f"Invalid item type: {type}")
        


    @staticmethod
    def map_dict_to_dangerous_structure(structure_dict):
        type = structure_dict.get('type')
        if type == STRUCTURE_TYPE_OPEN_FIELD:
            return OpenFields(
                name=structure_dict.get('name'),
                type=structure_dict.get('type'),
                width=structure_dict.get('width'),
                height=structure_dict.get('height'),
                dificulty=structure_dict.get('dificulty'),
                monsters=[DataMapper.map_dict_to_monster(monster) for monster in structure_dict.get('monsters', [])],
                structures=[DataMapper.map_structures_to_class_object(struct) for struct in structure_dict.get('structures', [])],
                city=structure_dict.get('city')
            )
        elif type == STRUCTURE_TYPE_DUNGEON:
            return Dungeon(
                name=structure_dict.get('name'),
                type=structure_dict.get('type'),
                dificulty=structure_dict.get('dificulty'),
                chests_opened=structure_dict.get('chests_opened'),
                layers=structure_dict.get('layers'),
                bosses=structure_dict.get('bosses'),
                chest_count=structure_dict.get('chest_count'),
                monsters=[DataMapper.map_dict_to_monster(monster) for monster in structure_dict.get('monsters', [])]
            )
        elif type == STRUCTURE_TYPE_CAVE:
            return Cave(
                name=structure_dict.get('name'),
                type=structure_dict.get('type'),
                dificulty=structure_dict.get('dificulty'),
                monsters=[DataMapper.map_dict_to_monster(monster) for monster in structure_dict.get('monsters', [])],
                ores=structure_dict.get('ores')
            )
        else:
            raise ValueError(f"Invalid structure type: {type}")

    @staticmethod
    def map_dict_to_monster(monster_dict):
        return Monster(
            health=monster_dict.get('health'),
            damage=monster_dict.get('damage'),
            defence=monster_dict.get('defence'),
            stamina=monster_dict.get('stamina'),
            race=monster_dict.get('race'),
            type=monster_dict.get('type'),
            name=monster_dict.get('name'),
            mana=monster_dict.get('mana'),
            description=monster_dict.get('description'),
            abilities=[DataMapper.map_dict_to_ability(ability) for ability in monster_dict.get('abilities', [])],
            level=monster_dict.get('level')
        )

    @staticmethod
    def map_dict_to_ability(ability_dict):
        return Ability(
            name=ability_dict.get('name'),
            description=ability_dict.get('description'),
            type=ability_dict.get('type'),
            value=ability_dict.get('value'),
            ability_cost=ability_dict.get('ability_cost')
        )
    


    @staticmethod
    def map_dict_to_good_structure(structure_dict):
        type = structure_dict.get('type')
        if type == STRUCTURE_TYPE_SHOP:
            return Shop(
                name=structure_dict.get('name'),
                type=structure_dict.get('type'),
                width=structure_dict.get('width'),
                height=structure_dict.get('height'),
                shopkeeper=DataMapper.map_dict_to_npc(structure_dict.get('shopkeeper')),
                items_for_sale=[DataMapper.map_dict_to_item(item) for item in structure_dict.get('items_for_sale', [])],
                city=structure_dict.get('city')
            )
        elif type == STRUCTURE_TYPE_INN:
            return Inn(
                name=structure_dict.get('name'),
                type=structure_dict.get('type'),
                width=structure_dict.get('width'),
                height=structure_dict.get('height'),
                inkeeper=DataMapper.map_dict_to_npc(structure_dict.get('inkeeper')),
                rooms=structure_dict.get('rooms', []),
                price_per_stay=structure_dict.get('price_per_stay'),
                city=structure_dict.get('city')
            )
        elif type == STRUCTURE_TYPE_TAVERN:
              return Tavern(
                name=structure_dict.get('name'),
                type=structure_dict.get('type'),
                width=structure_dict.get('width'),
                height=structure_dict.get('height'),
                tavern_keeper=DataMapper.map_dict_to_npc(structure_dict.get('tavern_keeper')),
                quests=[DataMapper.map_dict_to_quest(quest) for quest in structure_dict.get('quests', [])],
                tavern_keeper_dialog=structure_dict.get('tavern_keeper_dialog'),
                city=structure_dict.get('city')
            )
        else:
            raise ValueError(f"Invalid structure type: {type}")

    @staticmethod
    def map_dict_to_npc(npc_dict):
        return Npc(
            health=npc_dict.get('health'),
            defence=npc_dict.get('defence'),
            race=npc_dict.get('race'),
            type=npc_dict.get('type'),
            name=npc_dict.get('name'),
            description=npc_dict.get('description'),
            role=npc_dict.get('role')
        )
    

    @staticmethod
    def map_dict_to_quest(quest_dict):
        reward = quest_dict.get('reward')
        reward_type = quest_dict.get('reward_type')

        if reward_type == 'item':
            reward = DataMapper.map_dict_to_item(reward)

        return Quest(
            name=quest_dict.get('name'),
            description=quest_dict.get('description'),
            reward=reward,
            reward_type=reward_type,
            is_completed=quest_dict.get('is_completed', False)
        )