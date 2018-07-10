import random, pygame, sys, os, re
from pygame.locals import *

# game board class declaration
class GameBoard(object):
    # this is the constructor which declares variables for use within the class
    def __init__(self):
        self.GAME_TITLE1 = "THE LORD OF THE RINGS"
        self.GAME_TITLE2 = "MEMORY GAME"
        self.TITLE_CAPTION = "THE LORD OF THE RINGS - MEMORY GAME"
        self.ROW_ONE = 100
        self.ROW_TWO = 250
        self.ROW_THREE = 400
        self.WINDOW_WIDTH = 1440
        self.WINDOW_HEIGHT = 900
        self.TABLE_WIDTH = 900
        self.TABLE_HEIGHT = 600
        self.NUM_PICS = 27
        self.NUM_CARDS = 18
        self.NUM_PAIRS = 9
        self.NUM_RANKS = 4
        self.images = []
        self.icons = []
        self.table_top = 100
        self.table_left = 250

        self.number_of_columns = 8
        self.number_of_rows = 4
        self.number_of_players = 1
        self.board = []
        self.pairs = []
        self.ranks = []
        self.column = []
        self.revealedBoxes = []
        self.titleFont = ""
        self.input_font = ""
        self.proceed = ""
        self.helpFont = ""
        self.background_Image = ""
        self.table = ""
        self.helpButton = ""
        self.start_button =""
        self.rank_button = ""
        self.clock = pygame.time
        self.left = ""
        self.top = ""
        self.number_images = 4
        self.image_index = 0
        self.sprite_width = 80
        self.sprite_height = 80
        self.sprite_gap = 20
        self.sprite_y = 0
        self.sprite_x = 80
        self.mousex = 0
        self.mousey = 0
        self.FPS = 30


    # initializes the screen size of the window
    def InitializeScreenSize(self):
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT))


    # sets the game title
    def SetGameTitle(self):
        pygame.display.set_caption(self.TITLE_CAPTION)


    # gets data (img files) from the folder and stores them into various lists
    def InitializeGameData(self):
       # stores the playing cards (images)
        for x in range(self.NUM_PICS):
            self.images.append(pygame.image.load(os.path.join("data/img/",
                "img%d.png" % (x+1))).convert_alpha())

        ##########################################################################
        # stores the rank images
        for x in range(self.NUM_RANKS):
            #self.ranks.append(pygame.image.load(os.path.join("data/img/",
            #    "rank%d.png" % (x+1))))
            self.ranks.append(pygame.image.load(os.path.join("data/img/","rank.png")))
        ##########################################################################

        #load background images
        self.table = (pygame.image.load(os.path.join("data/img/", "table.png")))
        self.background_Image = pygame.image.load(os.path.join("data/img/", "back.png"))

        # load fonts into the game
        self.titleFont = pygame.font.Font(os.path.join("data/fnt/","anirb.ttf"),50)
        self.proceed = pygame.font.Font(os.path.join("data/fnt/","ring.ttf"),35)
        self.input_font = pygame.font.Font(os.path.join("data/fnt/","ring.ttf"),30)

       #################################################################################
        self.helpButton = pygame.image.load(os.path.join("data/img/", "restart.png"))  ###
        #self.start_button = pygame.image.load(os.path.join("data/img/","start.png"))
        self.rank_button = pygame.image.load(os.path.join("data/img/", "rank.png"))

        self.helpFont = pygame.font.Font(os.path.join("data/fnt/","ring.ttf"),14)####
        self.helpDescrFont = pygame.font.Font(os.path.join("data/fnt/","anirm.ttf"),30)###
        self.currentScoreFont = pygame.font.Font(os.path.join("data/fnt/","anirm.ttf"),30)###
        #################################################################################


    # randomizes the game pieces (images) inside the list using "shuffle"
    def RandomizeGamePieces(self):
        random.shuffle(self.images)
        self.NUM_PAIRS = int(int(self.number_of_columns) * int(self.number_of_rows) / 2)   ####broj parova koji trebam
        self.icons = self.images[:self.NUM_PAIRS] * 2
        random.shuffle(self.icons)


    # before the game starts, this initializes the start Menu
    def DisplayStartScreen(self):
        title_width_1 = 225
        title_height_1 = 250
        title_width_2 = 350
        title_height_2 = 400

        #black font
        titleBG1 = self.titleFont.render(self.GAME_TITLE1, True, (0, 0, 0))
        titleBG2 = self.titleFont.render(self.GAME_TITLE2, True, (0, 0, 0))
        proceed1 = self.proceed.render("Click Anywhere To Start!", True, (0, 0, 0))
        author1 = self.proceed.render("Created by Tomislav S", True,(0, 0, 0))

        #yellow font
        titleFG1 = self.titleFont.render(self.GAME_TITLE1, True, (255, 215, 0))
        titleFG2 = self.titleFont.render(self.GAME_TITLE2, True, (255, 215, 0))
        proceed2 = self.proceed.render("Click Anywhere To Start!", True, (255, 215, 0))
        author2 = self.proceed.render("Created by Tomislav S", True,(255, 215, 0))

        #display to SCREEN
        self.SCREEN.blit(self.background_Image,(0, 0))
        self.SCREEN.blit(titleBG1,(title_width_1 - 4,title_height_1 - 4))
        self.SCREEN.blit(titleBG2, (title_width_2 - 4, title_height_2 - 4))
        self.SCREEN.blit(titleFG1,(title_width_1,title_height_1))
        self.SCREEN.blit(titleFG2, (title_width_2, title_height_2))
        self.SCREEN.blit(proceed1,(title_width_1 + 300,title_height_1 + 440))
        self.SCREEN.blit(proceed2,(title_width_1 + 303, title_height_1 + 442))
        self.SCREEN.blit(author1,(title_width_1 + -200, title_height_1 + 590))
        self.SCREEN.blit(author2,(title_width_1 + -197, title_height_1 + 592))

        for event in pygame.event.get():
            if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif(event.type == MOUSEBUTTONUP):
                self.setup_menu_1()
                pygame.display.flip()
                return True
        pygame.display.flip()
        return False


     #setup menu_1
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
            self.SCREEN.blit(self.table, (250,150))
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
                    #if event.key == K_BACKSPACE:
                    #    input_1 = input_1[:-1]
                    #elif event.unicode.isdigit():
                    #    input_1 += event.unicode
                    if event.key == K_RETURN:
                        #input_1 = []
                        #input_1 = int(input_1[0])
                        #print(type(input_1))
                        #print(input_1)
                        self.setup_menu_2()
                        return True
            user_input = self.input_font.render(input_1, True, (255, 215, 0))
            rect = user_input.get_rect(center = (700,600))
            self.SCREEN.blit(user_input,rect)



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
                    #if event.unicode.isdigit():
                    #    self.number_of_rows += event.unicode
                    #elif event.key == K_BACKSPACE:
                    #    self.number_of_rows = self.number_of_rows[:-1]
                    if event.key == K_RETURN:
                    #    self.number_of_rows = ""
                        self.setup_menu_3()
                        return True
            #user_input = self.input_font.render(self.number_of_rows, True, (255, 215, 0))
            #rect = user_input.get_rect(center=(700, 600))
            #self.SCREEN.blit(user_input, rect)
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
            #input_bg_2 = self.input_font.render("Number of columns must be even or ", True, (0, 0, 0))
            input_bg_3 = self.input_font.render("leave blank for a default value(1) ", True, (0, 0, 0))

            # yellow font
            input_fg_1 = self.input_font.render("Please enter the number of players and press <enter>",
                                                True, (255, 215, 0))
            #input_fg_2 = self.input_font.render("Number of columns must be even or ", True, (255, 215, 0))
            input_fg_3 = self.input_font.render("leave blank for a default value(1) ", True, (255, 215, 0))

            self.SCREEN.blit(self.background_Image, (0, 0))
            self.SCREEN.blit(self.table, (250, 150))
            self.SCREEN.blit(input_bg_1, (input_width_1 - 2, input_height_1 - 2))
            #self.SCREEN.blit(input_bg_2, (input_width_2 - 2, input_height_2 - 2))
            self.SCREEN.blit(input_bg_3, (input_width_3 - 2, input_height_3 - 2))
            self.SCREEN.blit(input_fg_1, (input_width_1, input_height_1))
            #self.SCREEN.blit(input_fg_2, (input_width_2, input_height_2))
            self.SCREEN.blit(input_fg_3, (input_width_3, input_height_3))

            for event in pygame.event.get():
                if ((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                #    if event.unicode.isdigit():
                #        self.number_of_players += event.unicode
                #    elif event.key == K_BACKSPACE:
                #        self.number_of_players = self.number_of_players[:-1]
                    if event.key == K_RETURN:
                    #    self.number_of_players = ""
                        return True
            #user_input = self.input_font.render(self.number_of_players, True, (255, 215, 0))
            #rect = user_input.get_rect(center=(700, 600))
            #self.SCREEN.blit(user_input, rect)
            pygame.display.flip()

        ###################################################################
        # self.col_number = input("Please enter the number of columns: ")
        # if self.col_number % 2 != 0:
        #    self.col_number -= 1
        # self.row_number = input("Please enter the number or rows: ")
        # if self.row_number % 2 != 0:
        #    self.row_number -= 1
        ###################################################################

        #return self.col_number, self.row_number


    # displays the main background image (the table and the help button)
    def DisplayIngameBackground(self,numGuesses,numPairs):
        self.SCREEN.blit(self.background_Image, (0, 0))
        self.SCREEN.blit(self.table, (250, 150))

        self.SCREEN.blit(self.helpButton,(1350,50))
        displayScore = self.currentScoreFont.render("Number of Guesses: %d" %
            int(numGuesses/2), True, (255,255,255))
        pairs = self.currentScoreFont.render("Number of Pairs: (%d / %d)" %
            (numPairs, self.NUM_PAIRS), True, (255,255,255))
        self.SCREEN.blit(displayScore,(800,800))
        self.SCREEN.blit(pairs,(50,800))


        # returns the number of "pairs" that have been found
    def NumPairs(self):
        return len(self.pairs)

        # determines of two cards are a pairing match
    def IsPair(self, SELECTION_ONE, SELECTION_TWO):
        return (self.icons[SELECTION_ONE] == self.icons[SELECTION_TWO])

        # removes the previous selection from the list
    def RemoveSelection(self):
        self.pairs.pop()


    def DisplayGameBoard(self):
        XMARGIN = int((self.TABLE_WIDTH - (self.number_of_columns * (self.sprite_width + self.sprite_gap))) / 2)
        YMARGIN = int((self.TABLE_HEIGHT - (self.number_of_rows * (self.sprite_height + self.sprite_gap))) / 2)
        if (self.NumPairs() >= 1):
            for boxx in range(self.number_of_columns):
                for boxy in range(self.number_of_rows):
                    if self.IsSelectedImage():
                        # self.left, self.top  = leftTopCoordsOfBox(boxx, boxy)
                        self.left = boxx * (self.sprite_width + self.sprite_gap) + XMARGIN
                        self.top = boxy * (self.sprite_height + self.sprite_gap) + YMARGIN
                        print(self.icons)
                        self.SCREEN.blit(self.icons[0], (self.left + self.table_left, self.top + self.table_top),
                                        (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                        self.sprite_height))
                        #del self.icons[0]
        else:
            for boxx in range(self.number_of_columns):
                for boxy in range(self.number_of_rows):
                    # self.left, self.top  = leftTopCoordsOfBox(boxx, boxy)
                    self.left = boxx * (self.sprite_width + self.sprite_gap) + XMARGIN
                    self.top = boxy * (self.sprite_height + self.sprite_gap) + YMARGIN
                    print(self.icons)
                    self.SCREEN.blit(self.icons[0], (self.left + self.table_left, self.top + self.table_top),
                                    (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                    self.sprite_height))
                    #del self.icons[0]



    # determines if a specific card has been selected within our list
    # return true if current selection is in our list, else false
    def IsSelectedImage(self, checkMatch):
        for item in self.pairs:
            if (int(checkMatch) == int(item)):
                return True
        return False

    #def GetSelection(self, mouseX, mouseY):
    def getBoxAtPixel(self, mouseX, mouseY):
        XMARGIN = int((self.TABLE_WIDTH - (self.number_of_columns * (self.sprite_width + self.sprite_gap))) / 2)
        YMARGIN = int((self.TABLE_HEIGHT - (self.number_of_rows * (self.sprite_height + self.sprite_gap))) / 2)
        for boxx in range(self.number_of_columns):
            for boxy in range(self.number_of_rows):
                # self.left, self.top  = leftTopCoordsOfBox(boxx, boxy)
                self.left = boxx * (self.sprite_width + self.sprite_gap) + XMARGIN
                self.top = boxy * (self.sprite_height + self.sprite_gap) + YMARGIN
                boxRect = pygame.Rect((self.left + self.table_left), (self.top + self.table_top), self.sprite_width, self.sprite_height)
                if boxRect.collidepoint(mouseX, mouseY):
                    return (boxx, boxy)
        return (None, None)


    def drawHighlightBox(self, boxx, boxy):
        XMARGIN = int((self.TABLE_WIDTH - (self.number_of_columns * (self.sprite_width + self.sprite_gap))) / 2)
        YMARGIN = int((self.TABLE_HEIGHT - (self.number_of_rows * (self.sprite_height + self.sprite_gap))) / 2)
        self.left = boxx * (self.sprite_width + self.sprite_gap) + XMARGIN
        self.top = boxy * (self.sprite_height + self.sprite_gap) + YMARGIN
        pygame.draw.rect(self.SCREEN, (255, 215, 0),
                         (self.left - 5, self.top - 5, self.sprite_width + 10, self.sprite_height + 10), 4)


    def revealBoxesAnimation(self):
        # Do the "box reveal" animation.
        if (self.image_index <= self.number_images - 1):
            self.SCREEN.blit(self.top, self.left),(self.image_index * self.sprite_x, self.sprite_y, self.sprite_width, self.sprite_height)
            self.image_index += 1
            pygame.time.Clock().tick(self.FPS)
        else:
            self.image_index -= 1
            self.SCREEN.blit(self.top, self.left), (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                              self.sprite_height)


    def coverBoxesAnimation(self):
        # Do the "box cover" animation.
        if (self.image_index != 0):
            self.SCREEN.blit(self.top, self.left),(self.image_index * self.sprite_x, self.sprite_y, self.sprite_width, self.sprite_height)
            self.image_index -= 1
            pygame.time.Clock().tick(self.FPS)

    def hasWon(self, revealedBoxes):
        # Returns True if all the boxes have been revealed, otherwise False
        for i in self.revealedBoxes:
            if False in i:
                return False  # return False if any boxes are covered.
        return True

    def generateRevealedBoxesData(self, val):

        for i in range(self.table_width):
            self.revealedBoxes.append([val] * self.table_height)
        return self.revealedBoxes




    # adds matching pairs of cards to the list
    def AppendSelection(self, userSelection):
        self.pairs.append(userSelection)





    # display the game over Menu to the screen
    def GameOver(self,numGuesses):
        inGame = False
        width = 220
        height = 215
        bull = 3
        donkey = 2
        cat = 1
        fish = 0
        numGuesses = int(numGuesses/2)
        self.SCREEN.blit(self.background_Image,(0,0))
        displayScore = self.currentScoreFont.render("Number of Guesses: %d" %
            (numGuesses), True, (255,255,255))
        resumeGame = self.proceed.render("Click Anywhere To Continue!",
            True, (255,255,255))

        # display the game over ranks
        if(numGuesses >= 25): # bull
            self.SCREEN.blit(self.ranks[bull],(width,height))
            desc = self.currentScoreFont.render("Rank: BULL (May Need Glasses)",
                True, (255,255,255))
            desc2 = self.currentScoreFont.render("You Bulldozed Your Way To "
                "Completion Through Brute Force", True, (255,255,255))
            self.SCREEN.blit(desc,(180,95))
            self.SCREEN.blit(desc2,(15,145))

        elif(numGuesses >= 21): # donkey
            self.SCREEN.blit(self.ranks[donkey],(width,height))
            desc = self.currentScoreFont.render("Memory Rank: DONKEY (Average)",
                True, (255,255,255))
            desc2 = self.currentScoreFont.render("You Passively Trotted Your Way "
                "To Completion", True, (255,255,255))
            self.SCREEN.blit(desc,(180,95))
            self.SCREEN.blit(desc2,(105,145))

        elif(numGuesses >= 17): # cat
            self.SCREEN.blit(self.ranks[cat],(width,height))
            desc = self.currentScoreFont.render("Memory Rank: CAT (Smart)", True,
                (255,255,255))
            desc2 = self.currentScoreFont.render("You Cautiously Pawed Your Way "
                "To Completion", True, (255,255,255))
            self.SCREEN.blit(desc,(190,95))
            self.SCREEN.blit(desc2,(90,145))

        else: # fish
            self.SCREEN.blit(self.ranks[fish],(width,height))
            desc = self.currentScoreFont.render("Memory Rank: FISH (Genius)",
                True, (255,255,255))
            desc2 = self.currentScoreFont.render("You Sifted Your Way To "
                "Completion Like A Fish In Water", True, (255,255,255))
            self.SCREEN.blit(desc,(180,95))
            self.SCREEN.blit(desc2,(25,145))

        self.SCREEN.blit(displayScore,(230,35))
        self.SCREEN.blit(resumeGame,(90,515))

        while(not inGame):
            self.clock.wait(70)
            pygame.display.flip()
            for event in pygame.event.get():
                if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    return False
                elif(event.type == MOUSEBUTTONUP):
                    return True



    # after a game is over re-initialize the game board and cards
    def ReInitializeBoard(self):
        del self.pairs[:]
        del self.gamePieces[:]
        self.RandomizeGamePieces()


"""""
   #### displays the current game board to the screen
   def DisplayGameBoard(self):
       # do this if we have at least 1 card selected
       if (self.NumPairs() >= 1):
           width = 80  ## print row 1
           for row1 in range(0, 6):

               if(self.IsSelectedImage(row1)):

                   # print("TRUE = ",row1)
                   if (self.image_index <= self.number_images -1):
                       self.SCREEN.blit(self.icons[row1],(width, self.ROW_ONE),
                                    (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                     self.sprite_height))
                       self.image_index += 1
                   else:
                       self.image_index -= 1
                       self.SCREEN.blit(self.icons[row1],(width, self.ROW_ONE),
                                        (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                         self.sprite_height))






              else:
                   image_index = 0
                   self.SCREEN.blit(self.icons[row1], (width, self.ROW_ONE),
                                    (image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                     self.sprite_height))

               width += 100


           width = 80 ## print row 2
           #self.image_index = 4
           for row2 in range(6, 12):
               if (self.IsSelectedImage(row2)):
                   # print("TRUE = ",row1)
                   if (self.image_index <= self.number_images - 1):
                       self.SCREEN.blit(self.icons[row2], (width, self.ROW_TWO),
                                        (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                         self.sprite_height))
                       self.image_index += 1
                   else:
                       self.image_index -= 1
                       self.SCREEN.blit(self.icons[row2], (width, self.ROW_TWO),
                                        (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                         self.sprite_height))

               else:
                   image_index = 0
                   self.SCREEN.blit(self.icons[row2], (width, self.ROW_TWO),
                                    (image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                     self.sprite_height))
               width += 100

           width = 80 ## print row 3
           #self.image_index = 4
           for row3 in range(12, 18):
               if (self.IsSelectedImage(row3)):
                   # print("TRUE = ",row1)
                   if (self.image_index <= self.number_images - 1):
                       self.SCREEN.blit(self.icons[row3], (width, self.ROW_THREE),
                                        (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                         self.sprite_height))
                       self.image_index += 1
                   else:
                       self.image_index -= 1
                       self.SCREEN.blit(self.icons[row3], (width, self.ROW_THREE),
                                        (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                         self.sprite_height))

               else:
                   image_index = 0
                   self.SCREEN.blit(self.icons[row3], (width, self.ROW_THREE),
                                    (image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                     self.sprite_height))
               width += 100

       # NO MATCHES HAVE BEEN FOUND
       else:
           self.image_index = 0
           width = 80 ## print row 1

           for row1 in range(0, 6):
               self.SCREEN.blit(self.icons[row1],(width,self.ROW_ONE),
                                (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                 self.sprite_height))


               width += 100
           width = 80 ## print row 2
           for row2 in range(6, 12):
               self.SCREEN.blit(self.icons[row2],(width,self.ROW_TWO),
                                (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                 self.sprite_height))
               width += 100

           width = 80 ## print row 3
           for row3 in range(12, 18):
               self.SCREEN.blit(self.icons[row3],(width,self.ROW_THREE),
                                    (self.image_index * self.sprite_x, self.sprite_y, self.sprite_width,
                                     self.sprite_height))
               width += 100
   """
""""

    # determine if the user clicked on a game image/icon
    def GetSelection(self, mouseX, mouseY):
        ##################################################################
        # help image
        if((mouseY <= 60 and mouseY >= 33)and(mouseX <= 713 and mouseX >= 687)):
            return "help"
        ##################################################################

        # row 1
        elif((mouseY <= 190) and (mouseY >= 80)):
            #print("ROW 1")
            if((mouseX <= 170) and (mouseX >=80)):
                if(self.IsSelectedImage(0) == False):
                    return 0  # image 1
            elif((mouseX <= 270) and (mouseX >= 180)):
                if(self.IsSelectedImage(1) == False):
                    return 1  # image 2
            elif((mouseX <= 370) and (mouseX >= 280)):
                if(self.IsSelectedImage(2) == False):
                    return 2  # image 3
            elif((mouseX <= 470) and (mouseX >= 380)):
                if(self.IsSelectedImage(3) == False):
                    return 3  # image 4
            elif((mouseX <= 570) and (mouseX >= 480)):
                if(self.IsSelectedImage(4) == False):
                    return 4   # image 5
            elif((mouseX <= 670) and (mouseX >= 580)):
                if(self.IsSelectedImage(5) == False):
                    return 5  # image 6
        # row 2
        elif((mouseY <= 340) and (mouseY >= 250)):
            #print("ROW 2")
            if((mouseX <= 170) and (mouseX >= 80)):
                if(self.IsSelectedImage(6) == False):
                    return 6  # image 7
            elif((mouseX <= 270) and (mouseX >= 180)):
                if(self.IsSelectedImage(7) == False):
                    return 7  # image 8
            elif((mouseX <= 370) and (mouseX >= 280)):
                if(self.IsSelectedImage(8) == False):
                    return 8  # image 9
            elif((mouseX <= 470) and (mouseX >= 380)):
                if(self.IsSelectedImage(9) == False):
                    return 9  # image 10
            elif((mouseX <= 570) and (mouseX >= 480)):
                if(self.IsSelectedImage(10) == False):
                    return 10  # image 11
            elif((mouseX <= 670) and (mouseX >= 580)):
                if(self.IsSelectedImage(11) == False):
                    return 11  # image 12
        # row 3
        elif((mouseY <= 490) and (mouseY >= 400)):
            #print("ROW 3")
            if((mouseX <= 170) and (mouseX >= 80)):
                if(self.IsSelectedImage(12) == False):
                    return 12  # image 13
            elif((mouseX <= 270) and (mouseX >= 180)):
                if(self.IsSelectedImage(13) == False):
                    return 13  # image 14
            elif((mouseX <= 370) and (mouseX >= 280)):
                if(self.IsSelectedImage(14) == False):
                    return 14  # image 15
            elif((mouseX <= 470) and (mouseX >= 380)):
                if(self.IsSelectedImage(15) == False):
                    return 15  # image 16
            elif((mouseX <= 570) and (mouseX >= 480)):
                if(self.IsSelectedImage(16) == False):
                    return 16  # image 17
            elif((mouseX <= 670) and (mouseX >= 580)):
                if(self.IsSelectedImage(17) == False):
                    return 17  # image 18
        return -1
"""