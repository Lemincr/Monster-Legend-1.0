# Spécifications Techniques du Jeu de Combat de Monstres

## Introduction
Ce document décrit les classes principales, leurs attributs et leurs méthodes pour le jeu de combat de monstres. Il inclut également les règles du système de combat.

---

## Règles du Système de Combat

1. **Participants :** Un joueur et un ennemi s'affrontent avec des équipes de monstres.
2. **Monstres :** Chaque camp dispose de 1 à 6 monstres.
3. **Tours de jeu :** Le monstre le plus rapide attaque en premier.
4. **Types d'attaque :** Les attaques ont des éléments qui peuvent être plus ou moins efficaces selon le type du monstre adverse.
5. **Conditions de victoire :** Un camp gagne lorsque tous les monstres adverses sont vaincus.
6. **Effets spéciaux :** Certaines attaques infligent des effets comme le sommeil, le poison, etc.

---

## Classes et Spécifications

### 1. **Classe `Monster`**
Représente un monstre dans le jeu.

**Attributs :**
- `Name` *(str)* : Nom du monstre.
- `Hp` *(int)* : Points de vie actuels.
- `MaxHp` *(int)* : Points de vie maximum.
- `speed` *(int)* : Vitesse actuelle.
- `NormalSpeed` *(int)* : Vitesse de base.
- `Mp` *(int)* : Points de magie actuels.
- `MaxMp` *(int)* : Points de magie maximum.
- `Type1` *(int)* : Premier type élémentaire.
- `Type2` *(int)* : Second type élémentaire.
- `level` *(int)* : Niveau du monstre.
- `Statut` *(str)* : État du monstre ("Alive" ou "Down").
- `Effect` *(int | None)* : Effet de statut actif.
- `Atk` *(int)* : Multiplicateur d'attaque.
- `attacklist` *(list)* : Liste des attaques disponibles.
- `attacking` *(bool)* : Indique si le monstre peut attaquer.
- `multiplier` *(float)* : Multiplicateur de dégâts selon l'efficacité.

**Méthodes :**
- `select_random_attacks(attacklist)` : Sélectionne 3 attaques aléatoires.
- `Is_Dead()` : Met à jour le statut du monstre.
- `take_Damage(dmg)` : Inflige des dégâts au monstre.
- `Lose_Mp(Mplost)` : Réduit les points de magie.
- `heal(value)` : Restaure des points de vie.
- `healMp(value)` : Restaure des points de magie.
- `full_Heal()` : Régénère PV et PM.
- `attack(target, attack)` : Exécute une attaque sur un adversaire.

### 2. **Classe `Attack`**
Représente une attaque utilisée par les monstres.

**Attributs :**
- `Name` *(str)* : Nom de l'attaque.
- `dmg` *(int)* : Dégâts infligés.
- `element` *(int)* : Type élémentaire de l'attaque.
- `Mpcost` *(int)* : Coût en magie.
- `effect1` *(str | None)* : Effet infligé à l'adversaire.
- `effect2` *(str | None)* : Second effet.
- `heal` *(int)* : Points de vie récupérés.
- `selfeffect` *(str)* : Effet appliqué à soi-même.
- `selfdmg` *(int)* : Dégâts auto-infligés.
- `mpregen` *(int)* : Points de magie régénérés.
- `mpremove` *(int)* : Points de magie retirés à l'adversaire.

### 3. **Classe `Player`**
Représente le joueur.

**Attributs :**
- `Monster1` à `Monster6` *(Monster | None)* : Monstres du joueur.
- `CurrentMonster` *(Monster)* : Monstre actif.
- `status` *(str)* : "winner" ou "loser".

**Méthodes :**
- `select_random_monsters(MonsterList)` : Sélectionne 6 monstres aléatoires.

### 4. **Classe `Enemy`**
Représente l'adversaire contrôlé par l'IA.

**Attributs :**
- Mêmes que pour le joueur.
- `name` *(str)* : Nom de l'ennemi.

**Méthodes :**
- `select_random_monsters(MonsterList)` : Sélectionne les monstres.
- `select_random_name(NameList)` : Génère un nom.

### 5. **Classe `Duel`**
Gère le combat.

**Attributs :**
- `player` *(Player)* : Joueur.
- `enemy` *(Enemy)* : Ennemi.
- `current_player_monster` *(Monster)* : Monstre actif du joueur.
- `current_enemy_monster` *(Monster)* : Monstre actif de l'ennemi.
- `winner` *(str | None)* : Gagnant du combat.

**Méthodes :**
- `start_battle()` : Lance le combat.
- `resolve_turn()` : Déroulement d'un tour.
- `execute_turn(side)` : Exécution de l'attaque.
- `switch_monster(side)` : Change de monstre.
- `get_next_alive_monster(participant)` : Vérifie les monstres vivants.
- `check_game_over()` : Détecte la fin du jeu.
- `declare_winner()` : Annonce le gagnant.

---

## Données JSON Utilisées
- **`Monster_Liste.Json`** : Détails des monstres.
- **`Attaks_List.Json`** : Détails des attaques.
- **`Ennemies_Names.Json`** : Noms d'ennemis.

---

## Conclusion
Ce document décrit en détail les composantes du jeu de combat de monstres, incluant la structure des classes, leurs attributs et leurs méthodes.


