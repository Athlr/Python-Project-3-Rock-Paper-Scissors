import random

def game():
    user_choice = input("Rock(r), Paper(p) or Scissors(s): ").lower()
    rock_paper_scissors = ["r", "p", "s"]
    if user_choice not in rock_paper_scissors:
        print("These are not valid choices present in traditional rock, paper, scissor. Try again.")
        return "false answer choice"

    computer_choice = random.choice(rock_paper_scissors)
    # Testing
    # print(user_choice)
    # print(computer_choice)

    # If user & computer ties, return tie
    if user_choice == computer_choice:
        print("You've tied!")
        return "tie"

    #If user wins, return win
    elif (user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r") or (user_choice == "s" and computer_choice == "p"):
        print("You win!")
        return "win"
    
    #If user does not tie or win, it can be assumed that they lose, return lose
    else:
        print("You lose!")
        return "lose"

if __name__ == "__main__":
    game()