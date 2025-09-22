# Esther Li
# I pledge my honor that I have abided by the Stevens Honor System.
# CS 115

def get_user_input():
    """ Takes user input and returns it."""

    print("Type in your action and press <Enter>: ")
    
    return input();
  

def checkMoves(a, b, c, mouse_, liquid_, moves, started):
    """Also checks the amounts of moves the user made to trigger a bad ending."""
    
    if( ((moves > 10) and liquid_) or (moves>20)):
        print("You've taken too long.")
        print("Thirst and hunger overtakes you.")
        print("As you feel your consciousness take you, you feel that you could do better...")
        print("...If only you had a second chance...")
        print("Better luck next time!")
        print("BAD ENDING")
        print("\n\nPlay again..?")
        moves = 0
        print_choices("Yes", "No", "Quit Game")
        choiceFin = get_user_input()
        if (choiceFin == "a"):
            my_story()
        else:
            quit()
        
    else:
        print_choices(a,b,c)

def print_choices(a,b,c):
    """Prints choices for the user"""
    print("a) " + a)
    print("b) " + b)
    print("c) " + c)

def checkvariables():
    return mouse_, liquid_, moves, started
    
def homeBase(mouse_, liquid_, moves, started):
    """Plays the first scene the user can encounter."""

    if (not started):
        print("\n\n")
        print("You wake up in a dungeon. You have a pounding headache and your throat is dry.")
        print("It's cold yet extremely humid. You spot something glowing from the corner of your eye")
    
    started = True
    checkMoves("Go back to sleep", "Investigate the glow", "Look for a way out", mouse_, liquid_, moves, started)
    choiceA = get_user_input()
    moves = moves + 1
    if(choiceA == "a"):
        print("You fall in the warm embrace of slumber.")
        print("As your sleep progresses, you feel it getting colder and colder, more and more humid...")
        print("You wake up to your bedroom, the blankets are on the floor, and your cat is sitting on your chest.")
        print("Your cat gives your face another lick before gracefully jumping off, leaving you in your cold, blanket-less bed.")
        print("NEUTRAL ENDING")
        print("\n\nPlay again..?")
        print_choices("Yes", "No", "Quit Game")
        choiceFin = get_user_input()
        if (choiceFin == "a"):
            my_story()
        else:
            quit()
        
    elif(choiceA == "b"):
        print("\n\n")
        print("The source of the glow turns out to be a shallow puddle of liquid")
        print("Nearby, you see an unconscious mouse. Its breathing is shallow.")
        print("You think you can spot a slight glow eminating from its stomach.")
        glow(mouse_, liquid_, moves, started)
        
    else:
        print("\n\n")
        print("Almost blending into the walls, you see a door")
        print("It's seemingly made of steel and covered in dust")     
        door(mouse_, liquid_, moves, started)



def glow(mouse_, liquid_, moves, started):
    """Plays the scene that happens if the user decides to investigate the glow"""
    checkMoves("Investigate the liquid", "Save the mouse", "Do something else", mouse_, liquid_, moves, started)

    choiceB = get_user_input()
    moves = moves + 1
    if(choiceB == "a"):
        liquid(mouse_, liquid_, moves, started)
    elif(choiceB == "b"):
        mouse(mouse_, liquid_, moves, started)
    else:
        homeBase(mouse_, liquid_, moves, started)

def liquid(mouse_, liquid_, moves, started):
    """Plays the scene that happens if the user decides to examine the liquid.
    Just adds a move if only one gulp of liquid is drunk, but doubles the amount of moves made if more is drunk later"""
    
    print("\n\n")
    print("The liquid emits a soft glow.")
    print("Despite the appealing appearance of the liquid, the surrounding area is filled with dirt and grime")
    print("Drink the liquid?")

    checkMoves("Yes", "No", "Leave", mouse_, liquid_, moves, started)

    choiceC = get_user_input()
    moves = moves + 1
    if(choiceC == "a" and not liquid_):
        moves = moves + 1
        liquid_ = True
        print("The liquid doesn't taste like much of anything.")
        print("You feel mildly more thirsty now, but you feel as if you have made more progress")
    elif (choiceC == "a"):
        moves = moves * 2
        print("You take another gulp of the liquid. You feel rapidly more thirsty than before.")
              
    glow(mouse_, liquid_, moves, started)
    
def mouse(mouse_, liquid_, moves, started):
    """Plays the scene that happens if the user decides to save the mouse"""
    if(not mouse_):
        print("\n\n")
        print("You pick up the mouse and determine that it's the liquid that's causing the asphyxiation")
        print("You start doing mouse CPR, and before you know it...")
        print("The mouse lets out a splutter, and lets out a cough as the liquid leaves its system")
        print("The mouse gets up in your hand and looks up at you gratefully")
        print("You give it a pet, and the mouse moves to perch on your shoulder")
        print("Congrats! You have made a friend")

        mouse_ = True
    else:
        print("You have already saved the mouse.")

    glow(mouse_, liquid_, moves, started)

def door(mouse_, liquid_, moves, started):
    """Plays the scene that happens if the user decides to look for the exit"""
    if(mouse_):
        print("You reach your hand to touch the handle, but before you could turn it...")
        print("The mouse races down your arm, down to the floor, and disappears under a slit under the door")
        print("A moment later, the door swings open, with the mouse looking up at you expectantly from the other side")
        print("Somehow, you can tell that it feels very proud of itself")
        print("\n\nCongrats! You have reached the good ending. But since you saved the mouse, I would be compelled to say that you have reached the BEST ending")
        print("As such, I will congratulate you again")
        print("Congratulations!")
        print("BEST ENDING (Don't tell the good ending I said that...)")
        print("\n\nPlay again..?")
        print_choices("Yes", "No", "Quit Game")
        choiceFin = get_user_input()
        if (choiceFin == "a"):
            my_story()
        else:
            quit()
    else:
        checkMoves("Try the handle", "Try breaking through the door", "Knock politely", mouse_, liquid_, moves, started)
        choiceD = get_user_input()
        moves = moves + 1
        if(choiceD == "a"):
            print("You jiggle the handle up and down and try both pulling and pushing.")
            print("Unfortunately, your efforts end to no avail.")
            print("Whether it's jammed or locked is unclear, but trying the handle seems to be the wrong approach.")
            door(mouse_, liquid_, moves, started)
        if(choiceD == "b"):
            print("You jam your shoulder harshly against the unforgiving metal")
            print("Your shoulder hurts now")
            moves = moves + 1 #You lose a turn if this option is chosen
            door(mouse_, liquid_, moves, started)
        if(choiceD == "c"):
            print("You give the door two precise raps; Neither too quiet nor too loud, neither too little nor too much")
            print("Just the right amount in a polite society")
            print("Just as you expected, the door opens politely after a short pause")
            print("Beyond the door, you don't see anybody or anything.")
            print("You introduce yourself nevertheless. It's the polite thing to do, after all.")
            print("\n\nCongratulations! You have successfully escaped the dungeon.")
            print("As such, you have reached an ending")
            print("But not any ending-- you have reached the:")
            print("GOOD ENDING")
            print("\n\nPlay again..?")
            print_choices("Yes", "No", "Quit Game")
            choiceFin = get_user_input()
            if (choiceFin == "a"):
                my_story()
            else:
                quit()
            

        
def my_story():
    homeBase(False, False, 0, False)





