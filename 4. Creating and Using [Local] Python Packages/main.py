import random

# main function
def rock_paper_scissors():
    """This function houses all other functions that runs rock paper scissiors"""

    # step 1
    while True:
        print("Welcome to Rock, Paper and Scissors game:\nR - Rock\nP -Paper\nS - Scissors")

        # call player
        player_choice = None

        # step 2 - available choices
        choices = ['R', 'P', 'S']

        # step 3 - computer's random choice
        computer_choice = random.choice(choices)

        # step 4
        while player_choice not in choices:
            player_choice = call_player()
            
        # step 5
        result_checker = checker(player_choice, computer_choice)

        if result_checker == "win":
            print("Player wins!")
            break
        
        elif result_checker == "lose":
            print("Player lose!")
            break
        
        elif result_checker == "tie":
            continue

        
# auxilary functions
def call_player():
    player_input = str(input("Please enter item (R, P or S): "))
    return player_input.upper()


def checker(player_input, computer_input):
    if player_input == computer_input:
        print(f"Player({player_input})\nCPU({computer_input})")
        return "tie"

    elif player_input == "R":
        if computer_input == 'S':
            print("Player(Rock)\nCPU(Scissors)")
            return "win"
        elif computer_input == 'P':
            print("Player(Rock)\nCPU(Paper)")
            return "lose"


    elif player_input == 'P':
        if computer_input == 'R':
            print("Player(Paper)\nCPU(Rock)")
            return "win"
        elif computer_input == 'S':
            print("Player(Paper)\nCPU(Scissors)")
            return "lose"

    elif player_input == 'S':
        if computer_input == 'P':
            print("Player(Scissors)\nCPU(Paper)")
            return "win"
        elif computer_input == 'R':
            print("Player(Scissors)\nCPU(Rock)")
            return "lose"

    
# running the function
rock_paper_scissors()
