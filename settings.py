import pygame
from pygame.locals import *

pygame.init()

class settings :
    def __init__(self) :
        self.screen_width=1366 #In pixels
        self.screen_height=768 #in pixels
        self.back=pygame.image.load('texture/bg.png')
        self.ship_limit=3
        self.bullet_width=6
        self.bullet_height=12
        self.bullet_color=(255,175,55)
        self.bullets_allowed=100000000
        self.speed_scale=1.25
        self.score_scale=1.5
        self.fleet_direction=1
        self.initDynamicSettings()
    def initDynamicSettings(self) :
        self.ship_speed=2
        self.bullet_speed=2
        self.alien_speed=1
        self.fleet_drop_speed=2
        self.alien_point=15
    def speedIncrement(self) :
        self.ship_speed*=self.speed_scale ; self.bullet_speed*=self.speed_scale ; self.alien_speed*=self.speed_scale ; self.fleet_drop_speed*=self.speed_scale
        self.alien_point=int(self.score_scale*self.alien_point)
#settings