import keyboard
import json
import os
import random


items = [
    {'name': 'Bone', 'strength': 1, 'rarity': 'common'},
    {'name': 'Iron', 'strength': 5, 'rarity': 'uncommon'},
    {'name': 'Gold', 'strength': 10, 'rarity': 'rare'},
    {'name': 'Titanium', 'strength': 20, 'rarity': 'legendary'},
    
    {'name': 'Feather', 'speed': 1, 'rarity': 'common'},
    {'name': 'Silver', 'speed': 5, 'rarity': 'uncommon'},
    {'name': 'Magnesium', 'speed': 10, 'rarity': 'rare'},
    {'name': 'Meteorite', 'speed': 20, 'rarity': 'legendary'},
    
    {'name': 'Leaf', 'intelligence': 1, 'rarity': 'common'},
    {'name': 'Wood', 'intelligence': 5, 'rarity': 'uncommon'},
    {'name': 'Copper', 'intelligence': 10, 'rarity': 'rare'},
    {'name': 'Platinum', 'intelligence': 20, 'rarity': 'legendary'},

  
    {'name': 'Fur', 'health': 1, 'rarity': 'common'},
    {'name': 'Stone', 'health': 5, 'rarity': 'uncommon'},
    {'name': 'Aluminum', 'health': 10, 'rarity': 'rare'},
    {'name': 'Obsidian', 'health': 20, 'rarity': 'legendary'}
]


def play():
   
    print("\nYou win if your Attack Points are greater!")
    
    
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11] * 4
    random.shuffle(deck)
    
    player_cards = [deck.pop(), deck.pop()]
    enemy_cards = [deck.pop()]
    
    player_total = sum(player_cards)
    enemy_total = sum(enemy_cards)
    while True:
        print('\nAttack Points:', player_cards)
        print('Jungle Beast:', enemy_cards)
        action = input('\nDo you want to:\n1. Attack \n2. Charge\n')
        if action.lower() == '2':
            print("\nCharging Attack...")
            player_cards.append(deck.pop())
            if sum(player_cards) > 21:
                print('\nThe Jungle Devoured You. Try Again.')
                print('\nAttack Points:', player_cards, 'Total:', player_total)
                print('Jungle Beast:', enemy_cards , 'Total:', enemy_total)  
                return
        else:
            break
    
    enemy_cards.append(deck.pop())
    player_total = sum(player_cards)
    enemy_total = sum(enemy_cards)
    print('\nAttack Points:', player_cards)
    print('Jungle Beast:', enemy_cards)
    
    while enemy_total < 17:
        enemy_cards.append(deck.pop())
        enemy_total = sum(enemy_cards)
        print('\nAttack Points:', player_cards, 'Total:', player_total)
        print('Jungle Beast:', enemy_cards , 'Total:', enemy_total)    
    
    if player_total > enemy_total or enemy_total > 21: 
        print('\nCongratulations! You won.')
        item = random.choice(items)
        loaded_player.add_inventory(item)
        print('\nYou received', item['name'], 'with stats:', item)
        
    elif enemy_total > 21:
        print('\nThe Beast Ran Away. You Won.')
        item = random.choice(items)
        loaded_player.add_inventory(item)
        print('\nYou received', item['name'], 'with stats:', item)
        
    elif player_total == enemy_total:
        print("It's a draw.")
        
    elif enemy_total == 21:
        print('\nThe Jungle Devoured You. Try Again.')  
    else:
        print('\nThe Jungle Devoured You. Try Again.')
      
        


        
        
        
        
def pause():
    while True:
        if keyboard.read_key() == 'enter':
            break            
            


class Player:
    def __init__(self, name, house, inventory, equipped, stats):
        self.name = name
        self.house = house
        self.inventory = inventory
        self.equipped = equipped
        self.stats = stats
        
    def get_profile(self):
        return{
            "name": self.name,
            "house": self.house,
            "inventory": self.inventory,
            "equipped": self.equipped,
            "stats": self.stats}

    def add_inventory(self, item):
        self.inventory.append(item)
        save_profile(self)
        
    def add_equipped(self, item):
        self.equipped.append(item)
        self.inventory.remove(item)
        for k in item.keys():
            if k in self.stats.keys():
                self.stats[k] += item[k]
        save_profile(self)        
        
    def unequip(self, item):
        self.inventory.append(item)
        self.equipped.remove(item)
        for k in item.keys():
            if k in self.stats.keys():
                self.stats[k] -= item[k]
        save_profile(self)
    

def save_profile(player):
    filename = 'profiles.json'
    try:
        with open(f"{player.name}.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        with open(f"{player.name}.json", "w") as f:
            json.dump(player.get_profile(), f)
    else:
        data.update(player.get_profile())
        with open(f"{player.name}.json", "w") as f:
            json.dump(data, f)
        
def load_profile(name):
    with open(f"{name}.json", "r") as f:
        data = json.load(f)
    player = Player(data['name'], data['house'], data['inventory'], data['equipped'], data['stats'])
    return player
        

def inv():
    print('\nInventory:')
    for i, item in enumerate(loaded_player.inventory):
        print(f'{i+1}. {item["name"]}')
        

    while True:
        choice = input('\nEnter the number of the item you want to inspect or equip, or "q" to quit: ')
        if choice.lower() == 'q':
            return
        try:
            index = int(choice) - 1
            item = loaded_player.inventory[index]
            print(f'\n{item["name"]} stats: {item}')
            action = input('Do you want to equip this item? (y/n) ')
            if action.lower() == 'y':
                if len(loaded_player.equipped) == 4:
                    print('You cannot equip more than 4 items.')
                else:
                    loaded_player.add_equipped(item)
                    print(f'You equipped the {item["name"]}.')
            else:
                print(f'You chose not to equip the {item["name"]}.')
        except:
            print('Invalid choice.')

def unequip():
    print('\nEquipped items:')
    for i, item in enumerate(loaded_player.equipped):
        print(f'{i+1}. {item["name"]}')
        
   
    while True:
        choice = input('\nEnter the number of the item you want to inspect or unequip, or "q" to quit: ')
        if choice.lower() == 'q':
            return
        try:
            index = int(choice) - 1
            item = loaded_player.equipped[index]
            print(f'\n{item["name"]} stats: {item}')
            action = input('Do you want to unequip this item? (y/n) ')
            if action.lower() == 'y':
                loaded_player.unequip(item)
                print(f'You unequipped the {item["name"]}.')
            else:
                print(f'You chose not to unequip the {item["name"]}.')
        except:
            print('Invalid choice.')


    
#Start Game  

   
print("\n\n\n\nPress 'Enter' to start the game\n\n")
pause()
print("__________________d888b_______________d8b")
print("_________________d88888b_____________d888b")
print("_______________d88888888b__________d888888b")
print("_______________d8888888b************88888888b")
print("________88******888*_________________88888P")
print("______888____,888_______________________8P,")
print("____888____8888__________________________8,")
print("___88_____8888_______88888________________8,")
print("__888____d88888_____8888888______88888_____8,")
print("_8888____8888888_____888888_____8888888____8")
print("_88888___8888888______888_______888888____8,")
print("_888888___88888I88_______________888_____8,")
print("__888888___888I888888_____88888________88,")
print("___8888888__8888888888888__******___8888888,")
print("___888888888_88888888888888_**_88888888888")
print("___8888888888888888888888888888888Id888888")
print("____888888888888888888888888888888888888b")
print("_____888888888_8888888888b____88888888888")
print("______88888888__8888888888_____8888888888")
print("_______8888888__8888888888_____ad8888888")
print("________888888b__888888888______8888888")
print("__________________88888888")     
print("\nWELCOME TO THE JUNGLE")


while True:
    username = input("\nWhat is your name?\n")
    if os.path.isfile(f"{username}.json"):
        print("Profile found!")
        load_existing_profile = input("Would you like to load your existing profile? (y/n) ")
        if load_existing_profile.lower() == "y":
            loaded_player = load_profile(username)
            print(f"Welcome back, {loaded_player.name}!")
            break
    else:
        create_new_profile = input("Profile not found. Would you like to create a new profile? (y/n) ")
        if create_new_profile.lower() == "y":
            #House Selection
            print("\nWelcome to the House of Beasts!\n\nPlease choose your House:\n1. House of Rhino (+10 Strength)\n2. House of Falcon (+10 Speed)\n3. House of Orca (+10 Intelligence)\n4. House of Crocodile (+10 Health)\n\nEnter House Number:")

            stats = {"strength" : 1,
                     "speed" : 1,
                     "intelligence" : 1,
                     "health" : 1}
            while True:
                house = input("Please type and enter your chosen House:")                     
                if house in ("1", "2", "3", "4"):
                    break
                print("Invalid house name. Please try again.")

            if house == "1":
                print(f"\nYou have chosen the House of Rhino\nWelcome to the strongest house, {username}!")
                stats["strength"] = 10
        
            elif house == "2":
                print(f"\nYou have chosen the House of Falcon\nWelcome to the fastest house, {username}!")  
                stats["speed"] = 10
                
            elif house == "3":
                print(f"\nYou have chosen the House of Orca\nWelcome to the smartest house, {username}!")
                stats["intelligence"] = 10
                
            elif house == "4":
                print(f"\nYou have chosen the House of Crocodile\nWelcome to the healthiest house, {username}!")
                stats["health"] = 10
                
            inventory = []
            equipped = []

            # Create a new player object and save their profile
            player = Player(username, house, inventory, equipped, stats)
            save_profile(player)
            loaded_player = player
            break
            
while True:
    select = input("\nWhat do you want to do:\n1. play\n2. inventory\n3. equipped\n4. stats\n5. exit game\n")
    if select in ("1", "2", "3", "4", "5"):
        if select == "1":
            play()
        elif select == "2":
            inv()
        elif select == "3":
            unequip()
        elif select == "4":
            print("\n", loaded_player.stats)
            
        elif select == "5":
            
            
            
            print("\nClosing Game...")
            break
            
    else:
        print("Invalid selection. Please try again.")
              
            
            