import os
import time

# all art here is drawn by tyler manually :)

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


# ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
# ║  P1 NAME                                                                                            P2 NAME  ║
# ║  ▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐▐ [20] ▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌▌  ║
# ║                                                                                                              ║
# ║                                                                                                              ║
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

def draw_question(question_id=1, question_text="", answer_1="", answer_2="", answer_3=""):
    if len(question_text) > 78:
        if question_text[78] != " ":
            question_text = f"{question_text[1:78]}-\n{question_text[78:]}"
        else:
            question_text = f"{question_text[1:78]}\n{question_text[78:]}"
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