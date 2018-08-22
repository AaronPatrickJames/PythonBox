#Aaron James
#python projects

import os
import random
import sys
import time
import tkinter
from tkinter import *

def main():
    #main menu of python projects
    #infy loop
    a = 1
    while a != 0:
        #user input pull
        menuSelection = input("Please enter a comand or type H for help: ")
        try:
            menuSelection = str(menuSelection.upper())      
        except Exception as e:
            print("Unsupported menu selection. Please try again. Error 'To Upper'")

        #menu of submenu's / games
        mainMenu = {"R" : RockPaperScissors,
                    "GR" : GRockPaperScissors,
                    "H" : Help,
                    "Q" : Quiter}
        if menuSelection in mainMenu:
            mainMenu[menuSelection]()
        else:
            print("Sorry this command is currently not supported with our system.")
            print("If you believe this to be an error, please contact the system admin")
            
#help for main menu
def Help():
    print("'R' : Rock Paper Scissors")
    print("'GR' : Graphical Rock Paper Scissors")
    print("'H' : Help (You Are Here)")
    print("'Q' : Quit Applcaiton")











def popupmsg(msg):
    popup = Tk()
    popup.geometry("200x120")

    def BackToHome():
        popup.destroy()
        return 0
        
    def KillIt():
        popup.destroy()
        
    popup.wm_title("!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Yes", command = BackToHome)
    B1.pack()
    B2 = Button(popup, text="No", command = KillIt)
    B2.pack()
    popup.mainloop()
    
def GRockPaperScissors():
    class Window(Frame):
        def __init__(self, master = None):
           Frame.__init__(self, master)
           self.master = master
           self.init_window()
        def init_window(self):
            self.master.title("")
            self.pack(fill=BOTH, expand=1)
            #rock
            btnRock = Button(self, text="Rock", command=self.Rock)
            btnRock.place(x=10, y=400)
            btnRock.config(height = 3, width = 40)
            #Paper
            btnPaper = Button(self, text="Paper", command=self.Paper)
            btnPaper.place(x=365, y=400)
            btnPaper.config(height = 3, width = 40)
            #Scissors
            btnScissors = Button(self, text="Scissors", command=self.Scissors)
            btnScissors.place(x=700, y=400)
            btnScissors.config(height = 3, width = 40)
        def Rock(self):
            GInput(1)
        def Paper(self):
            GInput(2)
        def Scissors(self):
            GInput(3)
            
    root = Tk()
    root.geometry('1000x500')
    app = Window(root)
    #imgRock = PhotoImage(file='\\rock.jpg')
    #imgPaper = PhotoImage(file='\Paper.png')
    #imgScissors = PhotoImage(file='\Scissors.jpg')
    #root.create_image(0,0, anchor = NW, image = imgRock)
    root.mainloop()
    
def FinalPopScreen():
    pass




#RockPaper Scissors. (non graphical)
def RockPaperScissors():
    Speach()
    nonGInputs()
    
#Speaking (my own print statement)
def Speaking(Sentence):
    for letter in Sentence:
        print(letter, sep = " ", end='', flush=True)
        time.sleep(.015)
    time.sleep(3)
    print("\n")
    
#Linked with above, this is how the computer talks the the player (in short sentences)            
def Speach():
    firstLine = "Hello, and welcome to RO SHAM BO. Pick your weapon and do battle!"
    secondLine = "The weapons are as follows : "
    thirdLine = "||R = ROCK || P = PAPER || S = Scissors||"
    fourthLine = "You Ready?"
    fifthLine = "LETS GO!"

    Speaking(firstLine)
    Speaking(secondLine)
    Speaking(thirdLine)
    Speaking(fourthLine)
    Speaking(fifthLine)
    
#take player input and pass it to the winner chooser
def Player():
    pWeapon = input("WHAT IS YOUR WEAPON PLAYER? ")
    pWeapon = str(pWeapon.upper())
    weapon = weaponCashe(pWeapon)
    return weapon
    
def Computer():
    return (random.randint(1,3))

#detemine player weapon
def weaponCashe(weapon):
    if weapon == "R":
        return 1
    elif weapon == "P":
        return 2
    elif weapon == "S":
        return 3
    else:
        print("Sorry, " + str(weapon) + " is not a weapon")
        return 4

#gather inputs (Non Graphical)
def nonGInputs():
    pPick = Player()
    cPick = Computer()
    wld = Winner(pPick, cPick)

    value = reverceWeaponFinder(pPick)
    Speaking("You have chosen, " + str(value) + ".")
    value = reverceWeaponFinder(cPick)
    Speaking("The comptuer has chosen, " + str(value) + ".")

    value = win(wld)
    Speaking(value)

    playAgain()

#Gather input (Graphical) output win
def GInput(pClicked):
    pPick = pClicked
    cPick = Computer()
    wld = Winner(pPick, cPick)
    popupmsg("Hello world")

    #popup screen
    pvalue = reverceWeaponFinder(pPick)
    #change lblPWeap to value
    cvalue = reverceWeaponFinder(cPick)
    #change lblCWeap to value

    time.sleep(3)
    #print Image on Screen of Winner, Loser, or Other.

    playAgain()

#win screen for non graphical
def win(value):
    if value == 1:
        return " |\\\\\\\\\\\\***///////| \n |  YOU HAVE WON  | \n |\\\\\\\\\\\\***///////|"
    elif value == 2:
        return " |\\\\\\\\\\\\***///////| \n |  YOU ARE LOSER | \n |\\\\\\\\\\\\***///////|"
    else:
        return " |\\\\\\\\\\\\***///////| \n |  IT IS A DRAW  | \n |\\\\\\\\\\\\***///////|" 
#find weapon from number (reverce of weapon form letter)             
def reverceWeaponFinder(value):
    if value == 1:
        return "Rock"
    elif value == 2:
        return "Paper"
    else:
        return "Scissors"
    
#Checkes Winner ------> runs check for exit
def Winner(pChoice, cChoice):
    if pChoice == 1:
        if cChoice == 2:
            return 2
        elif cChoice == 3:
            return 1            
        else:
            return 3
    elif pChoice == 2:
        if cChoice == 1:
            return 1
        elif cChoice == 3:
            return 2
        else:
            return 3
    elif pChoice == 3:
        if cChoice == 2:
            return 1
        elif cChoice == 1:
            return 2
        else:
            return 3
    else:
        print("Quit trying to break the game. Cheater.")
    playAgain()
    
def playAgain():
    print("Would you like to play again?")
    playing = input("Enter N to Quit this game: ")
    try:
        playing = playing.upper()
    except:
        pass
    if playing == "N":
        main()
    else:
        nonGInputs()




#quit application with error code 0
def Quiter():
    sys.exit(0)
    
main()
