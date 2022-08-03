import time
import os
import datetime
from playsound import playsound

from file_operations import time_data
from utility import formatting


def main():
    MINUTES_TO_STUDY = 30
    MINUTES_FOR_BREAK = 5

    # Pomodoro Technique implementation
    STUDY_TIME = MINUTES_TO_STUDY * 60
    # set the amount of seconds in break time
    BREAK_TIME = MINUTES_FOR_BREAK * 60

    # show the user how much time they've studied today
    print('*-----------------------------------*')
    time_data.print_todays_practice_progress()
    print('*-----------------------------------*')
    print(
        f'It\'s currently { datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") }')
    # a counter to check where the time is sitting. It will reset each time a break has occured.
    pomodoro_start = time.time()
    # tracker for how many minute studied. I have to do this due to pauses in the code.
    total_time_studied = 0

    # play sound effect for the beginning of the loop
    playsound('./sounds/yeah-boy-memes-comedy-funny-amusing-jokes-114748.mp3')
    while True:
        # update the tracker's count
        pomodoro_tracker = time.time()

        # checks if the user has been studying for a study period.
        if pomodoro_tracker - pomodoro_start >= STUDY_TIME:
            # add 25 minutes to total time studied
            total_time_studied += STUDY_TIME

            # play sound effect to alert the user
            playsound('./sounds/pixel-death-66829.mp3')
            print(f"Warning: {MINUTES_FOR_BREAK}-minute break time!")

            # pause the program for 5 minutes
            for _ in range(BREAK_TIME):
                time.sleep(1)

            # after each break, check if the user wants to keep studyig
            continue_studying_check = input(
                "Hello again! Would you like to keep studying (yes/no)? ").strip()

            # check if the user's response is equal to anything in these lists
            if(continue_studying_check.lower() in ['yes', 'y', 'yeah', 'sure']):
                # reset the start of the time tracking to the current time. example: 35 (pomodoro_tracker) - 35 (pomodoro_start) = 0
                print(
                    f'It\'s currently { datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S") }')
                playsound(
                    './sounds/yeah-boy-memes-comedy-funny-amusing-jokes-114748.mp3')
                pomodoro_start = time.time()
            elif(continue_studying_check.lower() in ['no', 'n', 'never', 'nah']):
                break
            else:
                print("Invalid input. Exiting study timer.")
                break

    # print the time the program ran
    formatted_runtime = formatting.format_seconds_to_hms(total_time_studied)
    print(formatted_runtime)

    # Print the date
    print(f'It is currently {datetime.datetime.now()}')

    # file away the new data
    time_data.write_new_record(total_time_studied)


if __name__ == "__main__":
    main()
