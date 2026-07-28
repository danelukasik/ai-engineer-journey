# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

race_time = float(input("Enter the total race time in seconds: "))
pit_stop_count = int(input("Enter the number of pit stops made: "))
average_pit_stop_duration = float(input("Enter the average pit stop duration in seconds: "))
total_pit_stop_time = pit_stop_count * average_pit_stop_duration
pit_time_percentage = round((total_pit_stop_time / race_time) * 100 if race_time > 0 else 0,2)

print(f"Total pit stop time: {total_pit_stop_time} seconds")
print(f"Percentage of race time spent in pits: {pit_time_percentage}%")

if pit_time_percentage > 5:
    print("You need a new pit crew. 🛠️")