import random

# -> First fonction to find the bomb in relation to the player's position...

def find_direction(player_pos, bomb_pos):
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

# -> Fonctions to get the movements of the player...

def get_player_move(direction):
    print(f"Déplacez-vous dans la direction: {direction}")
    valid_moves = [direction]
    move = input(f"Choisissez la direction ({direction}) : ").strip().upper()
    while move not in valid_moves:
        print(f"Mauvais sens ! Veuillez prendre: {direction}.")
        move = input(f"Retentez votre chance et prenez {direction} : ").strip().upper()

    return move

# Fonction pour mettre à jour la grille
def update_grid(grid, player_pos, bomb_pos=None, reveal_bomb=False):
    updated_grid = [['o' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    updated_grid[player_pos[1]][player_pos[0]] = 'P'
    if reveal_bomb and bomb_pos is not None:
        updated_grid[bomb_pos[1]][bomb_pos[0]] = 'X' 
   
    return updated_grid

# -> Fonction to print the grid...

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

# Fonction for player deplacements...

def move_player_interactively(grid, bomb_pos):
    player_pos = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'P':
                player_pos = (x, y)
    if not player_pos:
        raise ValueError("La grille doit contenir un joueur 'P'")
    while player_pos != bomb_pos:
        print_grid(update_grid(grid, player_pos, bomb_pos, reveal_bomb=True))
        direction = find_direction(player_pos, bomb_pos)
        move = get_player_move(direction)
        
        x, y = player_pos
        if move == 'U':
            y -= 1
        elif move == 'D':
            y += 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        elif move == 'UL':
            x -= 1
            y -= 1
        elif move == 'UR':
            x += 1
            y -= 1
        elif move == 'DL':
            x -= 1
            y += 1
        elif move == 'DR':
            x += 1
            y += 1
        
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            player_pos = (x, y)
            grid = update_grid(grid, player_pos, bomb_pos, reveal_bomb=True)
        else:
            print("Vous ne pouvez pas faire ce mouvement, essayez à nouveau.")
    print_grid(update_grid(grid, player_pos, bomb_pos, reveal_bomb=True))
    print("Félicitations ! Vous avez trouvé la bombe.")
   
    # -> Generate a new game with a new grid, player and bomb...

    grid, player_pos, bomb_pos = generate_new_grid()
    print("Nouvelle grille générée :")
    move_player_interactively(grid, bomb_pos)

    # -> Fonction to generate a new grid after the last one...

def generate_new_grid():
    grids = [

        # -> First grid
        ([
            ["o", "o", "o", "o", "o"],
            ["o", "P", "o", "o", "o"],
            ["o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o"]
        ], (1, 1), (3, 1)),
        
        # ->  Second grid

        ([
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "X", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "P", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]
        ], (8, 8), (1, 6)),
        
        # -> Third grid

        ([
            ["o"],
            ["o"],
            ["o"],
            ["P"],
            ["o"],
            ["o"],
            ["o"],
            ["o"],
            ["o"],
            ["o"],
            ["o"],
            ["o"],
            ["o"],
            ["X"],
            ["o"],
            ["o"],
            ["o"],
            ["o"],
            ["o"],
            ["o"],
            ["o"]
        ], (0, 3), (0, 13))
    ]

    return random.choice(grids)
grid, player_pos, bomb_pos = generate_new_grid()

print("Grille initiale (bombe visible) :")
print_grid(update_grid(grid, player_pos=player_pos, bomb_pos=bomb_pos, reveal_bomb=True))
move_player_interactively(grid, bomb_pos)
