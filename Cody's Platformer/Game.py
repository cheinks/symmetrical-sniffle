import pygame
horizontal_boundary = 1440  # Right side of screen
vertical_boundary = 810  # Bottom of screen
gravity = 6


class Sprite(pygame.sprite.Sprite):
    def __init__(self, graphic, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.image = pygame.Surface([width, height])  # Creates a plane for the sprite to exist on
        self.image.blit(pygame.image.load(graphic), (0, 0))  # Adds the image to the view-model for the sprite
        self.rect = self.image.get_rect()  # Creates a coordinate plane "hitbox"
        self.rect.x = x
        self.rect.y = y

    def get_x_coord(self):
        return self.rect.x

    def get_y_coord(self):
        return self.rect.y


class Player(Sprite):
    def __init__(self, graphic, x, y, width, height):
        Sprite.__init__(self, graphic, x, y, width, height)

        self.x_velocity = 0  # Horizontal movement: (-) is left, (+) is right
        self.y_velocity = 0  # Vertical movement: (-) is up, (+) is down
        self.jump_strength = height  # Essentially the initial velocity of the jump

        self.want_jump = False
        self.grounded = True

    def add_x_velocity(self, dx):
        self.x_velocity += dx

    def set_jump(self, new_jump):
        self.want_jump = new_jump

    def move_self(self):
        if self.want_jump:
            self.jump()
        self.rect.x += self.x_velocity  # Move left or right
        self.rect.y += self.y_velocity + gravity  # Fall or jump
        self.y_velocity += gravity

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + self.width > horizontal_boundary:
            self.rect.x = horizontal_boundary - self.width
        # if self.rect.y < 0: (should be ok)
        # if self.rect.y > vertical_boundary: (kill self / die)

        if self.y_velocity > 0:
            self.grounded = False

    def jump(self):
        if self.grounded:
            self.y_velocity = -self.jump_strength
            self.grounded = False

    def land(self, ground_level):
        self.rect.y = ground_level - self.height
        self.grounded = True
        self.y_velocity = 0


class Platform(Sprite):
    def __init__(self, graphic, x, y, width, height):
        Sprite.__init__(self, graphic, x, y, width, height)


class Ground(Platform):
    def __init__(self, x, width):
        Platform.__init__(self, 'ground_main.png', x, 675, width, 135)


pygame.init()  # Start Pygame

pygame.display.set_caption("Cody's Platformer")
main_screen = pygame.display.set_mode([horizontal_boundary, vertical_boundary])
background = pygame.image.load('background_main.png')

# To keep track of time
clock = pygame.time.Clock()
play_speed = 30

# Instantiate all the sprites
player_1 = Player('player_main.png', 50, 200, 20, 35)
Players = pygame.sprite.Group()
Players.add(player_1)

starting_platform = Platform('platform_main.png', 0, 450, 250, 25)
ground_1 = Ground(400, 700)

All_Platforms = pygame.sprite.Group()
All_Platforms.add(starting_platform)
All_Platforms.add(ground_1)

playing = True

# ---------- Main Program Loop ----------
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.add_x_velocity(-10)
            elif event.key == pygame.K_RIGHT:
                player_1.add_x_velocity(10)
            elif event.key == pygame.K_SPACE:
                player_1.set_jump(True)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_1.add_x_velocity(10)
            elif event.key == pygame.K_RIGHT:
                player_1.add_x_velocity(-10)
            elif event.key == pygame.K_SPACE:
                player_1.set_jump(False)

    for each_player in Players:
        each_player.move_self()

    # Check collisions between the player and the ground
    gravity_check = pygame.sprite.groupcollide(Players, All_Platforms, False, False)
    for each_player in gravity_check:
        level = gravity_check[each_player][0].get_y_coord()
        each_player.land(level)

    # Draw everything so it can be seen
    main_screen.blit(background, [0, 0])
    All_Platforms.draw(main_screen)
    Players.draw(main_screen)

    pygame.display.flip()  # Update the changes we just made
    clock.tick(play_speed)

pygame.quit()
