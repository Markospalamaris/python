import random

def get_choices():
    player_choice = input("Enter a choice(rock ,paper ,sciccors): ")
    options = ["rock", "paper", "sciccors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices
def check_win(player, computer):
    print(f"you chose {player}  computer chose {computer}." )
    if player == computer:
      return "it's a tie!"
    elif player == "rock":
      if computer == "sciccors":
       return "rock smashes sciccors!! You win!"
      else:
       return "Paper covers rock!! You lose."
    elif player == "paper":
      if computer == "rock":
       return "Paper covers rock!! You win!"
      else:
       return "Sciccors cut paper!! You lose."
    elif player == "scissors":
      if computer == "paper":
       return "Sciccors cut paper!! You win!"
      else:
       return "Rock smashes scissors!! You lose."
choices = get_choices()
resault = check_win(choices["player"],choices["computer"])
print(resault)