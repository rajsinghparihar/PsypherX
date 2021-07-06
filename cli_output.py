from __future__ import print_function, unicode_literals
from pyfiglet import Figlet
from colorama import Fore, Style
import clanimate

def outputName(name: str) -> None:
    f = Figlet(font='slant')
    print(Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + f.renderText(name))
    print('PsypherX™')
    print(Style.RESET_ALL)
    

def startLoading(anim: clanimate.Animator) -> None:
    print(Fore.GREEN + Style.BRIGHT , end='')
    anim.start_animation()

def endLoading(anim: clanimate.Animator) -> None:
    anim.end_animation()
    print(Style.RESET_ALL, end='')

def catsay(message: str) -> None:
    space = (len(message)+4)
    upBlock = "  "+"_"*space+"\n "+ "/"+" "*space+"\\ \n |< "
    downBlock = " >|\n \\"+"_"*space+"/\n "
    catStr = "	      \\ \n "+"	       \\    /\\_/\\           ___\n "+"		\\  = o_o =_______    \\ \\ \n "+ "		    __^      __(  \\.__) )\n "+"		(@)<_____>__(_____)____/\n"
    print(Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + upBlock + message + downBlock + catStr + Style.RESET_ALL)

def gotoq2(answers: dict) -> bool:
    check1 = answers['first_question']
    if check1 == 'Secure and Store my Password':
        return True
    return False

questions = [
    {
        'type': 'list',
        'name': 'first_question',
        'message': 'What do you want to do?',
        'choices': [
            'Secure and Store my Password',
            'Show all my Secure Passwords',
            'Exit Application'
        ]
    },
    {
        'type': 'input',
        'name': 'password_raw',
        'message': 'Enter your original password',
        'filter': lambda val: str(val),
        'when': gotoq2
    },
    {
        'type': 'input',
        'name': 'key',
        'message': 'Enter your personalized key',
        'filter': lambda val: str(val),
        'when': gotoq2
    },
    {
        'type': 'input',
        'name': 'platform_used',
        'message': 'Which Platform did you use this password for?',
        'filter': lambda val: str(val),
        'when': gotoq2
    },
]