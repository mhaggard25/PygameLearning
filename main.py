# This is from my Python programming book. My addition is that I am going to make the rectangle
# randomly change colors everytime it touches the wall.

# Import pygame
import pygame, sys, random
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set the screen up
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Circles and Rectangles and Stuff")

# To draw text, we have to create the font object
myfont = pygame.font.Font(None, 60)

# Color variables
white = 255, 255, 255
blue = 0, 0, 255
red = 255, 0, 0
green = 0, 255, 0
black = 0, 0, 0
yellow = 255, 255, 0
pink = 255, 0, 255
purple = 127, 0, 255

# Other variables
position = 300, 300
radius = 100
width = 10

pos_x = 300
pos_y = 250
vel_x = 1
vel_y = 1
rect_width = 0
rect_pos = pos_x, pos_y, 100, 100

color = [white, blue, red, green, black, yellow, pink, purple]
newColor = white
circleColor = white
textColor = white

running = True

while running:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            running = False

    # Actually draw stuff and update the display
    screen.fill(black)

    # Make the rectangle move
    pos_x += vel_x
    pos_y += vel_y

    # Keep the rectangle on the screen
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
        newColor = color[random.randint(0, len(color)-1)]
        textColor = color[random.randint(0,len(color)-1)]
        circleColor = color[random.randint(0, len(color)-1)]
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y
        newColor = color[random.randint(0, len(color)-1)]
        textColor = color[random.randint(0, len(color)-1)]
        circleColor = color[random.randint(0, len(color)-1)]

    # Update the rectangle's position

    rect_pos = pos_x, pos_y, 100, 100

    # Draw a rectangle
    pygame.draw.rect(screen, newColor, rect_pos, rect_width)

    # Draw a circle
    pygame.draw.circle(screen, circleColor, position, radius, width)

    # Draw text to the screen
    textImage = myfont.render("Hello Pygame", True, textColor)

    # Show text to the screen
    screen.blit(textImage, (100, 100))

    pygame.display.update()

sys.exit()
