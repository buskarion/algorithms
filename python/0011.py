"""
INTRUCTIONS
    You are given a time period formatted as a string in the HH:MM:SS - HH:MM:SS format. HH:MM:SS represents the time in hours, minutes, and seconds form, and the hyphen (-) separates the start time from the end time of the period.

    Your task is to calculate how many minutes pass from the start time until the end time.

    Here are some guidelines:

    The input times are always valid time strings in the HH:MM:SS format, with HH ranging from 00 to 23, and MM and SS from 00 to 59.
    The output should be an integer, representing the total length of the time period in minutes.
    The start time of the period will always be earlier than the end time, so periods that cross over midnight (like 23:00:00 - 01:00:00) are not considered.
    We are interested in the number of times the time passes some HH:MM:00 after the start time until the end time. Any remaining seconds should be disregarded; for instance, a period of "12:15:00 - 12:16:59" represents 1 minute, not 2, and a period of "12:14:59 - 12:15:00" also represents 1 minute.
"""

def solution(time_period):
    start = time_period.split()[0].split(':')
    end = time_period.split()[2].split(':')
    
    start_parts = [int(part) for part in start]
    start_in_seconds = start_parts[0] * 3600 + start_parts[1] * 60 + start_parts[2]

    end_parts = [int(part) for part in end]
    end_in_seconds = end_parts[0] * 3600 + end_parts[1] * 60 + end_parts[2]

    time_difference_in_seconds = end_in_seconds - start_in_seconds
    output = time_difference_in_seconds // 60

    if start_parts[2] > end_parts[2]:
        output += 1

    return output

print(solution('12:15:30 - 14:00:00'))
