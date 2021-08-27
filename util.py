from pyfiglet import Figlet
from colors import bcolors

route = r"C:\Users\Eliana Rudas\Desktop\crud\db\tasks.xlsx"
actions = ["Agregar tarea", "Eliminar tarea", "Actualizar tarea"]

def printWord(word: str):
    f = Figlet(font='slant')
    curr_word = ''
    for char in word:
        curr_word += char

    print(bcolors.BOLD + bcolors.OKBLUE + f.renderText(curr_word) + bcolors.ENDC)