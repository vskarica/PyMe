# Simple pygame program https://realpython.com/pygame-a-primer/

# Import and initialize the pygame library
import pygame
# Import random for random numbers
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Setup for sounds. Defaults are good.
pygame.mixer.init()
# Initialize pygame
pygame.init()

# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("Apoxode_-_I_Can_t_Stop.mp3")#Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)
# Load all sound files
# Sound sources: Jon Fincher
##move_up_sound = pygame.mixer.Sound("Rising_putter.ogg")
##move_down_sound = pygame.mixer.Sound("Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("Explosion3.wav")
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        #self.surf.fill((255, 255, 255))
        pygame.draw.circle(self.surf, (0,0,0), (0,0), 5)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            #move_up_sound.play()
            pygame.draw.circle(self.surf, (0,0,0), (10,10), 5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            #move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        #self.surf = pygame.Surface((20, 10))
        #self.surf.fill((255, 255, 255))
        self.surf = pygame.image.load("missle.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surf0 = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#zodavanje pomaknutog zumiranog elementa na površinu
def addEllToSurf(surf1,surf2,shift=(0,0),zoom=1):
    surf2WH=surf2.get_size()
    shift=(
        int(round(shift[0]*zoom)),
        int(round(shift[1]*zoom)))

    surf1.blit(
        pygame.transform.scale(
            surf2,
            (
                int(round(surf2WH[0]*zoom)),
                int(round(surf2WH[1]*zoom)))),
        shift)
    #print(surf2.get_size())

# Run until the user asks to quit
running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            print(KEYDOWN)
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update the position of enemies and clouds
    enemies.update()
    clouds.update()

    # Fill the screen with sky blue
    #screen.fill((135, 206, 250))
    surf0.fill((135, 206, 250))
    ###################
    # Draw a solid blue circle in the center
    #krug=pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    krug=pygame.draw.circle(surf0, (0, 0, 255), (250, 250), 75)
    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((300, 300))
    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    imgg = pygame.image.load("missle.png")#.convert()
    imgg.set_colorkey((255, 255, 255), RLEACCEL)
    addEllToSurf(surf,imgg,(0,0),2)
    surf.blit(imgg,(10,10))
    #rect = surf.get_rect()
    # Put the center of surf at the center of the display
    surf_center = (
        (SCREEN_WIDTH-surf.get_width())/2,
        (SCREEN_HEIGHT-surf.get_height())/2
    )
    # This line says "Draw surf onto the screen at the center"
    #screen.blit(surf, surf_center)
    surf0.blit(surf, surf_center)
    ###################
    
    # Draw all sprites
    for entity in all_sprites:
        #screen.blit(entity.surf, entity.rect)
        surf0.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        # Stop any moving sounds and play the collision sound
        ##move_up_sound.stop()
        ##move_down_sound.stop()
        collision_sound.play()
        # Stop the loop
        running = False

    # Draw the player on the screen
    #screen.blit(player.surf, player.rect)#(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    surf0.blit(player.surf, player.rect)#(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    #screen.blit(surf0, (0,0))#(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    addEllToSurf(screen,surf0,(0,0),1)   

    # Flip everything to the display
    pygame.display.flip()



    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# All done! Stop and quit the mixer.

pygame.mixer.music.stop()
pygame.mixer.quit()
# Done! Time to quit.
pygame.quit()