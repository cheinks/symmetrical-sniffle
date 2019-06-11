import random


def roll_the_dice():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    return die_1 + die_2


game_counter = 1000000
jail_counter = 0
monopoly_database = {
    '0': {'NAME': 'GO', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '1': {'NAME': 'Mediterranean Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Purple'},
    '2': {'NAME': 'Community Chest (1)', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '3': {'NAME': 'Baltic Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Purple'},
    '4': {'NAME': 'Income Tax', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '5': {'NAME': 'Reading Railroad', 'TIMES_LANDED': 0, 'COLOR': 'Railroad'},
    '6': {'NAME': 'Oriental Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Gray'},
    '7': {'NAME': 'Chance (1)', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '8': {'NAME': 'Vermont Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Gray'},
    '9': {'NAME': 'Connecticut Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Gray'},
    '10': {'NAME': 'Jail / Just Visiting', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '11': {'NAME': 'St. Charles Place', 'TIMES_LANDED': 0, 'COLOR': 'Pink'},
    '12': {'NAME': 'Electric Company', 'TIMES_LANDED': 0, 'COLOR': 'Utility'},
    '13': {'NAME': 'States Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Pink'},
    '14': {'NAME': 'Virginia Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Pink'},
    '15': {'NAME': 'Pennsylvania Railroad', 'TIMES_LANDED': 0, 'COLOR': 'Railroad'},
    '16': {'NAME': 'St. James Place', 'TIMES_LANDED': 0, 'COLOR': 'Orange'},
    '17': {'NAME': 'Community Chest (2)', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '18': {'NAME': 'Tennessee Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Orange'},
    '19': {'NAME': 'New York Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Orange'},
    '20': {'NAME': 'Free Parking', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '21': {'NAME': 'Kentucky Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Red'},
    '22': {'NAME': 'Chance (2)', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '23': {'NAME': 'Indiana Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Red'},
    '24': {'NAME': 'Illinois Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Red'},
    '25': {'NAME': 'B & O Railroad', 'TIMES_LANDED': 0, 'COLOR': 'Railroad'},
    '26': {'NAME': 'Atlantic Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Yellow'},
    '27': {'NAME': 'Vermont Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Yellow'},
    '28': {'NAME': 'Water Works', 'TIMES_LANDED': 0, 'COLOR': 'Utility'},
    '29': {'NAME': 'Marvin Gardens', 'TIMES_LANDED': 0, 'COLOR': 'Yellow'},
    '30': {'NAME': 'Go to Jail', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '31': {'NAME': 'Pacific Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Green'},
    '32': {'NAME': 'North Carolina Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Green'},
    '33': {'NAME': 'Community Chest (3)', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '34': {'NAME': 'Pennsylvania Avenue', 'TIMES_LANDED': 0, 'COLOR': 'Green'},
    '35': {'NAME': 'Short Line', 'TIMES_LANDED': 0, 'COLOR': 'Railroad'},
    '36': {'NAME': 'Chance (3)', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '37': {'NAME': 'Park Place', 'TIMES_LANDED': 0, 'COLOR': 'Blue'},
    '38': {'NAME': 'Luxury Tax', 'TIMES_LANDED': 0, 'COLOR': 'N/A'},
    '39': {'NAME': 'Boardwalk', 'TIMES_LANDED': 0, 'COLOR': 'Blue'}
}
player_1 = {
    'LOCATION': 0,
    'IN_JAIL': False
}
purple = [0, 'purple']
railroad = [0, 'railroad']
gray = [0, 'gray']
pink = [0, 'pink']
utility = [0, 'utility']
orange = [0, 'orange']
red = [0, 'red']
yellow = [0, 'yellow']
green = [0, 'green']
blue = [0, 'blue']

while game_counter > 0:
    if not player_1['IN_JAIL']:
        player_1['LOCATION'] += roll_the_dice()
        if player_1['LOCATION'] > 39:
            player_1['LOCATION'] -= 40
    else:
        jail_counter += 1
        if jail_counter >= 3:
            jail_counter = 0
            player_1['IN_JAIL'] = False
    if player_1['IN_JAIL']:
        pass
    else:
        monopoly_database[str(player_1['LOCATION'])]['TIMES_LANDED'] += 1
    if player_1['LOCATION'] == 29:
        player_1['IN_JAIL'] = True
        player_1['LOCATION'] = 10
    game_counter -= 1

for item in monopoly_database:
    m_d = monopoly_database
    if m_d[item]['COLOR'] == 'Purple':
        purple[0] += m_d[item]['TIMES_LANDED']
    elif m_d[item]['COLOR'] == 'Railroad':
        railroad[0] += m_d[item]['TIMES_LANDED']
    elif m_d[item]['COLOR'] == 'Gray':
        gray[0] += m_d[item]['TIMES_LANDED']
    elif m_d[item]['COLOR'] == 'Pink':
        pink[0] += m_d[item]['TIMES_LANDED']
    elif m_d[item]['COLOR'] == 'Utility':
        utility[0] += m_d[item]['TIMES_LANDED']
    elif m_d[item]['COLOR'] == 'Orange':
        orange[0] += m_d[item]['TIMES_LANDED']
    elif m_d[item]['COLOR'] == 'Red':
        red[0] += m_d[item]['TIMES_LANDED']
    elif m_d[item]['COLOR'] == 'Yellow':
        yellow[0] += m_d[item]['TIMES_LANDED']
    elif m_d[item]['COLOR'] == 'Green':
        green[0] += m_d[item]['TIMES_LANDED']
    elif m_d[item]['COLOR'] == 'Blue':
        blue[0] += m_d[item]['TIMES_LANDED']

temp_var = monopoly_database['0']
is_highest = True
for item in monopoly_database:
    m_d = monopoly_database
    if m_d[item]['COLOR'] != 'N/A':
        if m_d[item]['TIMES_LANDED'] > temp_var['TIMES_LANDED']:
            temp_var = m_d[item]
        elif m_d[item]['TIMES_LANDED'] == temp_var['TIMES_LANDED']:
            is_highest = False

result_list = [purple, railroad, gray, pink, utility, orange, red, yellow, green, blue]
result_list.sort(key=None, reverse=True)
for each_result in result_list:
    print('A ' + each_result[1] + ' property was landed on ' + str(each_result[0]) + ' times.')

if is_highest:
    print('The property that landed on the most was the ' + temp_var['COLOR'].lower() + ' property ' +
          temp_var['NAME'] + '. ' + 'It was landed on ' + str(temp_var['TIMES_LANDED']) + ' times.')
