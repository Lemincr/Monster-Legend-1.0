import unittest
from unittest.mock import patch
from Project2_Main import Attack, Monster, Player, Enemy, Duel
import random

# Assuming the classes Monster, Attack, Player, Enemy, and Duel are imported from the main code

class TestMonsterBattle(unittest.TestCase):
    def setUp(self):
        self.attack = Attack("Fireball", 50, 2, 10, None, None, 0, None, 0, 0, 0)
        self.monster1 = Monster("Dragon", 100, 20, 50, 2, 3, [self.attack])
        self.monster2 = Monster("Phoenix", 80, 25, 40, 2, 4, [self.attack])
        self.player = Player([self.monster1, self.monster2])
        self.enemy = Enemy([self.monster1, self.monster2], ["Goblin King", "Dark Sorcerer"])
        self.duel = Duel(self.player, self.enemy)

    def test_monster_initialization(self):
        self.assertEqual(self.monster1.Name, "Dragon")
        self.assertEqual(self.monster1.Hp, 100)
        self.assertEqual(self.monster1.Mp, 50)
        self.assertEqual(len(self.monster1.attacklist), 3)

    def test_attack_execution(self):
        initial_hp = self.monster2.Hp
        self.monster1.attack(self.monster2, self.attack)
        self.assertLess(self.monster2.Hp, initial_hp)

    def test_player_monster_selection(self):
        self.assertTrue(self.player.Monster1 in [self.monster1, self.monster2])

    def test_enemy_name_selection(self):
        self.assertIn(self.enemy.name, ["Goblin King", "Dark Sorcerer"])

    @patch('builtins.input', side_effect=['1'])
    def test_duel_turn_resolution(self, mock_input):
        self.duel.resolve_turn()
        self.assertTrue(self.duel.current_enemy_monster.Hp <= self.enemy.CurrentMonster.MaxHp)

if __name__ == '__main__':
    unittest.main()