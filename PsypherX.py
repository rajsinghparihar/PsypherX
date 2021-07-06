from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from examples import custom_style_2
from colorama import Fore, Style
import clanimate
import encrypt
import cli_output
import store
import tabulate
import time
import sys

fun_called_once = True
def main():
    # can't have global animator objects because of bugs in animating the second iteration
    # to deal with this each time we call the function, a new animator is created.
    loadingAnim = clanimate.Animator('scroll_text', 10, name = " => PsypherX is Encrypting Your Passwords using AES Encryption", animation_frames="::::::::::::")
    endingAnim = clanimate.Animator('scroll_text', 10, name = " => Exiting PsypherX", animation_frames="::::::::::::")

    # printing cool name/logo figlet text
    if(fun_called_once):
        cli_output.outputName("PsypherX")

    #Styling and colors
    print(Fore.CYAN + Style.BRIGHT,end='')

    # displaying answers
    answers = prompt(cli_output.questions, style=custom_style_2)
    
    # getting pass and key from options
    password_raw = answers.get("password_raw")
    key = answers.get("key")

    # logic
    if answers.get("first_question") == "Secure and Store my Password":
        cli_output.startLoading(loadingAnim)
        encoded = encrypt.Enc(password_raw, key)
        store.store_data(encoded,key,answers.get("platform_used"))
        time.sleep(3)
        try:
            cli_output.endLoading(loadingAnim)
        except:
            sys.exit()
        cli_output.catsay("Password Secured and Stored meow!")

    elif answers.get("first_question") == "Show all my Secure Passwords":
        if(store.data == [["PASSWORD","KEY","PLATFORM USED"]]):
            cli_output.catsay("You haven't secured any passwords yet meow!")
        else:
            print(Fore.GREEN + Style.BRIGHT, end='') # different styling
            headers = ["PASSWORDS","KEYS","PLATFORMS"]
            table = store.data
            print("\n")
            print(tabulate.tabulate(table[1:],headers,tablefmt="presto"))
            print("\n")

    elif answers.get("first_question") == "Exit Application":
        cli_output.catsay("Have a nice day meow!")
        cli_output.startLoading(endingAnim)
        time.sleep(3)
        cli_output.endLoading(endingAnim)
        store.saveToCSV()
        exit()

# the program runs indefinately until you explitly select the exit application option.
while True:
    main()
    fun_called_once = True