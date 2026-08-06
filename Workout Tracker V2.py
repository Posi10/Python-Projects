import time
import json
workouts = []

def load_data():
    print("Loading...")
    time.sleep(2)
    try:
        with open("Workout.json", "r") as file:
            workouts = json.load(file)
    except FileNotFoundError:
        print("Welcome to workout tracker! ")
        time.sleep(2)
        print("to start, choos eoption 1 and create a workout!")

def save_data():
    print("Saving data...")
    time.sleep(3)
    try:
        with open("workouts.json", "w") as file:
            json.dump(workouts, file, indent=4)
    except Exception as error:
        print(f"Error saving data: {error}")

def show_menu():
    print("\nWorkout Tracker")
    print("1. Create Workout")
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
    print("Here you can create a workout!")
    time.sleep(2)
    print("If you ever want to quit just press 0!")
    time.sleep(1)

    Date = input("Date: ")
    if Date == "0": return

    Group = input("Muscle Group: ")
    if Group == "0": return

    current_workout = {
        "Date": Date,
        "Group": Group,
        "Exercises": [],
     }

    while True:
        Name = input("Exercise: ")
        if Name == "0": return

        
        exercise = {
            "Name": Name,
            "Sets": []
        }
        try:
          set_count = int(input("Sets: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        for index in range(1, set_count + 1):
            try:
                print(f"Set: {index}")
                weight = int(input("Weight: "))
                reps = int(input("Reps: "))
            except ValueError:
                print("Invalid input, setting weight and reps to 0")
                weight, reps = 0, 0

            Set_data = {
                "Weight": weight,
                "Reps": reps
            }
            exercise["Sets"].append(Set_data)
        current_workout["Exercises"].append(exercise)
        workouts.append(current_workout)

        quit = input("Do you want to add another exericise?(0 for no, any key for yes): ")

        if quit == "0": 
                save_data()
                break
        else:
               if current_workout["Exercises"]:
                workouts.append(current_workout)
                save_data()
               else:
                print("Workout cancelled. No exercises added.")



def main():
    load_data()
    while True:
        show_menu()
        Option = Choice()
        if Option == "1":
            Create()
        elif Option == "7":
            quit = input("are you sure you want to quit?(0 for yes any key for no): ")
            if quit == "0":
                break
            else:
                continue
            
main()
            
        
        