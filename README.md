# Deminer 💣

<a name="readme-top"></a>

## Index
 
- [Index](#index)
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Description](#description)
 
## Project Overview  

A program where a player moves on a grid to reach a bomb. The grid contains a player ('P') and a bomb ('X'), and the player does not know the bomb's position but must follow directions to get closer. (The goal is to determine the directions the player should move to reach the bomb as quickly as possible.)


## Prerequisites 
 
> [!IMPORTANT]
> To get started with this project, you'll need:
 
- [Python](https://www.python.org/downloads/) installed on your local machine for backend development.
- [Git](https://git-scm.com/downloads) for version control and collaboration.

## Built With 🔨
 
For this project i worked on this technologie
 
* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>
 

## Installation 
 
> [!NOTE]
>1. Request access to be added as a collaborator. (not necessary here)
 
2. Clone the repository:
   ```bash
   git clone https://github.com/Tokennn/deminer.git
   cd deminer/
 
3. Install dependencies and prepare your environment:
    ```bash
    go mod tidy
 
4. Open a (new) terminal in Visual-studio : 
    ```bash
    cd /deminer
    ```
 
<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>
 
 
## Getting Started  
 
After installation, follow these steps to run the game :
 
1. __Start__ the game :
    ```bash
    python3 deminer.py

    or 

    python deminer.py
 
 __Good luck__ !
 
<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>


## Description Grid Representation  


__*The grid is a list where :*__

    * An empty space is represented by the character 'o'.
    * The player is represented by the character 'P'.
    * The bomb is represented by the character 'X'.

__Available Directions:__

    -> 'U' (Up)

    -> 'D' (Down)

    -> 'R' (Right)

    -> 'L' (Left)

    -> 'UL' (Up Left)

    -> 'UR' (Up Right)

    -> 'DL' (Down Left)

    -> 'DR' (Down Right)
    
 

### **Steps to Solve the Problem:**  

__*Locate the Player and the Bomb*__

```Traverse the grid to find the coordinates of the player ('P') and the bomb ('X')```

__Calculate the Direction:__

```Determine the direction in which the player should move to get closer to the bomb. Use the coordinates of the player and the bomb to calculate this direction```

__Move the Player:__

```A loop to move the player in the determined direction. Update the`player's coordinates with each move and add each direction to a list of directions.```

__Stop When the Bomb is Reached:__

```End the process when the player's coordinates match those of the bomb```

<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>


## Note ! ⚠️

``` 
- When the game starts you have by default two grids (the top one which will give the position of the bomb (X) when it is found then the bottom one which represents the current game with the position of the character (P)).

Then, when you win the game, the grids are updated randomly, with one of the other grid layouts for P and X depending on the scenarios of the subject. However, you can stop the game at any time by doing a "ctrl + c" on your keyboard.

- You will always have two grids when you start the game because subsequently, the first grid will be used to represent the position of the bomb once found then the second will be that of your game in real time.

- Let's also add that there are three types of grids which are generated randomly: a SMALL one, a LARGE one and finally a VERTICAL one corresponding to the information given in the subject.
```

## Author / Contact 
 
- __[@Tokennn]__ (https://github.com/Tokennn)

<!-- (Markdown img link) : -->

[Python]: https://img.shields.io/badge/Python-grey?style=for-the-badge&logo=python

[Python-url]: https://www.python.org/