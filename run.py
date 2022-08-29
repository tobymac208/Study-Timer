import time
import sys

from datetime import datetime
from playsound import playsound

from file_operations import time_data
from utility import formatting


def main():
    # DEBUG: I'm going to try this out! I've already backed up all data :)
    time_data.clean_records()

    # check if the user passed a desired study time in minutes
    users_input = None
    
    try:
        # attempt to convert the value to an integer. if it's null, an exception will be thrown
        users_input = int(sys.argv[1].strip()) # strips empty space
    # naked exception
    except: # the user didn't pass another value
        pass

    MINUTES_TO_STUDY = users_input if users_input != None else 25 # sets MINUTES_TO_STUDY to what the user specified. if the user didn't specify then set it to 25 minutes.
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
        f'It\'s currently { datetime.now().strftime("%d/%m/%Y %H:%M:%S") }')
    # a counter to check where the time is sitting. It will reset each time a break has occured.
    pomodoro_start = time.time()

    # play sound effect for the beginning of the loop
    playsound('./sounds/yeah-boy-memes-comedy-funny-amusing-jokes-114748.mp3')
    while True:
        # update the tracker's count
        pomodoro_tracker = time.time()

        # checks if the user has been studying for a study period.
        if pomodoro_tracker - pomodoro_start >= STUDY_TIME:
            # play sound effect to alert the user
            playsound('./sounds/pixel-death-66829.mp3')
            print(f"Warning: {MINUTES_FOR_BREAK}-minute break time!")

            # write the study time to the file
            formatted_runtime = formatting.format_seconds_to_hms(STUDY_TIME)
            print(f"You just studied for {formatted_runtime}.")
            # write the studied time to the file
            time_data.write_new_record(STUDY_TIME)

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
                    f'It\'s currently { datetime.now().strftime("%d/%m/%Y %H:%M:%S") }')
                playsound(
                    './sounds/yeah-boy-memes-comedy-funny-amusing-jokes-114748.mp3')
                pomodoro_start = time.time()
            elif(continue_studying_check.lower() in ['no', 'n', 'never', 'nah', 'nein']):
                break
            else:
                print("Invalid input. Exiting study timer.")
                break

if __name__ == "__main__":
    main()
