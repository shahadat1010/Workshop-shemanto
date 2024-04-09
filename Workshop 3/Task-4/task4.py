'''
Prompt the user to enter the number of lap times and store it in the variable num_of_laps.
Initialize variables:
total_time set to 0.
fastest_time set to 9999.
slowest_time set to 0.
Start a loop iterating from 1 to num_of_laps:
Prompt the user to enter the lap time for the current lap and store it in the variable lap_time.
Add lap_time to total_time.
Check if lap_time is less than fastest_time:
If true, update fastest_time with the value of lap_time.
Check if lap_time is greater than slowest_time:
If true, update slowest_time with the value of lap_time.
Calculate the average lap time by dividing total_time by num_of_laps and round it to 2 decimal places.
Print the fastest lap time, slowest lap time, and average lap time.
'''


num_of_laps = int(input("Enter the number of lap times: "))

total_time = 0
fastest_time = 9999
slowest_time = 0

for lap in range(1, num_of_laps + 1):
    lap_time = float(input(f"Enter lap time {lap} of {num_of_laps}: "))
    total_time += lap_time

    if lap_time < fastest_time:
        fastest_time = lap_time
    if lap_time > slowest_time:
        slowest_time = lap_time

average = total_time / num_of_laps
average = round(average, 2)

print(f"Fastest lap time: {fastest_time}")
print(f"Slowest lap time: {slowest_time}")
print(f"Average lap time: {average}")
