import sys
import random
import textwrap


def interact(user_command):
    print()
    if user_command in directions2:
        index2 = directions2.index(user_command)
        user_command = directions[index2]

    if user_command in ['leave game', 'quit game', 'exit game']:
            print('So it\'s game over then? Bye.')
            sys.exit(0)

    elif user_command in ['', 'look']:
        player1.current_loc.entered = False
        player1.display()

    elif user_command in ['stats']:
        select_weapon()
        print('Location: %s' % player1.current_loc.name)
        print('Damage: %d' % player1.damage)
        print('Health: %d' % player1.health)

    elif user_command in ['i', 'inventory', 'bag']:
        if len(player1.items) == 0:
            print('You are not carrying anything.')

        else:
            print('You are carrying:')
            for item in range(len(player1.items)):
                print('A ' + player1.items[item].name)

    else:
        _words = str.split(user_command)
        if len(_words) > 0:
            if _words[0] not in ['go', 'up']:
                for word in keywords_list:
                    if word in _words:
                        _words.remove(word)

            if _words[0] in directions:
                try:
                    player1.move(_words[0])
                except KeyError:
                    print('You can\'t go that way.')

            elif _words[0] == 'go':
                if _words[1] in directions:
                    try:
                        player1.move(_words[1])
                    except KeyError:
                        print('You can\'t go that way.')

                else:
                    print('I don\'t know what you mean.')

            elif _words[0] in ['attack', 'kill', 'stab']:
                select_weapon()
                if player1.damage == 0:
                    print('You have nothing to attack with.')
                else:
                    # noinspection PyBroadException
                    try:
                        player1.attack(globals()[_words[1]])
                    except IndexError:
                        print('Who is it that you want to attack?.')
                    except:
                        print('You can\'t be serious.')
            elif _words[0] == 'open':
                try:
                    player1.open(globals()[_words[1]])
                except KeyError:
                    print('I don\'t know what you mean.')
                except IndexError:
                    print('What is it that you want to open?')

            elif _words[0] in ['take', 'grab', 'pick']:
                if len(player1.items) == 5:
                    print('You are carrying too many objects. You need to drop something first.')
                else:
                    try:
                        player1.take(globals()[_words[1]])
                    except KeyError:
                        print('I don\'t know what you mean.')
                    except IndexError:
                        print('What is it that you want to take?')

            elif _words[0] == 'drop':
                # noinspection PyBroadException,PyBroadException
                try:
                    player1.drop(globals()[_words[1]])
                except KeyError:
                    print('I don\'t know what you mean.')
                except IndexError:
                    print('What is it that you want to drop?')
            else:
                if len(_words) > 1:
                    try:
                        globals()[_words[1]].interact(_words[0])
                    except KeyError:
                        if player1.current_loc == old_car:
                            if _words[0] == 'unlock':
                                if _words[1] == 'car':
                                    if key in player1.items:
                                        car.interact('unlock')

                                    else:
                                        print('You need a key to unlock the car.')
                                else:
                                    print('You cannot see any such thing.')
                            else:
                                print('I don\'t know what you mean.')

                        elif player1.current_loc == treehouse:
                            if _words[0] == 'kill' and _words[1] in ['self', 'myself']:
                                print(textwrap.fill('You dive out one the windows in the treehouse and break your \
neck on the ground. You are dead.', width=100))
                                sys.exit(0)

                            else:
                                print('I don\'t know what you mean.')

                        elif player1.current_loc == up_a_tree:
                            if _words[0] == 'kill' and _words[1] in ['self', 'myself']:
                                print(textwrap.fill('You jump out of the tree and break your neck. You are dead.',
                                                    width=100))
                                sys.exit(0)

                            else:
                                print('I don\'t know what you mean.')

                        elif player1.current_loc == attic:
                            back_hallway.up = None
                            back_hallway.desc = 'The door to the south leads to out of the house. The hallway goes \
north into the living room. There is a small trapdoor with a handle on the ceiling and another door to the west.'
                            if _words[0] == 'turn' and _words[2] == 'flashlight':
                                if _words[1] == 'on':
                                    if flashlight in player1.items:
                                        flashlight.interact('on')
                                        print('Turning on the flashlight reveals a portal machine.')

                                elif _words[1] == 'off':
                                    if flashlight in player1.items:
                                        flashlight.interact('off')

                            else:
                                print('You do not have this item.')

                            if flashlight.on_off:
                                attic.objects.append(portal)
                                attic.desc = 'The trapdoor is locked.'

                        elif player1.current_loc == garden:
                            if _words[0] == 'water' and _words[1] in ['garden', 'plants']:
                                if can in player1.items:
                                    can.interact('water')

                                else:
                                    print('You have nothing to water the plants with.')
                            else:
                                print('I don\'t know what you mean.')
                        else:
                            print('I don\'t know what you mean.')
                else:
                    print('I don\'t know what you mean.')


class Interactable(object):
    def __init__(self, name, desc, used, keywords):
        self.name = name
        self.desc = desc
        self.used = used
        self.keywords = keywords

    def interact(self, command):
        if not self.used:
            self.used = True
            print()


class Window(Interactable):
    def __init__(self, name, desc, used, keywords):
        super(Window, self).__init__(name, desc, used, keywords)

    def interact(self, command):
        if command == 'open':
            if not self.used:
                self.used = True
                print(self.desc)
                west_of_house.east = 'kitchen'
                west_of_house.desc = 'You are west of the house. There is a window here that is open.'
                kitchen.west = 'west_of_house'
                kitchen.desc = 'You are in the kitchen. There is a door to the east and the south and an open window \
to the west.'
            else:
                print('You have already done this.')
        else:
            print('You cannot perform this action.')


class Door(Interactable):
    def __init__(self, name, desc, used, used2, keywords):
        super(Door, self).__init__(name, desc, used, keywords)
        self.used2 = used2

    def interact(self, command):
        if command == 'open':
            if not self.used:
                if player1.current_loc == living_room:
                    north_of_house.south = 'living_room'
                    north_of_house.desc = 'You are north of the house. The front door is open. There is a rusted \
mailbox here.'
                    living_room.north = 'north_of_house'
                    living_room.desc = 'The front door is open and leads to the north. There is a hallway to the \
northeast and a hallway to the southwest that leads to the back door.'
                    print(self.desc)
                    self.used = True

            if not self.used2:
                if player1.current_loc == behind_house:
                    behind_house.north = 'back_hallway'
                    behind_house.desc = 'You are behind the house. There is an open door here without a handle. There \
is also a garden to the south.'
                    print(self.desc)
                    self.used2 = True
            else:
                print('You have already done this.')
        else:
            print('You cannot perform this action.')


class Mailbox(Interactable):
    def __init__(self, name, desc, used, keywords):
        super(Mailbox, self).__init__(name, desc, used, keywords)

    def interact(self, command):
        if command == 'open':
            if not self.used:
                self.used = True
                print(self.desc)
                north_of_house.objects.append(paper)
            else:
                print('You have already done this.')
        else:
            print('You cannot perform this action.')


class Chest(Interactable):
    def __init__(self, name, desc, used, keywords):
        super(Chest, self).__init__(name, desc, used, keywords)

    def interact(self, command):
        if command == 'open':
            if not self.used:
                self.used = True
                print(self.desc)
                treehouse.objects.append(map)
            else:
                print('You have already done this.')
        else:
            print('You cannot perform this action.')


class Trapdoor(Interactable):
    def __init__(self, name, desc, used, keywords):
        super(Trapdoor, self).__init__(name, desc, used, keywords)

    def interact(self, command):
        if command == 'open':
            if not self.used:
                self.used = True
                print(self.desc)
                back_hallway.up = 'attic'
                back_hallway.desc = 'The door to the south leads to out of the house. The hallway goes north into the \
living room. There is an open trapdoor in the ceiling.'
            else:
                print('You have already done this.')
        else:
            print('You cannot perform this action.')


class Item(object):
    def __init__(self, name, keywords=None):
        if keywords is None:
            keywords = []
        self.name = name
        self.keywords = keywords

    def interact(self, command):
        print('You use your %s.' % self.name)


class WateringCan(Item):
    def __init__(self, name, used, keywords):
        super(WateringCan, self).__init__(name, keywords)
        self.used = used

    def interact(self, command):
        if command == 'water':
            if not self.used:
                self.used = True
                print('While you were watering the plants, you found a health potion.')
                player1.items.append(potion)
            else:
                print('You have already done this.')
        else:
            print('You cannot perform this action.')


class Paper(Item):
    def __init__(self, name, keywords):
        super(Paper, self).__init__(name, keywords)
        self.keywords = keywords

    def interact(self, command):
        if command == 'read':
            print(textwrap.fill('You are at an abandoned house on the edge of an extensive forest. The climate has \
changed dramatically, allowing deserts, forests, and swamps to exist within an area of a few square miles. To the \
south is a rundown city with people that will give you information. Your job is to explore the surrounding area and \
acquire any materials necessary to help restore the city to its former glory.', width=100))

        else:
            print('You cannot perform this action.')


class Egg(Item):
    def __init__(self, name, keywords):
        super(Egg, self).__init__(name, keywords)


class Treasure(Item):
    def __init__(self, name, keywords):
        super(Treasure, self).__init__(name, keywords)

    def interact(self, command):
        if player1.current_loc == city:
            if treasure in player1.items:
                if command in ['give', 'drop']:
                    print(textwrap.fill('You give the treasure to the people of the city. Now they can rebuild their \
city- Oh no! A thief stole the treasure. As he runs away he slashes at you with his knife. You see him running \
across the desert, but by the time you start after him he\'s already gone.', width=100))
                    sys.exit(0)


class Portal(Item):
    def __init__(self, name, keywords):
        super(Portal, self).__init__(name, keywords)
        self.open_closed = False

    def interact(self, command):
        if command == 'open':
            if not self.open_closed:
                print('You open the portal, but you cannot see where it leads to.')
                self.open_closed = True
                attic.north = 'desert'
                attic.northeast = 'desert'
                attic.northwest = 'desert'
                attic.south = 'desert'
                attic.southeast = 'desert'
                attic.southwest = 'desert'
                attic.east = 'desert'
                attic.west = 'desert'

            else:
                print('The portal is already open.')

        elif command == 'close':
            print('You cannot close the portal.')


class Tool(Item):
    def __init__(self, name, keywords):
        super(Tool, self).__init__(name, keywords)

    def interact(self, command):
        print('You use your %s.' % self.name)


class Map(Tool):
    def __init__(self, name, desc, keywords):
        super(Map, self).__init__(name, keywords)
        self.desc = desc

    def interact(self, command):
        if command == 'read':
            print(self.desc)


class Key(Tool):
    def __init__(self, name, keywords):
        super(Key, self).__init__(name, keywords)


class Flashlight(Tool):
    def __init__(self, name, keywords, on_off):
        super(Flashlight, self).__init__(name, keywords)
        self.on_off = on_off

    def interact(self, command):
        if command == 'on':
            self.on_off = True
            print('The flashlight is now on.')
        elif command == 'off':
            self.on_off = False
            print('The flashlight is now off.')


class Weapon(Item):
    def __init__(self, name, durability, damage, value, keywords):
        super(Weapon, self).__init__(name, keywords)
        self.durability = durability
        self.damage = damage
        self.value = value

    def attack(self, target):
        print('You attack %s for %s damage.' % (target, self.damage))


class Melee(Weapon):
    def __init__(self, name, durability, damage, value, keywords):
        super(Melee, self).__init__(name, durability, damage, value, keywords)

    def attack(self, target):
        print('You attack %s for %d damage.' % (target.name, self.damage))


class Sword(Melee):
    def __init__(self, name, durability, damage, value, keywords):
        super(Sword, self).__init__(name, durability, damage, value, keywords)

    def attack(self, target):
        if target.health > 0:
            print('You attack %s for %d damage.' % (target.name, self.damage))
            target.take_damage(self.damage)


class Knife(Melee):
    def __init__(self, name, durability, damage, value, keywords):
        super(Knife, self).__init__(name, durability, damage, value, keywords)

    def attack(self, target):
        print('You stab %s for %d damage.' % (target.name, self.damage))
        target.take_damage(self.damage)


class Consumable(Item):
    def __init__(self, name, lp, used, keywords):
        super(Consumable, self).__init__(name, keywords)
        self.health = lp
        self.used = used

    def interact(self, command):
        print('You consume your %s.' % self.name)


class Food(Consumable):
    def __init__(self, name, lp, used, keywords):
        super(Food, self).__init__(name, lp, used, keywords)

    def interact(self, command):
        if not self.used:
            print('You eat %s and gain %d health.' % (self.name, self.health))


class Lunch(Food):
    def __init__(self, name, lp, used, keywords):
        super(Lunch, self).__init__(name, lp, used, keywords)

    def interact(self, command):
        if command in ['consume', 'eat']:
            if not self.used:
                print('You eat your %s and gain %d health.' % (self.name, self.health))
                player1.health += self.health
                player1.items.remove(self)
        else:
            print('I don\'t know what you mean.')


class Potion(Consumable):
    def __init__(self, name, lp, used, keywords):
        super(Potion, self).__init__(name, lp, used, keywords)

    def interact(self, command):
        print('You consume the potion.')


class HPotion(Potion):
    def __init__(self, name, lp, used, keywords):
        super(HPotion, self).__init__(name, lp, used, keywords)

    def interact(self, command):
        if command in ['consume', 'drink']:
            if not self.used:
                self.used = True
                print('You consume the health potion and gain %d health.' % self.health)
                player1.health += self.health
                player1.items.remove(self)


class Vehicle(Item):
    def __init__(self, name, started, keywords):
        super(Vehicle, self).__init__(name, keywords)
        self.started = started

    def interact(self, command):
        if command == 'start':
            if not self.started:
                print('You insert the key and start the vehicle.')
                self.started = True
            else:
                print('The vehicle is already started.')
        else:
            print('I don\'t know what you mean.')


class Car(Vehicle):
    def __init__(self, name, started, keywords):
        super(Car, self).__init__(name, started, keywords)

    def interact(self, command):
        if command == 'unlock':
            print('You unlock the car and get in.')
            player1.in_car = True

        elif command == 'start':
            if not self.started:
                print('You insert the key and start the vehicle.')
                self.started = True
            else:
                print('The vehicle is already started.')


class Room:
    def __init__(self, name=None, north=None, northeast=None, east=None, southeast=None, south=None, southwest=None,
                 west=None, northwest=None, up=None, down=None, desc=None, entered=False, objects=None):
        if objects is None:
            objects = []
        self.name = name
        self.north = north
        self.northeast = northeast
        self.east = east
        self.southeast = southeast
        self.south = south
        self.southwest = southwest
        self.west = west
        self.northwest = northwest
        self.up = up
        self.down = down
        self.desc = desc
        self.entered = entered
        self.objects = objects


class Character(object):
    def __init__(self, name, damage, lp, current_loc):
        self.name = name
        self.damage = damage
        self.health = lp
        self.current_loc = current_loc
        self.stunned = False

    def attack(self, target):
        if target.health > 0:
            extra = random.randint(0, 11)
            if extra != 4:
                print('You attack the %s for %d damage.' % (target.name, self.damage))
                target.take_damage(self.damage)
            elif extra == 7:
                print('The %s is stunned!' % target.name)
                target.stunned = True
            else:
                print('Your attack is blocked! You deal no damage.')

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print('You have died.')


class Player(Character):
    def __init__(self, name, damage, lp, current_loc, items=None, in_car=False):
        super(Player, self).__init__(name, damage, lp, current_loc)
        if items is None:
            items = []
        self.items = items
        self.in_car = in_car

    def display(self):
        print('\033[1m' + self.current_loc.name + '\033[0m')
        if not self.current_loc.entered:
            print(textwrap.fill(self.current_loc.desc, width=100))
            self.current_loc.entered = True
        if self.current_loc != old_car:
            if len(self.current_loc.objects) > 0:
                for thing in self.current_loc.objects:
                    if not issubclass(thing.__class__, Interactable):
                        print('There is a %s here.' % thing.name)

    def move(self, direction):
            self.current_loc = globals()[getattr(self.current_loc, direction)]
            self.display()

    def open(self, target):
        if target in self.current_loc.objects:
            # noinspection PyBroadException
            try:
                target.interact('open')
            except:
                print('You cannot perform this action.')
        else:
            print('You cannot see any such thing.')

    def take(self, target):
        if target in self.current_loc.objects:
            if target in self.items:
                print('You already have this.')

            elif issubclass(target.__class__, Interactable):
                print('You can\'t be serious.')

            else:
                # noinspection PyBroadException
                try:
                    self.items.append(target)
                    self.current_loc.objects.remove(target)
                    print('Taken.')
                except:
                    pass
        else:
            print('You cannot see any such thing.')

    def drop(self, target):
        if target in self.items:
            self.items.remove(target)
            self.current_loc.objects.append(target)
            print('Dropped.')
        else:
            print('You cannot drop something you don\'t have.')


class Enemy(Character):
    def __init__(self, name, damage, lp, current_loc, weapon):
        super(Enemy, self).__init__(name, damage, lp, current_loc, )
        self.weapon = weapon

    def attack(self, target):
        if target.health > 0:
            print('The %s attacks you with his %s for %d damage.' % (self.name, self.weapon, self.damage))
            target.take_damage(self.damage)
            extra = random.randint(0, 11)
            if extra == 4:
                # noinspection PyBroadException
                try:
                    player1.items.remove(sword)
                    print('The %s knocks your sword out of your hands!' % self.name)
                except:
                    # noinspection PyBroadException
                    try:
                        player1.items.remove(knife)
                        print('The %s knocks your knife out of your hands!' % self.name)
                    except:
                        pass

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print('The ' + self.name + ' has died.')


# Items
can = WateringCan('watering can', False, ['watering'])
paper = Paper('piece of paper', ['piece', 'of'])
egg = Egg('jewel encrusted egg', ['jewel', 'encrusted'], )
treasure = Treasure('small treasure chest', ['small'], )
portal = Portal('portal', [])
# Interactable
window = Window('window', 'The window is now open far enough for you to enter.', False, ['rusty'])
door = Door('door', 'The door is now open.', False, False, [])
mailbox = Mailbox('mailbox', 'There is a small piece of paper in the mailbox.', False, [])
chest = Chest('chest', 'There is a map in the chest.', False, [])
trapdoor = Trapdoor('trapdoor', 'The trapdoor opens, revealing a staircase to the attic.', False, [])
# Tools
# noinspection PyShadowingBuiltins
map = Map('map', 'NOH to Cellar: E x3  NE  D, To escape: NE  SE  NW  E  SW', [])
key = Key('key', [])
flashlight = Flashlight('flashlight', [], False)
# Weapons
sword = Sword('metal sword', 200, 40, 250, ['metal'])
knife = Knife('rusty knife', 100, 25, 75, ['rusty'])
# Consumables
lunch = Lunch('brown sack lunch', 50, False, ['brown', 'sack'])
potion = HPotion('health potion', 100, False, [])
# Vehicles
car = Car('car', False, [])

# Rooms
field = Room('Field', 'forest1', None, 'river', 'field', 'north_of_house', 'forest2', 'forest2', 'forest5', None, None,
             'You are in a field. To the north and west is a forest. The field extends to the east and to the south is \
a small house.', True)
# Forest
forest1 = Room('Forest', 'forest3', 'river2', 'large_hole', 'field', 'field', 'forest2', 'forest5', 'forest6', None,
               None, 'You are in a forest. There appears to be a clearing to the south.', False)
forest2 = Room('Forest', 'forest5', 'forest1', 'field', 'field', 'shed', 'forest8', 'forest7', 'forest4', None, None,
               'You are in a forest. There appears to be a clearing to the east. In the distance you hear the sound of \
a chirping bird.', False)
forest3 = Room('Forest', 'forest0', 'forest0', 'river2', 'large_hole', 'forest1', 'forest5', 'forest6', 'forest0',
               'treehouse', None, 'There are trees all around you. What light there is seems to be coming from the \
south. A nearby tree appears to have rungs nailed into the trunk.', False)
forest4 = Room('Forest', 'forest0', 'forest6', 'forest5', 'forest2', 'forest7', 'forest0', 'forest0', 'forest0',
               'up_a_tree', None, 'There are trees all around you. What light there is seems to be coming from the \
east. One tree has some low hanging branches.', False)
forest5 = Room('Forest', 'forest6', 'forest3', 'forest1', 'field', 'forest2', 'forest7', 'forest4', 'forest0', None,
               None, 'There are trees all around you. What light there is seems to be coming from the southeast.',
               False)
forest6 = Room('Forest', 'forest0', 'forest0', 'forest3', 'forest1', 'forest5', 'forest4', 'forest0', 'forest0', None,
               None, 'There are trees all around you. What light there is seems to be coming from the southeast.',
               False)
forest7 = Room('Forest', 'forest4', 'forest5', 'forest2', 'shed', 'forest8', 'forest0', 'forest0', 'forest0', None,
               None, 'There are trees all around you. What light there is seems to be coming from the southeast.',
               False)
forest8 = Room('Forest', 'forest7', 'forest2', 'shed', 'west_of_house', 'forest9', 'forest0', 'forest0', 'forest0',
               None, None, 'There are trees all around you. What light there is seems to be coming from the southeast.',
               False)
forest9 = Room('Forest', 'forest8', 'shed', 'west_of_house', None, None, None, 'forest0', 'forest0', None, None,
               'There are trees all around you. What light there is seems to be coming from the east.', False)
forest0 = Room('Forest', 'death_forest', 'death_forest', 'forest5', 'forest5', 'forest5', 'death_forest',
               'death_forest', 'death_forest', None, None, 'The forest continues to extend far into the north and the \
west and it gets darker the farther you go.', False)
death_forest = Room('', None, None, None, None, None, None, None, None, None, None, 'As you pass by a tree, you glance \
down at your compass to ensure you\'re heading in the right direction. You trip over a tree root and your compass \
smashes on the ground and breaks. Panicked, you run in the complete wrong direction and become lost in the forest. You \
will die in a matter of days.', False)
treehouse = Room('Treehouse', None, None, None, None, None, None, None, None, None, 'forest3', 'You are in a \
treehouse. There are open windows on the north and east walls. There is a small chest beneath one of the windows.',
                 False, [chest])
up_a_tree = Room('Up a Tree', None, None, None, None, None, None, None, None, None, 'forest4', 'You can see the \
extensive forest to the northwest the mountain to the east, and the river that separates the two.', False, [egg])
# Hole in forest
large_hole = Room('Large Hole', 'river2', 'bottom_of_hole', 'bottom_of_hole', 'bottom_of_hole', 'field', 'field',
                  'forest1', 'forest3', None, None, 'There is a large hole in the forest, about the width of a tree \
trunk. There seems to be a corridor to the east at the bottom.', False)
bottom_of_hole = Room('Bottom of Hole', None, None, 'labyrinth', None, None, None, None, None, None, None, 'You lost \
your footing going around the hole and fell in. There is no way for you to climb back up, but a corridor leads to the \
east.', False)
labyrinth = Room('Labyrinth', 'labyrinth', 'labyrinth', 'labyrinth', 'labyrinth', 'labyrinth', 'labyrinth', 'labyrinth',
                 'labyrinth', 'labyrinth', 'labyrinth', 'You are in the Labyrinth. Many explorers have tried to reach \
the treasure in the heart of the near inescapable maze, but they all died inexplicably... The walls are constantly \
changing. Good luck getting out!', False)
# Outside House
north_of_house = Room('North of House', 'field', 'field', 'east_of_house', None, None, None, 'west_of_house', 'shed',
                      None, None, 'You are north of the house. All the windows appear to be barred and the door is \
locked. There is a rusted mailbox here.', False, [mailbox])
east_of_house = Room('East of House', 'north_of_house', 'river', 'bridge', 'old_car', 'behind_house', None, None, None,
                     None, None, 'You are east of the house. All the windows here are barred. There are animal tracks \
in the ground.', False)
west_of_house = Room('West of House', 'north_of_house', None, None, None, 'behind_house', 'forest9', 'forest9', 'shed',
                     None, None, 'You are west of the house. There is a window here that is slightly ajar.', False,
                     [window])
behind_house = Room('Behind House', None, None, 'east_of_house', 'outside_garden', 'garden', 'garden', 'west_of_house',
                    None, None, None, 'You are behind the house. There is door here. You may be able to open it. There \
is a garden to the south.', False, [door])
shed = Room('Shed', 'forest2', None, 'north_of_house', None, 'west_of_house', 'forest9', 'forest8', 'forest7', None,
            None, 'There is an old shed here. The door is locked.', False)
garden = Room('Garden', 'behind_house', None, None, None, None, None, None, None, None, None, 'You are in a beautiful \
garden. The only exit is to the north.', False, [can])
outside_garden = Room('Outside Garden', 'east_of_house', 'old_car', 'old_car', 'desert', 'desert', None, None,
                      'behind_house', None, None, 'You are outside the fence of the garden. There is a desert to the \
south. In the distance you can see a tall building.', False)
old_car = Room('Old Car', 'bridge', None, None, 'desert', 'desert', 'outside_garden', 'outside_garden', 'east_of_house',
               None, None, 'Here is an old, rusty car. There are no keys inside the car and the door is locked.',
               False, [car])
desert = Room('Desert', 'old_car', None, 'desert', 'desert2', 'desert2', 'desert2', 'desert', 'outside_garden',
              None, None, 'You are in the desert. There is a mountain to the north and the remains of a city to the \
south.')
desert2 = Room('Desert', 'desert', 'desert', 'desert2', 'city', 'city', 'city', 'desert2', 'desert', None, None, 'You \
are in the desert. There is a mountain to the north and the remains of a city to the south.')
city = Room('The City of Zork', 'desert2', 'desert2', None, None, None, None, None, 'desert2', None, None, 'Welcome to \
the City of Zork! At it\'s peak, this city was amazing. There were beautiful buildings, luscious parks, and friendly \
neighborhoods all throughout the city. One day, a rumor was spread about a treasure in the nearby forest. After a \
week, the city descended into chaos. Everyone wanted the treasure and many people were killing for it. Some even \
reported seeing a deadly troll guarding the treasure. In order to repair the city, the people need the treasure to \
buy materials from other cities. It\'s your job to find the treasure and save the city.')
# Inside House
kitchen = Room('Kitchen', None, None, 'living_room', None, None, None, None, None, None, None, 'You are in \
the kitchen. There is a door to the east and the and a window to the west.', False, [lunch])
living_room = Room('Living Room', None, 'bedroom', None, None, 'back_hallway', None, 'kitchen', None, None, None,
                   'The front door is to the north. There is a hallway to the northeast and a hallway to the south \
that leads to the back door. There is also a door to the west.', False, [door, sword])
storage_room = Room('Storage Room', None, None, 'back_hallway', None, 'basement', None, None, None, None, 'basement',
                    'There are a bunch of empty boxes in here. There is a door to the east and some stairs on the \
south side of the room.', False)
bedroom = Room('Bedroom', None, None, None, None, None, 'living_room', None, None, None, None, 'You are in the \
bedroom. The bed is made and the room is relatively clean.', False, [key])
back_hallway = Room('Back Hallway', 'living_room', None, None, None, 'behind_house', None, 'storage_room', None, None,
                    None, 'The door to the south leads to out of the house. The hallway goes north into the living \
room. There is a small trapdoor with a handle on the ceiling and another door to the west.', False, [trapdoor])
basement = Room('Basement', 'storage_room', None, None, None, None, None, None, None, 'storage_room', None, 'The light \
in the basement is broken, but some sunlight is coming through a broken window. There are stairs to the north. It \
smells funny in here... ', False)
attic = Room('Attic', None, None, None, None, None, None, None, None, None, None, 'It is dark in here. You \
can barely see anything. The trapdoor shuts loudly beneath you. You try to kick it open but someone has barred it \
from the outside.', False, [flashlight])
# Mountain
river = Room('River', 'river2', None, None, None, 'bridge', 'field', 'field', 'large_hole', None, None, 'At the end of \
the field is a river. It extends far north into the forest. Across the river is a large mountain. The river continues \
south and goes around the mountain.', False)
river2 = Room('River', 'river2', None, None, None, 'river', 'large_hole', 'forest3', 'forest0', None, None, '', False)
bridge = Room('Bridge', 'river', None, 'base_of_mountain', None, 'old_car', None, 'east_of_house', None, None, None,
              'You\'re at the bridge. Be careful going across, there might be a troll under it...', False)
base_of_mountain = Room('Base of Mountain', None, 'cave', None, None, None, None, 'bridge', None, None, None, 'You \
crossed the bridge and are at the base of the mountain. There is a cave to the northeast.', False)
cave = Room('Cave', None, None, 'cellar', None, None, None, 'base_of_mountain', None, None, 'cellar', 'You are in a \
cave. The light from outside illuminates a set of stairs to the east that lead into darkness.', False)
cellar = Room('Cellar', 'labyrinth', None, 'troll_room', None, None, 'cave', None, None, 'cave', None, 'You are a dark \
cellar. Despite no light coming from outside, there seems to be an ominous yellow glow that dimly lights up the room. \
There are paths to the north, east, and west.', False, [knife])
troll_room = Room('Troll Room', None, None, None, None, None, None, 'cellar', None, None, None,
                  'An angry, yellow-eyed, green troll, brandishing a bloody axe, blocks your path. There is an exit \
back to the west, but the troll doesn\'t seem to be letting you go freely anytime soon.', False)
heart_of_mountain = Room('Heart of Mountain', 'troll_room', None, 'treasure_room', None, None, None, None, None,
                         'treasure_room', None, 'You are in the center of the mountain. The yellow glow is very bright \
in here. There is a ladder going up on the east wall and an exit to the north.', False)
treasure_room = Room('Treasure Room', None, None, 'heart_of_mountain', None, None, None, 'basement', None, None,
                     'heart_of_mountain', 'Hey, you made it. There is a long corridor to the west and a \
ladder going down on the east wall.', False, [treasure])

# Characters
player1 = Player('name', 0, 100, field)
troll = Enemy('troll', 35, 75, troll_room, 'battle axe')

# Variables
alive = True
location = field
directions = ['north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest', 'up', 'down']
directions2 = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'u', 'd']
keywords_list = ['up', 'the', 'piece', 'of', 'jewel', 'encrusted', 'rusty', 'coil', 'metal', 'brown', 'sack',
                 'watering', 'front', 'back', 'small', 'at', 'health', 'old', 'rusty']


def select_weapon():
    if sword in player1.items:
        player1.damage = sword.damage
    elif knife in player1.items:
        player1.damage = knife.damage


# Controller
print(textwrap.fill('Welcome! To move around, type in "north", "northeast", "east", "southeast", etc. If you want to \
interact with any objects, type in what you want to do and what you want to interact with. To attack, type in "attack" \
and specify your target. If you want to check your inventory or your stats, type "inventory" or "stats".', width=100))
print()
game_start = input('Are you ready to play? ').lower()
if game_start != 'yes':
    print('Too bad.')
print()
print('\033[1m' + field.name + '\033[0m')
print(textwrap.fill(field.desc, width=100))
while alive:
    if player1.health <= 0:
        sys.exit(0)

    print()
    _user_command = input('> ').lower()
    if player1.in_car:
        player1.health += 75
        old_car.north = None
        old_car.southwest = None
        old_car.west = None
        old_car.northwest = None
        desert.northwest = None

    interact(_user_command)
    words = str.split(_user_command)

    if player1.current_loc == desert2 and player1.health < 100:
        print('You cannot survive the extreme desert heat. You are dead.')
        player1.health = 0

    elif player1.current_loc in [forest5, forest6]:
        new_room = random.randint(0, 11)
        if new_room == 1:
            player1.current_loc = forest1

        elif new_room == 2:
            player1.current_loc = forest2

        elif new_room == 3:
            player1.current_loc = forest3

        elif new_room == 4:
            player1.current_loc = forest4

        elif new_room == 5:
            player1.current_loc = forest5

        elif new_room == 6:
            player1.current_loc = forest6

    elif player1.current_loc == death_forest:
        sys.exit(0)

    elif player1.current_loc == troll_room:
        if troll.health > 0 and troll.stunned is False:
            troll.attack(player1)
        elif troll.health <= 0:
            troll_room.east = 'heart_of_mountain'
            troll_room.desc = 'There is an exit to the west and a path that continues to the east.'
        if troll.stunned:
            troll.stunned = False

    elif player1.current_loc == labyrinth:
        input_list = []
        escape_code = ['ne', 'se', 'nw', 'e', 'sw']
        while player1.current_loc == labyrinth:
            for index in range(len(input_list)):
                if input_list[index] != escape_code[index]:
                    input_list = []

            if input_list == escape_code:
                player1.current_loc = cellar
                print(player1.current_loc.name)
                print(textwrap.fill(player1.current_loc.desc, width=100))

            else:
                rand_num = random.randint(0, 1001)
                if rand_num % 28 == 0:
                    player1.current_loc = cellar
                    print()
                    print(player1.current_loc.name)
                    print(textwrap.fill(player1.current_loc.desc, width=100))

                elif rand_num % 70 == 0:
                    player1.current_loc = bottom_of_hole
                    print()
                    print(player1.current_loc.name)
                    print(textwrap.fill(player1.current_loc.desc, width=100))

                elif rand_num == 666:
                    player1.current_loc = treasure_room
                    print()
                    print(player1.current_loc.name)
                    print(textwrap.fill(player1.current_loc.desc, width=100))

                else:
                    pass
            interact(input('> ').lower())
            input_list.append(words[0])
