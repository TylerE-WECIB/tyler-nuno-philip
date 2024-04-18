import keyboard
import os
import art_dimension
import time
import random




player1_name = ""
player2_name = ""
p1_health = 50
p2_health = 50

with open("README.md", "r") as help_file:  # Opens the readme file for the help menu
    help_file = help_file.read()


class Questions:  # Philip
    def __init__(self, question_id, question_text, answer_1, answer_2, answer_3, correct_answer):
        self.question_id = question_id  # question_id is used to prevent repeats of questions
        self.question_text = question_text  # question_text stores the question that is being answered
        self.answer_1 = answer_1  # answer_1 is a possible answer to the question
        self.answer_2 = answer_2  # answer_2 is a possible answer to the question
        self.answer_3 = answer_3  # answer_3 is a possible answer to the question
        self.correct_answer = correct_answer  # correct_answer is the correct answer to the question, is equal to one of the answer arguments
        self.question_subject = None  # question_subject stores the question's subject




class PythonQuestions(Questions):  # Philip
    def __init__(self, question_id, question_text, answer_1, answer_2, answer_3, correct_answer):
        super().__init__(question_id, question_text, answer_1, answer_2, answer_3, correct_answer)
        Questions.question_subject = "Python"




class CtiQuestions(Questions):  # Philip
    def __init__(self, question_id, question_text, answer_1, answer_2, answer_3, correct_answer):
        super().__init__(question_id, question_text, answer_1, answer_2, answer_3, correct_answer)
        Questions.question_subject = "CTI"

# All questions by Philip
question_1 = CtiQuestions("01",
                          "Which Data Link Sublayer communicates between networking software and device hardware?",
                          "MAC Sublayer",
                          "LLC Sublayer",
                          "ARP Sublayer",
                          "LLC Sublayer")
question_2 = CtiQuestions("02",
                         "What is used to identify the network/host portion of an IPv4 address?",
                         "Subnet Mask",
                         "Boolean Mask",
                         "Address Algorithm",
                         "Subnet Mask", )
question_3 = CtiQuestions("03",
                         "How many layers are in the OSI model?",
                         "4",
                         "7",
                         "6",
                         "7")
question_4 = CtiQuestions("04",
                         "How many layers are in the TCP/IP model?",
                         "4",
                         "7",
                         "6",
                         "4")
question_5 = CtiQuestions("05",
                         "Which layer is present in both the OSI and TCP/IP models?",
                         "Presentation Layer",
                         "Session Layer",
                         "Application Layer",
                         "Application Layer")
question_6 = CtiQuestions("06",
                         "The hexadecimal value \"F\" equates to what decimal value?",
                         "14",
                         "15",
                         "16",
                         "15")
question_7 = CtiQuestions("07",
                         "How many octets are in an IPv4 Address?",
                         "4",
                         "8",
                         "32",
                         "4")
question_8 = PythonQuestions("08",
                            "What is the python programming language named after?",
                            "Monty Python's Flying Circus",
                            "The Python of greek mythology",
                            "The genus of constricting snakes",
                            "Monty Python's Flying Circus")
question_9 = CtiQuestions("09",
                          "The IEEE is primarily responsible for creating what?",
                          "Wireless technical standards",
                          "Wired technical standards",
                          "LAN devices",
                          "Wireless technical standards")
question_10 = CtiQuestions("10",
                           "DHCP should NOT be used to configure the IP address of which of these devices?",
                           "mobile devices",
                           "desktops",
                           "printers",
                           "printers")
question_11 = CtiQuestions("11",
                           "Which OSI model layers is NOT a part of the Network interface layer of the TCP/IP model?",
                           "Network Layer",
                           "Datalink Layer",
                           "Physical Layer",
                           "Network Layer")
question_12 = CtiQuestions("12",
                           "In what order are messages sent to acquire an IPv4 Address via DHCP?",
                           "DHCPDISCOVER -> DHCPOFFER -> DHCPREQUEST -> DHCPACK",
                           "DHCPDISCOVER -> DHCPREQUEST -> DHCPOFFER -> DHCPACK",
                           "DHCPDISCOVER -> DHCPACK -> DHCPREQUEST -> DHCPOFFER",
                           "DHCPDISCOVER -> DHCPOFFER -> DHCPREQUEST -> DHCPACK")
question_13 = CtiQuestions("13",
                          "What is true of UDP?",
                          "It keeps track of segments sent to the destination use acknowledgements",
                          "It operates on the Network Layer of the OSI model",
                          "It uses a \"best effort\" deliver system",
                          "It uses a \"best effort\" deliver system")
question_14 = CtiQuestions("14",
                          "Ports 1024 through 49151 are known as...",
                          "Well-Known Ports",
                          "Registered Ports",
                          "Private Ports",
                          "Registered Ports")
question_15 = CtiQuestions("15",
                          "What is NOT true of Fiber-Optic Cabling?",
                          "It is less expensive than Copper Cabling",
                          "It uses light to transmit data",
                          "It is completely immune to EMI and RFI",
                          "It is less expensive than Copper Cabling")
question_16 = CtiQuestions("16",
                          "Which of the following is a UTP Cable Standard?",
                          "T568B",
                          "T567A",
                          "T658A",
                          "T568B")
question_17 = PythonQuestions("17",
                             "Python is considered what of the following?",
                             "A Compiled Programming Language",
                             "Closed Source Software",
                             "An Object-Oriented Programming Language",
                             "An Object-Oriented Programming Language")
question_18 = CtiQuestions("18",
                           "Which is NOT a migration technique between IPv4 and IPv6?",
                           "Dual Stack",
                           "Translation",
                           "Burrowing",
                           "Burrowing")
question_19 = CtiQuestions("19",
                          "How long is an IPv6 address in bits?",
                          "128 Bits",
                          "64 Bits",
                          "256 Bits",
                          "128 Bits")
question_20 = CtiQuestions("20",
                          "What address is stored in the layer 2 ethernet frame?",
                          "MAC Address",
                          "IP Address",
                          "Logical Address",
                          "MAC Address")
question_21 = CtiQuestions("21",
                          "What is the loopback address?",
                          "127.0.0.1",
                          "8.8.8.8",
                          "255.255.255.255",
                          "127.0.0.1")
question_22 = CtiQuestions("22",
                          "Which of the following is a Cloud Service?",
                          "PaaS",
                          "FaaS",
                          "MaaS",
                          "PaaS")
question_23 = CtiQuestions("23",
                          "Which command mode in the Cisco IOS Command Line ends with the > symbol?",
                          "User EXEC Mode",
                          "Privileged EXEC Mode",
                          "Global Configuration Mode",
                          "User EXEC Mode")
question_24 = CtiQuestions("24",
                          "Which is the following is NOT a limitation of IPv4?",
                          "IPv4 Address Depletion",
                          "Lack of end-to-end-connectivity",
                          "Slower speeds",
                          "Slower speeds")
question_25 = CtiQuestions("25",
                          "What is ARP used to acquire?",
                          "Destination IP Address",
                          "Destination MAC Address",
                          "Source MAC Address",
                          "Destination MAC Address")


question_list = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10, question_11, question_12, question_13, question_14, question_15, question_16, question_17, question_18, question_19, question_20, question_21, question_22, question_23, question_24, question_25]




def title(): # title screen code Nuno
    global help_file
    selections = "> Start\n  Help\n  Quit"
    os.system("cls")
    while True: # constantly checks for keyboard interaction and changes variables accordingly
        title_screen = f"""
{art_dimension.draw_title(selections)}
"""


        print(title_screen)
        print('\033[100A\033[2K',end='')
        time.sleep(.1)
        if keyboard.is_pressed("down") and selections == "> Start\n  Help\n  Quit":
            selections = "  Start\n> Help\n  Quit"
            continue
        elif keyboard.is_pressed("down") and selections == "  Start\n> Help\n  Quit":
            selections = "  Start\n  Help\n> Quit"
            continue
        elif keyboard.is_pressed("up") and selections == "  Start\n> Help\n  Quit":
            selections = "> Start\n  Help\n  Quit"
            continue
        elif keyboard.is_pressed("up") and selections == "  Start\n  Help\n> Quit":
            selections = "  Start\n> Help\n  Quit"
            continue
        elif keyboard.is_pressed("shift") and selections == "> Start\n  Help\n  Quit":
            os.system("cls")
            character_select()
            break
        elif keyboard.is_pressed("shift") and selections == "  Start\n> Help\n  Quit":
            os.system("cls")
            print(help_file)
            keyboard.wait("shift")
            os.system("cls")
            main()
        elif keyboard.is_pressed("shift") and selections == "  Start\n  Help\n> Quit":
            os.system("cls")
            print("Thank you for playing")
            exit()




def game_over():  # screen that shows up after game ends Nuno
    os.system("cls")
    global p1_health
    global p2_health
    global player1_name
    global player2_name
    selections = "> Once Again            Quit"
    winner = "None"

    if p1_health <= 0 and p2_health <= 0:
        winner = f"""
Draw
"""
    elif p1_health <= 0:
        winner = f"""
{player2_name} has won
{art_dimension.p2_portrait}
"""
    elif p2_health <= 0:
        winner = f"""
{player1_name} has won
{art_dimension.p1_portrait}
"""

    while True:  # constantly checks for keyboard interaction and changes variables accordingly
        game_over_screen = f"{winner}\n{selections}"
        print(game_over_screen)
        print('\033[100A\033[2K',end='')
        if keyboard.is_pressed("left"):
            selections = "> Once Again            Quit"
            continue
        elif keyboard.is_pressed("right"):
            selections = "  Once Again          > Quit"
            continue
        elif keyboard.is_pressed("shift") and selections == "> Once Again            Quit":
            os.system("cls")
            main()
            break
        elif keyboard.is_pressed("shift") and selections == "  Once Again          > Quit":
            os.system("cls")
            print("Thank you for playing")
            exit()




def character_select():  # where player names their character Nuno
    global player1_name
    global player2_name
    while player1_name == "":  # makes sure player 1 name is inputted
        os.system("cls")
        print(art_dimension.p1_portrait)
        player1_name = input("Name: ")
    while player2_name == "":  # makes sure player 2 name is inputted
        os.system("cls")
        print(art_dimension.p2_portrait)
        player2_name = input("Name: ")
    game()




def game():  # the actual gameplay loop includes the printing of the graphics and the quiz feature Nuno and Philip(Wrong answer punishment and know when the wrong answer is inputted)
    os.system("cls")
    global p1_health
    global p2_health
    global player1_name
    global player2_name
    counter = 0  # iterates through question list
    while p1_health > 0 and p2_health > 0:  # the game keeps going as long as both players have hp
        start = time.time()
        p1_can_ans = True
        p2_can_ans = True
        p1_keys = ["a", "s", "d"]
        p2_keys = ["j", "k", "l"]
        while True:
            answers_list = [question_list[counter].answer_1, question_list[counter].answer_2, question_list[counter].answer_3]
            correct_index = answers_list.index(question_list[counter].correct_answer)  # finds the position of the correct answer
            wrong_index = []
            for x in answers_list:  # makes a list of the wrong answers
                wrong_index.append(answers_list.index(x))
            del wrong_index[correct_index]  # deletes the right
            end = time.time()
            print(art_dimension.draw_gameplay(clear=False, p1_name=player1_name, p1_health=p1_health, p2_name=player2_name, p2_health=p2_health, timer=int(20-(end-start)), question_id=question_list[counter].question_id, question_text=question_list[counter].question_text, answer_1=question_list[counter].answer_1, answer_2=question_list[counter].answer_2, answer_3=question_list[counter].answer_3))
            time.sleep(.01)
            print('\033[100A\033[2K',end='')
            
            if keyboard.is_pressed(p1_keys[correct_index]) and p1_can_ans == True:  # checks if player 1 clicked the right button
                art_dimension.animate_slash(winner="player_1", p1_name=player1_name, p1_health=p1_health, p2_name=player2_name, p2_health=p2_health, timer=int(20-(end-start)), question_id=question_list[counter].question_id, question_text=question_list[counter].question_text, answer_1=question_list[counter].answer_1, answer_2=question_list[counter].answer_2, answer_3=question_list[counter].answer_3)
                p2_health -= 10
                break
            elif keyboard.is_pressed(p2_keys[correct_index]) and p2_can_ans == True:  # checks if player 2 clicked the right button
                art_dimension.animate_slash(winner="player_2", p1_name=player1_name, p1_health=p1_health, p2_name=player2_name, p2_health=p2_health, timer=int(20-(end-start)), question_id=question_list[counter].question_id, question_text=question_list[counter].question_text, answer_1=question_list[counter].answer_1, answer_2=question_list[counter].answer_2, answer_3=question_list[counter].answer_3)
                p1_health -= 10
                break
            elif keyboard.is_pressed(p1_keys[wrong_index[0]]) or keyboard.is_pressed(p1_keys[wrong_index[1]]):  
                print(art_dimension.draw_gameplay(clear=False, p1_name=player1_name, p1_health=p1_health, p2_name=player2_name, p2_health=p2_health, timer=int(20-(end-start)), question_id=question_list[counter].question_id, question_text=question_list[counter].question_text, answer_1=question_list[counter].answer_1, answer_2=question_list[counter].answer_2, answer_3=question_list[counter].answer_3))
                print(f"{player1_name} is wrong\n")
                time.sleep(1)
                p1_can_ans = False
                print('\033[100A\033[2K',end='')
                continue
            elif keyboard.is_pressed(p2_keys[wrong_index[0]]) or keyboard.is_pressed(p2_keys[wrong_index[1]]):
                print(art_dimension.draw_gameplay(clear=False, p1_name=player1_name, p1_health=p1_health, p2_name=player2_name, p2_health=p2_health, timer=int(20-(end-start)), question_id=question_list[counter].question_id, question_text=question_list[counter].question_text, answer_1=question_list[counter].answer_1, answer_2=question_list[counter].answer_2, answer_3=question_list[counter].answer_3))
                print(f"{player2_name} is wrong\n")
                time.sleep(1)
                p2_can_ans = False
                print('\033[100A\033[2K',end='')
                continue
            elif p1_can_ans == False and p2_can_ans == False:
                art_dimension.animate_slash(winner="draw", p1_name=player1_name, p1_health=p1_health, p2_name=player2_name, p2_health=p2_health, timer=int(20-(end-start)), question_id=question_list[counter].question_id, question_text=question_list[counter].question_text, answer_1=question_list[counter].answer_1, answer_2=question_list[counter].answer_2, answer_3=question_list[counter].answer_3)
                p1_health -= 10
                p2_health -= 10 
                break
            elif end - start > 20.0:  # times out
                art_dimension.animate_slash(winner="draw", p1_name=player1_name, p1_health=p1_health, p2_name=player2_name, p2_health=p2_health, timer=int(20 - (end - start)), question_id=question_list[counter].question_id, question_text=question_list[counter].question_text, answer_1=question_list[counter].answer_1, answer_2=question_list[counter].answer_2, answer_3=question_list[counter].answer_3)
                p1_health -= 10
                p2_health -= 10
                break

        counter += 1
    game_over()




def main():
    global p1_health
    global p2_health
    global player1_name
    global player2_name
    random.shuffle(question_list)
    player1_name = ""  # resetting
    player2_name = ""
    p1_health = 50
    p2_health = 50
    title()  # title calls the function that starts the game




try:
    main()
except KeyboardInterrupt:
    os.system("cls")
    print("Goodbye")
    exit()
