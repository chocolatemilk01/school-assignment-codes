import pygame.font
from pygame.sprite import Group
from sympy import true

class button :
    def __init__(self,ai_game,msg) :
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.width,self.height=210,65
        self.button_color=(255, 255, 255)
        self.text_color=(9, 68, 219)
        self.font=pygame.font.SysFont('Inter',48)
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        self._prep_msg(msg)
    def _prep_msg(self,msg) :
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw(self) :
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

class Score :
    def __init__(self,ai_game) :
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings
        self.stats=ai_game.stats
        self.text_color=(255,255,255)
        self.text_color1=(255,255,0)
        self.text_color2=(0,255,0)
        self.text_color3=(255,0,0)
        self.font=pygame.font.SysFont('Inter',42)
        self._prep_score()
        self._prep_highest()
        self._prep_lvl()
        self._prep_ve()
    def _prep_score(self) :
        rounded_up=round(self.stats.score,-1)
        scStr='{:,}'.format(rounded_up)
        self.scImg=self.font.render(scStr,True,self.text_color)
        self.score_rect=self.scImg.get_rect()
        self.score_rect.right=self.screen_rect.right-45
        self.score_rect.top=45
    def _prep_highest(self) :
        rounded_up=round(self.stats.highest,-1)
        high_scStr='{:,}'.format(rounded_up)
        self.high_scImg=self.font.render(high_scStr,True,self.text_color1)
        self.high_sc_rect=self.high_scImg.get_rect()
        self.high_sc_rect.centerx=self.screen_rect.centerx
        self.high_sc_rect.top=self.score_rect.top
    def _prep_lvl(self) :
        lvlStr=str(self.stats.level)
        self.lvlImg=self.font.render(lvlStr,True,self.text_color2)
        self.lvl_rect=self.lvlImg.get_rect()
        self.lvl_rect.right=self.score_rect.right
        self.lvl_rect.top=self.score_rect.bottom+10
    def _prep_ve(self) :
        veStr=str(self.stats.ship_left)
        self.veImg=self.font.render(veStr,True,self.text_color3)
        self.ve_rect=self.veImg.get_rect()
        self.ve_rect.left=self.ve_rect.right
        self.ve_rect.top=45
    def _check_high(self) :
        if self.stats.score > self.stats.highest :
            self.stats.highest=self.stats.score
            self._prep_highest()
    def draw(self) :
        self.screen.blit(self.scImg,self.score_rect)
        self.screen.blit(self.high_scImg,self.high_sc_rect)
        self.screen.blit(self.lvlImg,self.lvl_rect)
        self.screen.blit(self.veImg,self.ve_rect)
#user interface