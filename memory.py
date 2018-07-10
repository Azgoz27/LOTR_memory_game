#####################################
#THE LORD OF THE RINGS - MEMORY GAME#
#   created by Tomislav Stančerić   #
#####################################

from gameBoard import *
from gameMusic import *

# These are default attributes that will be used for the program. They're
# passed to the "gameBoard" class and can be changed in the future if so desired
NUM_PAIRS = 9 # total num of possible matching pairs at any given time


def main():
    # variable and class declarations which are used in main
    inGame = False
    numGuesses = 0
    numPairs = 0
    SELECTION_ONE = None
    SELECTION_TWO = None
    mouseX = 0
    mouseY = 0
    boxx = None
    boxy = None
    clock = pygame.time
    game_Board = GameBoard()
    game_Music = Music("intro.wav","inGame.ogg","card.ogg",
        "pair.ogg","win.ogg","gameOver.ogg","noPair.ogg","helpMusic.ogg")

    # pre initialize the screen size and game board
    os.environ["SDL_VIDEO_CENTERED"] = '1' # place screen in the middle of monitor
    game_Board.InitializeScreenSize()
    game_Board.SetGameTitle()
    game_Board.InitializeGameData()
    game_Board.RandomizeGamePieces()
    game_Board.DisplayStartScreen()

    # start the intro music
    game_Music.PlayIntro()

    # this displays the initial START MENU to the screen
    while(not inGame):
        inGame = game_Board.DisplayStartScreen()
        clock.wait(100)

    # stop the intro music
    game_Music.StopIntro()

    # this is the main game loop which is the START OF THE GAME
    while(inGame):
        mouseClicked = False
        game_Board.DisplayIngameBackground(numGuesses, numPairs)
        #pygame.display.flip()

        game_Music.PlayInGame()


        if(numPairs < NUM_PAIRS):

            if(game_Board.NumPairs() < 1):
                print("NO MATCHES!")#######################
                game_Board.DisplayGameBoard()
                pygame.display.update()

            elif(game_Board.NumPairs() > 0):
                game_Board.DisplayGameBoard()
                pygame.display.update()

                if((SELECTION_ONE != None) and (SELECTION_TWO != None)):
                    print(SELECTION_ONE, SELECTION_TWO)
                    clock.wait(1000)

                    for event in pygame.event.get():
                        if(event.type == MOUSEBUTTONUP):
                            continue

                    if(game_Board.isPair(SELECTION_ONE,SELECTION_TWO)):
                        numPairs += 1
                        game_Music.PlayPairSoundFX()

                    else:
                        game_Music.PlayNoPairSoundFX()
                        game_Board.RemoveSelection()
                        game_Board.RemoveSelection()
                    SELECTION_ONE = None
                    SELECTION_TWO = None

             # GET MOUSE EVENTS
            for event in pygame.event.get():  # event handling loop
                if ((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    print("EXITING..")
                    inGame = False

             # get mouse motions
                elif (event.type == MOUSEMOTION):
                    mouseX, mouseY = event.pos
                    # print("x = ",mouseX," y = ",mouseY)

                # get mouse clicks
                elif (event.type == MOUSEBUTTONUP):
                    mouseX, mouseY = event.pos
                    mouseClicked = True
                    # print("MOUSE CLIKED")
                    # print("x = ",mouseX," y = ",mouseY)

                    # if the user clicks the help icon
                    #if (game_Board.GetSelection(mouseX, mouseY) == "help"):
                    # print("HELP ICON")
                    #    game_Music.PauseInGame()
                    #    game_Music.PlayHelp()
                    #    inGame = game_Board.DisplayHelp()
                    #    game_Music.StopHelp()
                    #    game_Music.ResumeInGame()


        boxx, boxy = game_Board.getBoxAtPixel(mouseX, mouseY)
        if boxx != None and boxy != None:
            if not game_Board.revealedBoxes[boxx][boxy] and mouseClicked:
                game_Board.revealBoxesAnimation(mainBoard, [boxx, boxy])
                game_Board.revealedBoxes[boxx][boxy] = True
                if SELECTION_ONE == None:
                    SELECTION_ONE = (boxx, boxy)
                else:
                    icon11, icon12 = SELECTION_ONE[0], SELECTION_ONE[1]
                    icon21, icon22 = boxx, boxy
                    if icon11 != icon21 or icon12 != icon22:
                        pygame.time.wait(1000)
                        game_Board.coverBoxesAnimation(mainBoard,[SELECTION_ONE[0],SELECTION_ONE[1], (boxx, boxy)])
                        game_Board.revealedBoxes[SELECTION_ONE[0]][SELECTION_ONE[1]] = False
                        game_Board.revealedBoxes[boxx][boxy] = False

                    elif game_Board.hasWon(revealedBoxes):




        # GAME IS OVER display end of game screen to user
        #else:
                        print(numPairs)
                        print(game_Board.NumPairs())
                        print("NUMBER OF GUESSES = ", numGuesses / 2)
                        game_Board.DisplayGameBoard()
                        pygame.display.update()
                        clock.wait(2000)
                        game_Music.StopInGame()
                        #game_Music.PlayWinSoundFX()
                        game_Music.PlayGameOver()
                        inGame = game_Board.GameOver(numGuesses)
                        game_Music.StopGameOver()
                        game_Board.ReInitializeBoard()
                        numGuesses = 0
                        numPairs = 0
        pygame.display.flip()
        clock.wait(100)  # do this so the CPU doesnt work too hard

    # end game if user doesnt want to play again
    # print("\nThanks For Playing!!!")
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



"""
            game_Board.boxx, game_Board.boxy = game_Board.getBoxAtPixel(mousex, mousey)
            if game_Board.boxx != None and boxy != None:
                #The mouse is cureently over a box

                if not revealedBoxes[game_Board.boxx][game_Board.boxy]:
                game_Board.drawHighlightBox(game_Board.boxx, game_Board.boxy)
                if not revealedBoxes[game_Board.boxx][game_Board.boxy] and mouseClicked:
                    revealBoxesAnimation(mainBoard, [(game_Board.boxx, game_Board.boxy)])
                    revealedBoxes[game_Board.boxx][game_Board.boxy] = True # set the box as "revealed"
                    if selection_one == None: # the current box was the first box clicked
                        selection_one = (game_Board.boxx, game_Board.boxy)
                    else:  # the current box was the second box clicked
                      # Check if there is a match between the two icons.
                        selection_two = (game_Board.boxx, game_Board.boxy)

                        if selection_one != selection_two:
                        # Icons don't match. Re-cover up both selections.
                         pygame.time.wait(1000) # 1000 milliseconds = 1 sec
                         coverBoxesAnimation(ainBoard, [(selection_one, selection_two), (boxx, boxy)])


                         pygame.time.wait(2000)

                        # Reset the board
                         mainBoard = getRandomizedBoard()
                         revealedBoxes = generateRevealedBoxesData(False)

                         # Show the fully unrevealed board for a second.
                         drawBoard(mainBoard, revealedBoxes)
                         pygame.display.update()
                         pygame.time.wait(1000)

                        # Replay the start game animation.
                         startGameAnimation(mainBoard)
                    firstSelection = None # reset firstSelection variable
"""


