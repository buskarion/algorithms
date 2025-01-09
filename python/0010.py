"""
INTRUCTIONS
You are given two input arguments: an array of strings timePoints and an integer added_seconds. Each string in timePoints is in the HH:MM:SS format, representing a valid time from "00:00:00" to "23:59:59" inclusive. The integer added_seconds represents a number of seconds, ranging from 1 to 86,400. Your task is to create a new function, add_seconds_to_times(timePoints, added_seconds), which takes these two arguments and returns a new array of strings. Each string in the returned array is the new time, calculated by adding the provided added_seconds to the corresponding time in timePoints, formatted in HH:MM:SS.

The array timePoints contains n strings, where n can be any integer from 1 to 100 inclusive. The time represented by each string in timePoints is guaranteed to be valid. The total time, after adding added_seconds, can roll over to the next day.

Example

For timePoints = ['10:00:00', '23:30:00'] and added_seconds = 3600, the output should be ['11:00:00', '00:30:00'].

==========================================================================================================

THOUGHT PROCCESS
    1. Iterate each string in the list
    2. Get the value in int format of each value to get the total seconds
    3. Add the value "seconds" to the total seconds
    4. Verify if it is lower than 86400
    5. Divide into hours, minutes and seconds
    6. Join everything together into the format 'HH:MM:SS'
    7. Replace the new string into the list
    8. Return the list

NOTES
    1. During the implementation I notice that I need to subtract the value 86400 in case the total_seconds be greater than this value
"""

def add_seconds_to_time(time_points, added_seconds):
    if added_seconds == 86400:
        return time_points

    time_list_updated = []

    for time in time_points:
        time_parts = [int(part) for part in time.split(':')]
        total_seconds = time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2] + added_seconds
        if total_seconds >= 86400:
            total_seconds -= 86400
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_list_updated.append(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

    return time_list_updated


time_points = ['10:00:00', '23:30:00']
added_seconds = 3600
print(add_seconds_to_time(time_points, added_seconds))
