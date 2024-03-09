from Displays import Displays
from Game import Game
from Computer import Computer
from Computer import Computer
from Human import Human
from Highscores import Highscore

#sets difficulty lvl and starts game vs computer
def computer_mode_start(player_one, is_normal_mode, highscores_main):
    Displays.printBotMenu()
    #easy/medium/hard mode then starts a game
    input_choice = input("Enter your choice (1 to 4): ")
    if input_choice in {"1", "2", "3"}:
        player_two = Computer(input_choice)
        pigGame = Game(player_one, player_two, is_normal_mode, highscores_main)  
        pigGame.start_game()
    #choice 4 goes back to main menu
    elif input_choice == "4":
        pass
    else:
        print("Enter a valid choice")

#gets player2 name and starts game player vs player
def player_mode_start(player_one, is_normal_mode, highscores_main):
    player2_name = input("Enter the name of player two: ")
    player2_name = check_name(player2_name)
    player_two = Human(player2_name)
    pigGame = Game(player_one, player_two, is_normal_mode, highscores_main)
    pigGame.start_game()

#cheat mode or normal mode
def get_play_mode():
    while True:
        user_input = input("Test using cheat mode? (y/n): ")
        if user_input == "n":
            return True
        elif user_input == "y":
            return False
        else:
            print("Incorrect input")

#checks input validity for usernames
def check_name(name):
    if not name.isalnum():
        return check_name(input("\nOnly letters and number allowed!"
                         + "Enter the name again: \n"))
    else: return name
        
def main():
    is_normal_mode = get_play_mode()
    player1_name = input("\nEnter the name of player one: ")
    player1_name = check_name(player1_name)
    player_one = Human(player1_name)
    highscores_main = Highscore(is_normal_mode)
    while True:
        Displays.printMenu()
        choice = input("Enter your choice (1 to 6): ")
        match choice:
            case "1":
                computer_mode_start(player_one, is_normal_mode, highscores_main)
            case "2":
                player_mode_start(player_one, is_normal_mode, highscores_main)
            case "3":
                highscores_main.display_scores()
                input("\nPress any key to go back to the main menu.\n")
            case "4":
                new_username = input("\nNew username: ")
                new_username = check_name(new_username)
                player_one.change_username(new_username)
                print(f"Your username was successfully changed to {player_one.username}")
                input("\nPress any key to go back to the main menu.\n")
            case "5":
                Displays.printRules()
                input("Press any key to go back to the main menu.\n")
            case "6":
                highscores_main.save_scores()
                exit()
            case default:
                print("Enter a valid choice!")


if __name__ == "__main__":
    main()
