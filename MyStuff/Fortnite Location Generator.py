import random
import string

named_locations = ["Anarchy Acres", "Dusty Divot", "Fatal Fields", "Flush Factory", "Greasy Grove", "Haunted Hills",
                   "Junk Junction", "Lonely Lodge", "Loot Lake", "Lucky Landing", "Moisty Mire", "Pleasant Park",
                   "Retail Row", "Risky Reels", "Salty Springs", "Shifty Shafts", "Snobby Shores", "Tilted Towers",
                   "Tomato Town", "Wailing Woods"]
alphabet = []
for character in string.ascii_uppercase:
    alphabet.append(character)
alphabet = alphabet[:10]
natural_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
off_map_coordinates = [" ", "(A, 1)", "(A, 2)", "(A, 3)", "(A, 7)", "(A, 8)", "(A, 9)", "(A, 10)", "(B, 8)", "(B, 9)",
                       "(B, 10)", "(C, 8)", "(C, 9)", "(C, 10)", "(D, 10)", "(E, 1)", "(F, 1)", "(G, 1)", "(H, 1)",
                       "(I, 1)", "(I, 10)", "(J, 1)", "(J, 9)", "(J, 10)"]

generating = True
invalid = True
user_choices = ['1', '2', "named location", "coordinate location"]
result = ''
locations_generated = 0


def random_named_location(locations):
    return locations[random.randint(1, len(locations)) - 1]


def random_coordinate_location(letters, numbers, bad_coordinates):
    coordinate_location = " "
    while coordinate_location in bad_coordinates:
        x_coordinate = letters[random.randint(1, len(letters)) - 1]
        y_coordinate = str(numbers[random.randint(1, len(numbers)) - 1])
        coordinate_location = '(' + x_coordinate + ', ' + y_coordinate + ')'
    return coordinate_location


print("Welcome to the Fortnite Battle Royale Location Generator!\n")
while invalid:
    user_input = input("Would you like to generate 1. named locations or 2. coordinate locations? ").lower()
    if user_input in ['1', '2', 'named location', 'coordinate location']:
        invalid = False
        print("Okay.")
    else:
        print("Please enter a valid response.\n")
while generating:
    generation_input = input("\nGenerate location? (Y/N): ").upper()
    if generation_input == 'Y':
        if user_input == user_choices[0] or user_input == user_choices[2]:
            result = random_named_location(named_locations)
        elif user_input == user_choices[1] or user_input == user_choices[3]:
            result = str(random_coordinate_location(alphabet, natural_numbers, off_map_coordinates))
        print('> ' + result)
        locations_generated += 1
    elif generation_input == 'N':
        generating = False
        print("Bye! Have a great time!")
    else:
        print("Please enter a valid response.")

print("\nLocations generated: " + str(locations_generated))
