import datetime
from file_operations import user_goal
from file_operations import create_directory
from utility import formatting

_filename = 'raw_data/timer_data.txt'


def retrieve_todays_practice_time():
    '''
    Grab all of the current day's time and return it to the user
    '''
    # time tracker for the day's studying
    todays_time_studying = 0

    # read data from file. if it doesn't exist then create it
    with create_directory.safe_open_read(_filename) as f:
        # 'seek' the beginning of the file (https://stackoverflow.com/questions/14639936/how-to-read-from-file-opened-in-a-mode)
        f.seek(0)
        for line in f.readlines():
            record = line.split(',')
            record[1] = record[1].strip()
            record_date = datetime.datetime.strptime(
                record[0], '%Y-%m-%d').date()
        # if they studied today, it will be added to our 'time_studying' counter
            if record_date == datetime.date.today():
                todays_time_studying = todays_time_studying + float(record[1])
    return todays_time_studying


def print_todays_practice_progress():
    """ 
    Display how much studying has been completed today
    """
    # grab the user's progress time for today
    todays_study_time = retrieve_todays_practice_time()

    # compare the user's goal with their time spent studying
    has_made_daily_goal = user_goal.has_made_goal(todays_study_time)

    # message for if the user has met their goal
    goal_message = ''
    if has_made_daily_goal:
        goal_message = 'Congratulations! You made your daily goal.'
    else:
        goal_message = 'Keep working at your goal!'

    # TODO: DRY compliance!!!!!
    if todays_study_time > 60 and todays_study_time < 3600:
        print(
            f'You\'ve studied for {todays_study_time/60:.2f} minutes(s) today. \n{goal_message}')
    elif todays_study_time > 3600:
        print(
            f'You\'ve studied for {todays_study_time/3600:.2f} hours(s) today. \n{goal_message}')
    else:
        print(
            f'You\'ve studied for {todays_study_time:.2f} second(s) today. \n{goal_message}')


def write_new_record(runtime):
    """ 
    Write new record to file
    Input Arguments: runtime
    """
    # log the user's study time to the timer_data.txt
    with open(_filename, 'a+') as f:
        f.write(f'{datetime.date.today()},{runtime:.2f}\n')


def print_all_work():
    '''
    Previous week's worth of work.
    Prints the last seven days' worth of studying.
    '''
    study_dictionary = {}

    # create a dictionary of all time records.
    with create_directory.safe_open_read(_filename) as f:
        f.seek(0)
        for line in f.readlines():
            date_study_time = line.split(',')
            date_thats_being_analyzed = date_study_time[0]
            study_time_thats_being_analyzed = float(date_study_time[1])
            if date_thats_being_analyzed in study_dictionary:
                study_dictionary[date_thats_being_analyzed] += study_time_thats_being_analyzed
            else:
                study_dictionary[date_thats_being_analyzed] = study_time_thats_being_analyzed

    # prints a formatted list of all of the study records
    count = 0
    print('*-------------------------------------*')
    for key in study_dictionary:
        count += 1
        # Print the date with formatted times.
        print(
            f'{count}. {key}={formatting.format_seconds_to_hms(study_dictionary[key])}')
