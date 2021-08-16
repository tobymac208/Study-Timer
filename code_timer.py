import time
import datetime
import file_operations

# show the user how much time they've studied today
file_operations.print_todays_practice_time()

# start the timer and the loop
start = time.time()
while True:
    # get the choice from the user
    print('enter \'end\' to end the timer')
    val = input()
    # the user chose to end the timer
    if val == 'end':
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

file_operations.write_new_record(runtime)