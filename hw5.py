import random
from functools import reduce
# === CS 115 Homework 5 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name: Esther Li
#
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Homework 5 ===

class Item:
    """
    An item with components name, damage points, damage types, regeneration points, and whether it is consumable or not 
    """
    def __init__(self, n, dp, rp, dt, ic):
        """
        The constructor that creats a new Item with new attributes
        """
        self.name =  n
        self.damage_points = dp
        self.damage_type = dt
        self.regeneration_points = rp
        self.is_consumable = ic
    def __str__(self):
        """
        Prints the item with its name and damage points
        """
        return "Name: " + self.name + " | Damage points: " + str(self.damage_points) + " | Regeneration points: " + str(self.regeneration_points)
  
    def __lt__(self, other):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return self.damage_points < other.damage_points

    def __hash__(self):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return hash((self.name, self.damage_points, self.regeneration_points, self.damage_type, self.is_consumable))

    def __repr__(self):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        return str(self)

    def __eq__(self, other):
        """ DO NOT CHANGE THIS FUNCTION UNLESS YOU 100% KNOW WHAT YOU ARE DOING """
        if not isinstance(other, Item):
            return False
        return (self.name == other.name and
            self.damage_points == other.damage_points and
            self.regeneration_points == other.regeneration_points and
            self.damage_type == other.damage_type and
            self.is_consumable == other.is_consumable)

class Character:
    """represents the character"""
    def __init__(self, name, max_health_points):
        """constructs the charater"""
        self.name = name
        self.health_points = max_health_points
        self.inventory = {}
        self.inventory[Item("rusty axe", 1, 0, "physical", False)] = 1
    def __str__(self):
        """Prints the character's name and health points"""
        return "Name: " + self.name + "| hp: " + str(self.health_points)
    def __lt__(self, other):
        """compares the health of the two characters"""
        return self.health_points < other.health_points
    def transfer_loot(self, loot):
        """transfers all items in loot to the character's inventory"""
        def add_item(item):
            """
            Adds everything in loot to inventory
            """
            if item in self.inventory:
                self.inventory[item] += loot[item]
            else:
                self.inventory[item] = loot[item]
            loot[item] = 0
                
        list(map(add_item, list(loot.keys())))
        loot = {}
        
    def get_next_move(self, other_characters):
        """Gets the next move the character will make, hitting the character with the least health with the item that makes the  most damage"""
        maxDamage = reduce(lambda x, y: y if x.damage_points < y.damage_points else x, self.inventory)
        return Move(min(other_characters), maxDamage)
        
    def perform_move(self, move):
        """
        Executes a move
        """
        if move.item in self.inventory:
            (move.other_character).health_points -= (move.item).damage_points
            self.health_points += (move.item).regeneration_points
            if move.item.is_consumable:
                self.inventory[move.item] -= 1
      

class Robot(Character):
    """Robot character"""
    def __init__(self, name, max_health_points):
        """Constructs the robot character"""
        super().__init__(name, max_health_points)
        self.inventory[Item("shock baton", 1, 0, "electrical", False)] = 1
    def get_next_move(self, other_characters):
        """Creates a move object"""
        return Move(other_characters[0], Item("shock button", 1, 0, "electrical", False))
    def perform_move(self, move):
        """Executes the move"""
        if move.item in self.inventory:
            (move.other_character).health_points -= (move.item).damage_points
            self.health_points += (move.item).regeneration_points
            if move.item.damage_type == "electrical":
                (move.other_character).health_points -= (move.item).damage_points
            if move.item.is_consumable:
                self.inventory[move.item] -= 1
        

class Zombie(Character):
    def __init__(self, name, max_health_points):
        """Constructs the Zombie character"""
        super().__init__(name, max_health_points)
        self.inventory[Item("brain grenade", 5, 0, "viral", True)] = 3
    def get_next_move(self, other_characters):
        """Creates a move object"""
        return Move(other_characters[0], Item("brain grenade", 5, 0, "viral", True))
    def perform_move(self, move):
        """Executes the move"""
        if move.item in self.inventory:
            (move.other_character).health_points -= (move.item).damage_points
            self.health_points += (move.item).regeneration_points
            if move.item.damage_type == "viral":
                (move.other_character).health_points -= (move.item).damage_points
            if move.item.is_consumable:
                self.inventory[move.item] -= 1 
        
    

class PlayableCharacter(Character):
    def get_user_input(self, other_characters):
        """Gets a move according to user's input"""
        print("Here is your inventory: ")
        print(self.inventory)
        print("Here are your enemies:")
        print(str((list(map(lambda x: str(x), other_characters)))))
        used_item = input("Enter item name: ")
        attack = int(input("Enter enemy number (starting from 0): "))
        return Move(other_characters[attack], get_inventory_item_from_item_name(used_item, self.inventory))
    def get_next_move(self, other_characters):
        """The next move is according to the user input"""
        return self.get_user_input(other_characters)
class Move:
    """
    Represents an action a character takes in a turn.
    """

    def __init__(self, other_character, item):

        """Constructs a move object"""
        self.other_character = other_character
        self.item = item

    def __str__(self):
        """ pretty prints Move. Do not change, but you can use as an example """
        return "Move: " + "\r\n" + "    Item: " + str(self.item) + "\r\n" + "    Target character: " + str(self.other_character)





def spawn_enemies():
    """
    returns enemies based on what has already been implemented

    change this to include any characters you have implemented!
    """
    cubebot_1 = Character("little cubebot", 1)
    cubebot_2 = Character("armor cube", 2)
    return [cubebot_1, cubebot_2]

def standard_battle(main_character, enemies, enemy_that_will_attack):
    """
    Executes one round of combat between the player and a chosen enemy.

    Steps:
    1. The main_character selects a move using get_next_move(enemies).
    2. The main_character applies that move to its chosen target.
    3. If the target's health points reach 0, the main_character transfers
       all items from that target's inventory.
    4. Otherwise, enemy_that_will_attack selects a move using
       get_next_move([main_character]) and applies it.
    5. If the main_character's health points reach 0, the attacking enemy
       transfers all items from the main_character's inventory.
    """
    if main_character.health_points > 0 and enemy_that_will_attack.health_points > 0:
        selectedMove = main_character.get_next_move(enemies)
        main_character.perform_move(selectedMove)
        if selectedMove.other_character.health_points <= 0:
            main_character.transfer_loot(selectedMove.other_character.inventory)
        else:
            enemy_that_will_attack.perform_move(enemy_that_will_attack.get_next_move([main_character]))
            if main_character.health_points <= 0:
                enemy_that_will_attack.transfer_loot(main_character.inventory)
        


def main_game_loop():
    """
    Do not change. If you would like a different game loop, implement 
    one and call it custom_main_game_loop 
    """
    main_character = PlayableCharacter("player", 15)
    enemies = spawn_enemies()
    while True:
        print("Main character info: " + str(main_character))
        enemies = [e for e in enemies if e.health_points > 0]
        if not enemies:
            print("You win!")
            break

        enemy = random.choice(enemies)
        standard_battle(main_character, enemies, enemy)
        print(f"Your stats: {main_character}")

        if main_character.health_points <= 0:
            print("You were defeated!")
            break

def get_inventory_item_from_item_name(item_name, inventory):
    """
    Helper function that might make get_next_move for PlayableCharacter easier
    Returns the Item object from inventory (dict with Item keys)
    whose name matches item_name, or None if not found.
    Assumes there will be just one matching item_name in the
    inventory, or will just match the first
    """
    name_matches = filter(lambda item: item.name == item_name, map(lambda i: i, inventory))
    return next(name_matches, None)


if __name__ == "__main__":

    main_game_loop() # uncomment this to start a game with the staff framework

        
