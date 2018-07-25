#####################################
#THE LORD OF THE RINGS - MEMORY GAME#
#   created by Tomislav Stančerić   #
#####################################
# imports
from game_board import *
from game_music import *

# constants
NUM_PAIRS = 14  # number of total pairs in the game
NUM_PICS = 28   # number of different images available to load

#main function
def main():
    # variable and class declarations which are used in main function
    game_run = False        # determines when game mechanics are active or not
    number_of_guesses = 0   # counts number of guesses during gameplay, just for flavor
    number_of_pairs = 0     # counts the number of pairs to achieve victory conditions
    SELECTION_ONE = -1      # stores the value of the first clicked card
    SELECTION_TWO = -1      # stores the value of the second clicked card
    clock = pygame.time
    game_board = gameboard()
    game_music = Music("intro.ogg", "inGame.ogg", "card.ogg", "pair.ogg", "gameOver.ogg")


    # pre initialize the screen size and game board
    os.environ["SDL_VIDEO_CENTERED"] = '1'      # place screen in the middle of monitor
    game_board.initialize_screen_size()         # initialize the screen size
    game_board.set_game_title()                 # set screen caption
    game_board.initialize_game_data(NUM_PICS)   # loads images, fonts, backgrounds
    game_board.randomize_cards()                # randomizes the cards
    game_board.display_start_screen()           # displays the start screen
    game_music.play_intro()                     # start the intro music

    # starting the initial "start screen"
    while(not game_run):
        game_run = game_board.display_start_screen()

    # when exiting the start screen, stop the intro music
    game_music.stop_intro()

    # this is the main game loop when after the start screen
    while(game_run):
        game_board.display_ingame_background(number_of_guesses, number_of_pairs)    #displays the ingame background
        game_music.play_in_game()                                                   #running in-game music

        # setting the victory conditions
        # game starts with 0 number_of_pars and needs to reach the NUM_PAIRS value to finish the game
        if(number_of_pairs < NUM_PAIRS):

            # if no pairs have been solved so far, display the gameboard
            if(game_board.number_of_pairs() < 1):
                game_board.display_game_board()
                pygame.display.update()

            # if some pairs have been found, display the gameboard
            elif(game_board.number_of_pairs() > 0):
                game_board.display_game_board()
                pygame.display.update()

                # if both cards have been clicked on, wait 1 second
                if((SELECTION_ONE > -1) and (SELECTION_TWO > -1)):
                    clock.wait(1000)
                    # check mousebutton press
                    for event in pygame.event.get():
                        if(event.type == MOUSEBUTTONUP):
                            continue

                    # if both cards match, add 1 to the number of pairs found, play the sound
                    if game_board.game_pieces[SELECTION_ONE] == game_board.game_pieces[SELECTION_TWO]:
                        number_of_pairs += 1
                        game_music.play_pair_soundFX()

                    # if not a match, remove values added to the mouseclicks
                    else:
                        game_music.play_no_pair_soundFX()
                        game_board.remove_selection()
                        game_board.remove_selection()
                    SELECTION_ONE = -1
                    SELECTION_TWO = -1

             # mouse events
            for event in pygame.event.get():
                if ((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    game_run = False

             # mouse motions
                elif (event.type == MOUSEMOTION):
                    mouseX, mouseY = event.pos

                # mouse clicks
                elif (event.type == MOUSEBUTTONUP):
                    mouseX, mouseY = event.pos

                    # if the restart button is clicked, restart the gameboard and victory conditions
                    if (game_board.get_selection(mouseX, mouseY) == "restart"):
                        game_board.reinitialize_board()
                        number_of_guesses = 0
                        number_of_pairs = 0

                    # return value for the first card clicked, if the value is other than -1, value is stored
                    elif ((number_of_guesses % 2) == 0):
                        SELECTION_ONE = game_board.get_selection(mouseX, mouseY)
                        if (SELECTION_ONE > -1):
                            game_music.play_card_soundFX()
                            game_board.append_selection(SELECTION_ONE)
                            number_of_guesses += 1

                    # return value for the second card clicked, if other than -1, value is stored
                    else:
                        SELECTION_TWO = game_board.get_selection(mouseX, mouseY)
                        if (SELECTION_TWO > -1):
                            game_music.play_card_soundFX()
                            game_board.append_selection(SELECTION_TWO)
                            number_of_guesses += 1

        # if the victory condition have been met, display game over screen
        else:
            print(game_board.number_of_pairs())
            print("NUMBER OF GUESSES = ", number_of_guesses / 2)
            game_board.display_game_board()
            pygame.display.update()
            clock.wait(2000)  # to avoid accidental clicks
            game_music.stop_in_game()
            game_music.play_game_over()
            game_run = game_board.game_over(number_of_guesses)
            game_music.stop_game_over()
            game_board.reinitialize_board()
            number_of_guesses = 0
            number_of_pairs = 0
    pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



#alternative card selection mechanics to avoid hard coding, not yet implemented
"""
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
"""


