# Tennis Score Tracker

## Description
This Python script works as a simple tennis game score tracker. 
You can input scores dynamically or read them from a file and outputs the current score using standard tennis terminology (Love, Fifteen, Thirty, Forty, Deuce, Advantage, and Win).

## Features
- Accepts user input to update scores.
- Supports input from a text file.
- Implements correct tennis scoring rules:
  - **Love**, **Fifteen**, **Thirty**, and **Forty** for scores from 0 to 3.
  - **Deuce** when both players have at least 3 points and are tied.
  - **Advantage** when a player has one more point than the opponent after Deuce.
  - **Win** when a player has at least 4 points and leads by at least 2 points.

## Usage
### Running the Script with Manual Input
Run the script and enter `1` for Player 1 or `2` for Player 2 to update the score. Type `q` to quit.

```sh
python tennis_game.py
```

### Running the Script with a File Input
Provide a text file containing points (one per line, either `1` or `2`).

```sh
python tennis_game.py testData.txt
```

## Example Input and Output
### User Input Example
```
Enter the player number who scored: 1 or 2, or q to quit scoring
Love-Love
Enter the player number who scored: 1
Fifteen-Love
Enter the player number who scored: 2
Fifteen-Fifteen
Enter the player number who scored: 1
Thirty-Fifteen
Enter the player number who scored: 2
Thirty-Thirty
Enter the player number who scored: 1
Forty-Thirty
```

### File Input Example (`testData.txt`)
```
1
2
1
2
1
2
1
2
1
2
1
1
2
2
1
2
1
2
```
#### Output
```
Love-Love
Fifteen-Love
Fifteen-Fifteen
Thirty-Fifteen
Thirty-Thirty
Forty-Thirty
Deuce
Advantage for player 1
Deuce
Advantage for player 1
Deuce
Advantage for player 1
Win for player1
Advantage for player 1
Deuce
Advantage for player 1
Deuce
Advantage for player 1
Deuce
```

## Requirements
- Python 3.x

## Notes
- This implementation only tracks a **single game** and does not support sets or matches.
- Ensure that the input file contains only valid entries (`1` or `2`).


⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⢋⣩⣌⣩⠹⠖⠉⠁⠀⠀⠀⠀⠈⠉⠓⠟⣉⣡⣭⡙⣷⠀⠀⠀⠀
⠀⠀⠀⣿⢸⣏⡾⠛⠀⢀⣀⡀⠀⠀⠀⠀⢀⣠⡄⠀⠉⢻⣜⡿⣸⡇⠀⠀⠀
⠀⠀⠀⢻⣾⣟⣀⡀⢀⣸⣦⠝⠀⠀⠀⠀⠺⣤⣞⡀⠀⣀⣽⣷⡿⠁⠀⠀⠀
⠀⣠⠖⠈⠀⠀⠀⠉⠛⠫⠿⡶⠒⢾⣶⠒⠲⠿⠟⠟⠋⠁⠀⠀⠉⠲⣤⠀⠀
⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣶⡞⠟⣶⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀
⣟⠀⠀⠀⠀⣀⢀⠀⠀⠀⠀⠘⢿⣏⣛⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⣿⠀⠀⢠⡞⢫⠙⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⡹⢳⣆⠀⠀⣸⠇
⠘⣧⡢⠘⡏⠀⠀⠀⠱⠄⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠀⠀⠀⠈⡅⢠⣾⠟⠀
⠀⠈⢻⡷⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢲⣿⠉⠀⠀
⠀⠀⣼⠃⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⢿⠀⠀⠀
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀
⠀⠀⠹⣧⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠀⠀⠀
⠀⠀⠀⠙⣳⣭⣐⡂⢀⠀⠀⣀⣀⣀⣀⣐⣀⠄⡀⠀⣀⣀⣤⣽⡟⠀⠀⠀⠀
⠀⠀⠀⢸⣇⣀⣨⣽⡿⠿⠛⠉⠉⠉⠉⠉⠉⠙⠻⢿⣭⣄⣀⣨⡷⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀
