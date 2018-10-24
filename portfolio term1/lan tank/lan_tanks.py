##koty butler
##sept 17, 2018
##first draft of game for project
##
##SPECIAL THANKS TO MONTY52_DRE FOR THE CAMERA CODE

import pygame
from pygame import *
import random as rd #although not yet used will be soon
WIN_WIDTH = 800
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)
#rd.seed(667, 2)
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

def main():
    global cameraX, cameraY
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("KOTY B level with easy editor")
    timer = pygame.time.Clock()

    up = down = left = right = running = False
    bg = Surface((32,32))
    bg.convert()
    bg.fill(Color("#001080"))
    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []

    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P P                                         P",
        "P P                                         P",
        "P P                             PPPPPEEEPPP P",
        "P P                                         P",
        "P P                         PPPPPPPPP       P",
        "P P                                         P",
        "P P   PPPPPPPP                              P",
        "P P                                         P",
        "P P                         PPPPPPP         P",
        "P P                                         P",
        "P P    CCCCC                                P",
        "P P                                         P",
        "P P                   PPPPPPPPPPP           P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                             PPPPP   PPP P",
        "P P                                         P",
        "P P                         PPPPPPPPP       P",
        "P P                                         P",
        "P P   PPPPPPPP                              P",
        "P P                                         P",
        "P P                         PPPPPPP         P",
        "P P                                         P",
        "P P    CCCCC                                P",
        "P P                                         P",
        "P P                   PPPPPPPPPPP           P",
        "P P                                         P",
        "P P             PPPPPPPPP                   P",
        "P P                                         P",
        "P P   PPPPPPPP                              P",
        "P P                                         P",
        "P P                         PPPPPPP         P",
        "P P                PPPPPP                   P",
        "P P                                         P",
        "P P        PPPPPPP                          P",
        "P P     C                                   P",
        "P P                    PPPPPP   PPPPPP      P",
        "P P                                         P",
        "P P  PPPPPPPPPPP                            P",
        "P P                                         P",
        "P P                PPPPPPPPPPP              P",
        "P P                                         P",
        "P P                                         P",
        "P P        P                 CCCCC          P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P       P                                 P",
        "P P                             PPPPP   PPP P",
        "P P                                         P",
        "P P                         PPPPPPPPP       P",
        "P P                                         P",
        "P P   PPPPPPPP                              P",
        "P P                                         P",
        "P P                         PPPPPPP         P",
        "P P                                         P",
        "P P    CCCCC                                P",
        "P P                                         P",
        "P P                   PPPPPPPPPPP           P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P          B                  PPPPP   PPP P",
        "P P                                         P",
        "P P                         PPPPPPPPP       P",
        "P P                                         P",
        "P P   PPPPPPPP                              P",
        "P P                                         P",
        "P P               B         PPPPPPP         P",
        "P P                                         P",
        "P P    CCCCC                                P",
        "P P                                         P",
        "P P                   PPPPPPPPPPP           P",
        "P P                                         P",
        "P P             PPPPPPPPP                   P",
        "P P                                         P",
        "P P   PPPPPPPP                              P",
        "P P                                         P",
        "P P                         PPPPPPP         P",
        "P P                PPPPPP                   P",
        "P P                                         P",
        "P P        PPPPPPP                          P",
        "P P     C                                   P",
        "P P                    PPPPPP   PPPPPP      P",
        "P P                                         P",
        "P P  PPPPPPPPPPP                            P",
        "P P                                         P",
        "P P                PPPPPPPPPPP              P",
        "P P                                         P",
        "P                                           P",
        "P                            CCCCC          P",
        "P                                           P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]

    level2 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P    BB                                   P",
        "P P                                         P",
        "P P                                         P",
        "P P                                        BP",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P            PP           PPPP            P",
        "P P           P                             P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P PPPPPPPPPP                                P",
        "P P                                         P",
        "P P                                         P",
        "P P                        PPP              P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                    BBBB                 P",
        "P P                                         P",
        "P P                                         P",
        "P      CCCC                                 P",
        "P                                           P",
        "P                                           P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    level3 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PcP                                    EEE  P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "PcP                                         P",
        "Pcc                                         P",
        "Pcc                                         P",
        "Pcc                                         P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    level4 = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P P                                         P",
        "P                                           P",
        "P                                           P",
        "P                                           P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]


















    value = int(99)
    
    # build the level
    for row in level3: #switch to level2 to do level2
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "C":
                 k = Kill(x, y)
                 platforms.append(k)
                 entities.add(k)
            if col == "B":
                 b = Boost(x, y)
                 platforms.append(b)
                 entities.add(b)
            if col == " ":
                if(rd.randint(0, 100)>value):
                    p = Platform(x, y)
                    platforms.append(p)
                    entities.add(p)
            x += 32
        y += 32
        x = 0


    total_level_width  = len(level[0])*32
    total_level_height = len(level)*32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)

        for e in pygame.event.get():
          #  if e.type == QUIT: raise SystemExit, "QUIT"
          #  if e.type == KEYDOWN and e.key == K_ESCAPE:
           #     raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        # draw background
        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x * 32, y * 32))

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
       # hits = pygame.sprite.spritecollide(Player, Boost, False)
        #if hits: boost = True
        pygame.display.update()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32,32))
        self.image.fill(Color("#0000FF"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self, up, down, left, right, running, platforms):
        if up:
            # only jump if on the ground
            self.yvel -= 8
        
 #       if running:
  #          self.xvel = 12
        if left:
            self.xvel = -8
        if right:
            self.xvel = 8
        if down:
            self.yvel = 6
        #if boost:
         #   self.yvel = -10

  #      if not(left or right):
   #         self.yvel = 0
  #      if not(up or down):
  #         self.xvel = 0
        # increment in x direction
            self.rect.left += self.xvel
        # do x-axis collisions
            self.collide(self.xvel, 0, platforms)
        # increment in y direction
            self.rect.top += self.yvel

        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print ("collide right")
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print ("collide left")
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom


class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#DDDDDD"))
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))

class Boost(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#6d1543"))
        self.rect = Rect(x, y, 32, 32)



class Kill(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#59f442"))
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass











    

if __name__ == "__main__":
    main()
