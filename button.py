#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame.font  # lets Pygame render text to the screen


class Button():
    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the dimensions and the properties of the button
        self.width, self.height = 300, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)  # rendering text

        """The None argument tells Pygame to use the default font, and 48 determines the size of the text."""

        # build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the button message needs to be  prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        """   The font.render()
             method also takes a Boolean value
             to turn antialiasing on or off (antialiasing
            makes the edges of the text smoother)."""
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

# In[ ]:
