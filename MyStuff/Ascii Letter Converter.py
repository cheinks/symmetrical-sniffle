import string

my_list = [
    ' #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ',
    '# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   # ',
    '### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #  ',
    '# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #   ',
    '# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ### '
]
my_list_2 = [
    '     #      ### ',
    '     #        # ',
    '     #       ## ',
    '                ',
    '     #  #    #  '
]
for i in range(0, 5):
    my_list[i] += my_list_2[i]
letters_list = []
for letter in string.ascii_uppercase:
    letters_list.append(letter)
letters_list.append(' ')
letters_list.append('!')
letters_list.append('.')
list_modifier = 0
character_list = []

length = 4  # int(input())
height = 5  # int(input())
user_input = input("What phrase do you want to be converted into ASCII art?\n> ").upper()

for each_index in range(0, len(user_input)):
    response_list = []
    if user_input[each_index] in letters_list:
        list_modifier = letters_list.index(user_input[each_index])
    else:
        list_modifier = len(letters_list)
    for index_2 in range(height):
        response_list.append(my_list[index_2][list_modifier * length:length + (list_modifier * length)])
    character_list.append(response_list)

for i in range(height):
    temp_string = ''
    for i_2 in range(0, len(character_list)):
        temp_string += character_list[i_2][i]

    print(temp_string)
