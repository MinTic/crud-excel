from actions import addTask, removeTask, read, updateTask, show
from colors import bcolors
from util import route, actions, printWord

def dialogue():
    end = False

    taskCount = 0
    for i in actions:
        taskCount += 1
        print(f"({taskCount}) {i}")

    todo = str(input(bcolors.OKCYAN +  "\nQue tareas deseas realizar? (Selecciona un numero): " + bcolors.ENDC))
    if todo == "1":
        addTask()
    elif todo == "2":
        removeTask()
    elif todo == "3":
        updateTask()
    elif todo == "4":
        show()
    elif todo == "exit":
        end = True
    else:
        todo = dialogue()

    return end

def main():
    data = read(route)
    printWord("Manejador de Tareas")
    print(f"Actualmente hay {len(data)} tareas registradas en nuestro sistema... \n")

    endIt = dialogue()
    if endIt == False:
        dialogue()

main()
