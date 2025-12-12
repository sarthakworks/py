import os
import pyjokes
import pyttsx3

os.system('cls' if os.name == 'nt' else 'clear')


class TextColors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

engine = pyttsx3.init()
# engine.say(pyjokes.get_joke())
engine.runAndWait()

print(f"{TextColors.WARNING}{pyjokes.get_joke()}{TextColors.ENDC}")

print(f"{TextColors.OKGREEN}{os.listdir('/Users/sarthak/Documents/adobe/personal repo/')}{TextColors.ENDC}")
