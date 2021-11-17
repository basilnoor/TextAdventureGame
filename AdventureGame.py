import sys
import time
import os

a = 1.5
b = 0.1

# Monster Ascii
monster_1 = r"""
                                     ,--,  ,.-.
               ,                   \,       '-,-`,'-.' | ._
              /|           \    ,   |\         }  )/  / `-,',
              [ ,          |\  /|   | |        /  \|  |/`  ,`
              | |       ,.`  `,` `, | |  _,...(   (      .',
              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\\
               \  \_\,``,   ` , ,  /  |         )         _,/
                \  '  `  ,_ _`_,-,<._.<        /         /
                 ', `>.,`  `  `   ,., |_      |         /
                   \/`  `,   `   ,`  | /__,.-`    _,   `\\
               -,-..\  _  \  `  /  ,  / `._) _,-\`       \\
                \_,,.) /\    ` /  / ) (-,, ``    ,        |
               ,` )  | \_\       '-`  |  `(               \\
              /  /```(   , --, ,' \   |`<`    ,            |
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
      (-, \           ) \ ('_.-._)/ /,`    /
      | /  `          `/ \\\\ V   V, /`     /
   ,--\(        ,     <_/`\\\\     ||      /
  (   ,``-     \/|         \-A.A-`|     /
 ,>,_ )_,..(    )\          -,,_-`  _--`
(_ \|`   _,/_  /  \_            ,--`
 \( `   <.,../`     `-.._   _,-`
 """


# Functions
def slow_text(start_text, end_text, speed):
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
    print("You look around and calmly you say.")
    time.sleep(a)
    print()
    slow_text(name, f": my name is {name}", b)
    slow_text(name, ": my ship was sunk by some monster....this thing it destroyed everything", b)
    print()
    print("Two paths are revealed:")
    time.sleep(a)
    print()
    print('Path #1: "Please we have to go save my crew! They\'re out there alone!"')
    print('Path #2: "I appreciate you saving me, but when do we reach land?"')
    time.sleep(a)
    print()
    first_path = input("Which path will you choose? (1/2): ")
    if first_path == '1':
        print()
        path_1()
    elif first_path == '2':
        print()
        path_2()
    else:
        print("You did not choose a proper path. As punishment start over.")


def path_1():
    slow_text(name, ": Please we have to go save my crew! They\'re out there alone!", b)
    print()
    print("You look around and realize everyone is laughing.")
    time.sleep(a)
    print("This is serious...why are they laughing!?")
    time.sleep(a)
    print()
    slow_text("Captain FJ: ", "look here matey. Wha's in it fer us? we be pirates after all", b)
    print()
    print("Captain FJ grins and gets closer")
    time.sleep(a)
    print("His breath reeks of alcohol")
    time.sleep(a)
    print("His teeth stained yellow.")
    time.sleep(a)
    print("Yet you understand...he's not to be messed with.")
    time.sleep(a)
    print()
    slow_text(name, ": I...I can lead you to treasure!", b)
    slow_text(name, ": You take me there and the treasure is all yours", b)
    print()
    time.sleep(1)
    path_3()


def path_2():
    slow_text(name, ": I appreciate you saving me, but when do we reach land?", b)
    print()
    print("You look around and realize everyone is laughing.")
    time.sleep(a)
    print()
    slow_text("Captain FJ: ", "Land!! ye hear that lads bucko here wants to go to land", b)
    time.sleep(a)
    print()
    print("Captain FJ grins and gets closer")
    time.sleep(a)
    print()
    slow_text("Captain FJ: ", "ye weren't jus' marooned at sea fer naught...wha' do ye know", b)
    slow_text("Captain FJ: ", "either ye tell me or ye walk the plank!", b)
    time.sleep(a)
    print()
    print("You start to tremble.")
    time.sleep(a)
    print("You can't go back...not to that thing. It'll kill you this time for sure.")
    time.sleep(a)
    print("Take a deep breathe in")
    time.sleep(a)
    slow_text("", "1", a)
    slow_text("", "2", a)
    slow_text("", "3", a)
    slow_text(name, ": Treasure...i can take you there", b)
    slow_text(name, ": but...but if we find my crew we bring them back safe", b)
    print()
    path_3()


def path_3():
    slow_text("Captain FJ: ", "now ye're talkin' me language...show me this map", b)
    time.sleep(a)
    print()
    print("Captain FJ glances at the map.")
    time.sleep(a)
    print("He turns to his parrot Hash.")
    time.sleep(a)
    print("A grin on his face as you see the excitement lit his eyes.")
    time.sleep(a)
    print()
    slow_text("Captain FJ: ", "looks like we got ourselves a big one boys", b)
    slow_text("Captain FJ: ", "Prep the decks, raise the sails...we're gon be rich lads!", b)
    slow_text("Captain FJ: ", f"and you {name}, it's because of yer beauty!", b)
    time.sleep(a)
    print()
    print("Captain FJ begins to laugh as he takes a sip of whiskey.")
    time.sleep(a)
    print("The crewmates begin preparing the ship.")
    time.sleep(a)
    print("Everyone is in high spirits...but are they ready for what's to come?")
    time.sleep(a)
    print("The crewmates begin preparing the ship.")
    time.sleep(2)
    print()
    print()
    slow_text("", "A WEEK LATER", b)
    time.sleep(3)
    print()
    print()
    print("The sky is calm. The ship sailed smoothly.")
    time.sleep(a)
    print("Nevertheless, there's tension in the air.")
    time.sleep(a)
    print("You pray that thing isn't still there.")
    time.sleep(a)
    print()
    slow_text("Captain FJ: ", f"cmon're {name} that's it! We found it!", b)
    slow_text("Captain FJ: ", "Lower the anchors!!", b)
    time.sleep(a)
    print()
    print("The boat begins to shake.")
    time.sleep(a)
    print("Fear.")
    time.sleep(a)
    print("You begin to feel fear.")
    time.sleep(a)
    print("It's here. That thing is still here.")
    time.sleep(a)
    print()
    slow_text(name, ": We have to go back. NOW!", b)
    time.sleep(a)
    print()
    print("Before you could even finish it appears")
    time.sleep(a)
    print(f"The legendary {monster}")
    time.sleep(a)
    print()
    for index in range(25):
        os.system('cls')
        time.sleep(0.05)
        for i in range(index):
            print()
        print(monster_1)
        time.sleep(0.05)
    for index in range(25, 0, -1):
        os.system('cls')
        time.sleep(0.05)
        for i in range(index):
            print()
        print(monster_1)
        time.sleep(0.05)
    time.sleep(5)
    print()
    slow_text("Captain FJ: ", "What the FUCK is that!", b)
    print()
    time.sleep(2)
    print("Two paths are revealed:")
    time.sleep(a)
    print()
    print('Path #1: Attack the monster!')
    print('Path #2: Run away!')
    print()
    second_path = input("Which path will you choose? (1/2): ")
    if second_path == '1':
        print()
        path_4()
    elif second_path == '2':
        print()
        path_5()
    else:
        print("You did not choose a proper path. As punishment start over.")


def path_4():
    print()
    print("Without hesitation you look around.")
    time.sleep(a)
    print(f"You see a {weapon}!")
    time.sleep(a)
    print("PERFECT!")
    time.sleep(a)
    print(f"You charge towards the {monster}")
    time.sleep(a)
    print()
    slow_text(name, f": You're dead {monster}", b)
    print()
    time.sleep(a)
    print(f"You throw the {weapon}. A DIRECT HIT.")
    time.sleep(a)
    print("It did nothing.")
    time.sleep(a)
    print(f"The {monster} SCREAMS")
    time.sleep(a)
    print("The sounds are deafening.")
    time.sleep(a)
    print("You take a step back.")
    time.sleep(a)
    print("You trip and fall.")
    time.sleep(a)
    print("You aren't shivering anymore.")
    time.sleep(2)
    print("You aren't scared.")
    time.sleep(2)
    print("You close your eyes.")
    time.sleep(2)
    os.system('cls')
    path_end()

def path_5():
    print()
    print("Without hesitation you begin to run.")
    time.sleep(a)
    print("You're scared. Tripping over yourself as you head for the life raft.")
    time.sleep(a)
    print()
    slow_text("Captain FJ: ", f"{name.upper()}!!!!!", b)
    slow_text("Captain FJ: ", "WHERE ARE YOU GOING COWARD", b)
    time.sleep(a)
    print("You ignore everything and run.")
    time.sleep(a)
    print("As fast as you've ever ran before")
    time.sleep(a)
    print("You reach the edge.")
    time.sleep(a)
    print("You look up")
    time.sleep(a)
    os.system('cls')
    print(monster_1)
    time.sleep(0.5)
    os.system('cls')
    path_end()

# Ending
def path_end():
    time.sleep(5)
    print()
    print()
    print("     ######################")
    print("     |                    |")
    print("     |       The End      |")
    print("     |                    |")
    print("     ######################")
    print()
    print()
    print("     Author: Basil Noor")
    time.sleep(10)
    print()


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
    time.sleep(3)
elif startGame == "y" or startGame == "Y":
    name = input("What is your name?: ")
    weapon = input("Choose any weapon of choice (any object): ")
    monster = input("Funniest word you can think of: ")
    intro()
else:
    print("You did not choose a proper path. As punishment start over.")
