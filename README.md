# Hanoi Tower Speedrun

This is a speedrun version of the _Hanoi Tower_ minigame

![HanoiSimulation](https://github.com/user-attachments/assets/a80d8d57-e348-4f0a-ab83-b158ed5adb16)


## Goal

Objective of the game is to stack all the pieces from one side to another making single moves (in the less amount of moves and time, that's why its a *speedrun*)

### Conditions for the moves
- You can move only one piece at a time
- A piece *CAN* be placed above another piece or in an empty column
- A piece can *NOT* be above a smaller piece

## Controls
You have to use the LEFT, DOWN and RIGHT arrows to move between columns
A move is divided in 2 steps:
1. select the TOP piece from a column
2. select the column where you want to move it.
If you want to move another piece you first need to release the one you are holding.

You can select the # of pieces from 3 to 10 and reset the game at any time

## Getting Started

### Prerequisites
- Python3
- pygame

### Installation
1. Clone repository:
```
git clone https://github.com/JuanasoKsKs/Hanoi-Tower-Speedrun
```

2. Install pygame (assuming you already have python)
```
pip install pygame
```
if you don't have pip, install it as well

3. Execute 'python3 main.py' in the root directory of the repo to start
```
python3 main.py
```

### Keep in mind
- Your current score won't be saved if you reset
- the scores are saved in the file "records.txt" on the root of the project and it is readed and updated every time you run/complete the game (do not edit the format of the file manually)
- I created the game in a venv with python=3.13 but it should work in any version you like