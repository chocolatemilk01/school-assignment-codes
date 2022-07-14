import sys
import os
import pygame
from time import sleep
from settings import *
from ve import *
from alien import *
from stats import *
from ui import *

#DON'T TOUCH
def resource_path(relative_path):
    try :
        base_path = sys._MEIPASS
        asset=resource_path('texture/ship_craft.png')
        asset1=resource_path('texture/bg.png')
        asset2=resource_path('texture/alien.png')
        assettPath=pygame.image.load(asset,asset1,asset2)
    except Exception :
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class AlienInvasion :
######START
    def __init__(self) :
        pygame.init()
        self.settings=settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.stats=stats(self)
        self.score=Score(self)
        self.ve=Vehicle(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()
        self.play=button(self,'Play')
    def run(self) :
        while True :
            self._check_events()
            if self.stats.game_active :
                self.ve.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.screen.blit(self.settings.back,[0,0])
            self.ve.blitme()

######INPUT & CHECK
    def _check_events(self) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT :
                    self.ve.moving_right=True
                elif event.key == pygame.K_LEFT :
                    self.ve.moving_left=True
            elif event.type == pygame.KEYUP :
                if event.key == pygame.K_RIGHT :
                    self.ve.moving_right=False
                elif event.key == pygame.K_LEFT :
                    self.ve.moving_left=False
    def _check_events(self) :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.KEYDOWN :
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP :
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse=pygame.mouse.get_pos()
                self._check_play(mouse)
    def _check_keydown_events(self,event) :
        if event.key == pygame.K_RIGHT :
            self.ve.moving_right=True
        elif event.key == pygame.K_LEFT :
            self.ve.moving_left=True
    def _check_keyup_events(self,event) :
        if event.key == pygame.K_RIGHT :
            self.ve.moving_right=False
        elif event.key == pygame.K_LEFT :
            self.ve.moving_left=False
        elif event.key == pygame.K_q :
            sys.exit()
        elif event.key == pygame.K_SPACE :
            self._fire_bullet()
    def _check_play(self,mouse) :
        click=self.play.rect.collidepoint(mouse)
        if click and not self.stats.game_active :
            self.settings.initDynamicSettings()
            self.stats.reset_stats()
            self.stats.game_active=True
            self.score._prep_score()
            self.score._prep_lvl()
            self.score._prep_ve()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ve.center_ship()
            pygame.mouse.set_visible(False)
    def _check_aliens_bottom(self) :
        screen_rect=self.screen.get_rect()
        for alien in self.aliens.sprites() :
            if alien.rect.bottom >= screen_rect.bottom :
                self._ship_hit()
                break
    def _check_fleet_edges(self) :
        for alien in self.aliens.sprites() :
            if alien.check_edges() :
                self._change_fleet_direction()
                break
    def _check_bullet_alien_collision(self) :
        collision=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if not self.aliens :
            self.stats.score+=self.settings.alien_point
            self.score._prep_score()
            self.bullets.empty()
            self._create_fleet()
            self.settings.speedIncrement()
            self.stats.level+=1
            self.score._prep_lvl()
        if collision :
            for aliens in collision.values() :
                self.stats.score+=self.settings.alien_point*len(aliens)
            self.score._prep_score()
            self.score._check_high()

######UPDATE & REFRESH
    def _update_bullets(self) :
        self.bullets.update()
        for bullet in self.bullets.copy() :
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)
        collision=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        self._check_bullet_alien_collision()
        if not self.aliens :
            self.bullets.empty()
            self._create_fleet()
    def _update_aliens(self) :
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ve,self.aliens) :
            self._ship_hit()
    def _update_screen(self) :
        self.screen.blit(self.settings.back,[0,0])
        self.ve.blitme()
        for bullet in self.bullets.sprites() :
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.score.draw()
        if not self.stats.game_active :
            self.play.draw()
        pygame.display.flip()

######ROWS OF ALIEN
    def _create_fleet(self) :
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        space_x=self.settings.screen_width-(2*alien_width)
        space_y=(self.settings.screen_height-(2*alien_height))-alien_height
        alienTotals=space_x//(2*alien_width)
        ship_height=self.ve.rect.height
        number_rows=space_y//(3*alien_height)
        for row in range(number_rows) :
            for alien_number in range(alienTotals) :
                self._create_alien(alien_number,row)
        for alien_number in range(alienTotals) :
            alien=Alien(self)
            alien.x=alien_width+2*alien_width+alien_number
            alien.rect.x=alien.x
            self.aliens.add(alien)
    def _create_alien(self,alien_number,row) :
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row
        self.aliens.add(alien)

######ETC
    def _ship_hit(self) :
        if self.stats.ship_left > 0 :
            self.stats.ship_left-=1
            self.score._prep_ve()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ve.center_ship()
            sleep(0.5)
        else :
            self.stats.game_active=False
            pygame.mouse.set_visible(True)
    def _fire_bullet(self) :
        if len(self.bullets) < self.settings.bullets_allowed :
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    def _change_fleet_direction(self) :
        for alien in self.aliens.sprites() :
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1

######RUN
if __name__ == '__main__' :
    ai=AlienInvasion()
    ai.run()
#main