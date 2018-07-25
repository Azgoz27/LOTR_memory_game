# this script holds the music and sounds

import pygame, os

# game music class declaration
class Music(object):

    # this is the constructor which declares variables for use within the class
    def __init__(self, intro, game, card, pair, over):
        pygame.mixer.pre_init(44100, -16, 2)
        pygame.init()
        self.intro_music = pygame.mixer.Sound(os.path.join("data/snd/",intro))
        self.game_music = pygame.mixer.Sound(os.path.join("data/snd/",game))
        self.card_soundFX = pygame.mixer.Sound(os.path.join("data/snd/",card))
        self.pair_soundFX = pygame.mixer.Sound(os.path.join("data/snd/",pair))
        self.game_over_music = pygame.mixer.Sound(os.path.join("data/snd/",over))
        self.no_pair_soundFX = pygame.mixer.Sound(os.path.join("data/snd/", card))
        self.semaphore = True # ensures only one backgroung music plays at a time
        self.clock = pygame.time

    # plays the intro (starting screen) music
    def play_intro(self):
        if(self.semaphore):
            self.intro_music.play(-1)
            self.semaphore = False

    # stops the intro (starting screen) music from playing
    def stop_intro(self):
        self.intro_music.stop()
        self.semaphore = True

    # plays the in game music
    def play_in_game(self):
        if(self.semaphore):
            self.game_music.play(-1)
            self.semaphore = False

    # pauses the in game music from playing
    def pause_in_game(self):
        pygame.mixer.pause() # pauses ALL current sounds
        self.semaphore = True

    # resumes the in game music from playing
    def resume_in_game(self):
        pygame.mixer.unpause()# unpauses ALL current sounds
        self.semaphore = False

    # stops the in game music from playing
    def stop_in_game(self):
        self.game_music.stop()
        self.semaphore = True

    # plays the card soundfx music
    def play_card_soundFX(self):
        self.card_soundFX.play()

    # plays the card "pair" music
    def play_pair_soundFX(self):
        self.pair_soundFX.play()

    # plays the "no pair" music
    def play_no_pair_soundFX(self):
        self.card_soundFX.play()

    # plays the game over music
    def play_game_over(self):
        if(self.semaphore):
            self.game_over_music.play(-1)
            self.semaphore = False

    # stop the game over music
    def stop_game_over(self):
        self.game_over_music.stop()
        self.semaphore = True


