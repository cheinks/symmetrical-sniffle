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


game_difficulty = 'Easy'
total_score = 100

old_high_scores = high_score()
if int(old_high_scores[game_difficulty]) < total_score:
    old_high_scores[game_difficulty] = str(total_score)
    final_export = ''
    for item in list(old_high_scores.items()):
        temp_string = item[0] + ' - ' + item[1]
        final_export = final_export + temp_string + '\n'
    print(final_export)
    file = open('HighScores.txt', 'w')
    file.write(final_export)
    file.close()
