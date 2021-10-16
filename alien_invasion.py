#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship  # Ship is a class
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # initialize game and create a screen object
    pygame.init()  # initializes background settings that Pygame needs to work properly.
    ai_settings = Settings()  # color y tamaño de pantalla
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # instancia where screen are shown
    pygame.display.set_caption("Alien Invasion by JC")  # titulo de la ventana emergente

    # make the Play button
    play_button = Button(ai_settings, screen, "Press P to play")

    # create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # make a ship
    ship = Ship(ai_settings, screen)  # instancia de la clase Ship
    # make a group to store bullets in
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    music = pygame.mixer.music.load("C:/Users/Jose/Documents/python/GENERAL STUFF/Alien Invasion/bg_music.mp3")
    pygame.mixer.music.play(-1)

    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)  # elimina las balas frias como el ferras
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()

# In[ ]:


# In[ ]:
