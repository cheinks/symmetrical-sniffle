import arcade
import random

# Screen title and size
# SCREEN_WIDTH = 1024
SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 768
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Skipford Beauregard"

# Constants for sizing
CARD_SCALE = 0.6

# How big are the cards?
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

# Size of card mats as percent of card size
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)

VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

# The spacing between piles
X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT
Y_SPACING = MAT_HEIGHT + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The X of where to start putting things on the left side
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

# The Y of the draw pile
MIDDLE_Y = SCREEN_HEIGHT / 2 + MAT_HEIGHT / 2

# The Y of the top and bottom play piles
TOP_Y = MIDDLE_Y + Y_SPACING
BOTTOM_Y = MIDDLE_Y - Y_SPACING

# To display a "stack" of cards rather than a pile
CARD_VERTICAL_OFFSET = CARD_HEIGHT * CARD_SCALE * 0.3

MAT_COLOR = arcade.csscolor.DARK_OLIVE_GREEN

# Card reference values
# CARD_VALUES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "SB"]
CARD_VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "K"]
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]
PILE_TYPES = ["DECK", "HAND", "PLAY", "STOCK", "DISCARD", "RECYCLE"]
FACE_DOWN_IMAGE = ":resources:images/cards/cardBack_red2.png"

# Constants to identify the various play piles
PILE_COUNT = 5
PLAY_PILE_1 = 0 # north
PLAY_PILE_2 = 1 # west
PLAY_PILE_3 = 2 # south
PLAY_PILE_4 = 3 # east
DRAW_PILE = 4 # center

# Control variables for the game instance
NUMBER_OF_PLAYERS = 1
STOCK_SIZE = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.background_color = arcade.color.AMAZON

        # List of cards we are dragging with the mouse
        self.held_cards = None

        # Sprite lists to handle the graphics
        self.pile_mat_list = None
        self.card_list = None

        self.players = None

        # Create a list of lists, each holds the place mats for a player
        self.player_mat_list = None

        # Create list shuffled and unshuffled cards
        self.draw_pile = None
        self.recycle = None

        # Create a list of lists, each holds a pile of cards
        self.play_piles = None
        self.stock_piles = None

        # Create of list of lists, each holds a list of discard piles
        self.discard_piles = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.held_cards = []

        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()
        self.card_list = arcade.SpriteList()

        self.players = []
        for i in range(NUMBER_OF_PLAYERS):
            self.players.append(Player(100, 100))

        """ Here we create the sprite for each pile, """

        # First the north play pile
        pile = Mat(PILE_TYPES[2])
        pile.position = START_X + X_SPACING, TOP_Y
        self.pile_mat_list.append(pile)
        # West
        pile = Mat(PILE_TYPES[2])
        pile.position = START_X, MIDDLE_Y
        self.pile_mat_list.append(pile)
        # South
        pile = Mat(PILE_TYPES[2])
        pile.position = START_X + X_SPACING, BOTTOM_Y
        self.pile_mat_list.append(pile)
        # East
        pile = Mat(PILE_TYPES[2])
        pile.position = START_X + 2 * X_SPACING, MIDDLE_Y
        self.pile_mat_list.append(pile)

        # Draw pile
        pile = Mat(PILE_TYPES[0])
        pile.position = START_X + X_SPACING, MIDDLE_Y
        self.pile_mat_list.append(pile)

        # Now create the mats for each player
        for i in range(NUMBER_OF_PLAYERS):
            stock_pos = self.players[i].get_stock_pos()
            pile = Mat(PILE_TYPES[3])
            pile.position = stock_pos
            self.pile_mat_list.append(pile)
            for j in range(4):
                pile = Mat(PILE_TYPES[4])
                pile.position = stock_pos[0] - (j + 1) * X_SPACING, stock_pos[1]
                self.pile_mat_list.append(pile)

        """ Next we construct the game cards """

        # Make the numbered cards
        for i in range(12):
            for card_value in CARD_VALUES:
                card = Card("Clubs", card_value, CARD_SCALE)
                self.card_list.append(card)

        # Make the Skip-Bos
        for i in range(18):
            # card = Card("Clubs", "SB", CARD_SCALE)
            card = Card("Clubs", "K", CARD_SCALE)
            self.card_list.append(card)

        # Shuffle the cards
        for pos1 in range(len(self.card_list)):
            pos2 = random.randrange(len(self.card_list))
            self.card_list.swap(pos1, pos2)

        # Instantiate the various piles
        self.draw_pile = []
        for card in self.card_list:
            card.position = self.pile_mat_list[DRAW_PILE].position
            card.location = PILE_TYPES[0]
            card.save_position()
            self.draw_pile.append(card)
        self.recycle = []

        self.play_piles = [ [] for _ in range(PILE_COUNT - 1) ]
        self.stock_piles = [ [] for _ in range(NUMBER_OF_PLAYERS) ]

        self.discard_piles = [ [ [] for _ in range(4) ] for _ in range(NUMBER_OF_PLAYERS) ]

        # Dealing mechanism
        # Reverse order so we "pop" cards from the top of the deck, not the bottom
        self.draw_pile.reverse()
        for i in range(STOCK_SIZE - 1):
            for j in range(NUMBER_OF_PLAYERS):
                """ For each stock card, loop through all players.
                For each player, add the next card in the list to their stock pile.
                The last card in the list is the 'top' of the pile. """
                card = self.draw_pile.pop()
                card.position = self.players[j].get_stock_pos()
                card.set_location(PILE_TYPES[3])
                card.save_position()
                self.stock_piles[j].append(card)
        # Now reveal the top card in each stockpile
        for j in range(NUMBER_OF_PLAYERS):
            card = self.draw_pile.pop()
            card.position = self.players[j].get_stock_pos()
            card.set_location(PILE_TYPES[3])
            card.save_position()
            card.face_up()
            self.stock_piles[j].append(card)
            # Reverse the order so the "face up" card we appended is on top
            self.stock_piles[j].reverse()

    def on_draw(self):
        """ Render the screen. """
        self.clear()
        self.pile_mat_list.draw()
        self.card_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        cards = arcade.get_sprites_at_point((x, y), self.card_list)
        if len(cards) > 0:
            # Get only the top card on the stack
            primary_card = cards[-1]
            assert isinstance(primary_card, Card)

            # What pile is it in? Can it even be picked up?
            primary_loc = primary_card.get_location()
            if primary_loc in [PILE_TYPES[0], PILE_TYPES[1], PILE_TYPES[3], PILE_TYPES[4]]:
                if primary_loc in [PILE_TYPES[0], PILE_TYPES[3]]:
                    primary_card.face_up()
                self.held_cards.append(primary_card)
                # Put on top in drawing order
                self.pull_to_top(self.held_cards[0])

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """ Called when the user presses a mouse button. """
        if len(self.held_cards) == 0:
            return

        reset_position = True
        pile, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)

        if arcade.check_for_collision(self.held_cards[0], pile):
            """ Having determined the card collides with a pile,
            decide whether the card can be placed there or not. """
            valid_move = False
            pile_type = pile.get_type()

            if pile_type not in [PILE_TYPES[0], PILE_TYPES[1], PILE_TYPES[3], PILE_TYPES[3]]:
                cards_below = arcade.get_sprites_at_point((x, y), self.card_list)
                if pile_type == PILE_TYPES[2]:
                    """ For a PLAY pile, card value must be 1 if pile is empty, 
                     or must be one higher than top card, or must be a skip-bo. """
                    held_value = self.held_cards[0].get_value()
                    below_length = len(cards_below)
                    # Check if card already there
                    if below_length > 0:
                        if held_value in ["SB", "K"]:
                            valid_move = True
                        else:
                            """ Number of cards in the stack must be one less than held value. """
                            valid_move = (CARD_VALUES[below_length] == held_value)
                            # if CARD_VALUES[below_length] == held_value:
                                # valid_move = True
                    else:
                        valid_move = (held_value in ["1", "SB", "K"])
                elif pile_type == PILE_TYPES[4]:
                    """For a DISCARD pile, must make 4 piles before stacking, 
                    but can play any card on top of any card."""
                    valid_move = True

            if valid_move:
                # Remove the card from the old pile
                # Move it to the new position
                self.held_cards[0].position = pile.position
                self.held_cards[0].save_position()
                # Put it in the new pile
                reset_position = False

        if reset_position:
            # Location invalid, return cards to original position
            self.held_cards[0].reset_position()

        # We are no longer holding cards
        self.held_cards.clear()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

    def on_key_press(self, symbol: int, modifiers: int):
        """ User presses key """
        if symbol == arcade.key.R:
            # Restart
            self.setup()

    def pull_to_top(self, card: arcade.Sprite):
        """ Pull card to top of rendering order """
        self.card_list.remove(card)
        self.card_list.append(card)

    def remove_card_from_pile(self, card):
        if card in self.draw_pile:
            self.draw_pile.remove(card)
        else:
            for player in self.discard_piles:
                for pile in player:
                    if card in pile:
                        pile.remove(card)
                        return


class Player:
    """ Container for game logic and sprite positioning """
    def __init__(self, x, y):
        # self.hand_position =

        self.stock_position = x + 4 * X_SPACING, y
        self.discard_position = [(x,y), (x+ X_SPACING,y), (x + 2 * X_SPACING, y), (x + 3 * X_SPACING, y)]

    def get_stock_pos(self):
        return self.stock_position


class Mat(arcade.SpriteSolidColor):
    """ Rectangle sprite to assist with game logic """
    def __init__(self, pile_type):
        self.pile_type = pile_type
        super().__init__(MAT_WIDTH, MAT_HEIGHT, 0, 0, MAT_COLOR)

    def get_type(self):
        return self.pile_type

class Card(arcade.Sprite):
    """ Card sprite """
    def __init__(self, suit, value, scale=1.0):

        self.suit = suit
        self.value = value

        # String description of where the card is
        self.location = ""
        self.old_position = None

        self.is_face_up = False
        self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"

        super().__init__(FACE_DOWN_IMAGE, scale, hit_box_algorithm="None")

    def set_location(self, loc):
        self.location = loc
    def get_location(self):
        return self.location
    def get_value(self):
        return self.value

    def save_position(self):
        self.old_position = self.position
    def reset_position(self):
        self.position = self.old_position

    def face_down(self):
        """ Turn card face down """
        self.texture = arcade.load_texture(FACE_DOWN_IMAGE)
        self.is_face_up = False

    def face_up(self):
        """ Turn card face up """
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True

    @property
    def is_face_down(self):
        """ Is this card face down? """
        return not self.is_face_up


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()