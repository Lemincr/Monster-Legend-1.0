# MONSTER LEGEND 1.0

## Description

**MONSTER LEGEND 1.0** est un jeu de rôle au tour par tour inspiré des jeux Pokémon® en 2D. Les joueurs dirigent une équipe de monstres pour combattre des équipes ennemies générées aléatoirement. L'objectif est de vaincre tous les monstres ennemis en utilisant des attaques stratégiques et une bonne gestion de ses monstres.

## Fonctionnalités

- **Combat au Tour par Tour :** Les monstres attaquent en fonction de leur vitesse.
- **Classes de Monstres :** Chaque monstre possède des attributs uniques comme les PV, PM, Vitesse et Types.
- **Équipes Aléatoires :** Les joueurs et ennemis reçoivent des monstres aléatoires au début de chaque partie.
- **Combat Dynamique :** Comprend la régénération de santé, les effets de statut et le changement de monstre après un K.O.

## Installation

1. **Télécharger Le .rar :**
   ```bash
   https://github.com/Lemincr/Monster-Legend-1.0/tree/main
   ```
   //installer la version recommander, la version couleur risque de ratêr l'affichage
2. **Extraire le .rar :**
   ```bash
   vous pouvez créé un fichier et y mettrent le .exe et les 3 JSON
   ```
3. **Installer Python (si nécessaire) :**
   Télécharger Python sur [python.org](https://www.python.org/) et l'installer.  //c'est une blague si jamais
   
3. **Executer Le .exe:**
   Voir Lancement basique

## Prérequis

- Python 3.8 ou version supérieure

## Exécution du Programme

### 1. **Lancement Basique :**
Lancer le script principal pour démarrer le jeu.
```bash
Project2_Main.exe
```

### 2. **Fichiers d'Entrée :**
- `Monster_Liste.json` : Contient les données des monstres sous ce format :
  ```json
  {
    "1": ["Dragonian_Beast", 200, 8, "plante", "terre", 10],
    "2": ["Lacroc", 90, 18, "terre", "plante", 20]
  }
  ```
  - `Attack_Liste.json` : Contient les données des Attaques sous ce format :
  ```json
  {
    "1": ["roulade", 30, 8, 2, null, null, 0, null, 0, 0, 0],
    "2": ["plante relaxante", 0, null, 6, null, null, 50, null, 0, 0, 0]
  }
  ```
  - `Ennemy_Name.Json` : Contient les nom des dresseurs ennemies sous ce format :
  ```json
  [
    "Ash Ketchum",
    "Misty"
  ]
  ```
- **Attributs Monstres:**
  - `Nom` : Nom du monstre
  - `Pv` : Points de Vie
  - `Vitesse` : Statistique de vitesse
  - `Type1` : Type élémentaire principal
  - `Type2` : Type élémentaire secondaire
  - `Pm` : Points de Magie
- **Attributs Attaque:**
  - `Nom` : Nom de l'attaque
  - `dmg` : Dégats
  - `Mpcost` : Coût en Mana
  - `Element` : Type élémentaire principal
  - `Type2` : Type élémentaire secondaire
  - `Pm` : Points de Magie

### 3. **Sortie du Programme :**
- Le jeu s'affiche dans la console avec :
  - Les statistiques des monstres
  - Les séquences d'attaque au tour par tour
  - Les PV et PM restants
  - Des notifications lorsque les monstres tombent K.O. ou changent
  - L'annonce du gagnant à la fin du combat

## Structure des Fichiers

```
RPG-Combat-Monstres/
├── main.py             # Script principal pour lancer le jeu
├── Monster.py          # Classe Monster et son comportement
├── Player.py           # Classe Player pour la gestion des monstres
├── Duel.py             # Mécanique de duel et déroulement des combats
├── Monster_Liste.json  # Données JSON pour tous les monstres
└── README.md           # Documentation du projet
```

## Déroulement du Jeu

1. **Chargement des Monstres :** Le programme charge les données depuis `Monster_Liste.json`.
2. **Sélection des Équipes :** Attribution aléatoire de 6 monstres pour le joueur et 2-4 monstres pour l'ennemi.
3. **Séquence de Combat :**
   - Les monstres attaquent selon leur vitesse.
   - Les dégâts sont appliqués, les monstres tombent K.O. et sont remplacés.
4. **Fin du Jeu :** Annonce du gagnant lorsque tous les monstres d'un camp sont vaincus.

## Licence

Ce projet est développé à des fins éducatives.

---
Profitez du combat avec vos monstres !


