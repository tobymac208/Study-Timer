import datetime

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
    
    # print the current time worked today
    # TODO: Refactor to follow DRY
    if todays_time_studying > 60 and todays_time_studying < 3600:
        print(f'You\'ve studied for {todays_time_studying/60:.2f} minutes(s) today')
    elif todays_time_studying > 3600:
        print(f'You\'ve studied for {todays_time_studying/3600:.2f} hours(s) today')
    else:
        print(f'You\'ve studied for {todays_time_studying:.2f} second(s) today')

""" Write new record to file

    Input Arguments: tunetime
 """
def write_new_record(runtime):
    # log the user's study time to the timer_data.txt
    with open(f'{_filename}', 'a') as f:
        f.write(f'{datetime.date.today()},{runtime:.2f}\n')
