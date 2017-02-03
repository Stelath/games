import pygame
import time
import random

# Set Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Screen
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200

# Creates The Sprites Group
allSprites = pygame.sprite.Group()

# Creates The Player Color Variables
player1color = "RED"
player2color = "BLUE"

def isEscape(keys):
    return keys[27]

def getMovementKeys(keys):
    return keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d], keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT]

def MoveCharacter(keys, Wkey, Akey, Skey, Dkey, upArrow, downArrow, leftArrow, rightArrow):
    if Wkey == 1:
        #print "W Key Was Pressed"
        if player1.rect.y - 5 >= 0 :
            player1.rect.y = player1.rect.y - 5

    if Akey == 1:
        #print "A Key Was Pressed"
        if player1.rect.x - 5 >= 0 :
            player1.rect.x = player1.rect.x - 5

    if Skey == 1:
        #print "S Key Was Pressed"
        if player1.rect.y + 15 <= SCREEN_HEIGHT :
            player1.rect.y = player1.rect.y + 5
        
    if Dkey == 1:
        #print "D Key Was Pressed"
        if player1.rect.x + 15 <= SCREEN_WIDTH :
            player1.rect.x = player1.rect.x + 5

    if upArrow == 1:
        #print "Up Arrow Was Pressed"
        if player2.rect.y - 5 >= 0 :
            player2.rect.y = player2.rect.y - 5

    if downArrow == 1:
        #print "Down Arrow Was Pressed"
        if player2.rect.y + 15 <= SCREEN_HEIGHT :
            player2.rect.y = player2.rect.y + 5

    if leftArrow == 1:
        #print "Left Arrow Was Pressed"
        if player2.rect.x - 5 >= 0 :
            player2.rect.x = player2.rect.x - 5
        
    if rightArrow == 1:
        #print "Right Arrow Was Pressed"
        if player2.rect.x + 15 <= SCREEN_WIDTH :
            player2.rect.x = player2.rect.x + 5

def changeColor(keys):

    global player1color
    global player2color
    
    if keys[pygame.K_c] and player1color == "RED":
        player1.changeColor(GREEN)
        player1color = "GREEN"
        time.sleep(0.1)

    elif keys[pygame.K_c] and player1color == "GREEN":
        player1.changeColor(RED)
        player1color = "RED"
        time.sleep(0.1)
        
    if keys[pygame.K_RCTRL] and player2color == "BLUE":
        player2.changeColor(BLACK)
        player2color = "BLACK"

    elif keys[pygame.K_RCTRL] and player2color == "BLACK":
        player2.changeColor(BLUE)
        player2color = "BLUE"


        
# Initialize Pygame
pygame.init()

# Set the height and width of the screen

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Updates Screen
pygame.display.update()

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

    def changeColor(self, color):
        self.image.fill(color)

player1 = Player(RED, 10, 10)
player2 = Player(BLUE, 10, 10)

# Sets Key Down Events
pygame.key.set_repeat(10, 10)

while True :
    
    for event in pygame.event.get() :
        keys = pygame.key.get_pressed()
        
        if isEscape(keys):
            pygame.quit()

        if getMovementKeys(keys):
            Wkey, Akey, Skey, Dkey, upArrow, downArrow, leftArrow, rightArrow = getMovementKeys(keys)
            MoveCharacter(keys, Wkey, Akey, Skey, Dkey, upArrow, downArrow, leftArrow, rightArrow)

        if pygame.sprite.collide_rect(player1, player2):
            print "COLLISION!!!"
            pygame.quit()

        changeColor(keys)
            

    # Clear Screen And Make It White
    screen.fill(WHITE)

    # Draws All Sprites
    allSprites.draw(screen)

    # Updates The Screen
    pygame.display.flip()

    # You can only have a max of 20 FPS
    clock = pygame.time.Clock()
    clock.tick(60)
    
