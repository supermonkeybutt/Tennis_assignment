import sys

class Tennis:
    SCORES_DESCRIPTION = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0

    def returnScore(self):
        """
        Return the current tennis score of the game
        """
        score_diff = self.player1_score - self.player2_score
        if self.player1_score >= 4 or self.player2_score >= 4:
            if score_diff == 0:
                return "Deuce"
            elif score_diff <= -2:
                return "Win for player2"
            elif score_diff == 1:
                return "Advantage for player 1"
            elif score_diff == -1:
                return "Advantage for player 2"
            else:
                return "Win for player1"
        elif self.player1_score == 3 and score_diff == 0:
            return "Deuce"
        else:
            return f"{self.SCORES_DESCRIPTION[self.player1_score]}-{self.SCORES_DESCRIPTION[self.player2_score]}"

    def addScore(self, player):
        """
        Add a score to the player
        """
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1
        else:
            raise ValueError("Invalid player number")
        
    def beginGame(self, input_file = None):
        """
        Start a new game, read the input file if provided
        """
        if input_file:
            with open(input_file, 'r') as f:
                print(self.returnScore())
                for line in f:
                    userInput = line.strip()
                    if userInput in ["1", "2"]:
                        self.addScore(int(userInput))
                        print(self.returnScore())
                    else:
                        raise ValueError(f"Invalid input, {userInput}")
        else:
            print("Enter the player number who scored: 1 or 2, or q to quit scoring")
            print(self.returnScore())
            while True:
                userInput = input("Enter the player number who scored: ")
                if userInput in ["1", "2"]:
                    self.addScore(int(userInput))
                    print(self.returnScore())
                elif userInput in [1, 2]:
                    self.addScore(userInput)
                    print(self.returnScore())
                elif userInput == "q":
                    break
                else:
                    print(f"Invalid input, {input}, enter 1 or 2 to score, or q to quit")

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else None
    tennis = Tennis()
    tennis.beginGame(input_file)
                
                    
                

