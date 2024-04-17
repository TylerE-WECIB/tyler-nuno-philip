import keyboard
import os

def title_screen(): # title screen code
    
    selections = "> Start\n  Help"  
    
    
    while True: # constantly checks for keyboard interaction and changes variables accordingly
        title = f"""  _________                                  .__ 
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
        print(title)
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


def game_over():
    selections = "> Once Again            Quit"

    while True:
        game_over_screen = f"""
game over
{selections}
"""    
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

game_over()