import pygame
import time
import random

# Set Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Snakes Speed
snakespeed = 250

# Tail Length
snakeTailLength = 5

# Screen
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200

# Creates The Sprites Group
allSprites = pygame.sprite.Group()
player1tailgroup = pygame.sprite.Group()
player2tailgroup = pygame.sprite.Group()
killGroup = pygame.sprite.Group()

def player1KeyHandler(keys):
    
    if keys[pygame.K_w]:
        player1.ismoveingforward = True
        player1.ismoveingleft = False
        player1.ismoveingright = False
        player1.ismoveingdown = False

    if keys[pygame.K_a]:
        player1.ismoveingforward = False
        player1.ismoveingleft = True
        player1.ismoveingright = False
        player1.ismoveingdown = False

    if keys[pygame.K_d]:
        player1.ismoveingforward = False
        player1.ismoveingleft = False
        player1.ismoveingright = True
        player1.ismoveingdown = False

    if keys[pygame.K_s]:
        player1.ismoveingforward = False
        player1.ismoveingleft = False
        player1.ismoveingright = False
        player1.ismoveingdown = True

def player2KeyHandler(keys):
    if keys[pygame.K_UP]:
        player2.ismoveingforward = True
        player2.ismoveingleft = False
        player2.ismoveingright = False
        player2.ismoveingdown = False

    if keys[pygame.K_LEFT]:
        player2.ismoveingforward = False
        player2.ismoveingleft = True
        player2.ismoveingright = False
        player2.ismoveingdown = False

    if keys[pygame.K_RIGHT]:
        player2.ismoveingforward = False
        player2.ismoveingleft = False
        player2.ismoveingright = True
        player2.ismoveingdown = False

    if keys[pygame.K_DOWN]:
        player2.ismoveingforward = False
        player2.ismoveingleft = False
        player2.ismoveingright = False
        player2.ismoveingdown = True


# Initialize Pygame
pygame.init()

# Set the height and width of the screen

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Updates Screen
pygame.display.update()

# You can only have a max of 20 FPS
clock = pygame.time.Clock()
clock.tick(60)

# Creates Player
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Adds it's self to the all sprites group
       allSprites.add(self)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

       # Starts Sprites In Random Position
       self.rect.x = random.randrange(0, SCREEN_WIDTH)
       self.rect.y = random.randrange(0, SCREEN_HEIGHT)

       self.ismoveingforward = False
       self.ismoveingleft = True
       self.ismoveingright = False
       self.ismoveingdown = False
       
    def moveForward(self, milliseconds):
        if milliseconds % snakespeed == 0 :
            if self.ismoveingforward :
                self.rect.y = self.rect.y - 5
                screen.fill(WHITE)
                allSprites.draw(screen)
                pygame.display.flip()

    def moveLeft(self, milliseconds):
        if milliseconds % snakespeed == 0 :
            if self.ismoveingleft :
                self.rect.x = self.rect.x - 5
                screen.fill(WHITE)
                allSprites.draw(screen)
                pygame.display.flip()

    def moveRight(self, milliseconds):
        if milliseconds % snakespeed == 0 :
            if self.ismoveingright :
                self.rect.x = self.rect.x + 5
                screen.fill(WHITE)
                allSprites.draw(screen)
                pygame.display.flip()

    def moveDown(self, milliseconds):
        if milliseconds % snakespeed == 0 :
            if self.ismoveingdown :
                self.rect.y = self.rect.y + 5
                screen.fill(WHITE)
                allSprites.draw(screen)
                pygame.display.flip()

class SnakeTail(pygame.sprite.Sprite):
    def __init__(self, color, width, height, player):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Adds it's self to the all sprites group
       allSprites.add(self)
       if player == player1:
           player1tailgroup.add(self)
           
       if player == player2:
           player2tailgroup.add(self)
       
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       
       # When It Gets Added It Goes To The Player 
       self.rect.x = player.rect.x
       self.rect.y = player.rect.y

    def killSelf(self):
        pygame.sprite.Sprite.kill(self)

       


player1 = Player(RED, 10, 10)
player2 = Player(BLUE, 10, 10)


while True:

    # Time In Milliseconds
    millis = int(round(time.time()*1000))
    
    # Moves Player Forward
    player1.moveForward(millis)
    player1.moveLeft(millis)
    player1.moveRight(millis)
    player1.moveDown(millis)
    player2.moveForward(millis)
    player2.moveLeft(millis)
    player2.moveRight(millis)
    player2.moveDown(millis)

    if millis % snakespeed == 0 :
        player1snaketail = SnakeTail(RED, 10, 10, player1)
        player2snaketail = SnakeTail(BLUE, 10, 10, player2)
        if len(pygame.sprite.Group.sprites(player1tailgroup)) == 10:
            player1snaketail.killSelf()
    
    for event in pygame.event.get() :
        
        keys = pygame.key.get_pressed()

        player1KeyHandler(keys)
        player2KeyHandler(keys)

        # Clear Screen And Make It White
        screen.fill(WHITE)

        # Draws All Sprites
        allSprites.draw(screen)

        # Updates The Screen
        pygame.display.flip()
