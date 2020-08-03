import pygame
import requests

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Chat Game")


class Bot(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 40


class ChatBG:
    def __init__(self, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def redraw_game_window():
    win.fill((0, 75, 50))
    pygame.draw.rect(win, (0, 140, 160), (bot.x, bot.y, bot.width, bot.height))
    pygame.draw.rect(win, (96, 96, 96), (chatbg.x, chatbg.y, chatbg.width, chatbg.height))
    text = font.render("Click Enter to chat...", 1, (255, 255, 255))
    win.blit(text, (0, 470))
    pygame.display.update()


# Main Loop
bot = Bot(210, 240, 40, 60)
chatbg = ChatBG(0, 465, 300, 40)
font = pygame.font.SysFont("Calibri", 30, True, True)   # font, size, bold, italicized
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and bot.x > bot.vel:
        bot.x -= bot.vel
    if keys[pygame.K_RIGHT] and bot.x < 500:
        bot.x += bot.vel
    if keys[pygame.K_UP]:
        bot.y -= bot.vel
    if keys[pygame.K_DOWN]:
        bot.y += bot.vel
    #if keys[pygame.K_RETURN]:
        #

    redraw_game_window()

pygame.quit()