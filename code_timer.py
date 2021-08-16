import time
import datetime
import os

# Display how much studying has been completed today
def print_todays_practice_time():
    FILENAME = 'timer_data.txt'
    todays_time_studying = 0
    
    # read data from file -- if it doesn't exist then create it'
    with open(f'{FILENAME}', 'a+') as f:
    # parse through the data and read in the records only for today
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

# show the user how much time they've studied today
print_todays_practice_time()
# start the timer and the loop
start = time.time()
while True:
    # get the choice from the user
    print('enter \'end\' to end the timer')
    val = input()
    print(time.time() - start)
    if val == 'end':
        # end the timer
        break
# calculate the time the program has run
runtime = time.time() - start
# print the time the program ran
if runtime > 60:
    print(f'You spent {runtime/60:.2f} minute(s)')
elif runtime > 3600:
    print(f'You spent {runtime/3600:.2f} hour(s)')
else:
    print(f'You spent {runtime:.2f} second(s)')
# Print the date
print(f'Today\'s date is {datetime.date.today()}')

# log the user's study time to the timer_data.txt
with open('timer_data.txt', 'a') as f:
    f.write(f'{datetime.date.today()},{runtime:.2f}\n')
