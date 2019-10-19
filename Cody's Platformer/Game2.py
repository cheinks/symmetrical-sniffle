import pygame
import random
play_speed = 40
screen_width = 1920
screen_height = 1080
scroll_speed = 10
gravity = 9.8


class Sprite(pygame.sprite.Sprite):
    def __init__(self, graphic, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.graphic = graphic
        self.width = width
        self.height = height

        self.image = pygame.Surface([width, height])
        self.image.blit(pygame.image.load(graphic), (0, 0))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def scroll(self):
        self.rect.x -= scroll_speed
        if self.rect.x + self.width < 0:
            self.kill()


class Player(Sprite):
    def __init__(self, graphic, x, y, width, height, strength):
        Sprite.__init__(self, graphic, x, y, width, height)
        self.strength = strength

        self.x_vel = scroll_speed
        self.y_vel = 0
        self.on_ground = True
        # self.jump = False

    def move(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.y_vel += gravity

    def jump(self):
        if self.on_ground:
            self.y_vel = self.strength


class Ground(Sprite):
    def __init__(self, x, y, width, height, graphic=None):
        if graphic is None:
            Sprite.__init__(self, 'ground.png', x, y, width, height)
        else:
            Sprite.__init__(self, graphic, x, y, width, height)


current_segment = 0
ground_spawn_rate = 500
next_ground = 0
# play speed / scroll speed = ticks per frame


def generate_ground():
    x = screen_width
    y = random.randint(270, 810)
    width = ground_spawn_rate / (play_speed / scroll_speed)
    height = screen_height - y
    ground = Ground(x, y, width, height)
    return ground


level = []
for i in range(50):
    level.append(generate_ground())

pygame.init()

clock = pygame.time.Clock()


pygame.display.set_caption("Cody's Arcade Scroller")
main_screen = pygame.display.set_mode([1920, 1080], pygame.SCALED)
main_background = pygame.image.load('sky.png')

main_ground = Ground(0, (screen_height / 2), screen_width, (screen_height / 2), 'starting_ground.png')
Obstacles = pygame.sprite.Group()
Obstacles.add(main_ground)

All_Sprites = pygame.sprite.Group()
All_Sprites.add(main_ground)

playing = True

while playing:
    timer = pygame.time.get_ticks()

    for event in pygame.event.get(pygame.QUIT):
        playing = False
    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == pygame.K_ESCAPE:
            playing = False

    if timer >= next_ground:
        next_ground = timer + ground_spawn_rate
        All_Sprites.add(level[current_segment])
        Obstacles.add(level[current_segment])
        current_segment += 1

    for each_sprite in All_Sprites:
        each_sprite.scroll()

    main_screen.blit(main_background, [0, 0])
    main_screen.blit(main_ground.image, [main_ground.rect.x, main_ground.rect.y])

    Obstacles.draw(main_screen)

    pygame.display.flip()
    clock.tick(play_speed)

pygame.quit()
