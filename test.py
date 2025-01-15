import unittest
from unittest.mock import patch

# Import classes from the main game code (assumed to be in 'game.py')
# from game import Monster, Attack, Player, Enemy, Duel

class TestAttack(unittest.TestCase):
    def setUp(self):
        self.attack = Attack("Fireball", 50, 2, 10, None, None, 0, None, 0, 0, 0)

    def test_attack_creation(self):
        self.assertEqual(self.attack.Name, "Fireball")
        self.assertEqual(self.attack.dmg, 50)
        self.assertEqual(self.attack.Mpcost, 10)

class TestMonster(unittest.TestCase):
    def setUp(self):
        self.attack = Attack("Fireball", 50, 2, 10, None, None, 0, None, 0, 0, 0)
        self.monster = Monster("Dragon", 200, 50, 100, 2, None, [self.attack])

    def test_monster_initialization(self):
        self.assertEqual(self.monster.Name, "Dragon")
        self.assertEqual(self.monster.Hp, 200)
        self.assertEqual(self.monster.Mp, 100)
        self.assertEqual(len(self.monster.attacklist), 3)

    def test_monster_take_damage(self):
        self.monster.take_Damage(50)
        self.assertEqual(self.monster.Hp, 150)

    def test_monster_heal(self):
        self.monster.take_Damage(50)
        self.monster.heal(30)
        self.assertEqual(self.monster.Hp, 180)

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.attack = Attack("Fireball", 50, 2, 10, None, None, 0, None, 0, 0, 0)
        self.monsters = [Monster(f"Monster{i}", 100, 30, 50, 2, None, [self.attack]) for i in range(6)]
        self.player = Player(self.monsters)

    def test_player_monster_selection(self):
        self.assertIsNotNone(self.player.Monster1)
        self.assertEqual(len([m for m in [self.player.Monster1, self.player.Monster2, self.player.Monster3, self.player.Monster4, self.player.Monster5, self.player.Monster6] if m is not None]), 6)

class TestDuel(unittest.TestCase):
    def setUp(self):
        self.attack = Attack("Fireball", 50, 2, 10, None, None, 0, None, 0, 0, 0)
        self.monsters = [Monster(f"Monster{i}", 100, 30, 50, 2, None, [self.attack]) for i in range(6)]
        self.player = Player(self.monsters)
        self.enemy = Enemy(self.monsters, ["GoblinKing"])
        self.duel = Duel(self.player, self.enemy)

    def test_duel_initialization(self):
        self.assertIsNotNone(self.duel.player)
        self.assertIsNotNone(self.duel.enemy)

    @patch('builtins.input', return_value='1')
    def test_duel_battle_flow(self, mock_input):
        with patch('builtins.print') as mock_print:
            self.duel.resolve_turn()
            self.assertTrue(mock_print.called)

class TestIntegration(unittest.TestCase):
    def test_player_vs_enemy_integration(self):
        attack = Attack("Fireball", 50, 2, 10, None, None, 0, None, 0, 0, 0)
        monsters = [Monster(f"Monster{i}", 100, 30, 50, 2, None, [attack]) for i in range(6)]
        player = Player(monsters)
        enemy = Enemy(monsters, ["GoblinKing"])
        duel = Duel(player, enemy)

        duel.resolve_turn()
        self.assertTrue(duel.player.status in ["winner", "loser"])

class TestEndToEnd(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '1', '1'])
    def test_full_gameplay(self, mock_input):
        attack = Attack("Fireball", 50, 2, 10, None, None, 0, None, 0, 0, 0)
        monsters = [Monster(f"Monster{i}", 100, 30, 50, 2, None, [attack]) for i in range(6)]
        player = Player(monsters)
        enemy = Enemy(monsters, ["GoblinKing"])
        duel = Duel(player, enemy)
        
        with patch('builtins.print') as mock_print:
            duel.start_battle()
            self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()
