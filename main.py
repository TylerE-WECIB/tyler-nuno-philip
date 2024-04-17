import keyboard
import os
import art_dimension

def title(): # title screen code
    
    selections = "> Start\n  Help"  
    
    
    while True: # constantly checks for keyboard interaction and changes variables accordingly
        title_screen = f"""  _________                                  .__ 
 /   _____/____    _____  __ ______________  |__|
 \_____  \\__  \  /     \|  |  \_  __ \__  \ |  | 
 /        \/ __ \|  Y Y  \  |  /|  | \// __ \|  | 
/_______  (____  /__|_|  /____/ |__|  (____  /__| 
        \/     \/      \/                  \/             
_________            .___         .___                   
\_   ___ \  ____   __| _/____   __| _/______  _  ______  
/    \  \/ /  _ \ / __ |/ __ \ / __ |/  _ \ \/ \/ /     \ 
\     \___(  <_> ) /_/ \  ___// /_/ (  <_> )     /   |  \\
 \______  /\____/\____ |\___  >____ |\____/ \/\_/|___|  /
        \/            \/    \/     \/                 \/ 

Duel of Destiny: 
CTI Ultimate Edition First Strike Second Half Gamma Omicron Tau Upsilon: 
"Beat the grass and alert the snake", "The swing of a sword cannot cut the mist from the sky" 
Version 3.12cti
{selections}
"""
        print(title_screen)
        os.system("cls")
        if keyboard.is_pressed("down"):
            selections = "  Start\n> Help"
            continue
        if keyboard.is_pressed("up"):
            selections = "> Start\n  Help"
            continue
        if keyboard.is_pressed("enter") and selections == "> Start\n  Help":
           print("gmae has started")
           break     
        if keyboard.is_pressed("enter") and selections == "  Start\n> Help":
            break


def game_over(): # screen that shows up after game ends
    selections = "> Once Again            Quit"

    while True:
        game_over_screen = f"""
game over
{selections}
"""    
        print(game_over_screen)
        os.system("cls")
        if keyboard.is_pressed("left"):
            selections = "> Once Again            Quit"
            continue
        if keyboard.is_pressed("right"):
            selections = "  Once Again          > Quit"
            continue
        if keyboard.is_pressed("enter") and selections == "> Once Again            Quit":
           print("new gmae has started")
           break     
        if keyboard.is_pressed("enter") and selections == "  Once Again          > Quit":
            break

def character_select(): # where you name your character
	player1_name = input("Name: ")
	player2_name = input("Name: ")

	while True:
		character_select_screen = f"""
{}                  Player 2
{player1_name}            {player2_name}
"""
	print(character_select_screen)
