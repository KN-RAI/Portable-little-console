import pygame
import time
class Player(pygame.sprite.Sprite):

    def __init__(self,screen):

        self.image_= pygame.image.load("celownik.png").convert()
        self.screen_=screen
        self.rect_=self.image_.get_rect()
        self.x_ = 240
        self.y_ = 160






    def draw(self):
        self.screen_.blit(self.image_, self.rect_)
        self.rect_.center = [self.x_, self.y_]


    def move(self,dx,dy):
        if self.x_+dx-3>0 and self.x_+ dx+3 < 475 and self.y_+dy>0 and self.y_+dy<320:
                self.x_+=dx
                self.y_+=dy


    def sterowanie(self,dx,dy):
        dx = 0
        dy = 0
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            dx -= 8
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            dx += 8
        if pygame.key.get_pressed()[pygame.K_UP]:
            dy -= 8
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            dy += 8
        self.move(dx, dy)