import datetime
## File Operations for goal.txt file ##
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

## File Operations for timer_data.txt file ##
_filename = 'timer_data.txt'
""" Display how much studying has been completed today """
def print_todays_practice_time():
    todays_time_studying = 0
    
    # read data from file. if it doesn't exist then create it
    with open(f'{_filename}', 'a+') as f:
        # 'seek' the beginning of the file (https://stackoverflow.com/questions/14639936/how-to-read-from-file-opened-in-a-mode)
        f.seek(0)
        lines = f.readlines()
        # go through each line, split it into an array, and look for today's date
        for line in lines:
            record = line.split(',')
        # remove the newline character from the time
            record[1] = record[1].strip()
        # convert date string to date
            record_date = datetime.datetime.strptime(record[0], '%Y-%m-%d').date()
        # if they studied today, it will be added to our 'time_studying' counter
            if record_date == datetime.date.today():
                todays_time_studying = todays_time_studying + float(record[1])
    
    # TODO: Refactor to follow DRY
    # grab the user's goal and check if they've met it
    the_users_goal = retrieve_goal()
    # the user hasn't set a goal yet
    if the_users_goal == 0:
        # request the goal and write the goal to the file
        write_goal(request_goal())
        # attempt to retrieve the goal again
        the_users_goal = retrieve_goal()
    
    # append this string to the end of each message
    achieved_goal = ''
    if todays_time_studying/60 >= the_users_goal:
        achieved_goal = 'You\'ve achieved your goal! Congratulations!'
    else:
        achieved_goal = 'You haven\'t achieved your goal. Keep up the work!'

    # print the current time worked today
    if todays_time_studying > 60 and todays_time_studying < 3600:
        print(f'You\'ve studied for {todays_time_studying/60:.2f} minutes(s) today. {achieved_goal}')
    elif todays_time_studying > 3600:
        print(f'You\'ve studied for {todays_time_studying/3600:.2f} hours(s) today. {achieved_goal}')
    else:
        print(f'You\'ve studied for {todays_time_studying:.2f} second(s) today. {achieved_goal}')

""" Write new record to file

    Input Arguments: runtime
 """
def write_new_record(runtime):
    # log the user's study time to the timer_data.txt
    with open(f'{_filename}', 'a') as f:
        f.write(f'{datetime.date.today()},{runtime:.2f}\n')
