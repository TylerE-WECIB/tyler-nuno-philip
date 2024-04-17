# The Questions, PythonQuestions, and CtiQuestions classes and the question objects were created by Philip Thomas
class Questions:
    def __init__(self, question_id, question_text, answer_1, answer_2, answer_3, correct_answer):
        self.question_id = question_id  # question_id is used to prevent repeats of questions
        self.question_text = question_text  # question_text stores the question that is being answered
        self.answer_1 = answer_1  # answer_1 is a possible answer to the question
        self.answer_2 = answer_2  # answer_2 is a possible answer to the question
        self.answer_3 = answer_3  # answer_3 is a possible answer to the question
        self.correct_answer = correct_answer  # correct_answer is the correct answer to the question, is equal to one of the answer arguments
        self.question_subject = None  # question_subject stores the question's subject


class PythonQuestions(Questions):
    def __init__(self, question_id, question_text, answer_1, answer_2, answer_3, correct_answer):
        super().__init__(question_id, question_text, answer_1, answer_2, answer_3, correct_answer)
        Questions.question_subject = "Python"


class CtiQuestions(Questions):
    def __init__(self, question_id, question_text, answer_1, answer_2, answer_3, correct_answer):
        super().__init__(question_id, question_text, answer_1, answer_2, answer_3, correct_answer)
        Questions.question_subject = "CTI"


question_1 = CtiQuestions("01",
                          "Which Data Link Sublayer communicates between networking software at the upper layers and device hardware at the lower layers",
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
                          "The Institute of Electrical and Electronics Engineers is the main organization responsible for the creation of what?",
                          "Wireless technical standards",
                          "Wired technical standards",
                          "LAN devices",
                          "Wireless technical standards")
question_10 = CtiQuestions("10",
                           "DHCP should NOT be used to configure the IP address of which of the following devices?",
                           "mobile devices",
                           "desktops",
                           "printers",
                           "printers")
question_11 = CtiQuestions("11",
                           "Which of the following OSI model layers is NOT a part of the Network interface layer of the TCP/IP model?",
                           "Network Layer",
                           "Datalink Layer",
                           "Physical Layer",
                           "Network Layer")
question_12 = CtiQuestions("12",
                           "In what order are messages sent between a host and a DHCP server so that the host can acquire an IPv4 Address?",
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
                           "Which of the following is NOT a migration technique between IPv4 and IPv6",
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
