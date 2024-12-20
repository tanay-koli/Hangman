import pygame
import random
import time

pygame.init()
pygame.font.init()

width, height = 1050, 700
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("HANGMAN")

Border = (0, 0, 0)
Whiteboard = (255, 255, 255)
Black = (0, 0, 0)
X_guess_font = pygame.font.SysFont("comicsansms", 20)
txt_font = pygame.font.SysFont("comicsansms", 25)
guess_font = pygame.font.SysFont("comicsansms", 30)
finish_font = pygame.font.SysFont("comicsansms", 50)

def text_object(text, font):
    textSurface = font.render(text, True, Black)
    return textSurface, textSurface.get_rect()

def draw_text(text, x, y, font):
    textSurf, textRect = text_object(text, font)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)

def clear_screen():
    gameDisplay.fill(Border)
    pygame.draw.rect(gameDisplay, Whiteboard, pygame.Rect(33, 30, 975, 645))

def redraw_window():
    global limbs, guess, word, incorrect_guesses, gameImgs
    limbs = min(limbs, len(gameImgs) - 1)
    gameDisplay.blit(gameImgs[limbs], (150, 180))
    display_word = " ".join([letter if letter in guess else "_" for letter in word])
    draw_text(display_word, 525, 600, guess_font)
    draw_text(f"Wrong Guesses: {', '.join(incorrect_guesses)}", 675, 75, X_guess_font)

def random_word():
    with open("words.txt") as file:
        words = file.readlines()
    return random.choice(words).strip()

def check_game_status():
    global inGame
    if all(letter in guess for letter in word):
        draw_text("YOU WON :)", 600, 180, finish_font)
        pygame.display.update()
        time.sleep(2)
        reset()
    elif limbs == len(gameImgs) - 1:
        draw_text(f"YOU LOST :( \nWord: {word}", 600, 180, finish_font)
        pygame.display.update()
        time.sleep(2)
        reset()

def reset():
    global limbs, guess, word, incorrect_guesses
    limbs = 0
    guess = []
    incorrect_guesses = []
    word = random_word()

limbs = 0
guess = []
incorrect_guesses = []
word = random_word()
gameImgs = [pygame.image.load(f"hang{i}.png") for i in range(1, 8)]
inGame = True

def main_loop():
    global limbs, guess, incorrect_guesses, word, inGame
    while inGame:
        clear_screen()
        draw_text("Press SPACE to Start a New Game", 525, 450, txt_font)
        redraw_window()
        check_game_status()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inGame = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset()

                elif pygame.K_a <= event.key <= pygame.K_z:
                    letter = event.unicode.lower()
                    if letter in guess or letter in incorrect_guesses:
                        draw_text("Letter already guessed", 675, 345, txt_font)
                        pygame.display.update()
                        time.sleep(1)
                    elif letter not in word:
                        draw_text(f"The letter {letter} is not in the word", 675, 345, txt_font)
                        limbs += 1
                        incorrect_guesses.append(letter)
                        pygame.display.update()
                        time.sleep(1)
                    else:
                        guess.append(letter)

main_loop()
pygame.quit()
