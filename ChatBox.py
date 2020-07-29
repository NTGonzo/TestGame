import pygame

pygame.init()

validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
wordList = ["Forward", "Backward", "Left", "Right"]


class TextBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.text = ""
        self.font = pygame.font.Font(None, 50)
        self.image = self.font.render("Choose direction", False, [0, 0, 0])
        self.rect = self.image.get_rect()

    def add_chr(self, char):
        global shiftDown
        if char in validChars and not shiftDown:
            self.text += char
        elif char in validChars and shiftDown:
            self.text += shiftChars[validChars.index(char)]
        self.update()

    def update(self):
        old_rect_pos = self.rect.center
        self.image = self.font.render(self.text, False, [0, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.center = old_rect_pos


screen = pygame.display.set_mode([500, 500])
textBox = TextBox()
shiftDown = False
textBox.rect.center = [145, 485]

run = True
while run:
    screen.fill([0, 140, 160])
    screen.blit(textBox.image, textBox.rect)
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if keys[pygame.K_LSHIFT]:
                shiftDown = False
        if event.type == pygame.KEYDOWN:
            textBox.add_chr(pygame.key.name(event.key))
        if keys[pygame.K_SPACE]:
            textBox.text += " "
            textBox.update()
        if keys[pygame.K_LSHIFT]:
            shiftDown = True
        if keys[pygame.K_BACKSPACE]:
            textBox.text = textBox.text[:-1]
            textBox.update()
        if keys[pygame.K_RETURN]:
            if len(textBox.text) > 0:
                print(textBox.text)
                running = False

pygame.quit()
