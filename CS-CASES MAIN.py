#CS:GO Case Opening Sim#

#Defining Rarity#
rarities = {
    "Damaged": 66.92,
    "Worn": 23.87,
    "Normal": 13.05,
    "Cleaned": 3.42,
    "Mint-Condition": 2.98,
    "Stellar": 33.21,
    "One of a Kind": 0.0112
}

#Blue Case Contents#
case_contents = {
    "Damaged": ["Five-Seven | Blue Sky", "P2000 | Aqua"],
    "Worn": ["Nova | Icicle", "MAC-10 | Snowflake"],
    "Normal": ["Desert Eagle | Icy Wind", "AUG | Fresh Wash"],
    "Cleaned": ["MAC-10 | SpearHead", "FAMAS | Booty"],
    "Mint-Condition": ["SSG 08 | Avalanche"],
    "Stellar": ["AK-47 | Black Ice", "AWP | OBSIDIAN"],
    "One of a Kind": ["Karambit | Sapphire Fragment"]
}
import random

def choose_rarity():
    roll = random.uniform(0, 100)
    cumulative = 0
    for rarity, chance in rarities.items():
        cumulative += chance
        if roll <= cumulative:
            return rarity
    return "Damaged"

def open_case():
    rarity = choose_rarity()
    item = random.choice(case_contents[rarity])
    print(f"You got: {item} ({rarity})")

# Example usage
open_case()

#Red Case Contents#
#Black Case Contents#