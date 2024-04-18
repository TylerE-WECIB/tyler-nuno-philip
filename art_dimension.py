import os
import time

# all art here is drawn by tyler manually :)
# all code here is also from tyler

p1_portrait = """PLAYER 1
╔════════════════════════════════╗
║           \\______              ║
║      _--‾‾       ‾‾-_          ║
║   _-‾            ____\\------_  ║
║  /          _-‾‾‾            \\ ║
║  |        -‾                  |║
║-_|                            |║
║  |   /   /__                  |║
║   |  |  |   ‾‾-_   \\          |║
║   | /|  |   \\\\  ‾‾-|---\\ /\\  / ║
║    | | /    0\\\\     //  |  \\/  ║
║_  / \\|/             0  |       ║
║ \\/    \\          _\\   /        ║
║   \\    \\     --_    /          ║
║    ‾--_  \\_________/           ║
╚════════════════════════════════╝"""

# PLAYER 1
# ╔════════════════════════════════╗
# ║           \______              ║
# ║      _--‾‾       ‾‾-_          ║
# ║   _-‾            ____\------_  ║
# ║  /          _-‾‾‾            \ ║
# ║  |        -‾                  |║
# ║-_|                            |║
# ║  |   /   /__                  |║
# ║   |  |  |   ‾‾-_   \          |║
# ║   | /|  |   \\  ‾‾-|---\ /\  / ║
# ║    | | /    0\\     //  |  \/  ║
# ║_  / \|/             0  |       ║
# ║ \/    \          _\   /        ║
# ║   \    \     --_    /          ║
# ║    ‾--_  \_________/           ║
# ╚════════════════════════════════╝



p2_portrait = """PLAYER 2
╔════════════════════════════════╗
║                 _-‾ / \\        ║
║            __--‾---/-|_\\       ║
║      __--‾‾__/    /  |  \\      ║
║ __--‾     /  ----/____|  \\     ║
║‾  --__  /       /     |‾‾‾\\    ║
║-_     / ---___ /      |    \\   ║
║  ‾-_/         /‾‾----_|_____\\  ║
║     ‾-__     /        |      \\ ║
║     | __‾‾--___        |      \\║
║    |   0\\    __‾‾‾‾---_________║
║    |       ‾ 0     |_/         ║
║    \\    /_        /  |         ║
║     \\    _--_   /  __-‾‾‾‾--_  ║
║      \\________/  /‾          \\ ║
╚════════════════════════════════╝"""

# PLAYER 2
# ╔════════════════════════════════╗
# ║                 _-‾ / \        ║
# ║            __--‾---/-|_\       ║
# ║      __--‾‾__/    /  |  \      ║
# ║ __--‾     /  ----/____|  \     ║
# ║‾  --__  /       /     |‾‾‾\    ║
# ║-_     / ---___ /      |    \   ║
# ║  ‾-_/         /‾‾----_|_____\  ║
# ║     ‾-__     /        |      \ ║
# ║     | __‾‾--___        |      \║
# ║    |   0\    __‾‾‾‾---_________║
# ║    |       ‾ 0     |_/         ║
# ║    \    /_        /  |         ║
# ║     \    _--_   /  __-‾‾‾‾--_  ║
# ║      \________/  /‾          \ ║
# ╚════════════════════════════════╝


def draw_title(selections=">Play\nHelp\nQuit"):
    return f"""
_________                                   .__
/   _____/____    _____  __ ______________  |__|                                       _-|_-
\\_____  \\\\__  \\  /     \\|  |  \\_  __ \\__  \\ |  |                                    /\\/    /
/        \\/ __ \\|  Y Y  \\  |  /|  | \\// __ \\|  |                               _____/     _- 
/_______  (____  /__|_|  /____/ |__|  (____  /__|                           _-‾     ‾\\--‾‾
        \\/     \\/      \\/                  \\/                              /   ______ |
_________            .___         .___                                     |/ /__ __| |
\\_   ___ \\  ____   __| _/____   __| _/______  _  ______                     |/\\0| 0 |/
/    \\  \\/ /  _ \\ / __ |/ __ \\ / __ |/  _ \\ \\/ \\/ /     \\                     /\\ ^ _/
\\     \\___(  <_> ) /_/ \\  ___// /_/ (  <_> )     /   |  \\\\               ---‾‾  ‾‾‾ -__
 \\______  /\\____/\\____ |\\___  >____ |\\____/ \\/\\_/|___|  /               /|  | |    / /  ‾|\\
        \\/            \\/    \\/     \\/                 \\/               / |   \\ \\  / /    | \\
                                                                      /  |    \\ \\/ /    /  |
Duel of Destiny: CTI Ultimate Edition & Knuckles                     |   \\     \\ \\/    /    \\
First Strike Second Half Gamma Omicron Tau Upsilon:                  |    |     \\  \\  /      |
"Beat the grass and alert the snake",                               /     |______\\__\\/ \\     |  
"The swing of a sword cannot cut the mist from the sky"             |  ___|__________|  \\     \\
Version 3.12cti                                                     |_- --|           \\  \\___--\\
                                                                    |_-‾ \\             \\ |____-- /  
©2024 Tyler Ellis, Nuno Ribeiro, Philip Thomas                      v \\-‾       /|      \\   \\__//‾-_
                                                                       |       /  |      |     /‾-_ ‾-_
                                                                       |       |  |      |         ‾-_ ‾-_
                                                                      |        | |       |            ‾-_ ‾-_
                                                                      |        | |       |               ‾-_ ‾-_   
                                                                      |        | |       |                  ‾-_ ‾-_       *
                                                                      /       |  |       |                     ‾-_ ‾---___-/
                                                                     /        |  |        |                       ‾---___-‾  
                                                                     |__     _|  /________\\                          
                                                                       |‾‾‾‾|       |   |
                                                                     _-__   |      /     --_
                                                                    =====_-‾       |=====/==|
                                                                    ‾‾‾‾‾
{selections}"""

# Title Screen
# _________                                   .__
# /   _____/____    _____  __ ______________  |__|                                       _-|_-
# \_____  \\__  \  /     \|  |  \_  __ \__  \ |  |                                    /\/    /
# /        \/ __ \|  Y Y  \  |  /|  | \// __ \|  |                               _____/     _-
# /_______  (____  /__|_|  /____/ |__|  (____  /__|                           _-‾     ‾\--‾‾
#         \/     \/      \/                  \/                              /   ______ |
# _________            .___         .___                                     |/ /__ __| |
# \_   ___ \  ____   __| _/____   __| _/______  _  ______                     |/\0| 0 |/
# /    \  \/ /  _ \ / __ |/ __ \ / __ |/  _ \ \/ \/ /     \                     /\ ^ _/
# \     \___(  <_> ) /_/ \  ___// /_/ (  <_> )     /   |  \\               ---‾‾  ‾‾‾ -__
#  \______  /\____/\____ |\___  >____ |\____/ \/\_/|___|  /               /|  | |    / /  ‾|\
#         \/            \/    \/     \/                 \/               / |   \ \  / /    | \
#                                                                       /  |    \ \/ /    /  |
# Duel of Destiny: CTI Ultimate Edition & Knuckles                     |   \     \ \/    /    \
# First Strike Second Half Gamma Omicron Tau Upsilon:                  |    |     \  \  /      |
# "Beat the grass and alert the snake",                               /     |______\__\/ \     |
# "The swing of a sword cannot cut the mist from the sky"             |  ___|__________|  \     \
# Version 3.12cti                                                     |_- --|           \  \___--\
#                                                                     |_-‾ \             \ |____-- /
# ©2024 Tyler Ellis, Nuno Ribeiro, Philip Thomas                      v \-‾       /|      \   \__//‾-_
#                                                                        |       /  |      |     /‾-_ ‾-_
#                                                                        |       |  |      |         ‾-_ ‾-_
#                                                                       |        | |       |            ‾-_ ‾-_
#                                                                       |        | |       |               ‾-_ ‾-_
#                                                                       |        | |       |                  ‾-_ ‾-_       *
#                                                                       /       |  |       |                     ‾-_ ‾---___-/
#                                                                      /        |  |        |                       ‾---___-‾
#                                                                      |__     _|  /________\
#                                                                        |‾‾‾‾|       |   |
#                                                                      _-__   |      /     --_
#                                                                     =====_-‾       |=====/==|
#                                                                     ‾‾‾‾‾
# {selections}


def draw_question(question_id=1, question_text="", answer_1="", answer_2="", answer_3=""):
    return f"""║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║
║  Question {str(question_id)}: {str(question_text)+(" "*(97-len(str(question_id)+str(question_text))))}║
║                                                                                                              ║
║  A/J: {str(answer_1)+(" "*(103-len(str(answer_1))))}║
║  S/K: {str(answer_2)+(" "*(103-len(str(answer_2))))}║
║  D/L: {str(answer_3)+(" "*(103-len(str(answer_3))))}║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"""

# ║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║
# ║  Question 1: The quick brown fox jumps over the lazy dog but also the dog is the wolf guy from NC State?     ║
# ║                                                                                                              ║
# ║  A/J: Goku                                                                                                   ║
# ║  S/K: Vegeta                                                                                                 ║
# ║  D/L: Trunks                                                                                                 ║
# ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝


# ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║  P1 NAME                                                                                            P2 NAME  ║
# ║  ▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐ [20] ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌  ║
# ║                                                                                                              ║
# ║  neutral state                                                                                               ║
# ║                                                                                                              ║
# ║                                                                                                              ║
# ║                                                                                                              ║
# ║         _.                                                                                                   ║
# ║     /     |                                                                                                  ║
# ║   -________\                                                                                                 ║
# ║   | .\  /.|___                                                         other guy lol                         ║
# ║    \__-_ /     ---                                                                                           ║
# ║        /_          \ ---------|                                                                              ║
# ║   \---      /        \-------|                                                                               ║
# ║  ___\ _____            \___                                                                                  ║
# ║ |______     \----------   /                                                                                  ║
# ║          /            \    \                                                                                 ║
# ║     /___|                \___\                                                                               ║
# ║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║

def draw_health(p1_name, p1_health, p2_name, p2_health,timer):
    timer = str(int(timer))
    if len(timer) < 2:
        timer = "0" + timer
    if p1_health > 50:
        p1_health = 50
    if p2_health > 50:
        p2_health = 50

    return f"""╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║  {str(p1_name) + (" "*(106-len((str(p1_name)+str(p2_name))))) + str(p2_name)}  ║
║  {(" "*(50-int(p1_health)))+("▐"*int(p1_health))} [{timer}] {("▌"*(int(p2_health))) + (" "*(50-p2_health))}  ║"""


# ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║  Son Goku asdsaddsadd                                                      Kazuya Mishima King of Iron Fist  ║
# ║                                          ▐▐▐▐▐▐▐▐▐▐ [99] ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌     ║

anim_frames = {"blank":"""║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"neutral":"""║                                                                                                              ║
║                                                                                                 __.          ║
║          __ __-‾/___                                                                         -‾‾---\\         ║
║         /  ‾     <_                                                                      _-‾--/--/-\\_\\       ║
║    _____/_ _______<_                                                                     ‾‾|‾‾‾‾----___\\     ║
║  /    __ \\‾                                                                                |0\\ /0  |         ║
║ |   /‾/0\\_\\__                                                                          _---\\   --  /         ║
║ |/ /0 __ /   ‾-_                                                          _          -‾     \\‾‾‾‾‾ -         ║
║  \\/‾----‾  \\    ‾-_______-------‾‾‾|                                     / -------__ \\       ‾--__ /         ║
║        /    |      \\     _______--/                                     /_____      ‾ \\          ‾‾/--_      ║
║   ___-‾     /      |\\‾‾‾‾                                                     ‾‾‾‾‾--/  \\          /___/     ║
║  __\\_      /_____--  ‾-_                                                            /    ‾--_     /    --_   ║
║  \\  _\\____/ _---__      ‾-_                                                        |       _-‾--‾‾        /  ║
║   ‾‾/     <‾      ‾-_      ‾-_                                                    |      /      ‾‾‾‾/    /   ║
║    \\_______‾>         ‾-_______>_                                              __/___   /         /_____/    ║
║      /______\\             \\______\\                                            /______|‾‾            |____\\   ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"dash1":"""║                                                                                                              ║
║                                                                                         __.  ___________     ║
║     -----------  __ __-‾/___                                                         -‾‾---\\                 ║
║ ______________  /  ‾     <_                                                      _-‾--/--/-\\_\\  __________   ║
║            _____/_ _______<_                                                     ‾‾|‾‾‾‾----___\\             ║
║   ------ /    __ \\‾                                                                |0\\ /0  |     ----------  ║
║ _______ |   /‾/0\\_\\__                                                          _---\\   --  / ------------    ║
║   ----- |/ /0 __ /   ‾-_                                          _          -‾     \\‾‾‾‾‾ -                 ║
║--------- \\/‾----‾  \\    ‾-_______-------‾‾‾|                     / -------__ \\       ‾--__ /  ____________   ║
║    _________   /    |      \\     _______--/                     /_____      ‾ \\          ‾‾/--_              ║
║           ___-‾     /      |\\‾‾‾‾                                     ‾‾‾‾‾--/  \\          /___/ ----------  ║
║ -------  __\\_      /_____--  ‾-_                                            /    ‾--_     /    --_           ║
║ ________ \\  _\\____/ _---__      ‾-_                                        |       _-‾--‾‾        / -------- ║
║  ________ ‾‾/     <‾      ‾-_      ‾-_                                    |      /      ‾‾‾‾/    /           ║
║            \\_______‾>         ‾-_______>_                              __/___   /         /_____/  ------    ║
║    --------  /______\\             \\______\\                            /______|‾‾            |____\\   ______  ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"slash1":"""║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║               ▄▄▄█████▀▀                                                                                     ║
║            ▄████████▀                                                                                        ║
║          ▄████████▀                                                                                          ║
║          ██████▀                                                                                             ║
║           ▀▀▀▀                                                                           ▄▄▄▄▄▄▄▄██          ║
║                                                                                    ▄██████████████▀          ║
║                                                                                  ▄████████████▀▀             ║
║                                                                                                              ║
║                                                                                                              ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"slash2":"""║                                                                                                              ║
║                                         ▄▄▄▄▄▄▄▄▄▄▄▄▄                                                        ║
║                                       ▄██████████████████▄▄▄▄▄                                               ║
║                                       ▀████████████████████████████▄▄▄                                       ║
║                                                       ▀▀▀██████████████████▄▄▄                               ║
║                                                                  ▀▀█████████████▄▄                           ║
║                                                                         ▀▀▀█████████▄                        ║
║                                                                               ▀▀███████▄                     ║
║                                                                                   ▀██████▄                   ║
║                                                                                      ▀█████▄                 ║
║          ▄▄▄                                                                           ▀█████                ║
║         █████████▄▄▄                                           ▄▄▄▄                      ▀████               ║
║          ▀███████████████████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██████                       ▀▀                ║
║                ▀▀█████████████████████████████████████████████████▀                                          ║
║                                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                                              ║
║                                                                                                              ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"slash3":"""║                                        ▄▄▄▄▄▄▄▄▄                                                             ║
║                                   ███████████████████                                                        ║
║                               █████████████████████████▄                                                     ║
║                            ███████████████████████████▀                                                      ║
║                         █████████████████▀▀▀▀▀                                                               ║
║                      █████████████████▀                     ███████████▄▄▄▄▄                                 ║
║                    █████████████████▀                        ███████████████████████████▄▄▄▄                 ║
║                  █████████████████▀                             ▀▀▀▀▀▀▀███████████████████████████▄▄▄        ║
║                ██████████████████                                           ▀▀▀▀▀█████████████████████▄      ║
║               ██████████████████                                                ▄▄▄███████████████████▀      ║
║              ██████████████████                                       ▄▄▄▄▄██████████████████████▀▀▀         ║
║            ███████████████████                             ▄▄▄▄▄▄███████████████████████████▀▀▀              ║
║          ██████████████████▀             ▄▄▄████████████████████████████████████████▀▀▀▀▀                    ║
║          ████████▀▀▀▀▀                 ██████████████████████████████████████▀▀▀▀                            ║
║          ▀▀▀▀▀                                ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                                       ║
║                                                                                                              ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"slash4":"""║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                     ▄▄▄▄▄                                                                                    ║
║                   ▄██▀▀                      ▀▀████████████████████████▄▄▄▄                                  ║
║                 ▄███                             ▀▀▀▀▀▀▀▀█████████████████████▄                              ║
║               ▄███▀                                          ▀▀▀▀▀▀█████████▀▀                               ║
║             ▄████                                                                                            ║
║            █████                                                                                             ║
║          ▄█████                                                                                              ║
║        ▄█████████▄▄▄▄                                                                                        ║
║       ▄█████████████████▀▀                                                                                   ║
║      ███████████▀▀▀                                                                                          ║
║       ▀▀▀▀▀▀▀▀                                                                                               ║
║                                                                                                              ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"dash2":"""║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                              __________        _____________         _____________                           ║
║                                                                                                              ║
║                                   -----------                                                                ║
║                                                          ____________    --------------                      ║
║                                                                                                              ║
║                    --------------             ----------           _________________                         ║
║                                                                                                              ║
║                                                                                                              ║
║            --------------------      ______________            --------------                                ║
║                                                                                                              ║
║                        ------------               ---------------                  -----------               ║
║                                                                                                              ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"final":"""║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                  \\--__                                                       ║
║                                                   \\_  ‾‾---___                    ___>‾‾‾‾‾‾-_  ___          ║
║            /‾--__                                   ‾‾--___   ‾‾‾---__             >          ‾‾   ‾\\        ║
║           /-/ _\\_‾--__         __                          ‾‾‾---__   ‾‾-/__________‾--__---|\\ -___  \\       ║
║          /-/-- ____-‾         / /                                  ‾‾‾--/   \\       ‾‾‾‾‾‾-| |/ 0\\ ‾\\\\       ║
║         /_---‾‾   |          / /                                         ‾‾‾ \\   ____--     ‾--____/         ║
║            \\/0   _/‾‾‾‾‾---_/ /                                               \\-‾    /    _____---\\          ║
║             ----‾     /    / /                                            .----__________|        /          ║
║          __-‾        /    / / ‾-_                                         |___            ‾-_    <--_        ║
║_____| _-‾\\_____      /---/ /     ‾-_                                          ‾‾‾‾‾‾‾‾‾‾‾___ ‾-___|__\\       ║
║_____|/___/ _--‾‾‾‾‾‾ _---‾‾-_       ‾-_                                   _--‾        _-‾   ‾‾>       ‾>     ║
║     |     /_________/        ‾-________‾-_                              _=___________/      /_________/      ║
║            /______|                \\______\\                               /_______\\             |______\\     ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"p1_win":"""║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                  \\--__                                                       ║
║                                                   \\_  ‾‾---___                    ___>‾‾‾‾‾‾-_  ___          ║
║                                                     ‾‾--___   ‾‾‾---__             >        //‾‾   ‾\\        ║
║                                                            ‾‾‾---__   ‾‾-/__________‾--__---|\\ -___  \\       ║
║                                                                    ‾‾‾--/   \\       ‾‾‾‾‾‾-| |/ 0\\ ‾\\\\       ║
║                           __                                             ‾‾‾ \\   ____--     ‾--____/         ║
║                          / /                                                  \\-‾    /    _____---\\          ║
║                         / /                                               .----__________|        /          ║
║      _-‾\\              / /                                                |___            ‾-_    <--_        ║
║   _-‾    \\       _____/ /                                                     ‾‾‾‾‾‾‾‾‾‾‾___ ‾-___|__\\       ║
║  ----------__---=______/‾‾‾‾‾---__                                        _--‾        _-‾   ‾‾>       ‾>     ║
║   /     \\/            /‾‾\\        ‾‾--_                                 _=___________/      /_________/      ║
║   |-----/---------------------------/---->                                /_______\\             |______\\     ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"p2_win":"""║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║            /‾--__                                                                                            ║
║           /-/ _\\_‾--__         __                                                                            ║
║          /-/-- ____-‾         / /                                                                            ║
║         /_---‾‾   |          / /                                                                             ║
║            \\/0   _/‾‾‾‾‾---_/ /                                                 \\‾‾\\        -__  /\\          ║
║             ----‾     /    / /                                                   \\  \\    ___\\  ‾   \\^        ║
║          __-‾        /    / / ‾-_                                                 \\  \\    ‾->        \\       ║
║_____| _-‾\\_____      /---/ /     ‾-_                                               \\  \\  <‾_____      |      ║
║_____|/___/ _--‾‾‾‾‾‾ _---‾‾-_       ‾-_                                     ________\\  \\--------_‾__==_      ║
║     |     /_________/        ‾-________‾-_                         _-‾‾|‾‾‾‾          -------‾‾‾ / \\   \\     ║
║            /______|                \\______\\                       /_____\\____________/_|________|_/_____\\    ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║""",

"draw":"""║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                                                                                                              ║
║                           __                                                                                 ║
║                          / /                                                    \\‾‾\\        -__  /\\          ║
║                         / /                                                      \\  \\    ___\\  ‾   \\^        ║
║      _-‾\\              / /                                                        \\  \\    ‾->        \\       ║
║   _-‾--- \\       _____/ /                                                          \\  \\  <‾_____      |      ║
║  ----------__---=______/‾‾‾‾‾---__                                          ________\\  \\--------_‾__==_      ║
║   /     \\/            /‾‾\\        ‾‾--_                            _-‾‾|‾‾‾‾          -------‾‾‾ / \\   \\     ║
║   |-----/---------------------------/---->                        /_____\\____________/_|________|_/_____\\    ║
║══════════════════════════════════════════════════════════════════════════════════════════════════════════════║"""}

