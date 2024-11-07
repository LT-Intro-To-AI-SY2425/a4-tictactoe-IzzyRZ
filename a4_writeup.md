# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
    I didn't realize that make_move was supposed to return a boolean at first, so the hardest part of the program was probably making the play_tic_tac_toe function compatible with my code above. It also took some creativity to figure out how to check for a winning position, but I'm proud of my winning combinations list
2. Explain how you would add a computer player to the game.
    Instead of taking input from 2 players, assign the computer to be one of the players and have the play_tic_tac_toe code check for which player is playing to determine whether to take player input or make a computer move. (moves explained below)
3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
    Tic-tac-toe is a solved game, so you could make a massive database of all the optimal moves and have the computer reference it. This is probably the most straightforward way to get a tic-tac-toe bot to play all the optimal moves from the start. Instead you could make a "learning" tic-tac-toe bot that chooses randomly from a list of possible moves in any given situation. Moves that lead to loss would be removed from the list and moves that lead to victory would be reinforced. I'm not quite sure how you would handle missed wins that lead to drawing, though.