# Deminer
Objectif
Créer un programme où un joueur se déplace sur une grille pour atteindre une bombe. La grille contient un joueur ('P') et une bombe ('X'), et le joueur ne connaît pas la position de la bombe mais doit suivre des directions pour s'en rapprocher. Le but est de déterminer les directions dans lesquelles le joueur doit se déplacer pour atteindre la bombe le plus rapidement possible.
Instructions

## Représentation de la Grille :

__La grille est une liste où :__

- Un espace vide est représenté par le caractère 'o'.
- Le joueur est représenté par le caractère 'P'.
- La bombe est représentée par le caractère 'X'.

__Directions Disponibles :__
'U' (Haut)
'D' (Bas)
'R' (Droite)
'L' (Gauche)
'UL' (Haut Gauche)
'UR' (Haut Droite)
'DL' (Bas Gauche)
'DR' (Bas Droite)

## Étapes pour Résoudre le Problème :

__Localiser le Joueur et la Bombe :__

Parcourez la grille pour trouver les coordonnées du joueur ('P') et de la bombe ('X').
Calculer la Direction :
Déterminez la direction dans laquelle le joueur doit se déplacer pour se rapprocher de la bombe. Utilisez les coordonnées du joueur et de la bombe pour calculer cette direction.
Déplacer le Joueur :
Créez une boucle pour déplacer le joueur dans la direction déterminée. Mettez à jour les coordonnées du joueur à chaque déplacement et ajoutez chaque direction à une liste de directions.
Arrêter Lorsque la Bombe est Atteinte :
Terminez le processus lorsque les coordonnées du joueur correspondent à celles de la bombe.
