# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working
winningCombinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """
    def __init__(self):
        self.board = ["*","*","*","*","*","*","*","*","*"]
    def __str__(self):
        return f"{self.board[0]} {self.board[1]} {self.board[2]}\n{self.board[3]} {self.board[4]} {self.board[5]}\n{self.board[6]} {self.board[7]} {self.board[8]}"
    def make_move(self, player: str, i: int) -> None:
        if self.board[i] == "*":
            self.board[i] = player
        else: print("That square is occupied! Try again.")
    def has_won(self, player: str) -> bool:
        for combo in winningCombinations:
            if self.board[combo[0]] == player and self.board[combo[1]] == player and self.board[combo[2]] == player:
                return True
        return False 
    def game_over(self,players: list[str]) -> bool:
        if self.has_won(players[0]):
            return True
        if self.has_won(players[1]):
            return True
        for square in self.board:
            if square == "*":
                return False
        return True
    def clear(self):
        self.board = ["*","*","*","*","*","*","*","*","*","*"]


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over(players):
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not (is_int(move) and 0 <= int(move) <= 8):
            print(f"The position {move} is invalid! Please input an integer between 0 and 8 (inclusive)!")
            # raise ValueError(
            #     f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            # )
        else:
            brd.make_move(players[turn],int(move))
            if turn == 0:
                turn += 1
            else: turn -= 1

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over(["X","O"]) == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over(["X","O"]) == True

    brd.clear()

    assert brd.game_over(["X","O"]) == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over(["X","O"]) == True

    print("All tests passed!")

    # uncomment to play!
    play = True
    while play == True:
        play_tic_tac_toe()
        endLoop = False
        while not endLoop:
            answer: str = input("Would you like to play again? Please answer 'Yes' or 'No'!")
            if answer == "No":
                play = False
                endLoop = True
            elif answer == "Yes":
                endLoop = True
            else: print("Please respond with 'Yes' or 'No'.")
        
