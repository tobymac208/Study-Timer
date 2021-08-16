import datetime
from file_operations import user_goal_operations

# Defines methods for managing the tracking of the user's time
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
    # TODO: Fix '0' return for user's goal
    # grab the user's goal and check if they've met it
    the_users_goal = user_goal_operations.retrieve_goal()
    # the user hasn't set a goal yet
    if the_users_goal == 0:
        # request the goal and write the goal to the file
        user_goal_operations.write_go_to_file(user_goal_operations.request_goal_from_user())
        # attempt to retrieve the goal again
        the_users_goal = user_goal_operations.retrieve_goal()
    
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
