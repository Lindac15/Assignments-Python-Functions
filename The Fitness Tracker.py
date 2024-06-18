# Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.
# Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5
# Task 3: Create a summary function that provides a report of all activities and total calories burned for the day

def fitness_tracker():
    activities, durations = log_activity()
    calories_burned = calculate_calories(activities, durations)
    summary(activities, durations, calories_burned)

def log_activity():
    activities = []
    durations = []
    while True:
        activity = input("Enter the activity you did today: ")
        duration = int(input("Enter the duration of the activity in minutes: "))
        activities.append(activity)
        durations.append(duration)
        more_activities = input("Would you like to log another activity? (yes/no) ")
        if more_activities.lower() == "no":
            break
    return activities, durations

def calculate_calories(activities, durations):
    calories_burned = []
    for i in range(len(activities)):
        calories = durations[i] * 3.5
        calories_burned.append(calories)
    return calories_burned

def summary(activities, durations, calories_burned):
    print("Summary of your activities and calories burned:")
    for i in range(len(activities)):
        print(f"{activities[i]}: {durations[i]} minutes, {calories_burned[i]} calories burned.")
    print(f"Total calories burned for the day: {sum(calories_burned)}")

fitness_tracker()