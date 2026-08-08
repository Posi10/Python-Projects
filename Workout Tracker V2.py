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
        print("To start, choose option 1 to create a workout!")

def save_data():
    print("Saving data...")
    time.sleep(2)
    try:
     with open("workouts.json", "w") as file:
        json.dump(workouts, file, indent=4)
    except Exception as error:
       print(f"Error saving file: {error}")

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
    print("If you ever want to quit, just press 0")
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
        Name = input("Exercise Name: ")
        if Name == "0": break

        Exercise = {
            "Name": Name,
            "Sets": []
        }
        try:
            Set_count = int(input("Sets: "))
            if Set_count == 0: break
        except ValueError:
           print("Please enter a valid number.")
           continue
        for index in range(1, Set_count + 1):
           print(f"Set {index}: ")
           Weight = input("Weight: ")
           if Weight == "0": return
           Reps = input("Reps: ")
           if Reps == "0": return

           Set = {
              "Weight" : Weight,
              "Reps": Reps
           }
           Exercise["Sets"].append(Set)
        current_workout["Exercises"].append(Exercise)
        quit = input("Do you want to add more exercises?(0 for no, any for yes)")
        if quit == "0": 
           break

    if current_workout["Exercises"]:
       workouts.append(current_workout)
       save_data()

def History():
   if len(workouts) == 0:
      print("No workouts logged.")
   else:
      for workout in workouts:
         print(f"\nDate: {workout['Date']} | Muscle Group: {workout['Group']}")
         for item in workout["Exercises"]:
            print(f"  {item['Name']}")
            for i, s in enumerate(item['Sets'], 1):
               print(f"    Set {i}: {s['Weight']}lbs {s['Reps']} reps")
            print()

          
      
    

         
def main():
   load_data()
   while True:
      show_menu()
      Option = Choice()
      if Option == "1":
         Create()
      elif Option == "2":
         History()
      elif Option == "7":
         quit = input("Are you sure you want to quit(0 for yes, any key for no): ")
         if quit == "0":
               break
         else:
               print("Invalid input, please choose one of the following options.")
               continue
    
main()


