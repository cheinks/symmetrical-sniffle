import pygame
import random


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Bot(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.speed = 5
        self.width = 15
        self.height = 15
        self.directions = ["N", "E", "S", "W"]
        self.current_direction = ""

        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(pygame.image.load("test_sprite.png"), (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_self(self, direction):
        if direction == "N":
            self.rect.y -= self.speed
        elif direction == "E":
            self.rect.x += self.speed
        elif direction == "S":
            self.rect.y += self.speed
        elif direction == "W":
            self.rect.x -= self.speed

        if self.rect.x < 0:
            self.rect.x = 500 - self.width
        elif self.rect.x > 500 - self.width:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 500 - self.height
        elif self.rect.y > 500 - self.height:
            self.rect.y = 0

    def rand_direct(self):
        d = random.randint(0, len(self.directions) - 1)
        return self.directions[d]

    def opposite(self, direction):
        if direction == "N":
            return "S"
        if direction == "S":
            return "N"
        if direction == "W":
            return "E"
        if direction == "E":
            return "W"


class PathMarker(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pygame.Surface([15, 15])
        self.image.blit(pygame.image.load("path.png"), (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


pygame.init()


screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Random Path")
bckg = pygame.image.load("template_bckg.png")

clock = pygame.time.Clock()
f_p_s = 30

path_bot = Bot(250, 250)
Bot_Group = pygame.sprite.Group()
Bot_Group.add(path_bot)

move_count = 0
m_i = (10, 20)
interval = random.randint(m_i[0], m_i[1])

Path = pygame.sprite.Group()

playing = True
while move_count < 777 and playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    for each_bot in Bot_Group:
        path_marker = PathMarker(each_bot.rect.x, each_bot.rect.y)
        Path.add(path_marker)

        if move_count % interval == 0:
            each_bot.current_direction = each_bot.rand_direct()
            interval = random.randint(m_i[0], m_i[1])

        each_bot.move_self(each_bot.current_direction)
        move_count += 1

    screen.blit(bckg, [0, 0])
    Path.draw(screen)
    Bot_Group.draw(screen)
    pygame.display.flip()
    clock.tick(f_p_s)

pygame.quit()
