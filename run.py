import time
import datetime
from file_operations import time_data


def main():
    # show the user how much time they've studied today
    time_data.print_todays_practice_progress()

    exit_string = '(e)nd'

    # start the timer and the loop
    start = time.time()
    while True:
        # get the choice from the user
        print(f"enter '{exit_string}' to end the timer")
        val = input()
        # the user chose to end the timer
        if val.lower() == 'end' or val.lower() == 'e':
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
    print(f'It is currently {datetime.datetime.now()}')

    # file away the new data
    time_data.write_new_record(runtime)

    time_data.print_study_record_all()


if __name__ == "__main__":
    main()
