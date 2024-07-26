import random

def find_direction(player_pos, bomb_pos):
    """
    Détermine la direction dans laquelle le joueur doit se déplacer pour se rapprocher de la bombe.
    :param player_pos: Tuple (x, y) représentant la position actuelle du joueur
    :param bomb_pos: Tuple (x, y) représentant la position de la bombe
    :return: Une chaîne représentant la direction ('U', 'D', 'L', 'R', 'UL', 'UR', 'DL', 'DR')
    """
    player_x, player_y = player_pos
    bomb_x, bomb_y = bomb_pos
   
    direction = ""
   
    if player_y > bomb_y:
        direction += "U"
    elif player_y < bomb_y:
        direction += "D"
   
    if player_x > bomb_x:
        direction += "L"
    elif player_x < bomb_x:
        direction += "R"
   
    return direction

def update_grid(grid, player_pos, bomb_pos, reveal_bomb=False):
    """
    Met à jour la grille avec la nouvelle position du joueur.
    :param grid: Liste de listes représentant la grille de jeu
    :param player_pos: Tuple (x, y) représentant la position actuelle du joueur
    :param bomb_pos: Tuple (x, y) représentant la position de la bombe
    :param reveal_bomb: Booléen pour indiquer si la position de la bombe doit être révélée
    :return: La grille mise à jour
    """
    updated_grid = [['o' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    updated_grid[player_pos[1]][player_pos[0]] = 'P'
   
    if reveal_bomb:
        updated_grid[bomb_pos[1]][bomb_pos[0]] = 'X'
