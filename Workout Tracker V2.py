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
       print("Welcome to Workout Tracker!!!")
       time.sleep(2)
       print("To start, pick option 1 and log a workout!")
       time.sleep(1)
 
def save_data():
    print("Saving data...")
    time.sleep(2)
    try:
        with open("workouts.json", "w") as file:
            json.dump(workouts, file, indent=4)
    except Exception as e:
        print(f"Error saving file: {e}")

def show_menu():
    print("\nWorkout Tracker")
    print("1. Create workout")
    print("2. Workout History")
    print("3. Suggestions")
    print("4. Personal Records")
    print("5. Statistics")
    print("6. Weekly Charts")
    print("7. Quit")

def Choice():
    Cho = input("Pick an option: ")
    return Cho

def Create():
    print("Here you can log your workouts!")
    time.sleep(2)
    print("If you ever want to quit, just press 0")
    time.sleep(1)

    Date = input("Date: ")
    if Date == "0": return

    Group = input("Muscle Group: ")
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
             print("Invalid input, please enter a valid number.")
         for i in range(1, Set_count + 1):
                 print(f"Set {i}")
                 try:
                  Weight = int(input("Weight: "))
                  Reps = int(input("Reps: "))
                 except ValueError:
                     print("Invalid input, please enter a valid number.")
                     Weight, Reps = 0, 0
                

                 Set = {
                     "Weight": Weight,
                     "Reps": Reps
                 }
                 Exercise["Sets"].append(Set)
         current_workout["Exercises"].append(Exercise)
         quit = input("Do you want to add more execises?(0 for no, any key for yes): ")
         if quit == "0":
             if current_workout["Exercises"]:
                 workouts.append(current_workout)
                 save_data()
                 break

def Workout_History():
    if len(workouts) == 0:
        print("No workouts found, please log a workout.")
    print("\n---Workout History---")
    for workout in workouts:
     print(f"Date: {workout['Date']} | {workout['Group']}")
     for item in workout["Exercises"]:
      print(f"Exercise: {item['Name']}")
      for i, s in enumerate(item["Sets"], start=1):
          print(f"Set {i}: Weight: {s['Weight']}lbs x {s['Reps']} reps")

def Suggestions():
    print("\n---Workout Suggestions---")
    time.sleep(2)
    print("Here you can get workout suggestions from our ai!")
    time.sleep(1)
    print("Pick a workout by number to better your workouts!")
    time.sleep(1)

    for index, workout in enumerate(workouts, start=1):
        print(f"{index}: {workout['Date']} | {workout['Group']}")
    try:
        Pick = int(input("Pick an option(0 to quit): "))
    except ValueError:
        print("Invalid input, Please enter a valid number!")

    if Pick == 0:
        print("Leaving")
        time.sleep(2)
        return
    elif Pick < 1 or Pick > len(workouts):
        print("Invalid option, please pick one of the workouts listed above!")
    else:
        selected_workout = workouts[Pick - 1]
        print(f"You chose {index}: {selected_workout['Date']} | {selected_workout['Group']}")
        for exercise in workout["Exercises"]:
            print(f"  Exercise: {exercise['Name']}")
            for i, s in enumerate(exercise["Sets"], start=1):
                Total_reps = 0
                print(f"   Set {i}: {s['Weight']}lbs {s['Reps']} reps")
                Total_reps += ['Reps']
            print(Total_reps)
        

        

def main():
    load_data()
    while True:
        show_menu()
        Option = Choice()
        if Option == "1":
            Create()
        elif Option == "2":
            Workout_History()
        elif Option == "3":
            Suggestions()
        elif Option == "7":
            Quit = input("Are you sure you want to quit?(0 for no): ")
            if Quit == "0": 
                break
            else:
                continue

     
main()
             
                 
