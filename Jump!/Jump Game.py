import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, ground_level):
        pygame.sprite.Sprite.__init__(self)
        self.ground_level = 520 - 50


class BlueSquare(Sprite):
    def __init__(self, x, y, ground_level=None):
        Sprite.__init__(self, ground_level)
        self.on_ground = True
        self.velocity = 0
        self.jump_height = 42

        self.image = pygame.Surface([50, 50])
        self.image.blit(pygame.image.load('test_sprite.png'), (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_self(self, dist, y_dist):
        self.rect.x += dist
        if self.rect.x < 5:
            self.rect.x = 5
        elif self.rect.x > 945:
            self.rect.x = 945
        self.rect.y -= y_dist
        if self.rect.y > self.ground_level:
            self.rect.y = self.ground_level
            self.on_ground = True

    def check_jump(self, is_jumping):
        if not self.on_ground:
            self.velocity -= 9.8
        else:
            self.velocity = 0
        if is_jumping:
            if self.on_ground:
                self.velocity = self.jump_height
                self.on_ground = False
        return self.velocity


pygame.init()


screen = pygame.display.set_mode([999, 750])
pygame.display.set_caption("Jump!")
bckg_image_1 = pygame.image.load('template_bckg.png')  # Adapted from noobtuts.com
'''bckg_image_2 = pygame.image.load('jump_game_bckg_2.png')  # Adapted from noobtuts.com'''

clock = pygame.time.Clock()
f_p_s = 30

character = BlueSquare(100, 400)
Characters = pygame.sprite.Group()
Characters.add(character)
move = 0
y_move = 0
jump = False

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move = -10
            elif event.key == pygame.K_RIGHT:
                move = 10
            elif event.key == pygame.K_SPACE:
                jump = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                move = 0
            else:
                jump = False

    for each_character in Characters:
        y_move = each_character.check_jump(jump)
        each_character.move_self(move, y_move)

    screen.blit(bckg_image_1, [0, 0])
    Characters.draw(screen)
    # Bscreen.blit(bckg_image_2, [0, 508])
    pygame.display.flip()
    clock.tick(f_p_s)

pygame.quit()
