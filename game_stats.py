#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class GameStats():
    """Tracks statistics for the game"""
    
    def __init__(self,ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #start alien invasion in inactive state
        self.game_active = False
        
        #high score should never be reset
        self.high_score = 0
        
        
    def reset_stats(self):
        """Initialize statistics tha can be change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

