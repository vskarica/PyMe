"""# Moving a pygame window with Tkinter.
# Used code from:
#    https://stackoverflow.com/questions/8584272/using-pygame-features-in-tkinter
#    https://stackoverflow.com/questions/31797063/how-to-move-the-entire-window-to-a-place-on-the-screen-tkinter-python3

import tkinter as tk
import os, random

w, h = 400, 500

# Tkinter Stuffs
root = tk.Tk()
embed = tk.Frame(root, width=w, height=h)
embed.pack()

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib' # This was needed to work on my windows machine.

root.update()

# Pygame Stuffs
import pygame
pygame.display.init()
screen = pygame.display.set_mode((w, h))

# This just gets the size of your screen (assuming the screen isn't affected by display scaling).
screen_full_size = pygame.display.list_modes()[0]

# Basic Pygame loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

            if event.key == pygame.K_SPACE:
                # Press space to move the window to a random location.
                r_w = random.randint(0, screen_full_size[0])
                r_h = random.randint(0, screen_full_size[1])
                root.geometry("+"+str(r_w)+"+"+str(r_h))

    # Set to green just so we know when it is finished loading.
    screen.fill((0, 220, 0))

    pygame.display.flip()

    root.update()

pygame.quit()
root.destroy()"""
x=100
y=0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)

#create a display
import pygame
pygame.init()
screen=pygame.display.set_mode((100,100))

#wait before moving the display
import time
time.sleep(2)

#set where the display will move to
x=200
y=200
os.environ['SDL_VIDEO_WINDOW_POS']='%d,%d' %(x,y)

#resize the screen causing it to move to x y set by environ
pygame.display.set_mode((101,100))

#set the size back to normal
pygame.display.set_mode((100,100))