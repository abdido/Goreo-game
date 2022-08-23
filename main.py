from Module.Character import Chara
from Module.Gatcha import Gatcha
import json

# id_chara, name, hp, atk, defence, critical_damage, critical_chance, equipment = None, skin = None
# Noir = Chara('Lucius', 200, 20, 10, 40, 10)

# introduction
print("""Selamat Datang di Gatcha v.Alpha
Apakah anda ingin Melanjutkan ?""")
while True:
    # lanjut = str(input(" YA / TIDAK :")).upper()
    lanjut = "YA"
    print(lanjut)
    if lanjut == "TIDAK":
        name = input("Masukkan nama :\n")
        break
    elif lanjut == "YA":
        with open("data/data_characters.json") as characters:
            chara = json.load(characters)
            check_chara = chara.keys()
            for i in check_chara:
                print(i)
            name = input("Siapakah anda ? :\n")
            # name = "Noir"
            if name in check_chara:
                print("Baiklah {} kami akan membawamu kembali.".format(name))
                data = chara[name]
                # print(data['hp'])
                # print(data['name'])
                player = Chara(data['id_chara'], name, data['hp'], data['attack'], data['defence'], data['critical_damage'], data['critical_chance'])
                print(player.get_status())
                lanjut = input("Apakah kamu yakin itu dirimu ? YA / TIDAK\n").upper()
                if lanjut == 'YA':
                    break
                elif lanjut == 'TIDAK':
                    continue
                else:
                    print("Maaf aku tidak mengerti.")
            else:
                print("Maaf, Kami tidak mengenalmu\n")
        break
    else:
        print("Maaf, Aku tidak mendengarmu. Bisa ucapkan sekali lagi ?")

# play
if __name__ == "__main__":
    while True:
        print("Hai Tuan {} apakah yang ingin kamu lakukan ?".format(player.get_name()))
    # x = input("1. Eksplorasi\t2. Dungeon\t3. Gacha\t4.Shop")
        x = 3
        if x == 1:
            continue
        elif x == 2:
            continue
        elif x == 3:
            print(Gatcha.spin())
        elif x == 4:
            continue
        break

# with open("data/data_characters.json", "w") as players_data:
#     json.dump(data_players, players_data)
# with open("data/data_monsters.json", "w") as monsters:
#     json.dump(data_monsters, monsters)


