# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
goal_scorer_1 = 'Ruud Gullit'
goal_scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = goal_scorer_1 + " " + str(goal_0) + ", " + goal_scorer_2 + " " +str(goal_1)

report = f'''{goal_scorer_1} scored in the {str(goal_0)}nd minute
{goal_scorer_2} scored in the {str(goal_1)}th minute'''

player = 'Frank Rijkaard'
first_name = player[0:player.find(' ')]
last_name = player[(player.find(' ') + 1):]
last_name_len = len(last_name)
name_short = f'{first_name[0]}. {last_name}'

chant = (f'{first_name}! ' * int(len(first_name))).rstrip()
good_chant = (chant[(len(chant) - 1)] != ' ')
