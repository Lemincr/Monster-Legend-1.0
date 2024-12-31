import json
import random

class Monster:
    def __init__(self, Name, Hp, speed, Mp, Type1, Type2, attacklist):
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
        self.Effect = None
        self.Atk = 1
        self.select_random_attacks(attacklist)
    
    def select_random_attacks(self, attacklist):
        selected_attacks = []
        for i in range(4):
            random_index = random.randint(0, len(attacklist)- 1)
            selected_attacks.append(attacklist[random_index])
        
        self.Attack1 = selected_attacks[0]
        self.Attack2 = selected_attacks[1]
        self.Attack3 = selected_attacks[2]
        self.Attack4 = selected_attacks[3]
        self.attacklist = [self.Attack1,self.Attack2,self.Attack3,self.Attack4]

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
                multiplier = 1
                if attack.element != None:
                    if target.Type1 - attack.element == -1 or target.Type1 == attack.element:
                        multiplier = 0.5
                        print("ce n'est pas très efficace")
                    elif target.Type1 - attack.element == 1:
                        multiplier = 2
                        print("c'est très efficace")
                elif target.Type1 == 1 and attack.element == 9:
                    multiplier = 2
                    print("c'est très efficace")
                elif target.Type1 == 9 and attack.element == 1:
                    multiplier = 0.5
                    print("ce n'est pas très efficace")
                target.take_Damage(attack.dmg * self.Atk * multiplier)
                self.heal(attack.heal)
                target.Effect = attack.effect1
                self.Effect = attack.selfeffect
                self.take_Damage(attack.selfdmg)
                self.healMp(attack.mpregen)
                target.Lose_Mp(attack.mpremove)
                self.attacked = True
            else:
                print(f"{self.Name} don't have enough Mp")
                self.attacked = False
        else:
            print(f"{self.Name} is currently dead")
            self.Statut == "Dead"


        

class Attack:
    def __init__(self, Name, dmg, element, Mpcost, effect1, effect2, heal, selfeffect, selfdmg, mpregen, mpremove):
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
        
        self.Monster1 = selected_monsters[0]
        self.Monster2 = selected_monsters[1]
        self.Monster3 = selected_monsters[2]
        self.Monster4 = selected_monsters[3]
        self.Monster5 = selected_monsters[4]
        self.Monster6 = selected_monsters[5]
        self.CurrentMonster = selected_monsters[0]

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
        random_index = random_index = random.randint(0, len(NameList))
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
        for i in range(1, 7): 
            monster_player = getattr(player, f"Monster{i}")
            print(monster_player.Name)
        print("The battle begins!")
        

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
            print(f"{attacker.Name}, remaining MP: {attacker.Mp}")
            attack_str = f"{attacker.Attack1.Name}"
            if attacker.Attack1.dmg != 0:
                attack_str += f", dmg: {attacker.Attack1.dmg}"
            if attacker.Attack1.element != 0:  # Assuming element is not an integer. Use another condition if it's not 0 in some other way.
                attack_str += f", element: {attacker.Attack1.element}"
            if attacker.Attack1.Mpcost != 0:
                attack_str += f", Mpcost: {attacker.Attack1.Mpcost}"
            if attacker.Attack1.effect1 != 0:
              attack_str += f", effect1: {attacker.Attack1.effect1}"
            if attacker.Attack1.heal != 0:
               attack_str += f", heal: {attacker.Attack1.heal}"
            if attacker.Attack1.selfeffect != 0:
               attack_str += f", selfeffect: {attacker.Attack1.selfeffect}"
            if attacker.Attack1.selfdmg != 0:
               attack_str += f", selfdmg: {attacker.Attack1.selfdmg}"
            if attacker.Attack1.mpregen != 0:
                attack_str += f", mpregen: {attacker.Attack1.mpregen}"
            if attacker.Attack1.mpremove != 0:
             attack_str += f", mpremove: {attacker.Attack1.mpremove}"
            print(attack_str)
            attack_str = f"{attacker.Attack2.Name}"
            if attacker.Attack2.dmg != 0:
                attack_str += f", dmg: {attacker.Attack2.dmg}"
            if attacker.Attack2.element != 0:  # Assuming element is not an integer. Use another condition if it's not 0 in some other way.
                attack_str += f", element: {attacker.Attack2.element}"
            if attacker.Attack2.Mpcost != 0:
                attack_str += f", Mpcost: {attacker.Attack2.Mpcost}"
            if attacker.Attack2.effect1 != 0:
              attack_str += f", effect1: {attacker.Attack2.effect1}"
            if attacker.Attack2.heal != 0:
               attack_str += f", heal: {attacker.Attack2.heal}"
            if attacker.Attack2.selfeffect != 0:
               attack_str += f", selfeffect: {attacker.Attack2.selfeffect}"
            if attacker.Attack2.selfdmg != 0:
               attack_str += f", selfdmg: {attacker.Attack2.selfdmg}"
            if attacker.Attack2.mpregen != 0:
                attack_str += f", mpregen: {attacker.Attack2.mpregen}"
            if attacker.Attack2.mpremove != 0:
             attack_str += f", mpremove: {attacker.Attack2.mpremove}"
            print(attack_str)
            attack_str = f"{attacker.Attack3.Name}"
            if attacker.Attack3.dmg != 0:
                attack_str += f", dmg: {attacker.Attack3.dmg}"
            if attacker.Attack3.element != 0:  # Assuming element is not an integer. Use another condition if it's not 0 in some other way.
                attack_str += f", element: {attacker.Attack3.element}"
            if attacker.Attack3.Mpcost != 0:
                attack_str += f", Mpcost: {attacker.Attack3.Mpcost}"
            if attacker.Attack3.effect1 != 0:
              attack_str += f", effect1: {attacker.Attack3.effect1}"
            if attacker.Attack3.heal != 0:
               attack_str += f", heal: {attacker.Attack3.heal}"
            if attacker.Attack3.selfeffect != 0:
               attack_str += f", selfeffect: {attacker.Attack3.selfeffect}"
            if attacker.Attack3.selfdmg != 0:
               attack_str += f", selfdmg: {attacker.Attack3.selfdmg}"
            if attacker.Attack3.mpregen != 0:
                attack_str += f", mpregen: {attacker.Attack3.mpregen}"
            if attacker.Attack3.mpremove != 0:
             attack_str += f", mpremove: {attacker.Attack3.mpremove}"
            print(attack_str)
            attack_str = f"{attacker.Attack4.Name}"
            if attacker.Attack4.dmg != 0:
                attack_str += f", dmg: {attacker.Attack4.dmg}"
            if attacker.Attack4.element != 0:  # Assuming element is not an integer. Use another condition if it's not 0 in some other way.
                attack_str += f", element: {attacker.Attack4.element}"
            if attacker.Attack4.Mpcost != 0:
                attack_str += f", Mpcost: {attacker.Attack4.Mpcost}"
            if attacker.Attack4.effect1 != 0:
              attack_str += f", effect1: {attacker.Attack4.effect1}"
            if attacker.Attack4.heal != 0:
               attack_str += f", heal: {attacker.Attack4.heal}"
            if attacker.Attack4.selfeffect != 0:
               attack_str += f", selfeffect: {attacker.Attack4.selfeffect}"
            if attacker.Attack4.selfdmg != 0:
               attack_str += f", selfdmg: {attacker.Attack4.selfdmg}"
            if attacker.Attack4.mpregen != 0:
                attack_str += f", mpregen: {attacker.Attack4.mpregen}"
            if attacker.Attack4.mpremove != 0:
             attack_str += f", mpremove: {attacker.Attack4.mpremove}"
            print(attack_str)
            print("c'est à vous d'attaquer, choisissez une attaque (1-4)")
            selected_attack = input()
            if selected_attack == "quit" or selected_attack == "exit":
                self.player.status = "loser"
            if selected_attack.isdecimal():
                selected_attack = int(selected_attack)
                selected_attack -= 1
                if 0 <= selected_attack <= 3 :
                    selected_attack = attacker.attacklist[selected_attack]
                else:
                    print("chiffre entré non compris entre 1 et 4, attaque par défaul lancée")
                    selected_attack = attacker.attacklist[0]
            else:
                print("veuiller entrer un chiffre entre 1 et 4, attaque par défaul lancée")
                selected_attack = attacker.attacklist[0]


        else:
            attacker, defender = self.current_enemy_monster, self.current_player_monster
            selected_attack = attacker.attacklist[random.randint(0, 3)]
        print(f"{attacker.Name} is attacking {defender.Name} with {selected_attack.Name}!")

        # Attaque
        if selected_attack:
            attacker.attack(defender, selected_attack)
        if defender.Hp <= 0:
            defender.Hp = 0
        print(f"{defender.Name} takes {selected_attack.dmg} damage remaining hp: {defender.Hp}/{defender.MaxHp} HP.")
        if defender.Statut == "Down" or defender.Hp <= 0:
            print(f"{defender.Name} fainted!")
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
        print(f"The battle is over! The winner is {self.winner}!")
        #for i in range(1, 7): # monstre de 1 à 6
        #    monster = getattr(participant, f"Monster{i}") #recupère les arguments(vie, Mp, ...) des Monstres du participant
        #    monster.full_heal()



def load_Monster_Data(filename="Monster_Liste.Json"):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def load_Name_Data(filename="Ennemies_Names.Json"):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def load_Attacks_Data(filename="Attaks_List.Json"):
    with open(filename, "r") as file:
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