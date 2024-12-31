import json
import random

class Monster:
    def __init__(self, Name, Hp, speed, Mp, Type1, Type2):
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
            if self.Mp - attack.MpCost >= 0:
                self.Lose_Mp(attack.MpCost)
                target.take_Damage(attack.Dmg * self.Atk)
                self.heal(attack.Heal)
                target.Effect = attack.Effect
            else:
                print(f"{self.Name} don't have enough Mp")
        else:
            print(f"{self.Name} is currently dead")


        

class Obj:
    def __init__(self, Name, HpRegen, Effect, MpRegen, Boost, dmg, AtkMultiplier, SpeedMultiplier):
        self.Name = Name
        self.HpRegen = HpRegen
        self.Effect = Effect
        self.MpRegen = MpRegen
        self.Boost = Boost
        self.dmg = dmg
        self.AtkMultiplier = AtkMultiplier
        self.SpeedMultiplier = SpeedMultiplier

    def Heal(self, Monster):
        Monster.heal(self.HpRegen)
        Monster.Mp += self.MpRegen

    def Inflict(self, Target):
        Target.take_Damage(self.dmg)
        Target.Effect = self.Effect

    def BoostMonster(self, Monster):
        Monster.speed *= self.SpeedMultiplier
        Monster.Atk *= self.AtkMultiplier





class Player:
    def __init__(self, MonsterList):
        self.select_random_monsters(MonsterList)

    def select_random_monsters(self, MonsterList):
        selected_monsters = []
        for i in range(6):
            random_index = random.randint(0, len(MonsterList) - 1)
            selected_monsters.append(MonsterList[random_index])
        
        self.Monster1 = selected_monsters[0]
        self.Monster2 = selected_monsters[1]
        self.Monster3 = selected_monsters[2]
        self.Monster4 = selected_monsters[3]
        self.Monster5 = selected_monsters[4]
        self.Monster6 = selected_monsters[5]
        self.CurrentMonster = selected_monsters[0]

class Enemy:
    def __init__(self, MonsterList):
        self.select_random_monsters(MonsterList)
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

class Duel:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.current_player_monster = player.CurrentMonster
        self.current_enemy_monster = enemy.CurrentMonster
        self.winner = None

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
        else:
            attacker, defender = self.current_enemy_monster, self.current_player_monster
            
        print(f"{attacker.Name} is attacking {defender.Name}!")

        # Attaque basique pour l'instant (5 à 15 dégats, pas d'effect, pas de consomation d'energie)
        if attacker.Statut == "Alive" or attacker.Hp >= 0:
            damage = random.randint(5, 15)  
            defender.take_Damage(damage)
            print(f"{defender.Name} takes {damage} damage remaining hp: {defender.Hp}/{defender.MaxHp} HP.")
            if defender.Statut == "Down" or defender.Hp <= 0:
                print(f"{defender.Name} fainted!")
                self.switch_monster(side)
        else:
            print(f"{attacker.Name} is unable to fight! (bot Alive)")

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
        player_alive = self.get_next_alive_monster(self.player) is not None   #Player a t-il des monstres en vie ?
        enemy_alive = self.get_next_alive_monster(self.enemy) is not None     #ennemy a t-il des monstres en vie ?

        if not player_alive:
            self.winner = "enemy"
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
            Type2=value[4]
        )
        monsters_list.append(monster)
    
    return monsters_list


monsters_list = create_monsters_from_json()

player = Player(monsters_list)  
enemy = Enemy(monsters_list)   #on créé joueur et ennemy

# Example
duel = Duel(player, enemy)
duel.start_battle()
