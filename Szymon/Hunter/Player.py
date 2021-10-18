import pygame
import RPi.GPIO as GPIO
adc = MCP3008()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(31,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(33,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(32,GPIO.IN,pull_up_down=GPIO.PUD_UP)
class Player(pygame.sprite.Sprite):

    def __init__(self,screen):
        self.image_= pygame.image.load("celownik.png")
        self.screen_=screen
        self.rect_=self.image_.get_rect()
        self.x_ = 240
        self.y_ = 160
        self.zycia_=3
        self.punkty_=0
        self.counter_a=0
        self.szerokosc_ = self.image_.get_width()
        self.wysokosc_ = self.image_.get_height()

    def draw(self):
        self.screen_.blit(self.image_, self.rect_)
        self.rect_.center = [self.x_, self.y_]

    def move(self,dx,dy):
        if self.x_+dx-self.szerokosc_/2>0 and self.x_+ dx+self.szerokosc_/2 < 480 and self.y_+dy>0 and self.y_+dy<320:
                self.x_+=dx
                self.y_+=dy

    def sterowanie(self,dx,dy):
        dx = 0
        dy = 0
        if pygame.key.get_pressed()[pygame.K_LEFT] or adc.read(channel=2) > 600 or GPIO.input(33) == 0:
            dx -= 9
        if pygame.key.get_pressed()[pygame.K_RIGHT] or adc.read(channel=2) < 50 or GPIO.input(31) == 0:
            dx += 9
        if pygame.key.get_pressed()[pygame.K_UP] or adc.read(channel=1) < 50 or GPIO.input(32) == 0:
            dy -= 9
        if pygame.key.get_pressed()[pygame.K_DOWN] or adc.read(channel=1) > 600 or GPIO.input(37) == 0 :
            dy += 9
        self.move(dx, dy)

    def napisy(self, screen, font_style):
        text_zycia = font_style.render("Życia: " + str(self.zycia_), True, (255, 255, 0))
        screen.blit(text_zycia, [0, 0])
        text_zycia = font_style.render("Punkty: " + str(self.punkty_), True, (255, 255, 0))
        screen.blit(text_zycia, [0, 20])
