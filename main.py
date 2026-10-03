import json
from ensurepip import __main__
from gc import set_debug
from operator import index
import random
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


    def transform(self):
        if self.form == '0':
            print(f"{self.name.title()} have no form")
        elif self.is_transformed:
            print(" Already Transformed ")
        else:
            if  int(self.energy) >= int(self.form["energy_consumed"]):
                print(f"\n{self.name} transformed into {self.form['form_name']}")
                self.energy = int(self.energy) - int(self.form["energy_consumed"])
                self.is_transformed = True
                self.hp = int(int(self.hp) * float(self.form["hp_mul"]))
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
        if self.is_transformed:
            new_attack = int(amount*0.5)
            print(f"\n 🔻{self.form['form_name']} Activated! Attack Suppressed!!")
            super().take_damage(new_attack)
        else:
            super().take_damage(amount)

class Naruto(Character):
    def fight(self,target):
        Baryon_Rasengan = 0
        if self.is_transformed :
            attack_multiplier = float(self.form["attack_mul"])
            if int(self.energy) >= 250:
                Baryon_Rasengan = input("Do you wanna throw Baryon Rasengan [1 for yes] ? ")
        else:
            attack_multiplier = 1
        if Baryon_Rasengan == '1':
            damage_given = 1350
            self.energy = int(self.energy) - 250
            print(f"\n 💥💥💥{self.name} used BARYON Rasengan ON  {target.name} 💥💥💥")
            target.take_damage(damage_given)
        else:
            super().fight(target)

def show_characters():
    with open("heros.json") as h:
        roster_list = json.load(h)
    rosters = pd.DataFrame.from_dict(roster_list,orient="index" )
    print(rosters.index.tolist())

hero_registry = {"Goku" : Goku,"Vegeta" : Character,"Naruto":Naruto ,"Sasuke":Character,"Kakashi":Character,"Luffy":Character,"Zoro":Character,"Ichigo":Character}
def load_player(hero_name)->Character | None:
    if hero_name in hero_registry:
            with open("heros.json") as h:
                roster_list = json.load(h)
            cls = hero_registry.get(hero_name, Character)
            return cls (roster_list[hero_name])
    else:
        print(f"{hero_name} is not Availbale")
        return None

if __name__ == "__main__":
    print(f" {'WELCOME TO ANIME RUSH \n':>50}")
    what_to_do = int(input("1. Start\n2. Show Rosters\n3. Exit : "))
    if what_to_do == 1:
        player_choice = input("Choose Your Player [P1/P2]: ").upper()
        show_characters()
        char_choice = input(f"Choose a Character : ")
        if player_choice == 'P1':
               p1 = load_player(char_choice)
               p2 = load_player(random.choice(['Goku', 'Naruto', 'Vegeta', 'Sasuke', 'Kakashi', 'Luffy', 'Zoro', 'Ichigo']))
        elif player_choice == 'P2':
               p2 = load_player(char_choice)
               p1 = load_player(random.choice(['Goku', 'Naruto', 'Vegeta', 'Sasuke', 'Kakashi', 'Luffy', 'Zoro', 'Ichigo']))
        else:
            print("Wrong Selection")

        print("Player One : ",p1.name)
        print("Player Two : ",p2.name)



    elif what_to_do == 2:
        print("\nAvailable Rosters : ")
        show_characters()
    elif what_to_do == 3:
        print("Come Back Again !!! ")