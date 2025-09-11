import os

###################################################################################################################
'''                      Examples of objects that will go inside the lists in Player dict below!!!        
 
    "answer_checker": [
        {
            "problem": "2 + 2",
            "user_answer": 4,
            "correct_answer": 4,
            "correct": True
        },
        {
            "problem": "5 * 3",
            "user_answer": 16,
            "correct_answer": 15,
            "correct": False
        },
        {
            "problem": "10 / 2",
            "user_answer": 5,
            "correct_answer": 5,
            "correct": True
        }
    ]

'''
###################################################################################################################

# Player data for now (We will add more to this as we go)
player = {
    "name": "Unknown",
    "answer_checker": [],
    "memory_bank": [],
    "number_guesser": [],
    "score_answer_checker": 0,
    "score_memory_bank": 0,
    "score_number_guesser": 0
}



# Helper methods
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
    
# Used https://www.asciiart.eu/text-to-ascii-art
def print_starting_screen():
    logo = r"""
++--------------------------------------------------++
++--------------------------------------------------++
||    __        __   _                              ||
||    \ \      / /__| | ___ ___  _ __ ___   ___     ||
||     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \    ||
||      \ V  V /  __/ | (_| (_) | | | | | |  __/    ||
||       \_/\_/ \___|_|\___\___/|_| |_| |_|\___|    ||
||                                                  ||
||                   _                              ||
||                  | |_ ___                        ||
||                  | __/ _ \                       ||
||                  | || (_) |                      ||
||                   \__\___/                       ||
||                                                  ||
||   ____        _                              _   ||
||  |  _ \  __ _| |_ __ _ _ __ ___   ___  _ __ | |  ||
||  | | | |/ _` | __/ _` | '_ ` _ \ / _ \| '_ \| |  ||
||  | |_| | (_| | || (_| | | | | | | (_) | | | |_|  ||
||  |____/ \__,_|\__\__,_|_| |_| |_|\___/|_| |_(_)  ||
||                                                  ||
++--------------------------------------------------++
++--------------------------------------------------++
                                                               
    """
    print(logo)
    input("Press any key to continue...")
    clear_terminal()


def print_menu():
    logo = r"""
.-----------------------------------------------------------------------------.
|                                                                             |
| ____        _                                       __  __                  |
||  _ \  __ _| |_ __ _ _ __ ___   ___  _ __    _     |  \/  | ___ _ __  _   _ |
|| | | |/ _` | __/ _` | '_ ` _ \ / _ \| '_ \  (_)    | |\/| |/ _ \ '_ \| | | ||
|| |_| | (_| | || (_| | | | | | | (_) | | | |  _     | |  | |  __/ | | | |_| ||
||____/ \__,_|\__\__,_|_| |_| |_|\___/|_| |_| (_)    |_|  |_|\___|_| |_|\__,_||
|                                                                             |
'-----------------------------------------------------------------------------'                                                       
    """
    print(logo)
    print(f"\t\t\t\tPLAYER: {player['name']}\n")
    print("1] Answer Checker")
    print("2] Memory Bank")
    print("3] Number Guesser")
    print("0] Exit\n")

def create_player_menu():
    logo = r"""
.------------------------------------------------------------------------------------------------------------------.
|                                                                                                                  |
| ____        _                                        ____                _         ____  _                       |
||  _ \  __ _| |_ __ _ _ __ ___   ___  _ __    _      / ___|_ __ ___  __ _| |_ ___  |  _ \| | __ _ _   _  ___ _ __ |
|| | | |/ _` | __/ _` | '_ ` _ \ / _ \| '_ \  (_)    | |   | '__/ _ \/ _` | __/ _ \ | |_) | |/ _` | | | |/ _ \ '__||
|| |_| | (_| | || (_| | | | | | | (_) | | | |  _     | |___| | |  __/ (_| | ||  __/ |  __/| | (_| | |_| |  __/ |   |
||____/ \__,_|\__\__,_|_| |_| |_|\___/|_| |_| (_)     \____|_|  \___|\__,_|\__\___| |_|   |_|\__,_|\__, |\___|_|   |
|                                                                                                  |___/           |
|                                                                                                                  |
'------------------------------------------------------------------------------------------------------------------'                                                     
    """
    print(logo)
    player["name"] = input("What is your name?: ")

# Sprint 1?
def answer_checker():
    print("\n[Answer Checker]")
    print("This feature is coming soon!")

# Sprint 2?
def memory_bank():
    print("\n[Memory Bank]")
    print("This feature is coming soon!")

# Sprint 3?
def number_guesser():
    print("\n[Number Guesser]")
    print("This feature is coming soon!")


### Main method (where the game will loop) ###
def main():
#Setting up Game/Player
    print_starting_screen()
    create_player_menu()

# Game Loop starts here
    while True:
        clear_terminal()
        print_menu() # Edit menu in this function
        choice = input("Selected: ")

        # Check for valid input
        if not choice.isdigit():
            print("⚠️ Please enter a number!")
            input("Press Enter to continue...")
            continue

        choice = int(choice) #cast to integer
        clear_terminal()
        
        # Switch-case
        match choice:
            case 1:
                answer_checker()
            case 2:
                memory_bank()
            case 3:
                number_guesser()
            case 0:
                print("\n👋 Goodbye!")
                break
            case _:
                print("⚠️ Invalid option!")

        input("\nPress Enter to return to the menu...")

# Calls main to run the program
if __name__ == "__main__":
    main()
