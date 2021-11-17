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
    print("(Let our story begin!)")
    time.sleep(2)
    print()
    slow_text("Date: ", "July 23rd 1720", b)
    time.sleep(a)
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
    slow_text("Captain FJ: ", "Me bucko don't worry, ye be safe wit' me crew", b)
    slow_text("Captain FJ: ", "Wha's yer name? we found ye marooned at sea", b)
    print()
    print("You release the rock. Still confused and on edge.")
    time.sleep(a)
    print()
    slow_text("Captain FJ: ", "are ye jus' goin't' sit thar? I dont reckon he talks Hash", b)
    print()
    print("You stand up slowly.")
    time.sleep(a)
    print("Reaching around for something to hold you upright.")
    time.sleep(a)
    print("You look around and calmly you pronounce.")
    time.sleep(a)
    print()
    slow_text(name, f": my name is {name}", b)
    slow_text(name, ": my ship was sunk by some monster....this thing it destroyed everything", b)
    print()
    print("Two paths are revealed:")
    time.sleep(a)
    print()
    print('Path #1: "Please we have to go save my crew! They\'re out there alone!"')
    time.sleep(a)
    print('Path #2: "I appreciate you saving me. When do we reach land?"')
    time.sleep(a)
    print()
    first_path = input("Which path will you choose? (1/2): ")
    if first_path == '1':
        print()
    elif first_path == '2':
        print()
    else:
        print("You did not choose a proper path. As punishment start over.")


# Game Starts
print()
print()
print("     ######################")
print("     |                    |")
print("     |     Lost at Sea    |")
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
    name = input("What is your name?: ")
    weapon = input("Choose any weapon of choice (any object): ")
    ship = input("Funniest word you can think of: ")
    intro()