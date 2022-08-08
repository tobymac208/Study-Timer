def format_seconds_to_hms(seconds):
    '''
    Returns a formatted string of the amount of time spent studying.
    Converts seconds to hours, minutes, or seconds.
    '''
    # Return to the caller if the user gives a invalid input.
    try:
        seconds = float(seconds)
    except ValueError:
        print('You need to pass this function a numerical value.')
        return

    formatted_str = ''

    if seconds >= 3600:
        formatted_str = f'{seconds/3600.00:.2f} hour(s).'
    elif seconds >= 60:
        formatted_str = f'{seconds/60.00:.2f} minute(s).'
    elif seconds >= 0:
        formatted_str = f'{seconds:.2f} second(s).'

    return formatted_str
