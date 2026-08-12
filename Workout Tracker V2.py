import time
import json
workouts = []

def load_data():
    global workouts
    print("Loading data...")
    time.sleep(3)
    try:
        with open("workouts.json", "r") as file:
            workouts = json.load(file)
    except FileNotFoundError:
        print("Welcome to Workout Tracker!")
        time.sleep(2)
        print("To start, Please pick optino 1 and log a workout!")
        time.sleep(1)

def save_data():
    print("Saving data...")
    time.sleep(2)
    try:
        with open("workouts.json", "w") as file:
            json.dump(workouts, file, indent=4)
    except Exception as error:
        print(f"Error saving data: {error}")

def show_menu():
    print("\n---WorkoutTracker---")
    print("1. Create a Workout")
    print("2. Workout History")
    print("3. Suggestions")
    print("4. Personal Records")
    print("5. Statistics")
    print("6. Weekly Chart")
    print("7. Quit")

def Choice():
    Choice = input("Pick an option: ")
    return Choice

def Create():
    print("Here you can log your workouts!")
    time.sleep(2)
    print("If you ever want to quit, just press 0!")
    time.sleep(1)

    Date = input("Date: ")
    if Date == "0": return

    Group = input("Group: ")
    if Group == "0": return

    current_workout = {
        "Date": Date,
        "Group": Group,
        "Exercises": []
    }

    while True:
        Name = input("Exercise name: ")
        if Name == "0": return

        Exercise = {
            "Name": Name,
            "Sets": []
        }
        while True:
            try:
                Set_count = int(input("Sets: "))
                if Set_count == 0: return
            except ValueError:
                print("Please enter a vlid number")
            for index in range(1, Set_count +1):
                print(f"Set {index}: ")
                Weight = input("Weight: ")
                if Weight == "0": return
                Reps = input("Reps: ")
                if Reps == "0": return

                Set = {
                    "Weight": Weight,
                    "Reps": Reps
                }
                Exercise["Sets"].append(Set)
            current_workout["Exercises"].append(Exercise)
            quit = input("Do you want to add more exercises (0 for no, any key for yes): ")
            if quit == "0":
                workouts.append(current_workout)
                save_data()
                return
            else:
             break


def History():
    print("\n---Workout History---")
    for workout in workouts:
     print(f"Date: {workout['Date']} | Muscle Group: {workout['Group']}")
     for item in workout["Exercises"]:
         print(f"  Exercise: {item['Name']}")
         for i, s in enumerate(item['Sets'], 1):
             print(f"   Set {i}: {s['Weight']}lbs x {s['Reps']} reps")
         print()

def Suggestions():
    print("\n---Workout Suggestions---")
    time.sleep(2)
    print("Here you can get suggestions from our AI for your workouts!")
    time.sleep(2)
    print("Pick a workout by number to get feedback!")
    time.sleep(1)

    if not workouts:
        print("No workouts found. Please log a workout first.")
        return

    for index, workout in enumerate(workouts, start=1):
        print(f"{index}. Date: {workout['Date']} | Muscle Group: {workout['Group']}")

    try:
        Pick = int(input("Pick a workout (0 to quit): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if Pick == 0:
        print("Leaving...")
        time.sleep(2)
        return
    elif Pick < 1 or Pick > len(workouts):
        print("Invalid option, please pick one of the options listed above.")
        return

    selected_workout = workouts[Pick - 1]
    print(f"You selected workout {Pick}: {selected_workout['Date']} | {selected_workout['Group']}")
    # TODO: Add suggestion logic for selected_workout here
    
    

def Main():
    load_data()
    while True:
        show_menu()
        Option = Choice()
        if Option == "1":
            Create()
        elif Option == "2":
            History()
        elif Option == "3":
            Suggestions()
        elif Option == "7":
            quit = input("Are you sure youw ant to quit?(0 for yes, any key for no): ")
            if quit == "0":
                break
            else:
                continue
        else:
            print("Invalid option, please pick one of the options listed.")
        

Main()

