# Defines methods for the user to set their own goals for using this application.
_goal_filename = 'goal.txt'
""" Read in the 'study time goal' for the user 

    Returns: time goal
"""
def retrieve_goal():
    goal = 0
    # open the file. 'a+' is for if the file doesn't exist
    with open(_goal_filename, 'a+') as f:
        # go to the first character and then read the goal
        f.seek(0)
        goal_read = f.read().strip()
        if goal_read == '':
            goal = 0
        else:
            float(goal_read)
    # give the caller the goal
    return goal
""" Write the user's time goal to the file """
def write_goal(goal):
    with open(_goal_filename, 'w') as f:
        f.write(str(goal))
""" Get the user's study goal """
def request_goal():
    print('It appears you haven\'t set a goal. \nLet\'s set a goal so you know where you stand!')
    goal = float(input('Your goal (in minutes): '))

    return goal