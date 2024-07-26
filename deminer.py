import random

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

def update_grid(grid, player_pos, bomb_pos, reveal_bomb=False):

    updated_grid = [['o' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    updated_grid[player_pos[1]][player_pos[0]] = 'P'
   
    if reveal_bomb:
        updated_grid[bomb_pos[1]][bomb_pos[0]] = 'X'
   
    return updated_grid

def print_grid(grid):

    for row in grid:
        print(" ".join(row))
    print()

def get_player_move():

    valid_moves = ['U', 'D', 'L', 'R', 'UL', 'UR', 'DL', 'DR']
    move = input("Choisissez une direction (U, D, L, R, UL, UR, DL, DR) : ").strip().upper()
    while move not in valid_moves:
        print("Direction invalide. Veuillez choisir parmi : U, D, L, R, UL, UR, DL, DR.")
        move = input("Retantez votre chance et choisissez une direction : ").strip().upper()
    return move

def move_player_interactively(grid, bomb_pos):

    player_pos = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'P':
                player_pos = (x, y)
   
    if not player_pos:
        raise ValueError("La grille doit contenir un joueur 'P'")
   
   
    while player_pos != bomb_pos:
        print_grid(update_grid(grid, player_pos, bomb_pos))
        direction = get_player_move()
        x, y = player_pos
        if direction == 'U':
            y -= 1
        elif direction == 'D':
            y += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'R':
            x += 1
        elif direction == 'UL':
            x -= 1
            y -= 1
        elif direction == 'UR':
            x += 1
            y -= 1
        elif direction == 'DL':
            x -= 1
            y += 1
        elif direction == 'DR':
            x += 1
            y += 1
       
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            player_pos = (x, y)
            grid = update_grid(grid, player_pos, bomb_pos)
        else:
            print("Vous ne pouvez pas faire ce mouvement, essayez à nouveau.")
   
    print_grid(update_grid(grid, player_pos, bomb_pos, reveal_bomb=True))
    print("Félicitations ! Vous avez trouvé la bombe.")
   
    # Générer une nouvelle grille et recommencer le jeu
    grid, bomb_pos = generate_new_grid(len(grid), len(grid[0]))
    print("Nouvelle grille générée :")
    move_player_interactively(grid, bomb_pos)

def generate_new_grid(rows, cols):

    grid = [['o' for _ in range(cols)] for _ in range(rows)]
    player_x = random.randint(0, cols - 1)
    player_y = random.randint(0, rows - 1)
    grid[player_y][player_x] = 'P'
   
    while True:
        bomb_x = random.randint(0, cols - 1)
        bomb_y = random.randint(0, rows - 1)
        if (bomb_x, bomb_y) != (player_x, player_y):
            break
    return grid, (bomb_x, bomb_y)

# Example of initial grid...
initial_grid = [
    ["o", "o", "o", "o", "o"],
    ["o", "P", "o", "o", "o"],
    ["o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o"],
    ["o", "o", "o", "o", "o"]
]
# Initial position of bomb (hide)
initial_bomb_pos = (3, 1)


print("Grille initiale (bombe cachée) :")
print_grid(update_grid(initial_grid, (1, 1), initial_bomb_pos))
move_player_interactively(initial_grid, initial_bomb_pos)
