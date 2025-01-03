import json
import random
import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset= True)
class Monster:
    def __init__(self, Name: str, Hp: int, speed: int, Mp: int, Type1: int, Type2: int, attacklist: list):
        self.Name = Name
        self.MaxHp = Hp
        self.NormalSpeed = speed
        self.speed = speed
        self.MaxMp = Mp
        self.Mp = Mp
        self.Type1 = Type1
        self.Type2 = Type2
        self.level = 1
        self.Hp = Hp
        self.Statut = "Alive"
        self.Effect: int|None = None
        self.Atk: int = 1
        self.select_random_attacks(attacklist)
        self.attacking: bool = True
        self.multiplier = 1
    def select_random_attacks(self, attacklist):
        selected_attacks = []
        for i in range(3):
            random_index = random.randint(0, len(attacklist)- 1)
            selected_attacks.append(attacklist[random_index])
        
        self.Attack1: Attack = selected_attacks[0]
        self.Attack2: Attack = selected_attacks[1]
        self.Attack3: Attack = selected_attacks[2]
        

        if self.Name == "Exodia_The_Forbidden_One":
            self.Attack1: Attack = Attack("Obliterate", 300, 6, 20, "None", "None", 0, "None", 0, 0, 0)
            self.Attack2: Attack = Attack("Seal_of_Exodia", 0, 4, 15, "sleeping", "poison", 0, "None", 0, 50, 0)
            self.Attack3: Attack = Attack("Exodia's_Retribution", 100, 6, 10, "None", "saignement", 35, "Heal", 0, 0, 0)

        self.attacklist = [self.Attack1,self.Attack2,self.Attack3]

    def Is_Dead(self):
        if self.Hp <= 0:
            self.Statut = "Down"

        
    def take_Damage(self, dmg):
        self.Hp -= dmg
        self.Is_Dead()
        
    def Lose_Mp(self, Mplost):
        self.Mp -= Mplost
        if self.Mp <= 0:
            self.Mp = 0
    
    def heal(self, value):
        self.Hp += value
        if self.Hp > self.MaxHp:
            self.Hp = self.MaxHp
    
    def healMp(self, value):
        self.Mp += value
        if self.Mp > self.MaxMp:
            self.Mp = self.MaxMp
            
    def full_Heal(self):
        self.Hp = self.MaxHp
        self.Mp = self.MaxMp
    
    def attack(self, target, attack):
        if self.Effect == "Sleeping":
            self.Effect == "None"
            print(f"{self.Name} Was Sleeping and just woke up")

        elif self.Statut == "Alive":
            if self.Mp - attack.Mpcost >= 0:
                self.Lose_Mp(attack.Mpcost)
                self.multiplier = 1
                if attack.element != None:
                    if target.Type1 - attack.element == -1 or target.Type1 == attack.element:
                        self.multiplier = 0.5
                        print("ce n'est pas très efficace")
                    elif target.Type1 - attack.element == 1:
                        self.multiplier = 2
                        print(Fore.RED +"c'est très efficace")
                elif target.Type1 == 1 and attack.element == 9:
                    self.multiplier = 2
                    print(Fore.RED + "c'est très efficace")
                elif target.Type1 == 9 and attack.element == 1:
                    self.multiplier = 0.5
                    print(Fore.CYAN + "ce n'est pas très efficace")
                target.take_Damage(attack.dmg * self.Atk * self.multiplier)
                self.heal(attack.heal)
                target.Effect = attack.effect1
                self.Effect = attack.selfeffect
                self.take_Damage(attack.selfdmg)
                self.Mp += attack.mpregen
                target.Lose_Mp(attack.mpremove)
                self.attacking = True
            else:
                print(f"{self.Name} don't have enough Mp")
                self.attacking = False
        else:
            print(f"{self.Name} is currently dead")
            self.Statut == "Dead"


        

class Attack:
    def __init__(self, Name: str, dmg: int, element: int, Mpcost: int, effect1: int, effect2: int, heal: int, selfeffect: str, selfdmg: int, mpregen: int, mpremove: int):
        self.Name = Name
        self.dmg = dmg
        self.element = element
        self.Mpcost = Mpcost
        self.effect1 = effect1
        self.effect2 = effect2
        self.heal = heal
        self.selfeffect = selfeffect
        self.selfdmg = selfdmg
        self.mpregen = mpregen
        self.mpremove = mpremove





class Player:
    def __init__(self, MonsterList):
        self.select_random_monsters(MonsterList)
        self.status = "winner"

    def select_random_monsters(self, MonsterList):
        selected_monsters = []
        for i in range(6):
            random_index = random.randint(0, len(MonsterList)-1)
            selected_monsters.append(MonsterList[random_index])
        
        self.Monster1 = MonsterList[-1]
        self.Monster2 = selected_monsters[1]
        self.Monster3 = selected_monsters[2]
        self.Monster4 = selected_monsters[3]
        self.Monster5 = selected_monsters[4]
        self.Monster6 = selected_monsters[5]
        self.CurrentMonster = MonsterList[-1]

class Enemy:
    def __init__(self, MonsterList, NameList):
        self.select_random_monsters(MonsterList)
        self.select_random_name(NameList)
    def select_random_monsters(self, MonsterList):
        selected_monsters = []
        for i in range(random.randint(2, 4)):
            random_index = random.randint(0, len(MonsterList) - 1)
            selected_monsters.append(MonsterList[random_index])
        for j in range(6 - len(selected_monsters)):
            selected_monsters.append(None)
        
        self.Monster1 = selected_monsters[0]
        self.Monster2 = selected_monsters[1]
        self.Monster3 = selected_monsters[2]
        self.Monster4 = selected_monsters[3]
        self.Monster5 = selected_monsters[4]
        self.Monster6 = selected_monsters[5]
        self.CurrentMonster = selected_monsters[0]

    def select_random_name(self, NameList):
        random_index = random_index = random.randint(0, len(NameList) - 1)
        self.name = NameList[random_index]

class Duel:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.current_player_monster = player.CurrentMonster
        self.current_enemy_monster = enemy.CurrentMonster
        self.winner = None
        self.types = {
            1: "eau",
            2: "feu",
            3: "nature",
            4: "magie",
            5: "metal",
            6: "lumière",
            7: "ténèbre",
            8: "terre",
            9: "foudre"
}
    def start_battle(self):
        print("here are your champions: \n")
        for i in range(1, 7): 
            monster_player = getattr(player, f"Monster{i}")
            print(f"{i}. {monster_player.Name}, {self.types[monster_player.Type1]}, Hp: {monster_player.Hp} \n")
        print(Fore.RED + "The battle begins! \n")
        

        while not self.check_game_over():
            self.resolve_turn()
        self.declare_winner()

    def resolve_turn(self):
        # Determine quel côté attaque en prmier
        if self.current_player_monster.speed >= self.current_enemy_monster.speed:
            first, second = "player", "enemy"
        else:
            first, second = "enemy", "player"

        # Execute turns
        self.execute_turn(first)
        if not self.check_game_over():  # On vérifie si la partie s'est finie après le premiers tour
            self.execute_turn(second)

    def execute_turn(self, side):
        if side == "player": #définie qui attaque qui défend
            attacker, defender = self.current_player_monster, self.current_enemy_monster

            print(f"ENNEMY {defender.Name}, {self.types[defender.Type1]}, Hp: {defender.Hp}")
            print(f"{attacker.Name}, remaining MP: {attacker.Mp} \n")
            attack_str = f"{attacker.Attack1.Name}"
            if attacker.Attack1.dmg != 0:
                attack_str += f", dmg: {attacker.Attack1.dmg}"
            if attacker.Attack1.element != 0:
                attack_str += f", element: {self.types[attacker.Attack1.element]}"
            if attacker.Attack1.Mpcost != 0:
                attack_str += f", Mpcost: {attacker.Attack1.Mpcost}"
            if attacker.Attack1.effect1 != None:
              attack_str += f", effect1: {attacker.Attack1.effect1}"
            if attacker.Attack1.heal != 0:
               attack_str += f", heal: {attacker.Attack1.heal}"
            if attacker.Attack1.selfeffect != None:
               attack_str += f", selfeffect: {attacker.Attack1.selfeffect}"
            if attacker.Attack1.selfdmg != 0:
               attack_str += f", selfdmg: {attacker.Attack1.selfdmg}"
            if attacker.Attack1.mpregen != 0:
                attack_str += f", mpregen: {attacker.Attack1.mpregen}"
            if attacker.Attack1.mpremove != 0:
             attack_str += f", mpremove: {attacker.Attack1.mpremove}"
            print(Fore.GREEN + attack_str + "\n")
            attack_str = f"{attacker.Attack2.Name}"
            if attacker.Attack2.dmg != 0:
                attack_str += f", dmg: {attacker.Attack2.dmg}"
            if attacker.Attack2.element != 0:
                attack_str += f", element: {self.types[attacker.Attack2.element]}"
            if attacker.Attack2.Mpcost != 0:
                attack_str += f", Mpcost: {attacker.Attack2.Mpcost}"
            if attacker.Attack2.effect1 != None:
              attack_str += f", effect1: {attacker.Attack2.effect1}"
            if attacker.Attack2.heal != 0:
               attack_str += f", heal: {attacker.Attack2.heal}"
            if attacker.Attack2.selfeffect != None:
               attack_str += f", selfeffect: {attacker.Attack2.selfeffect}"
            if attacker.Attack2.selfdmg != 0:
               attack_str += f", selfdmg: {attacker.Attack2.selfdmg}"
            if attacker.Attack2.mpregen != 0:
                attack_str += f", mpregen: {attacker.Attack2.mpregen}"
            if attacker.Attack2.mpremove != 0:
             attack_str += f", mpremove: {attacker.Attack2.mpremove}"
            print(Fore.GREEN + attack_str + "\n")
            attack_str = f"{attacker.Attack3.Name}"
            if attacker.Attack3.dmg != 0:
                attack_str += f", dmg: {attacker.Attack3.dmg}"
            if attacker.Attack3.element != 0:
                attack_str += f", element: {self.types[attacker.Attack3.element]}"
            if attacker.Attack3.Mpcost != 0:
                attack_str += f", Mpcost: {attacker.Attack3.Mpcost}"
            if attacker.Attack3.effect1 != None:
              attack_str += f", effect1: {attacker.Attack3.effect1}"
            if attacker.Attack3.heal != 0:
               attack_str += f", heal: {attacker.Attack3.heal}"
            if attacker.Attack3.selfeffect != None:
               attack_str += f", selfeffect: {attacker.Attack3.selfeffect}"
            if attacker.Attack3.selfdmg != 0:
               attack_str += f", selfdmg: {attacker.Attack3.selfdmg}"
            if attacker.Attack3.mpregen != 0:
                attack_str += f", mpregen: {attacker.Attack3.mpregen}"
            if attacker.Attack3.mpremove != 0:
             attack_str += f", mpremove: {attacker.Attack3.mpremove}"
            print(Fore.GREEN + attack_str+ "\n"*2)
            print(Fore.BLUE + "c'est à vous d'attaquer, choisissez une attaque (1-3)")
            selected_attack = input()
            if selected_attack == "quit" or selected_attack == "exit":
                self.player.status = "loser"
            if selected_attack.isdecimal():
                selected_attack = int(selected_attack)
                selected_attack -= 1
                if 0 <= selected_attack <= 2 :
                    selected_attack = attacker.attacklist[selected_attack]
                else:
                    print("chiffre entré non compris entre 1 et 3, attaque par défaul lancée")
                    selected_attack = attacker.attacklist[0]
            else:
                print("veuiller entrer un chiffre entre 1 et 3, attaque par défaul lancée")
                selected_attack = attacker.attacklist[0]


        else:
            attacker, defender = self.current_enemy_monster, self.current_player_monster
            selected_attack = attacker.attacklist[random.randint(0, 2)]

        # Attaque
        if selected_attack:
            if attacker.attacking == True:
                print(f"{attacker.Name} is attacking {defender.Name} with {selected_attack.Name}!")
                attacker.attack(defender, selected_attack)
            else:
                print(f"{attacker.Name} is attacking {defender.Name} with Struggle (10dmg, no mana needed!)")
                selected_attack = Attack("struggle", 10, None, 0, None, None, None, None, None, None, None)
            if defender.Hp <= 0:
                defender.Hp = 0
            print(f"{defender.Name} takes {selected_attack.dmg * attacker.multiplier * attacker.Atk} damage remaining hp: {defender.Hp}/{defender.MaxHp} HP.")
            if defender.Statut == "Down" or defender.Hp <= 0:
                print(Fore.RED + f"{defender.Name} fainted!")
                self.switch_monster(side)
            if attacker.Statut == "Down" or attacker.Hp <= 0:
                print(f"{attacker.Name} fainted! due to his attack")
                if side == "player":
                    self.switch_monster("ennemy")
                else:
                    self.switch_monster("player")

        

    def switch_monster(self, side):
        if side == "player":
            new_monster = self.get_next_alive_monster(self.enemy)
            self.current_enemy_monster = new_monster
        else:
            new_monster = self.get_next_alive_monster(self.player)
            self.current_player_monster = new_monster

        if new_monster:
            print(f"A new monster joins the battle: {new_monster.Name}!")
        else:
            if side == "player":
                print(f"No more monsters available for enemy!")
            else:
                 print(f"No more monsters available for player!")

    def get_next_alive_monster(self, participant):
        for i in range(1, 7): # monstre de 1 à 6
            monster = getattr(participant, f"Monster{i}") #recupère les arguments(vie, Mp, ...) des Monstres du participant
            if monster and monster.Statut == "Alive":
                return monster  #revois le prochain monstre vivant 
        return None

    def check_game_over(self):
        if self.player.status != "winner":
            return 1
        player_alive = self.get_next_alive_monster(self.player) is not None   #Player a t-il des monstres en vie ?
        enemy_alive = self.get_next_alive_monster(self.enemy) is not None     #ennemy a t-il des monstres en vie ?

        if not player_alive:
            self.winner = "enemy"
            player.status = "dead"
            return True                 #détermine le gagnant et met fin au duel 
        elif not enemy_alive:
            self.winner = "player"
            return True
        return False
        

    def declare_winner(self):
        print(f"The battle is over! The winner is {self.winner}! \n \n \n")
        for i in range(1, 7): # monstre de 1 à 6
            monster = getattr(self.player, f"Monster{i}") #recupère les arguments(vie, Mp, ...) des Monstres du participant
            monster.full_Heal()



def load_Monster_Data(filename="Monster_Liste.Json"):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def load_Name_Data(filename="Ennemies_Names.Json"):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def load_Attacks_Data(filename="Attaks_List.Json"):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_attacks_from_json():
    attacks_data = load_Attacks_Data()
    attack_list = []
    
    for key, value in attacks_data.items():
        attack = Attack(
            Name = value[0],
            dmg = value[1],
            element = value[2],
            Mpcost = value[3],
            effect1 = value[4],
            effect2 = value[5],
            heal = value[6],
            selfeffect = value[7],
            selfdmg = value[8],
            mpregen = value[9],
            mpremove = value[10],
        )
        attack_list.append(attack)
    
    return attack_list

def create_monsters_from_json():
    Monsters_data = load_Monster_Data()
    monsters_list = []
    
    for key, value in Monsters_data.items():
        monster = Monster(
            Name=value[0],
            Hp=value[1],
            speed=value[2],
            Mp=value[5],
            Type1=value[3],
            Type2=value[4],
            attacklist = create_attacks_from_json()
        )
        monsters_list.append(monster)
    
    return monsters_list
  
Name_List = load_Name_Data()
monsters_list = create_monsters_from_json()


# Example

player = Player(monsters_list) 
while player.status == "winner":
    enemy = Enemy(monsters_list, Name_List)   #on créé joueur et ennemy
    duel = Duel(player, enemy)
    duel.start_battle()