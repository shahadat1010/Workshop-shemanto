'''
Initialize an empty list to store lap times: lap_times.
Print a message to prompt the user to enter lap times, specifying that they should enter 'x' when done.
Start an endless loop:
Prompt the user to enter a lap time and store it in the variable lap_time_input.
Check if lap_time_input is 'x':
If true, break out of the loop.
Convert lap_time_input to a float and append it to lap_times.
Check if any lap times are recorded in lap_times:
If true:
Calculate the fastest lap time using the min() function on lap_times and store it in fastest_time.
Calculate the slowest lap time using the max() function on lap_times and store it in slowest_time.
Calculate the average lap time by dividing the sum of lap_times by its length and round it to 2 decimal places.
Print the fastest lap time, slowest lap time, and average lap time.
If false, print a message indicating that no lap times are recorded.
'''
lap_times = []

print("Enter lap times. When done press ('x' to end):")

while True:
    lap_time_input = input(f"Enter lap time {len(lap_times) + 1} ('x' to end): ")
    
    if lap_time_input.lower() == "x":
        break
    
    lap_time = float(lap_time_input)
    lap_times.append(lap_time)

if lap_times:
    fastest_time = min(lap_times)
    slowest_time = max(lap_times)
    average_time = sum(lap_times) / len(lap_times)

    print(f"Fastest Lap Time: {fastest_time}")
    print(f"Slowest Lap Time: {slowest_time}")
    print(f"Average Lap Time: {average_time:.2f}")
else:
    print("No lap times recorded.")