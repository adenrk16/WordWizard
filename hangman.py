# Word Wizard - Hangman Game
# Created by Sohan K. and Aden K.

# imports
import pygame
import math
import random
from tkinter import messagebox 

# setup display
pygame.init()
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Wizard - Hangman Game")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
# create the alphabet on the screen to allow the user to select letters
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 65)

# load images of the hangman
images = []
for i in range(10):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)




# game variables
hangman_status = 0
wordsForOnePlayer = ["PAINT", "DREAM", "BRAVE", "GAME", "WORD", "STORM"]
wordForOnePlayer = random.choice(wordsForOnePlayer)
guessed = []




# colors
GAME_BGCOLOR = (56, 116, 219)
BLACK = (0, 0, 0)


# draw the setup for the game - the title, words, and the buttons
def draw():
    win.fill(GAME_BGCOLOR)

    # draw title
    titleText = TITLE_FONT.render("Hangman", 1, BLACK)
    win.blit(titleText, (WIDTH / 2 - titleText.get_width() / 2, 20))

    # draw instructions button for game

    # draw return to main menu button for game

    # draw word blanks
    display_word = ""
    for letter in wordForOnePlayer:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))



    pygame.display.update()


# main program
def main():
    global hangman_status, wordForOnePlayer, guessed

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in wordForOnePlayer:
                                hangman_status += 1

        draw()

        won = True
        for letter in wordForOnePlayer:
            if letter not in guessed:
                won = False
                break
        if won:
            result = messagebox.askquestion("GOOD JOB!, Play Again?", "Do you want to play again?")
            if result == 'no':
                import main
            else:
                # reset game variables
                hangman_status = 0
                guessed = []
                wordForOnePlayer = random.choice(wordsForOnePlayer)
                for letter in letters:
                    letter[3] = True
        if hangman_status == 9:
            result = messagebox.askquestion("YOU LOST, Play Again?", "Do you want to play again?")
            if result == 'no':
                import main
            else:
                # reset game variables
                hangman_status = 0
                guessed = []
                wordForOnePlayer = random.choice(wordsForOnePlayer)
                for letter in letters:
                    letter[3] = True




while True:
    main()
pygame.quit()






