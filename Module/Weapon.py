import json

class Weapon:
    def __init__(self, type_w, attack, crd, crc):
        self.type_w = type_w
        self.attack = attack
        self.crd = float(crd) / 100
        self.crc = crc

    def get_type(self):
        return self.type_w

wp1 = Weapon('legend', 100, 10, 25)

weapon = {
    "Weapon": 
    [
        {
        "name": "Nidira",
        "id_wp":2,
        "hp": 200,
        "attack": "20", 
        "defence": "10", 
        "critical_damage": "40", 
        "critical_chance": "10"
    },
    {
        "name": "Monster",
        "id_wp":2,
        "hp": 200,
        "attack": "20", 
        "defence": "10", 
        "critical_damage": "40", 
        "critical_chance": "10"
    }
    ]
}

weapon2 = {
    "Weapon": 
    [
        {
        "name": "Nidira",
        "id_wp":2,
        "hp": 200,
        "attack": "20", 
        "defence": "10", 
        "critical_damage": "40", 
        "critical_chance": "10"
    },
    {
        "name": "Monster",
        "id_wp":2,
        "hp": 200,
        "attack": "20", 
        "defence": "10", 
        "critical_damage": "40", 
        "critical_chance": "10"
    }
    ]
}

# with open("data/data_test.json", "w") as weapons:
#         wp = json.dump(weapon, weapons)

with open("data/data_test.json", "r") as weapons:
    wp = json.load(weapons)

print(wp['Weapon'][0])

# print(wp)