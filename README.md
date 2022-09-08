# Rock, Paper, Scissors

Rock, Paper, Scissors is  Command terminal game for Python Users.
This game plays between user and computer, in which each player simultaneously selects one of three options. These options are "rock", "paper", and "scissors". It has three possible outcomes: a draw, a win, or a loss. A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors" or "breaks scissors" or sometimes "blunts scissors"), but will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper"). If both players choose the same option, the result will be draw.

Link to deployed website - [Rock, Paper, Scissors_Game](https://rock-paper-scissors-python-gam.herokuapp.com/)

![responsive_screenshot](/picture/screenshot.png)

[Go to How to Play](#how-to-play)

[Go to Features](#features)
  - [Go to Existing Features](#existing-features)


[Go to Testing](#testing)

[Go to Validator Testing](#validator-testing)

[Go to Deployment](#deployment)

[Go to Credits](#credits)

## How to Play

'Rock, Paper, Scissors' is Command game. On [Wikipedia](https://en.wikipedia.org/wiki/Rock_paper_scissors), you may find out more information.

This game plays between user and computer, in which each player simultaneously selects one of three options. 

These options are "rock", "paper", and "scissors". It has three possible outcomes: a draw, a win, or a loss.

 A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors" or "breaks scissors" or sometimes "blunts scissors"), but will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper"). If both players choose the same option, the result will be draw.


## Features

#### __Key Features__

  - Talk the user name first.
  - All inputs are validated and checked for errors.
  - You cannot enter coordinates outside the boundaries of the options.
  - You can just choose one option.
  - Generated randomly


- The Game Options

  - The game options include a clear icons and each button has a title, It's visible for them when user hover with mouse on it.
  - In this section the user can click on buttons and make their choice and plays the game.

  ![game_photo]()

- The Game Results

  - When the user make a choice, the option relating to their choice is shown on next line.
  - Game randomly selects an option for the computer player and displays the option relating to the computer's choice and then determines who the winner is.
  - The final score will show when user decided to exit the game and write the (Q) character.
  - At the end of game will show the user and computer score.

  ![game_result]()
  
  
## Testing

I manually tested this project by carrying out the subsequent actions:

- Verified there are no issues by running the code through a PEP8 linter.

- Given invalid inputs: strings when numbers are anticipated, inputs that are outside of boundaries, and numerous instances of the same guess.

- Tested in my local terminal and the Heroku terminal for the Code Institute.



