import os

class Forms:
    def __init__(self,name, character, ki_required , hp_increase , attack_increase):
        self.name = name
        self.character = character
        self.hp_increase = hp_increase
        self.attack_increase = attack_increase
        self.ki_required = ki_required

    def Form_info(self):
        print("Name : " , self.name)
        print("Bound To : " , self.character)
        print("Requirement in Ki : " , self.ki_required)
        print("Increase in Health " , self.hp_increase)
        print("Increase in Attack Power : " , self.attack_increase)
        

class Character(Forms):
    def __init__(self,name , category , max_hp , max_ki , current_attack):
        self.name = name
        self.category = category
        self.max_hp = max_hp
        self.max_ki = max_ki
        self.current_attack = current_attack
        self.hp = max_hp
        self.ki = 1500

    def show_info(self):
        print("Name : " , self.name)
        print("Category : " , self.category)
        print("Maximum Health : " , self.max_hp)
        print("Maximum Ki Energy : " , self.max_ki)
        print("Maximum Attack Power : " , self.current_attack)


Goku = Character("Goku" , "PowerHouse" , 3500 , 10000 , 450)
Vegeta = Character("Vegeta" , "PowerHouse" , 3800 , 10000 , 440)

Goku.show_info()
Vegeta.show_info()
        
    



