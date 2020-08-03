import pygame   #imports pygame cmds

pygame.init()   #initializes pygame modules

win = pygame.display.set_mode((800, 600))      #size of window

pygame.display.set_caption("Twitch Chat")

screenheight = 800
screenwidth = 600


class Player(object):     #defining robot parameters
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 15
        self.left = False
        self.right = False
        self.WalkCount = 0
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):

        pygame.draw.rect(win, (0, 140, 160), self.hitbox, 2)


def redraw_game_window():
    bot.draw(win)

    pygame.display.update()


#Main Loop
bot = Player(300, 410, 64, 64)  #x, y, width, height
run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and bot.x > bot.velocity:
        bot.x -= bot.velocity
        bot.left = True
        bot.right = False
    elif keys[pygame.K_RIGHT] and bot.x < 500 - bot.width - bot.velocity:
        bot.x += bot.velocity
        bot.right = True
        bot.left = False


pygame.quit()


