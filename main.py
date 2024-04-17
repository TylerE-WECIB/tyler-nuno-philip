import keyboard
import os
import art_dimension
from time import sleep


def title(): # title screen code
    
	selections = "> Start\n  Help\n  Quit"  
	
	while True: # constantly checks for keyboard interaction and changes variables accordingly
		title_screen = f"""
{selections}
"""

		print(title_screen)
		sleep(.01)
		os.system("cls")
		if keyboard.is_pressed("down") and selections == "> Start\n  Help\n  Quit":
			selections = "  Start\n> Help\n  Quit"
			continue
		if keyboard.is_pressed("down") and selections == "  Start\n> Help\n  Quit":
			selections = "  Start\n  Help\n> Quit"
			continue
		if keyboard.is_pressed("up") and selections == "  Start\n> Help\n  Quit":
			selections = "> Start\n  Help\n  Quit"
			continue
		if keyboard.is_pressed("up") and selections == "  Start\n  Help\n> Quit":
			selections = "  Start\n> Help\n  Quit"
			continue
		if keyboard.is_pressed("enter") and selections == "> Start\n  Help\n  Quit":
			game_start()
			break     
		if keyboard.is_pressed("enter") and selections == "  Start\n> Help\n  Quit":
			break
		if keyboard.is_pressed("enter") and selections == "  Start\n  Help\n> Quit":
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
           game_start()
           break     
        if keyboard.is_pressed("enter") and selections == "  Once Again          > Quit":
           break


def character_select(): # where player names their character
	global player1_name
	global player2_name
	print(art_dimension.p1_portrait)
	player1_name = input("Name: ")
	os.system("cls")
	print(art_dimension.p2_portrait)
	player2_name = input("Name: ")


def game_start():
	p1_health = 100
	p2_health = 100
	while p1_health > 0 and p2_health > 0:
		pass



def main():
	pass
        
title()