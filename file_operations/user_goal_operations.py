from file_operations import create_directory
# Defines methods for the user to set their own goals for using this application.
_goal_filename = 'raw_data/goal.txt'


""" Read in the 'study time goal' for the user 

    Returns: time goal
"""
def retrieve_goal():
    goal = 0
    # open the file. 'a+' is for if the file doesn't exist
    with create_directory.safe_open_read(_goal_filename) as f:
        try:
            # go to the first character and then read the goal
            f.seek(0)
            goal = float(f.read().strip())
        except ValueError as e:
            # there was no goal found
            goal = 0
    # give the caller the goal
    return goal


""" Write the user's time goal to the file """
def write_goal_to_file(goal):
    with open(_goal_filename, 'w') as f:
        f.write(str(goal))


""" Get the user's study goal from the user. They haven't set it yet. """
def request_goal_from_user():
    print('It appears you haven\'t set a goal. \nLet\'s set a goal so you know where you stand!')
    goal = float(input('Your goal (in minutes): '))

    return goal


""" Compare the goal and today's study time. 
    returns: boolean for if they have made their time or not
"""
def has_made_goal(todays_time_studying):
    users_goal = retrieve_goal()
    made_goal = False

    # the user hasn't set a goal yet
    if users_goal == 0:
        # request the goal and write the goal to the file
        write_goal_to_file(request_goal_from_user())
        # attempt to retrieve the goal again
        users_goal = retrieve_goal()
    
    if todays_time_studying/60 >= users_goal:
        made_goal = True

    return made_goal