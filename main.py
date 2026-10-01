import json
import pandas as pd

class Character:
    def __init__(self,data : dict):
        self.name = data["hero_name"]
        self.category = data["category"]
        self.max_hp = data["max_hp"]
        self.hp = data['max_hp']
        self.energy = data['max_energy']
        self.max_energy = data["max_energy"]
        self.attack = data["attack"]
        self.anime = data["anime"]
        self.energy_name = data["energy_name"]
        self.form = data.get('form','0')
        self.is_transformed = False

    def show_info(self, stats = None):
        if stats is None:
            print(f"{'Name ' : <21} : {self.name}")
            print(f"{'Anime || Category' :<22}: {self.anime} || {self.category}" )
            print(f"{'Health ' : <21} : {self.hp}")
            print(f"{f'{self.energy_name} ' : <21} : {self.max_energy}")
            print(f"{'Damage ' : <21} : {self.attack}")
            if self.form == '0':print("No form available")
            else:print(f"{'Form Name ' : <21} : {self.form['form_name']}")
            print("\n")
        elif stats == 'hp':
            print(f"{f'\nHealth of {self.name}' : <21} : {self.hp}")
            print("\n")


    def transform(self):
        if self.form == '0':
            print(f"{self.name.title()} have no form")
        else:
            if int(self.energy) - int(self.form["energy_consumed"]) > 0:
                print(f"{self.name} transformed into {self.form['form_name']}")
                self.is_transformed = True
                self.hp = int(self.hp) * float(self.form["hp_mul"])
            else:
                print("Energy Below Level !! ")

    def fight(self,target):
        if self.is_transformed :
            attack_multiplier = float(self.form["attack_mul"])
        else:
            attack_multiplier = 1
        damage_given = int(self.attack) * attack_multiplier
        print(f"\n 💥{self.name} attacked {target.name} for {damage_given} damage")
        target.take_damage(damage_given)

    def take_damage(self , amount):
        self.hp = max(0 ,int(self.hp) - amount)
        if int(self.hp)>100:
            print(f"\n 🔻{self.name} left with {self.hp} HP!!")
        elif int(self.hp)>0:
            print(f"\n Critical Blowwwwww")
            print(f"\n 🔻{self.name} left with {self.hp} HP!!")
        elif int(self.hp) == 0:
            print(f"\n 🔻{self.name} KNOCKED OUT!!!!!!!!!!!")

    def end_turn(self):
        pass

class Goku(Character):
    #I made Ultra Instinct dodge attack by 0.5x
    def take_damage(self , amount):
        if self.is_transformed == True:
            self.hp = max(0, (int(self.hp) - amount*0.5) )
            print(f"\n 🔻{self.form["form_name"]} Activated! Attack Suppressed!!")
        else:
            self.hp = max(0, int(self.hp) - amount)

        if int(self.hp)>100:
            print(f"\n 🔻{self.name} left with {self.hp} HP!!")
        elif int(self.hp)>0:
            print(f"\n Critical Blowwwwww")
            print(f"\n 🔻{self.name} left with {self.hp} HP!!")
        elif int(self.hp) == 0:
            print(f"\n 🔻{self.name} KNOCKED OUT!!!!!!!!!!!")


def show_characters():
    with open("heros.json") as h:
        roster_list = json.load(h)
    rosters = pd.DataFrame.from_dict(roster_list, orient="index")
    print(rosters["hero_name"])

hero_registry = {"Goku" : Goku,"Vegeta" : Character,"Naruto":Character ,"Sasuke":Character,"Kakashi":Character,"Luffy":Character,"Zoro":Character,"Ichigo":Character}
def load_player(hero_name)->Character:
    if hero_name in hero_registry:
            with open("heros.json") as h:
                roster_list = json.load(h)
            cls = hero_registry.get(hero_name, Character)
            return cls (roster_list[hero_name])
    else:
        print(f"{hero_name} is not Availbale")





