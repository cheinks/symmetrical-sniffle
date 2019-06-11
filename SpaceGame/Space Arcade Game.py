# Imports
import pygame
import random
import textwrap
playing = True
test = False
read = False


# The Game
def play_game(is_test, read_instructions):

    # Spaceship class definition
    class Spaceship(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([68, 71])
            self.image.set_colorkey(black)
            self.image.blit(pygame.image.load("galaxy_explorer.png"), (0, 0))  # Image adapted from Galaga

            self.rect = self.image.get_rect()
            self.rect.x = 216
            self.rect.y = 514

        def move_spaceship(self, x_distance, y_distance):  # Moves the spaceship. If it goes out of bounds, reset the
            if self.rect.x in range(5, 428):               # corresponding coordinates.
                self.rect.x += x_distance
            if self.rect.y in range(215, 579):
                self.rect.y += y_distance
            if self.rect.x < 5:
                self.rect.x = 5
            elif self.rect.x > 427:
                self.rect.x = 427
            if self.rect.y < 215:
                self.rect.y = 215
            elif self.rect.y > 578:
                self.rect.y = 578

    # Alien class definition
    class Alien(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)

            self.type = random.randint(1, 6)
            self.image = pygame.Surface([66, 51])
            self.image.set_colorkey(black)

            # Assigns an image, speed, and point value based off of the type of the instance.
            # Images adapted from Space Invaders.
            if self.type <= 3:
                self.image.blit(pygame.image.load("blue_orange_alien.png"), (0, 0))
                self.Speed = 5
                self.Score = 5
            elif self.type <= 5:
                self.image.blit(pygame.image.load("red_green_alien.png"), (0, 0))
                self.Speed = 10
                self.Score = 15
            else:
                self.image.blit(pygame.image.load("yellow_purple_alien.png"), (0, 0))
                self.Speed = 15
                self.Score = 25

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def move_alien(self):  # Moves the alien. If it goes out of bounds, 'kill' it.
            self.rect.y += self.Speed
            if self.rect.y >= 634:
                self.kill()

    # Boss class definition
    class AlienBoss(pygame.sprite.Sprite):
        def __init__(self, x, health):
            pygame.sprite.Sprite.__init__(self)
            self.Direction = 'right'
            self.Health = health
            self.Score = int(health / 2)
            self.Alive = False

            self.image = pygame.Surface([297, 228])
            self.image.set_colorkey(white)
            self.image.blit(pygame.image.load("alien_invader.png"), (0, 0))  # Image adapted from Space Invaders.
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = 5

        def move_boss(self):  # Moves the boss. Keeps it in bounds.
            if self.Direction == 'right':
                self.rect.x += 2
            elif self.Direction == 'left':
                self.rect.x -= 2
            if self.rect.x >= 198:
                self.rect.x = 198
                self.Direction = 'left'
            elif self.rect.x <= 5:
                self.rect.x = 5
                self.Direction = 'right'

        def fire_weapon(self, group):  # Fires a projectile back at the player.
            alien_laser = AlienLaser(self.rect.x + 149, 233, random.randint(5, 10))
            group.add(alien_laser)

    # Laser projectile definition
    class Laser(pygame.sprite.Sprite):
        def __init__(self, x, y, speed):
            pygame.sprite.Sprite.__init__(self)

            self.Speed = speed

            self.image = pygame.Surface([5, 10])
            self.image.set_colorkey(black)
            self.image.blit(pygame.image.load('laser_weapon.png'), (0, 0))

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def move_laser(self):  # Moves the laser. If it goes out of bounds, 'kill' it.
            self.rect.y -= self.Speed
            if self.rect.y <= 5:
                self.kill()

    # Alien projectile definition
    class AlienLaser(pygame.sprite.Sprite):
        def __init__(self, x, y, speed):
            pygame.sprite.Sprite.__init__(self)

            self.Speed = speed

            self.image = pygame.Surface([20, 20])
            self.image.set_colorkey(black)
            self.image.blit(pygame.image.load('alien_weapon.png'), (0, 0))

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def move_alien_laser(self):
            self.rect.y += self.Speed
            if self.rect.y >= screen_height - 5:
                self.kill()

    # Powerup class definition
    class Powerup(pygame.sprite.Sprite):
        def __init__(self, x, y, speed, type_of_powerup):
            pygame.sprite.Sprite.__init__(self)

            self.Speed = speed
            self.Type = type_of_powerup

            self.image = pygame.Surface([50, 50])

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def move_powerup(self):  # Moves the powerup.
            self.rect.y += self.Speed

    # Health powerup subclass definition
    class HealthPowerup(Powerup):
        def __init__(self, x, y, speed, type_of_powerup):
            Powerup.__init__(self, x, y, speed, type_of_powerup)

            self.image.set_colorkey(black)
            self.image.blit(pygame.image.load('health_powerup.jpg'), (0, 0))

    pygame.init()  # Pygame starts running.

    # Draws all the screens, loads a background image
    screen_width = 500
    screen_height = 690
    start_screen = pygame.display.set_mode([screen_width, screen_height])
    main_screen = pygame.display.set_mode([screen_width, screen_height])
    end_screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Invaders From Planet X")
    background_image = pygame.image.load('black_background.png').convert()
    background_image_2 = pygame.image.load('space_background.jpg').convert()  # CC0 Public Domain

    clock = pygame.time.Clock()
    f_p_s = 30

    # Define basic colors for future reference
    black = (0, 0, 0)
    blue = (0, 0, 200)
    brown = (123, 66, 15)
    gray = (170, 170, 170)
    orange = (250, 88, 0)
    green = (22, 116, 50)
    purple = (123, 0, 149)
    red = (200, 0, 0)
    white = (255, 255, 255)
    yellow = (245, 200, 0)

    random_color_list = [white]
    default_font = pygame.font.Font(None, 36)

    # Define additional Functions and Procedures here
    game_start = False
    game_end = True
    play_again = False
    instructions = textwrap.wrap("Move your spaceship with WASD or the arrow keys and press space to shoot. Kill aliens \
to earn points. You start with three lives and a limited ammo supply. Collect powerups for various boosts. Your ammo \
will regenerate over time. Click the screen to begin.", 40)
    new_high_score = False

    # Creates all the groups of sprites so they can interact
    fleet = pygame.sprite.Group()
    spaceship = Spaceship()
    fleet.add(spaceship)

    projectiles = pygame.sprite.Group()
    alien_projectiles = pygame.sprite.Group()
    herd = pygame.sprite.Group()
    powerup_storage = pygame.sprite.Group()
    bosses = pygame.sprite.Group()
    boss_alive = False

    # Additional variables for future reference
    x_movement = 0
    y_movement = 0
    total_score = 0
    lives = 3
    game_difficulty = ''
    ammunition = 50
    regen_modifier = 0

    spawn_rate_values = {
        'Easy': [5000, 0.25, 25],
        'Medium': [3750, 0.5, 50],
        'Hard': [2500, 0.75, 75],
        'Impossible': [1250, 1, 100],
        '': [None, None]
    }
    max_spawn_rate = 250
    spawn_rate_modifier = 0
    shooting = False

    movement_keys = [pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d, pygame.K_UP, pygame.K_w, pygame.K_DOWN,
                     pygame.K_s]

    # Functions to make life easier.
    def create_a_font(size):  # Makes a font.
        temporary_font = pygame.font.Font(None, size)
        return temporary_font

    def draw_text(message, screen, x_coord, y_coord, color, font, bckg_color):  # Used to 'draw' text on a screen.
        message_display = font.render(message, 1, color, bckg_color)
        screen.blit(message_display, [x_coord, y_coord])

    def random_color():  # Random color generator.
        red_value = random.randint(0, 255)
        green_value = random.randint(0, 255)
        while red_value == green_value:
            green_value = random.randint(0, 255)
        blue_value = random.randint(0, 255)
        while green_value == blue_value:
            blue_value = random.randint(0, 255)
        return red_value, blue_value, green_value

    # Interprets the player's inputs or keys pressed.
    def check_input(u_i, lives_left, m_keys, shoot, x_dist, y_dist, g_e, i_t):  # Creates a list of values, runs them
        if u_i.type == pygame.QUIT:                                             # through two sub-algorithms to check
            lives_left = 0                                                      # the inputs, and returns the updated
            g_e = False                                                         # list.
            i_t = True
        value_list = [lives_left, x_dist, y_dist, shoot, g_e, i_t]
        key_press(u_i, value_list, m_keys)
        key_release(u_i, value_list, m_keys)
        return value_list

    def key_press(u_i, values, m_keys):  # Changes the coordinates of the spaceship if a specific key is pressed.
        if u_i.type == pygame.KEYDOWN:
            if u_i.key in [m_keys[0], m_keys[1]]:
                values[1] -= 10
            elif u_i.key in [m_keys[2], m_keys[3]]:
                values[1] += 10
            elif u_i.key in [m_keys[4], m_keys[5]]:
                values[2] -= 10
            elif u_i.key in [m_keys[6], m_keys[7]]:
                values[2] += 10

            if u_i.key == pygame.K_SPACE:
                values[3] = True

    def key_release(u_i, values, m_keys):  # Resets the coordinates of the spaceship when the key is released.
        if u_i.type == pygame.KEYUP:
            if u_i.key in [m_keys[0], m_keys[1]]:
                values[1] += 10
            elif u_i.key in [m_keys[2], m_keys[3]]:
                values[1] -= 10
            elif u_i.key in [m_keys[4], m_keys[5]]:
                values[2] += 10
            elif u_i.key in [m_keys[6], m_keys[7]]:
                values[2] -= 10

            elif u_i.key == pygame.K_SPACE:
                values[3] = False

    # Formats the high scores
    def high_score():
        high_scores = repr(open('HighScores.txt', 'r').read())[1:]

        high_scores_list = []
        for i in range(4):
            high_scores_list.append(high_scores[0:high_scores.index('n') - 1])
            high_scores = high_scores[high_scores.index('n') + 1:]

        high_scores_dict = {
            'Easy': 0,
            'Medium': 0,
            'Hard': 0,
            'Impossible': 0
        }

        for each_record in high_scores_list:
            temp_list = each_record.split()
            high_scores_dict[temp_list[0]] = temp_list[2]

        return high_scores_dict

    # --------- Main Program Loop(s) ---------
    while not game_start:  # Controls instructions/starting screen.
        timer = pygame.time.get_ticks()
        temp_timer = 5000

        for event in pygame.event.get():  # If you click the 'x' in the upper right, actually stop the game.
            if event.type == pygame.QUIT:
                game_start = True
                lives = -1
                game_end = False
                is_test = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                mouse_position = list(event.pos)
                if read_instructions:  # After reading instructions (or if skipped)
                    if mouse_position[0] < 250 and mouse_position[1] in range(218, 410):
                        # Makes sure the player actually clicks on the game difficulty they want
                        m_p = mouse_position[1]
                        if m_p in range(218, 259):
                            game_difficulty = "Easy"
                            regen_modifier = 10000
                        elif m_p in range(260, 311):
                            game_difficulty = "Medium"
                            regen_modifier = 15000
                        elif m_p in range(312, 363):
                            game_difficulty = "Hard"
                            regen_modifier = 20000
                        elif m_p in range(364, 410):
                            game_difficulty = "Impossible"
                            regen_modifier = 25000
                        game_start = True
                        base_spawn_rate = spawn_rate_values[game_difficulty][0]
                else:
                    read_instructions = True

        start_screen.blit(background_image, [0, 0])
        if read_instructions:  # Instruction skip (if decided to play again)
            draw_text("Please select a difficulty:", start_screen, 30, 82, green, default_font, None)
            draw_text("Easy", start_screen, 30, 218, white, create_a_font(32), None)
            draw_text("Medium", start_screen, 30, 270, yellow, create_a_font(32), None)
            draw_text("Hard", start_screen, 30, 322, orange, create_a_font(32), None)
            draw_text("Impossible", start_screen, 30, 374, red, default_font, None)
        else:
            if timer < temp_timer:  # Only update the color every frame for a certain amount of time.
                draw_text("Welcome!", start_screen, 30, 20, random_color(), create_a_font(42), None)
            else:
                draw_text("Welcome!", start_screen, 30, 20, red, create_a_font(42), None)
            temp_counter = 82
            for each_line in instructions:
                draw_text(each_line, start_screen, 30, temp_counter, white, create_a_font(28), None)
                temp_counter += 40
            draw_text("Good luck!", start_screen, 30, 400, purple, default_font, None)
        pygame.display.flip()
        clock.tick(f_p_s)

    # Control variables needed for main game.
    game_delay = pygame.time.get_ticks()
    next_laser = game_delay
    next_alien = game_delay + 2000
    next_health = game_delay + 35000
    ammo_regen = game_delay + 45000 - regen_modifier
    next_boss = game_delay + 60000 - regen_modifier
    next_alien_laser = game_delay

    while lives > 0:  # Controls actual game screen.
        timer = pygame.time.get_ticks()

        for event in pygame.event.get():  # Analyzes user input.
            input_result = check_input(event, lives, movement_keys, shooting, x_movement, y_movement, game_end, is_test)
            lives = input_result[0]
            x_movement = input_result[1]
            y_movement = input_result[2]
            shooting = input_result[3]
            game_end = input_result[4]
            is_test = input_result[5]

        # Update sprites here - makes changes based on user input
        if timer >= ammo_regen:  # Ammunition regeneration.
            ammunition += 50
            ammo_regen += 45000 - regen_modifier
            if ammunition > 150:  # Max ammo.
                ammunition = 150

        if timer > next_alien:  # Alien spawn rate.
            next_alien += random.randint(max_spawn_rate, base_spawn_rate - spawn_rate_modifier)
            x_coordinate = random.randint(5, 429)
            alien = Alien(x_coordinate, 5)
            herd.add(alien)

        if timer > next_health:  # Health powerup spawn rate.
            next_health += 45000 - regen_modifier
            x_coordinate = random.randint(5, 445)
            health_powerup = HealthPowerup(x_coordinate, 5, 5, 'health')
            powerup_storage.add(health_powerup)

        if shooting:  # Controls rate of fire (spaceship).
            if ammunition > 0:
                if timer > next_laser:
                    laser = Laser(spaceship.rect.x + 31, spaceship.rect.y, 15)
                    projectiles.add(laser)
                    ammunition -= 1
                    next_laser += 250
            else:
                shooting = False
        else:
            next_laser = timer

        if not boss_alive:  # Boss spawn rate.
            if timer > next_boss:
                alien_boss = AlienBoss(random.randint(5, 198), 5000 * spawn_rate_values[game_difficulty][1])
                bosses.add(alien_boss)
                boss_alive = True
                next_alien_laser = timer + 2000

        for each_boss in bosses:  # Controls boss rate of fire.
            if timer > next_alien_laser:
                each_boss.fire_weapon(alien_projectiles)
                next_alien_laser += 2000

        # Moves all of the sprites
        for each_alien in herd:
            each_alien.move_alien()
        for each_laser in projectiles:
            each_laser.move_laser()
        for each_powerup in powerup_storage:
            each_powerup.move_powerup()
        for each_boss in bosses:
            each_boss.move_boss()
        for each_alien_laser in alien_projectiles:
            each_alien_laser.move_alien_laser()

        # Controls collisions between sprites - lives counter and score counter
        dead_aliens = pygame.sprite.groupcollide(herd, projectiles, False, True)
        for each_alien in dead_aliens:
            total_score += each_alien.Score
            each_alien.kill()
        crashed_ships = pygame.sprite.groupcollide(fleet, herd, False, True)
        for _ in crashed_ships:
            lives -= 1
        crashed_ships = pygame.sprite.groupcollide(fleet, alien_projectiles, False, True)
        for _ in crashed_ships:
            lives -= 1
        powerups_activated = pygame.sprite.groupcollide(powerup_storage, fleet, True, False)
        for each_powerup in powerups_activated:
            if each_powerup.Type == 'health':  # Add a life if acquired health power-up.
                lives += 1
        bosses_damaged = pygame.sprite.groupcollide(bosses, projectiles, False, True)
        for each_boss in bosses_damaged:
            each_boss.Health -= spawn_rate_values[game_difficulty][2]
            if each_boss.Health <= 0:  # If the player killed the boss, update these variables.
                each_boss.Alive = False
                each_boss.kill()
                total_score += each_boss.Score
                next_boss += 60000
                boss_alive = False
        if lives > 5:  # Max lives.
            lives = 5

        # Draws everything on the screen so the user can play the game
        main_screen.blit(background_image_2, [0, 0])
        if lives > 0:  # Only 'draw' these things if necessary.
            spaceship.move_spaceship(x_movement, y_movement)
            fleet.draw(main_screen)
            projectiles.draw(main_screen)
            herd.draw(main_screen)
            powerup_storage.draw(main_screen)
            bosses.draw(main_screen)
            alien_projectiles.draw(main_screen)
            draw_text(str(int(total_score)), main_screen, 5, 5, gray, default_font, black)
            draw_text("Lives: " + str(lives), main_screen, 5, 659, blue, default_font, black)
            draw_text("Ammo: " + str(ammunition), main_screen, 350, 659, brown, default_font, black)
        pygame.display.flip()
        clock.tick(f_p_s)
        if base_spawn_rate - spawn_rate_modifier > max_spawn_rate:  # Increases the spawn rate of aliens each frame.
            spawn_rate_modifier += 1

    # Exports the score of the game just played to a high scores file
    if not is_test:  # Only export a high score if the game is legitimate.
        old_high_scores = high_score()
        if int(old_high_scores[game_difficulty]) < total_score:  # If the current current score is greater, go ahead and
            old_high_scores[game_difficulty] = str(total_score)  # update the existing high score.
            new_high_score = True
            final_export = ''
            for item in list(old_high_scores.items()):
                temp_string = item[0] + ' - ' + item[1]
                final_export = final_export + temp_string + '\n'
            file = open('HighScores.txt', 'w')
            file.write(final_export)
            file.close()

    color_change = pygame.time.get_ticks()

    while game_end:  # Controls game over/end screen.
        timer = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                m_p = list(event.pos)
                if m_p[0] in range(150, 300) and m_p[1] in range(500, 550):
                    play_again = True
                    game_end = False

        if timer > color_change:
            random_color_list.append(random_color())
            random_color_list.remove(random_color_list[0])
            color_change += 950

        end_screen.blit(background_image, [0, 0])
        draw_text("GAME OVER", end_screen, 100, 100, random_color_list[-1], create_a_font(72), None)
        draw_text("Play Again", end_screen, 155, 500, purple, create_a_font(48), None)
        draw_text("Score: " + str(total_score), end_screen, 25, 375, gray, default_font, None)
        draw_text("Difficulty: " + game_difficulty, end_screen, 25, 425, green, default_font, None)
        if new_high_score:
            draw_text("New high score!", end_screen, 160, 160, yellow, default_font, None)
        pygame.display.flip()
        clock.tick(f_p_s)

    pygame.quit()  # Pygame stops running.

    return play_again


while playing:
    playing = play_game(test, read)
    read = True
