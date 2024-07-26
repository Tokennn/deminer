 def find_direction(player_pos, bomb_pos):
     """
     Détermine la direction dans laquelle le joueur doit se déplacer pour se rapprocher de la bombe.
     :param player_pos: Tuple (x, y) représentant la position actuelle du joueur
     :param bomb_pos: Tuple (x, y) représentant la position de la bombe
     :return: Une chaîne représentant la direction ('U', 'D', 'L', 'R', 'UL', 'UR', 'DL', 'DR')
     """
     player_x, player_y = player_pos
     bomb_x, bomb_y = bomb_pos
