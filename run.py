import time
import os
import datetime

from file_operations import time_data
from utility import formatting


def main():
    end_conditions = ['end', 'e']
    clear_conditions = ['cls', 'clear']

    # show the user how much time they've studied today
    print('*-----------------------------------*')
    time_data.print_todays_practice_progress()
    print('*-----------------------------------*')
    print(
        f'It\'s currently { datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") }')
    exit_string = '(e)nd'
    # start the timer and the loop
    start = time.time()

    while True:
        # get the choice from the user
        print(f"enter '{exit_string}' to end the timer")
        val = input().lower()
        # the user chose to end the timer
        if val in end_conditions:
            break
        elif val in clear_conditions:
            os.system('clear')

    # calculate the time the program has run
    runtime = time.time() - start

    # print the time the program ran
    formatted_runtime = formatting.format_seconds_to_hms(runtime)
    print(formatted_runtime)

    # Print the date
    print(f'It is currently {datetime.datetime.now()}')

    # file away the new data
    time_data.write_new_record(runtime)


if __name__ == "__main__":
    main()
