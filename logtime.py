from utility import formatting
from file_operations import time_data

def get_runtime():
    runtime = 0
    while True:
        try:
            runtime = float(input('Your study time (in seconds): '))
        except ValueError:
            print('Invalid time.')

        if runtime > 0:
            # log the time #
            return runtime
        else:
            # make the user give another time #
            pass

if __name__ == '__main__':
    runtime = get_runtime()

    # print the time the program ran
    formatted_runtime = formatting.format_seconds_to_hms(runtime)
    print(formatted_runtime)

    # file away the new data
    time_data.write_new_record(runtime)
