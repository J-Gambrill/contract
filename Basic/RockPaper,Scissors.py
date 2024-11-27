import random

def game():
    print('Rock, Paper, or Scissors?')
    choice = input('Enter your choice: ').strip().lower() #ChatGPT recomendations: .strip() --> removes any whitespace before or after string or specific characters. 
    computer_choice = randomChoice()                                             # .lower() --> converts all uppercase to lowercase
    print(f"Computer chose: {computer_choice}")
    result = whoWon(choice, computer_choice)  
    print(result)

def randomChoice():
    num = random.randint(1, 3)
    if num == 1:
        return 'rock'
    elif num == 2:
        return 'paper'
    else:
        return 'scissors'

def whoWon(player, computer):
    if player == computer:
        return "It's a draw!" # the / allows us to continue the coalition on the next line for readabilitu
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return 'You win!'
    elif player in ['rock', 'paper', 'scissors']:
        return 'You lose!'
    else:
        return "Invalid choice! Please choose rock, paper, or scissors."

# Main game loop
while True:
    game()
    playagain = input('Try again? (yes/no): ').strip().lower()
    if playagain == 'no':
        print('Thanks for playing!')
        break
