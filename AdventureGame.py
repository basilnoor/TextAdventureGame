# Author: Basil Noor

import sys
import time
import os

a = 1.5
b = 0.05

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


def text_time(text, speed):
    print(text)
    time.sleep(speed)


def intro():
    print()
    text_time("(Let our story begin!)", 2)
    print()
    slow_text("Date: ", "July 23rd 1720", b)
    time.sleep(a)
    print()
    text_time("(EVERYTHING IS DARK)", a)
    text_time("You feel around, using your hands to see.", a)
    text_time("The ground is cold, hard, and you hear footsteps.", a)
    text_time("The footsteps get closer.", a)
    text_time("You feel around and pick up a rock. Preparing yourself for whoever is approaching.", a)
    text_time("A loud THUD.", a)
    text_time("Light begins flooding in.", a)
    print()
    slow_text("Captain FJ: ", "Ahoy!!", b)
    slow_text("Captain FJ: ", "Look who\'s up", b)
    print()
    time.sleep(a)
    text_time("You look around! You're on a boat!", a)
    print()
    slow_text("Captain FJ: ", "Me bucko don't worry, ye be safe wit' me crew", b)
    slow_text("Captain FJ: ", "Wha's yer name? we found ye marooned at sea", b)
    print()
    text_time("You release the rock. Still confused and on edge.", a)
    print()
    slow_text("Captain FJ: ", "Are ye jus' goin't' sit thar? I dont reckon he talks Hash", b)
    print()
    text_time("You stand up slowly.", a)
    text_time("Reaching around for something to hold you upright.", a)
    text_time("You look around and calmly you say.", a)
    print()
    slow_text(name, f": My name is {name}", b)
    slow_text(name, ": My ship was sunk by some monster....this thing it destroyed everything", b)
    print()
    text_time("Two paths are revealed:", a)
    print()
    print('Path #1: "Please we have to go save my crew! They\'re out there alone!"')
    print('Path #2: "I appreciate you saving me, but when do we reach land?"')
    print()
    first_path = input("Which path will you choose? (1/2): ")
    if first_path == '1':
        print()
        path_1()
    elif first_path == '2':
        print()
        path_2()
    else:
        text_time("You did not choose a proper path. As punishment start over.", 3)


def path_1():
    slow_text(name, ": Please we have to go save my crew! They\'re out there alone!", b)
    print()
    text_time("You look around and realize everyone is laughing.", a)
    text_time("This is serious...why are they laughing!?", a)
    print()
    slow_text("Captain FJ: ", "Look here matey. Wha's in it fer us? we be pirates after all", b)
    print()
    text_time("Captain FJ grins and gets closer.", a)
    text_time("His breath reeks of alcohol.", a)
    text_time("His teeth stained yellow.", a)
    text_time("Yet you understand...he's not to be messed with.", a)
    print()
    slow_text(name, ": I...I can lead you to treasure!", b)
    slow_text(name, ": You take me there and the treasure is all yours", b)
    print()
    time.sleep(1)
    path_3()


def path_2():
    slow_text(name, ": I appreciate you saving me, but when do we reach land?", b)
    print()
    text_time("You look around and realize everyone is laughing.", a)
    print()
    slow_text("Captain FJ: ", "Land!! ye hear that lads bucko here wants to go to land", b)
    time.sleep(a)
    print()
    text_time("Captain FJ grins and gets closer.", a)
    print()
    slow_text("Captain FJ: ", "Ye weren't jus' marooned at sea fer naught...wha' do ye know", b)
    slow_text("Captain FJ: ", "Either ye tell me or ye walk the plank!", b)
    time.sleep(a)
    print()
    text_time("You start to tremble.", a)
    text_time("You can't go back...not to that thing. It'll kill you this time for sure.", a)
    text_time("Take a deep breathe in.", a)
    slow_text("", "1", a)
    slow_text("", "2", 2)
    slow_text("", "3", 2)
    print()
    slow_text(name, ": Treasure...i can take you there", b)
    slow_text(name, ": But...but if we find my crew we bring them back safe", b)
    print()
    path_3()


def path_3():
    slow_text("Captain FJ: ", "Now ye're talkin' me language...show me this map", b)
    time.sleep(a)
    print()
    text_time("Captain FJ glances at the map.", a)
    text_time("He turns to his parrot Hash.", a)
    text_time("A grin on his face as you see the excitement lit his eyes.", a)
    print()
    slow_text("Captain FJ: ", "Looks like we got ourselves a big one boys", b)
    slow_text("Captain FJ: ", "Prep the decks, raise the sails...we're gon be rich lads!", b)
    slow_text("Captain FJ: ", f"And you {name}, it's because of yer beauty!", b)
    time.sleep(a)
    print()
    text_time("Captain FJ begins to laugh as he takes a sip of whiskey.", a)
    text_time("The crew mates begin preparing the ship.", a)
    text_time("Everyone is in high spirits...but are they ready for what's to come?", a)
    text_time("The crew mates begin preparing the ship.", 3)
    print()
    os.system('cls')
    slow_text("", "A WEEK LATER", b)
    time.sleep(3)
    print()
    print()
    text_time("The sky is calm. The ship sailed smoothly.", a)
    text_time("Nevertheless, there's tension in the air.", a)
    text_time("You pray that thing isn't still there.", a)
    print()
    slow_text("Captain FJ: ", f"Com'er {name} that's it! We found it!", b)
    slow_text("Captain FJ: ", "Lower the anchors!!", b)
    time.sleep(a)
    print()
    text_time("The boat begins to shake.", a)
    text_time("Fear.", a)
    text_time("You begin to feel fear.", a)
    text_time("It's here. That thing is still here.", a)
    print()
    slow_text(name, ": We have to go back. NOW!", b)
    time.sleep(a)
    print()
    text_time("Before you could even finish it appears.", a)
    text_time(f"The legendary {monster}.", 2)
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
    time.sleep(2)
    print()
    slow_text("Captain FJ: ", "What in the Davy Jones' locker!!", b)
    print()
    time.sleep(2)
    print("Two paths are revealed:")
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
        text_time("You did not choose a proper path. As punishment start over.", 3)


def path_4():
    print()
    text_time("Without hesitation you look around.", a)
    text_time(f"You see a {weapon}!", a)
    text_time("PERFECT!", a)
    text_time(f"You charge towards the {monster}.", a)
    print()
    slow_text(name, f": You're dead {monster}", b)
    print()
    time.sleep(a)
    text_time(f"You throw the {weapon}. A DIRECT HIT.", a)
    text_time("It did nothing. Not even a scratch", a)
    text_time(f"The {monster} SCREAMS.", a)
    text_time("The sounds are deafening and your ears start ringing.", a)
    text_time("You take a step back.", a)
    text_time("Off balance you trip and fall.", a)
    text_time("For some reason you aren't shivering anymore.", 2)
    text_time("As you lay there you aren't scared.", 2)
    text_time("You take a deep breath and close your eyes.", a)
    time.sleep(2)
    os.system('cls')
    path_end()


def path_5():
    print()
    text_time("Without hesitation you begin to run.", a)
    text_time("You're scared. Tripping over yourself as you head for the life raft.", a)
    print()
    slow_text("Captain FJ: ", f"{name.upper()}!!!!!", b)
    slow_text("Captain FJ: ", "WHERE ARE YOU GOING COWARD", b)
    time.sleep(a)
    print()
    text_time("You ignore everything and run.", a)
    text_time("As fast as you've ever ran before.", a)
    text_time("You reach the edge of the boat.", a)
    text_time("You look up and...", 2)
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
    text_time("Tragic, maybe later!", 3)
elif startGame == "y" or startGame == "Y":
    name = input("What is your name?: ")
    weapon = input("Choose any weapon of choice (any object): ")
    monster = input("Funniest word you can think of: ")
    intro()
else:
    text_time("You did not choose a proper path. As punishment start over.", 3)
