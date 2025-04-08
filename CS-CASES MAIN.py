#CS:GO Case Opening Sim#

#Defining Rarity#
rarities = {
    "Damaged": 55.92,
    "Worn": 17.87,
    "Normal": 13.05,
    "Cleaned": 7.42,
    "Mint-Condition": 6.98,
    "Stellar": 3.21,
    "One of a Kind": 0.0112
}

#Blue Case Contents#
blue_case_contents = {
    "Damaged": ["Five-Seven | Blue Sky", "P2000 | Aqua"],
    "Worn": ["Nova | Icicle", "MAC-10 | Snowflake"],
    "Normal": ["Desert Eagle | Icy Wind", "AUG | Fresh Wash"],
    "Cleaned": ["MAC-10 | SpearHead", "FAMAS | Booty"],
    "Mint-Condition": ["SSG 08 | Avalanche"],
    "Stellar": ["AK-47 | Black Ice", "AWP | OBSIDIAN"],
    "One of a Kind": ["Karambit | Sapphire Fragment"]
}
#Red Case Contents#
red_case_contents = {
    "Damaged": ["M4A4 | Dragon Breath", "USP-S | Blood Red"],
    "Worn": ["P90 | Sunrise", "CZ75-Auto | Flame"],
    "Normal": ["AWP | FlatLine", "MP7 | Bloodsport"],
    "Cleaned": ["AK-47 | Ruby", "Desert Eagle | Blaze"],
    "Mint-Condition": ["Butterfly Knife | Scarlet Moon"],
    "Stellar": ["M4A1-S | Jordan 1", "AWP | Vandy"],
    "One of a Kind": ["Karambit | Sharingan"]
}
#Black Case Contents#
black_case_contents = {
    "Damaged": ["MAC-10 | Heat", "UMP-45 | Minimal"],
    "Worn": ["P90 | Stalker", "Glock-18 | Bones"],
    "Normal": ["FAMAS | Survivor", "M4A4 | Skull"],
    "Cleaned": ["AK-47 | Shadow", "M4A4 | Beru"],
    "Mint-Condition": ["Karambit | Black Pearl"],
    "Stellar": ["AWP | Igris", "M4A1-S | Howl"],
    "One of a Kind": ["Stiletto Knife | Eclipse"]
}

#The good stuff i love doing #
import random

def choose_rarity():
    roll = random.uniform(0, 100)
    cumulative = 0
    for rarity, chance in rarities.items():
        cumulative += chance
        if roll <= cumulative:
            return rarity
    return "Damaged" #Default if doesnt work#

#Choosing Case#


#more fun stuff to open cases#
def open_case(case_type):

    if case_type == 'blue':
        case_contents = blue_case_contents
    elif case_type == 'red':
        case_contents = red_case_contents
    else:
        case_contents = black_case_contents
    
    
    rarity = choose_rarity()
    item = random.choice(case_contents[rarity])
    print(f"Opening a {case_type.capitalize()} case now!")
    print(f"You got: {item} ({rarity})")

#Possible user input to select which case#
def user_choose_case():
    print ("Pick out which case you would like to open")
    print("1. Blue Case")
    print("2. Red Case")
    print("3. Black Case")

    choice = input("Enter the number of whichever case you want to open (1 | 2 | 3)").strip()

    if choice == '1':
        open_case('blue')
    elif choice == '2':
        open_case('red')
    elif choice == '3':
        open_case('black')
    else:
        print("I SAID PICK ONE TWO OR THREE. TRY AGAIN AND USE YOUR BRAIN")


# Example usage
user_choose_case()

