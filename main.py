# Importing csv and time. csv is for reading the csv story file and time is to delay the game for 2 seconds when it ends.
import csv
import time
# user defined function for loading a game from the main menu
def loadGame():
    # tries to read the number in the saved.txt file and set the rowNum variable to that number to know where to start the game.
    try:
        infile = open("saved.txt", "r")
        txtReader = infile.readline()
        rowNum = int(txtReader)
        infile.close()
        # If it cannot find a file named saved.txt, it will alert the player and set the starting point to the beginning
    except FileNotFoundError:
        print("")
        print("No save file found! Starting New Game.")
        print("")
        rowNum = 0
    return rowNum
# saveGame function for saving the game while in progress
def saveGame(rowNum):
    # writes the rowNum variable to the saved.txt file
    outfile = open("saved.txt", "w")
    rowNum = outfile.write(str(rowNum))
    outfile.close()
    print(">>> Game has been saved!")


# gameStart function for playing our game
def gameStart(rowNum):
    # reads the csv story file and copies it to a 2d list
    infile = open("story.csv","r")
    csvReader = csv.reader(infile)
    storyList = []
    for row in csvReader:
        storyList.append(row)
    infile.close()
    # infinite loop for printing the lines of our story, options and inputs from the player.
    while True:
        try:
            print("")
            # This checks to see if rowNum represents an index outside of the range of the list
            # rowNum is only not 0 if the game has been saved or a game is in process. 
            # If it detects it, it will start the game from the beginning
            if rowNum > len(storyList):
                rowNum = 0
                print("Save file has an unexpected value. Starting a new game")
                print("")
            # uses the rowNum variable passed in from the main function to know which part of the story to print.
            print(storyList[rowNum][0])
            # delays for 2 seconds if the story is finished and then goes back to the title screen.
            if storyList[rowNum][1] == "":
                time.sleep(2)
                break
            print("What do you want to do?")
            print("1 -", storyList[rowNum][1])
            print("2 -", storyList[rowNum][2])
            print("3 - Save Game")
            # option select is a variable that records which option is chosen
            optionSelect = abs(int(input(">")))
            # used if the first option is chosen
            if optionSelect == 1:
                rowNum = int(storyList[rowNum][3]) - 1
            # used if the second option is chosen
            if optionSelect == 2:
                rowNum = int(storyList[rowNum][4]) - 1
            # used if the save option is chosen. Goes to the saveGame function and passes in which row the story is at.
            # it will then save the row in a .txt file
            if optionSelect == 3:
                print("")
                saveGame(rowNum)
                print("")
            # Error trapping for numbers not 1,2 or 3
            if optionSelect >= 4:
                print("")
                print("Please enter either 1 or 2 to choose an option and 3 to save.")
                print("")
            if optionSelect <= 0:
                print("")
                print("Please enter either 1 or 2 to choose an option and 3 to save.")
                print("")
        # Error trapping for non absolute integer values
        except ValueError:
            print("")
            print("Please enter either 1 or 2 to choose an option and 3 to save. Make sure you only enter the number. No spaces, symbols, or letters.")
            print("")


def main():
    # Infinite loop to keep our game running until the user exits the game
    while True:
        try:
            # setting variables and printing the main menu
            rowNum = 0
            mainScreenInput = ""
            print("")
            print("**Text Adventure Game**")
            print("*                     *")
            print("*     1. New Game     *")
            print("*     2. Load Game    *")
            print("*     3. Exit         *")
            print("*                     *")
            print("***********************")
            # collecting which option the user chooses.
            mainScreenInput = abs(int(input(">")))
            # option 1 starts new game
            if mainScreenInput == 1:
                gameStart(rowNum)
                
            # option 2 loads a save file if there is one. 
            if mainScreenInput == 2:
                rowNum = loadGame()
                gameStart(rowNum)
            # option 3 exits the game by breaking the infinite loop
            if mainScreenInput == 3:
                break
            # Error trapping for not 1,2 or 3
            if mainScreenInput >= 4:
                print("")
                print("Please enter either 1 to start a new game, 2 to load a previously saved game or 3 to close the game")
                print("")
            if mainScreenInput <= 0:
                print("")
                print("Please enter either 1 to start a new game, 2 to load a previously saved game or 3 to close the game")
                print("")
        # Error trapping non absolute integers
        except ValueError:
            print("")
            print("That was not 1, 2 or 3. Please enter 1 for a new game, 2 to load a previous game or 3 to exit. Make sure you only enter the number. No spaces, symbols, or letters.")
            print("")


main()