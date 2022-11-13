'''
	I created this timer to fix the inefficiencies with my other program.
	
	This just waits a certain amount of time.
'''

import time

minutes_to_wait = 30
preferred_time = minutes_to_wait * 60

time.sleep(preferred_time)

print(f'The timer is up! You\'ve studied for {minutes_to_wait} minutes.')

