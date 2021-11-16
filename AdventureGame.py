import sys
import time

a = 1.5
b = 0.1
c = 0.05

# Functions
def slow_text(start_text,end_text, speed):
    print(start_text, end="")
    for character in end_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def intro():
    print()
    print("(EVERYTHING IS DARK)")
    time.sleep(a)
    print("You feel around, using your hands to see.")
    time.sleep(a)
    print("The ground is cold, hard, and you hear footsteps.")
    time.sleep(a)
    print("The footsteps get closer.")
    time.sleep(a)
    print("You feel around and pick up a rock. Preparing yourself for whoever is approaching.")
    time.sleep(a)
    print("A loud THUD.")
    time.sleep(a)
    print("Light begins flooding in.")
    time.sleep(a)
    print()
    slow_text("Captain FJ: ", "Ahoy!!", b)
    slow_text("Captain FJ: ", "Look who\'s up", b)
    print()
    time.sleep(1.0)
    print("You look around! You're on a boat!")
    time.sleep(a)
    print()
    slow_text("Captain FJ: ", "My friend not to worry. You are safe with me crew", b)
    print()
    print("You release the rock. Still confused and on edge")
    time.sleep(a)
    print()
    slow_text("Captain FJ: ", "My friend not to worry. You are safe with me crew", b)
    print()
    print("Two paths are revealed:")
    time.sleep(a)
    print()
    print('Path #1: "My name is Oregano, How did i get here? Do you know who i AM!"')
    time.sleep(a)
    print('Path #2: "Call me Oregano. who are you? why am i here"')
    time.sleep(a)
    print()
    firstPath = input("Which path will you choose? (1/2): ")
    if firstPath == '1':
        print()
    elif firstPath == '2':
        print()
    else:
        print("You did not choose a proper path. As punishment start over.")


# Game Starts
print()
print()
print("     ######################")
print("     |                    |")
print("     |   Rich or poor   |")
print("     |                    |")
print("     ######################")
print()
print()
time.sleep(1)
print()
startGame = input("Welcome! Are you ready to begin this adventure? (Y/N): ")
if startGame == "n" or startGame == "N":
    print("Tragic, maybe later!")
elif startGame == "y" or startGame == "Y":
    intro()