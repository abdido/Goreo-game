import random

class Chara:
    def __init__(self, id_chara, name, hp, atk, defence, critical_damage, critical_chance, equipment = None, skin = None):
        self.id_chara = id_chara
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.critical_damage = float(critical_damage) / 100
        self.critical_chance = critical_chance
        self.equipment = equipment
        self.skin = skin

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_atk(self):
        return self.atk

    def get_defence(self):
        return self.defence

    def get_critical_damage(self):
        return self.critical_damage

    def get_critical_chance(self):
        return self.critical_chance


    def attack(self):
        random_number = random.randrange(0, 100)
        crit = self.get_atk() + (float(self.get_critical_damage()) * self.get_atk())
        attack_type = (crit) if float(self.get_critical_chance()) > random_number else self.get_atk()
        
        return attack_type, random_number

    def get_status(self):
        kalimat = """
Status of {}
HP\t: {}
ATK\t: {}
DEF\t: {}
CRD\t: {}
CRC\t: {}
        """.format(self.get_name(), self.get_hp(), self.get_atk(), self.get_defence(), self.get_critical_damage(), self.get_critical_chance())

        return kalimat