

import random, pygame, sys, os
from pygame.locals import *

# game board class declaration
class gameboard(object):
    # this is the constructor which declares variables for use within the class
    def __init__(self):
        self.GAME_TITLE1 = "THE LORD OF THE RINGS"      # title 1
        self.GAME_TITLE2 = "MEMORY GAME"                # title 2
        self.TITLE_CAPTION = "THE LORD OF THE RINGS - MEMORY GAME"  #title caption
        self.ROW_ONE = 200          # x value of the 1st row of cards
        self.ROW_TWO = 350          # x value of the 2nd row of cards
        self.ROW_THREE = 500        # x value of the 3rd row of cards
        self.ROW_FOUR = 650         # x vakze if the 4th row of cards
        self.WINDOW_WIDTH = 1440    # width of the screen
        self.WINDOW_HEIGHT = 900    # height of the screen
        #self.TABLE_WIDTH = 900     # game table width, not yet implemented
        #self.TABLE_HEIGHT = 600    # game table height, not yet implemented
        self.NUM_PICS = 28          # total number of imported images
        self.NUM_CARDS = 28         # total number of cards in play
        self.NUM_PAIRS = 14         # total number of pairs
        self.images = []            # list where image files will be loaded to
        self.game_pieces = []       # list where loaded images will be randomized
        self.table_top = 100        # x point of the game table
        self.table_left = 250       # y point of the game table
        #self.number_of_columns = 7 # number of card columns for the option_menu_1, not yet implemented
        #self.number_of_rows = 4    # number of card rows for the option_menu_2, not yet implemented
        #self.number_of_players = 1 # number of players for the option_menu_3, not yet implemented
        #self.board = []            # not yet implemented
        self.pairs = []             # list where selected cards are compared
        #self.column = []           # not yet implemented
        #self.revealedBoxes = []    # not yet implemented
        self.title_font = ""        # title font
        self.input_font = ""        # font to be used with option_menu, not yet implemented
        self.continue_font = ""     # "click to start" text font
        self.background_image = ""  # background image
        self.table = ""             # game table image
        self.restart_button = ""    # restart button
        self.win_button = ""        # win button
        self.clock = pygame.time    # clock
        #self.left = ""             # not yet implemnted
        #self.top = ""              # not yet implemented
        self.number_images = 4      # number of frames (image_index) per image
        self.image_index = 0        # image index
        self.sprite_width = 80      # sprite width
        self.sprite_height = 80     # sprite height
        self.sprite_gap = 20        # gap between sprites
        self.sprite_y = 0           # sprite y start point
        self.sprite_x = 80          # sprite x start point
        #self.mousex = 0            # not yet implemented
        #self.mousey = 0            # not yet implemented
        #self.FPS = 30              # frames per second, not yet implemented
        self.card_cover = (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                      self.sprite_height)  #frame animation


    # initializes the screen size of the game window
    def initialize_screen_size(self):
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))


    # sets the game title
    def set_game_title(self):
        pygame.display.set_caption(self.TITLE_CAPTION)


    # loads the image files from the img folder and stores them into lists
    def initialize_game_data(self, total_pics):
        self.NUM_PICS = total_pics

        # load card images
        for x in range(self.NUM_PICS):
            self.images.append(pygame.image.load(os.path.join("data/img/",
                                                              "img%d.png" % (x + 1))).convert_alpha())

        # load background images
        self.table = (pygame.image.load(os.path.join("data/img/", "table.png")))
        self.background_image = pygame.image.load(os.path.join("data/img/", "back.png"))

        # load other images
        self.win_button = (pygame.image.load(os.path.join("data/img/", "win.png")))
        self.restart_button = pygame.image.load(os.path.join("data/img/", "restart.png"))

        # load fonts into the game
        self.title_font = pygame.font.Font(os.path.join("data/fnt/", "anirb.ttf"), 50)
        self.continue_font = pygame.font.Font(os.path.join("data/fnt/", "ring.ttf"), 35)
        self.input_font = pygame.font.Font(os.path.join("data/fnt/", "ring.ttf"), 30)
        self.score_font = pygame.font.Font(os.path.join("data/fnt/", "anirm.ttf"), 30)


    # randomizes the images and load them into a new list to get duplicate number of cards
    def randomize_cards (self):
        random.shuffle(self.images)
        random.shuffle(self.images)
        for x in range(self.NUM_PAIRS):
            self.game_pieces.append(self.images[x])
        random.shuffle(self.game_pieces)
        for x in range(self.NUM_PAIRS, self.NUM_CARDS):
            self.game_pieces.append(self.game_pieces[x-self.NUM_PAIRS])
        random.shuffle(self.game_pieces)


    # draw the start screen text and background
    def display_start_screen(self):
        title_width_1 = 225
        title_height_1 = 250
        title_width_2 = 350
        title_height_2 = 400

        # black font (shadow)
        titleBG1 = self.title_font.render(self.GAME_TITLE1, True, (0, 0, 0))
        titleBG2 = self.title_font.render(self.GAME_TITLE2, True, (0, 0, 0))
        proceed1 = self.continue_font.render("Click Anywhere To Start!", True, (0, 0, 0))
        author1 = self.continue_font.render("Created by Tomislav S", True, (0, 0, 0))
        # gold font
        titleFG1 = self.title_font.render(self.GAME_TITLE1, True, (255, 215, 0))
        titleFG2 = self.title_font.render(self.GAME_TITLE2, True, (255, 215, 0))
        proceed2 = self.continue_font.render("Click Anywhere To Start!", True, (255, 215, 0))
        author2 = self.continue_font.render("Created by Tomislav S", True, (255, 215, 0))
        # draw the background image and the font on the screen
        self.SCREEN.blit(self.background_image, (0, 0))
        self.SCREEN.blit(titleBG1, (title_width_1 - 4, title_height_1 - 4))
        self.SCREEN.blit(titleBG2, (title_width_2 - 4, title_height_2 - 4))
        self.SCREEN.blit(titleFG1, (title_width_1, title_height_1))
        self.SCREEN.blit(titleFG2, (title_width_2, title_height_2))
        self.SCREEN.blit(proceed1, (title_width_1 + 300, title_height_1 + 440))
        self.SCREEN.blit(proceed2, (title_width_1 + 303, title_height_1 + 442))
        self.SCREEN.blit(author1, (title_width_1 + -200, title_height_1 + 590))
        self.SCREEN.blit(author2, (title_width_1 + -197, title_height_1 + 592))

        for event in pygame.event.get():
            if ((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif (event.type == MOUSEBUTTONUP):
                #self.setup_menu_1()   #leads to setup menu instead, not yet implemented
                #pygame.display.flip()
                return True
        pygame.display.flip()
        return False


    # displays the main background image, table, text and buttons
    def display_ingame_background(self, number_of_guesses, number_of_pairs):
        self.SCREEN.blit(self.background_image, (0, 0))
        self.SCREEN.blit(self.table, (250, 150))
        self.SCREEN.blit(self.restart_button, (1350, 50))
        display_score = self.score_font.render("Number of Guesses: %d" %
                                                    int(number_of_guesses / 2), True, (255, 255, 255))
        pairs = self.score_font.render("Number of Pairs: (%d / %d)" %
                                                 (number_of_pairs, self.NUM_PAIRS), True, (255, 255, 255))
        self.SCREEN.blit(display_score, (800, 800))
        self.SCREEN.blit(pairs, (50, 800))


    # returns the number of "pairs" that have been found
    def number_of_pairs(self):
        return len(self.pairs)


    # removes the previous selection from the "pairs" list
    def remove_selection(self):
        self.pairs.pop()


    # adds matching pairs of cards to the "pairs" list
    def append_selection(self, user_selection):
        self.pairs.append(user_selection)


    # displays the gameboard to the screen
    def display_game_board(self):
        if (self.number_of_pairs() >= 1):   # if user selected 1 card

            ######### ROW 1 ###########
            width = 300                     # 1st row starts with "width" from the start of the screen
            for row1 in range(0, 7):        # draw cards in row 1
                if(self.selected_image(row1)):
                    image_index = 3
                    self.SCREEN.blit(self.game_pieces[row1],(width, self.ROW_ONE),
                                     (image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                      self.sprite_height))

                else:                       # draw the "closed" card
                    self.SCREEN.blit(self.game_pieces[row1],(width, self.ROW_ONE),
                                     (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                         self.sprite_height))
                width += 100                # add "width" between the next card

            ######### ROW 2 ###########
            width = 300                     # 2nd row starts with "width" from the start of the screen
            for row2 in range(7, 14):       # draw cards in row 2
                if(self.selected_image(row2)):
                    image_index = 3         # draw the "open" card
                    self.SCREEN.blit(self.game_pieces[row2],(width, self.ROW_TWO),
                                     (image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                         self.sprite_height))
                else:                       # draw the "closed" card
                        self.SCREEN.blit(self.game_pieces[row2],(width, self.ROW_TWO),
                                         (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                             self.sprite_height))
                width += 100                # add "width" between the next card

            ######### ROW 3 ###########
            width = 300                     # 3rd row starts with "width" from the start of the screen
            for row3 in range(14, 21):      # draw cards in row 3
                if(self.selected_image(row3)):
                    image_index = 3         # draw the "open" card
                    self.SCREEN.blit(self.game_pieces[row3],(width, self.ROW_THREE),
                                     (image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                         self.sprite_height))
                else:                       # draw the "closed" card
                    self.SCREEN.blit(self.game_pieces[row3],(width, self.ROW_THREE),
                                     (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                         self.sprite_height))
                width += 100                # add "width" between the next card

            ########## ROW 4 ############
            width = 300                     # 4th row starts with "width" from the start of the screen
            for row4 in range(21, 28):      # draw cards row 4
                if (self.selected_image(row4)):
                    image_index = 3         # draw the "open" card
                    self.SCREEN.blit(self.game_pieces[row4], (width, self.ROW_FOUR),
                                         (image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                          self.sprite_height))
                else:                       # draw the "closed" card
                    self.SCREEN.blit(self.game_pieces[row4], (width, self.ROW_FOUR),
                                         (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                          self.sprite_height))
                width += 100                # add "width" between the next card

        else:                               # starting gameboard with all cards closed

            ######### ROW 1 ##########
            width = 300                     # 1st row starts with "width" from the start of the screen
            for row1 in range(0, 7):        # draw "closed" cards in row 1
                self.SCREEN.blit(self.game_pieces[row1],(width,self.ROW_ONE),(self.card_cover))
                width += 100                # add "width" between the next card

            ######## ROW 2 ###########
            width = 300                     # 2nd row starts with "width" from the start of the screen
            for row2 in range(7, 14):       # draw "closed" cards in row 2
                self.SCREEN.blit(self.game_pieces[row2],(width,self.ROW_TWO),(self.card_cover))
                width += 100                # add "width" between the next card

            ######## ROW 3 ###########
            width = 300                     # 3rd row starts with "width" from the start of the screen
            for row3 in range(14, 21):      # draw "closed" cards in row 3
                self.SCREEN.blit(self.game_pieces[row3],(width,self.ROW_THREE),(self.card_cover))
                width += 100                # add "width" between the next card

            ######## ROW 4 ###########
            width = 300                     # 4th row starts with "width" from the start of the screen
            for row4 in range(21, 28):      # draw "closed" cards in row 4
                self.SCREEN.blit(self.game_pieces[row4], (width, self.ROW_FOUR), (self.card_cover))
                width += 100                # add "width" between the next card


    # checks the value of the selected card, if value is found in the list it returns True and animates the card
    def selected_image(self, checkMatch):
        for item in self.pairs:
            if(int(checkMatch) == int(item)):
                return True
        return False


    # display the game over screen
    def game_over(self, number_of_guesses):
        game_run = False
        self.SCREEN.blit(self.background_image, (0, 0))
        number_of_guesses = int(number_of_guesses / 2)
        display_score = self.score_font.render("Number of Guesses: %d" % (number_of_guesses), True, (255, 255, 255))
        new_game = self.continue_font.render("Click Anywhere To Start New Game!",
            True, (255, 255, 255))
        self.SCREEN.blit(self.win_button,(600,350))
        self.SCREEN.blit(display_score,(400, 250))
        self.SCREEN.blit(new_game,(350,650))

        while(not game_run):
            self.clock.wait(100)
            pygame.display.flip()
            for event in pygame.event.get():
                if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    return False
                elif(event.type == MOUSEBUTTONUP):
                    return True
        pygame.display.flip()


    # check if the user clicked on a game image or the buttons
    # this part is hard coded at the moment
    def get_selection(self, mouseX, mouseY):
        # the restart button
        if((mouseY <= 130 and mouseY >= 50) and (mouseX <= 1430 and mouseX >= 1350)):
            return "restart"
        # cards
        ########## ROW 1 ##########
        elif((mouseY <= 290) and (mouseY >= 180)):
            if((mouseX <= 390) and (mouseX >=300)):
                if(self.selected_image(0) == False):
                    return 0   # image 1
            elif((mouseX <= 490) and (mouseX >= 400)):
                if(self.selected_image(1) == False):
                    return 1   # image 2
            elif((mouseX <= 590) and (mouseX >= 500)):
                if(self.selected_image(2) == False):
                    return 2   # image 3
            elif((mouseX <= 690) and (mouseX >= 600)):
                if(self.selected_image(3) == False):
                    return 3   # image 4
            elif((mouseX <= 790) and (mouseX >= 700)):
                if(self.selected_image(4) == False):
                    return 4   # image 5
            elif((mouseX <= 890) and (mouseX >= 800)):
                if(self.selected_image(5) == False):
                    return 5   # image 6
            elif((mouseX <= 990) and (mouseX >= 900)):
                if(self.selected_image(6) == False):
                    return 6   # image 7
                
        ########### ROW 2 ############
        elif((mouseY <= 440) and (mouseY >= 350)):
            if((mouseX <= 390) and (mouseX >= 300)):
                if(self.selected_image(7) == False):
                    return 7   # image 8
            elif((mouseX <= 490) and (mouseX >= 400)):
                if(self.selected_image(8) == False):
                    return 8   # image 9
            elif((mouseX <= 590) and (mouseX >= 500)):
                if(self.selected_image(9) == False):
                    return 9   # image 10
            elif((mouseX <= 690) and (mouseX >= 600)):
                if(self.selected_image(10) == False):
                    return 10  # image 11
            elif((mouseX <= 790) and (mouseX >= 700)):
                if(self.selected_image(11) == False):
                    return 11  # image 12
            elif((mouseX <= 890) and (mouseX >= 800)):
                if(self.selected_image(12) == False):
                    return 12  # image 13
            elif((mouseX <= 990) and (mouseX >= 900)):
                if(self.selected_image(13) == False):
                    return 13  # image 14

        ######### ROW 3 ###########
        elif((mouseY <= 590) and (mouseY >= 500)):
            if((mouseX <= 390) and (mouseX >= 300)):
                if(self.selected_image(14) == False):
                    return 14  # image 15
            elif((mouseX <= 490) and (mouseX >= 400)):
                if(self.selected_image(15) == False):
                    return 15  # image 16
            elif((mouseX <= 590) and (mouseX >= 500)):
                if(self.selected_image(16) == False):
                    return 16  # image 17
            elif((mouseX <= 690) and (mouseX >= 600)):
                if(self.selected_image(17) == False):
                    return 17  # image 18
            elif((mouseX <= 790) and (mouseX >= 700)):
                if(self.selected_image(18) == False):
                    return 18  # image 19
            elif((mouseX <= 890) and (mouseX >= 800)):
                if(self.selected_image(19) == False):
                    return 19  # image 20
            elif((mouseX <=990) and (mouseX >= 900)):
                if(self.selected_image(20) == False):
                    return 20  # image 21

        ######### ROW 4 #######
        elif ((mouseY <= 740) and (mouseY >= 650)):
            if ((mouseX <= 390) and (mouseX >= 300)):
                if (self.selected_image(21) == False):
                    return 21  # image 22
            elif ((mouseX <= 490) and (mouseX >= 400)):
                if (self.selected_image(22) == False):
                    return 22  # image 23
            elif ((mouseX <= 590) and (mouseX >= 500)):
                if (self.selected_image(23) == False):
                    return 23  # image 24
            elif ((mouseX <= 690) and (mouseX >= 600)):
                if (self.selected_image(24) == False):
                    return 24  # image 25
            elif ((mouseX <= 790) and (mouseX >= 700)):
                if (self.selected_image(25) == False):
                    return 25  # image 26
            elif ((mouseX <= 890) and (mouseX >= 800)):
                if (self.selected_image(26) == False):
                    return 26  # image 27
            elif ((mouseX <= 990) and (mouseX >= 900)):
                if (self.selected_image(27) == False):
                    return 27  # image 28
        return -1              # resets selection


    # after a game is over re initialize the game board and cards
    def reinitialize_board(self):
        del self.pairs[:]
        del self.game_pieces[:]
        self.randomize_cards()


# setup menus for changing rows, columns and player numbers, not yet implemented
"""
    # setup menu_1
    def setup_menu_1(self):
        inGame = False

        input_width_1 = 300
        input_height_1 = 250
        input_width_2 = 425
        input_height_2 = 400
        input_width_3 = 450
        input_height_3 = 475
        input_1 = ""

        while (not inGame):
            # black font
            input_bg_1 = self.input_font.render("Please enter the number of columns and press <enter>",
                                                True, (0, 0, 0))
            input_bg_2 = self.input_font.render("Number of columns must be even or ", True, (0, 0, 0))
            input_bg_3 = self.input_font.render("leave blank for a default value(6) ", True, (0, 0, 0))

            # yellow font
            input_fg_1 = self.input_font.render("Please enter the number of columns and press <enter>",
                                                True, (255, 215, 0))
            input_fg_2 = self.input_font.render("Number of columns must be even or ", True, (255, 215, 0))
            input_fg_3 = self.input_font.render("leave blank for a default value(6) ", True, (255, 215, 0))

            self.SCREEN.blit(self.background_Image, (0, 0))
            self.SCREEN.blit(self.table, (250, 150))
            self.SCREEN.blit(input_bg_1, (input_width_1 - 2, input_height_1 - 2))
            self.SCREEN.blit(input_bg_2, (input_width_2 - 2, input_height_2 - 2))
            self.SCREEN.blit(input_bg_3, (input_width_3 - 2, input_height_3 - 2))
            self.SCREEN.blit(input_fg_1, (input_width_1, input_height_1))
            self.SCREEN.blit(input_fg_2, (input_width_2, input_height_2))
            self.SCREEN.blit(input_fg_3, (input_width_3, input_height_3))

            for event in pygame.event.get():
                if ((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                     if event.key == K_BACKSPACE:
                        input_1 = input_1[:-1]
                     elif event.unicode.isdigit():
                        input_1 += event.unicode
                     if event.key == K_RETURN:
                         input_1 = []
                         input_1 = int(input_1[0])
                         print(type(input_1))
                         print(input_1)
                         self.setup_menu_2()
                         return True
            user_input = self.input_font.render(input_1, True, (255, 215, 0))
            rect = user_input.get_rect(center=(700, 600))
            self.SCREEN.blit(user_input, rect)

            pygame.display.flip()

    def setup_menu_2(self):
        inGame = False

        input_width_1 = 300
        input_height_1 = 250
        input_width_2 = 425
        input_height_2 = 400
        input_width_3 = 450
        input_height_3 = 475

        while (not inGame):
            # black font
            input_bg_1 = self.input_font.render("Please enter the number of rows and press <enter>",
                                                True, (0, 0, 0))
            input_bg_2 = self.input_font.render("Number of columns must be even or ", True, (0, 0, 0))
            input_bg_3 = self.input_font.render("leave blank for a default value(3) ", True, (0, 0, 0))

            # yellow font
            input_fg_1 = self.input_font.render("Please enter the number of rows and press <enter>",
                                                True, (255, 215, 0))
            input_fg_2 = self.input_font.render("Number of columns must be even or ", True, (255, 215, 0))
            input_fg_3 = self.input_font.render("leave blank for a default value(3) ", True, (255, 215, 0))

            self.SCREEN.blit(self.background_Image, (0, 0))
            self.SCREEN.blit(self.table, (250, 150))
            self.SCREEN.blit(input_bg_1, (input_width_1 - 2, input_height_1 - 2))
            self.SCREEN.blit(input_bg_2, (input_width_2 - 2, input_height_2 - 2))
            self.SCREEN.blit(input_bg_3, (input_width_3 - 2, input_height_3 - 2))
            self.SCREEN.blit(input_fg_1, (input_width_1, input_height_1))
            self.SCREEN.blit(input_fg_2, (input_width_2, input_height_2))
            self.SCREEN.blit(input_fg_3, (input_width_3, input_height_3))

            for event in pygame.event.get():
                if ((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                     if event.unicode.isdigit():
                        self.number_of_rows += event.unicode
                     elif event.key == K_BACKSPACE:
                        self.number_of_rows = self.number_of_rows[:-1]
                     if event.key == K_RETURN:
                        self.number_of_rows = ""
                        self.setup_menu_3()
                        return True
            user_input = self.input_font.render(self.number_of_rows, True, (255, 215, 0))
            rect = user_input.get_rect(center=(700, 600))
            self.SCREEN.blit(user_input, rect)
            pygame.display.flip()

    def setup_menu_3(self):
        inGame = False

        input_width_1 = 300
        input_height_1 = 250
        input_width_2 = 425
        input_height_2 = 400
        input_width_3 = 450
        input_height_3 = 475

        while (not inGame):
            # black font
            input_bg_1 = self.input_font.render("Please enter the number of players and press <enter>",
                                                True, (0, 0, 0))
            # input_bg_2 = self.input_font.render("Number of columns must be even or ", True, (0, 0, 0))
            input_bg_3 = self.input_font.render("leave blank for a default value(1) ", True, (0, 0, 0))

            # yellow font
            input_fg_1 = self.input_font.render("Please enter the number of players and press <enter>",
                                                True, (255, 215, 0))
            # input_fg_2 = self.input_font.render("Number of columns must be even or ", True, (255, 215, 0))
            input_fg_3 = self.input_font.render("leave blank for a default value(1) ", True, (255, 215, 0))

            self.SCREEN.blit(self.background_Image, (0, 0))
            self.SCREEN.blit(self.table, (250, 150))
            self.SCREEN.blit(input_bg_1, (input_width_1 - 2, input_height_1 - 2))
            # self.SCREEN.blit(input_bg_2, (input_width_2 - 2, input_height_2 - 2))
            self.SCREEN.blit(input_bg_3, (input_width_3 - 2, input_height_3 - 2))
            self.SCREEN.blit(input_fg_1, (input_width_1, input_height_1))
            # self.SCREEN.blit(input_fg_2, (input_width_2, input_height_2))
            self.SCREEN.blit(input_fg_3, (input_width_3, input_height_3))

            for event in pygame.event.get():
                if ((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.unicode.isdigit():
                        self.number_of_players += event.unicode
                    elif event.key == K_BACKSPACE:
                        self.number_of_players = self.number_of_players[:-1]
                        if event.key == K_RETURN:
                            self.number_of_players = ""
                        return True
            user_input = self.input_font.render(self.number_of_players, True, (255, 215, 0))
            rect = user_input.get_rect(center=(700, 600))
            self.SCREEN.blit(user_input, rect)
            pygame.display.flip()
"""
