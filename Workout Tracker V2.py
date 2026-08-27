import time
import json
import difflib
workouts = []

def load_data():
    global workouts
    print("Loading data...")
    try:
        with open("workouts.json", "r") as file:
            workouts = json.load(file)
    except FileNotFoundError:
        print("Welcome to Workout Tracker!")
        time.sleep(2)
        print("To start, please pick option 1 to log workouts")
        time.sleep(1)
        

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
    print("1. Log Workout")
    print("2. Workout History")
    print("3. Suggestions")
    print("4. Personal Record")
    print("5. Statistics")
    print("6. Weekly Chart")
    print("7. Quit")

def Choice():
    Cho = input("Pick an option: ")
    return Cho

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
        Name = input("Exercise Name: ")
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
                print("Invalid input, please input a valid number.")
                continue
            for i in range(1, Set_count + 1):
                print(f"Set {i}: ")
                try:
                 Weight = int(input("Weight: "))
                 if Weight == 0: return

                 Reps = int(input("Reps: "))
                 if Reps == 0: return
                except ValueError:
                   print("Invalid input, please input a valid number.")
                   continue

                Set = {
                    "Weight": Weight,
                    "Reps": Reps
                }
                Exercise["Sets"].append(Set)
            current_workout["Exercises"].append(Exercise)
            quit = input("Do you want to add more exercises?(0 to quit, any key to continue): ")
            if quit == "0":
                if current_workout["Exercises"]:
                    workouts.append(current_workout)
                    save_data()
                    return
                else:
                    return
            else:
                break

def History():
    if len(workouts) == 0:
        print("No workouts logged")
    else:
        print("\n---Workout History---")
        for workout in workouts:
            print(f"{workout['Date']} | {workout['Group']}")
            for exercise in workout["Exercises"]:
                print(f"  {exercise['Name']}")
                for i, s in enumerate(exercise["Sets"], start=1):
                    print(f"   Set {i}: {s['Weight']}lbs x {s['Reps']} reps")
            print()
                    

def Suggestions():
    if len(workouts) == 0:
        print("No workouts found, please log a workout.")
    else:
     print("\n---Suggestions---")
     time.sleep(2)
     print("Here you can get suggestions from our ai for your workouts!")
     time.sleep(1)
     print("Pick a workout by number to get suggestions for that workout!(0 to quit)")
     while True:
         for index, workout in enumerate(workouts, start=1):
             print(f"{index}. {workout['Date']} | {workout['Group']}")
         try:
          Pick = int(input("Pick an option(0 to quit): "))
          if Pick == 0:
             print("Leaving...")
             time.sleep(2)
             break
          elif Pick < 1 or Pick > len(workouts):
             print("Invalid option, please pick one of the following options")
             continue
          else:
             selected_workout = workouts[Pick - 1]
             print(f"The workout you chose was {selected_workout['Date']} | {selected_workout['Group']}")
         except ValueError:
          print("Invalid input, Please enter a valid number")
          continue

         for exercise in selected_workout["Exercises"]:
                 Total_reps = 0
                 print(f"{exercise['Name']}")
                 for i, s in enumerate(exercise["Sets"], start=1):
                     print(f"Set {i}. {s['Weight']}lbs x {s['Reps']} reps")
                     Total_reps += s["Reps"]

                 Average = Total_reps/len(exercise["Sets"])
                 if Average >= 12:
                  print("That is great that you can lift that amount of weight with that much reps. But with working out, it is better to up the weight when you get to a certain amount of reps.  That is called progressive overload. I would suggest you up the weight by at least 5lbs. That is what will maximze muscle growth.")
                 elif Average <= 5:
                  print("It is amazing that you can lift that weight. But it may be a little too heavy for you. Having little reps shows you might not be lifting with optimal form. Try and lower the weight, I know it sounds counterintuitive but it is better to have a less weight with a better stretch and controlled negative then more weight and swinging all over the place.  ")
                 else:
                  print("Honestly your great where your at right now. Just remember once it starts feeling easy, progressive overload. ")


def Record():
    if len(workouts) == 0:
        print("No workouts logged")
        return

    print("\n---Personal Records---")
    time.sleep(2)
    print("Here you can get your personal records of weight lifted for each exercise you've done!")
    time.sleep(1)
    print("Pick one of the following exercises to see your personal record for it!")
    time.sleep(1)

    while True:
        user = input("Search for an exercise(0 to quit): ")
        if user == "0":
            return

        all_exercise_names = []
        for workout in workouts:
            for exercise in workout["Exercises"]:
                name = exercise.get("Name", "")
                if name:
                    all_exercise_names.append(name)

        matches = difflib.get_close_matches(user.title(), [name.title() for name in all_exercise_names], n=3, cutoff=0.7)

        if not matches:
            print("No exercises found fitting that name. Please try again.")
            continue

        selected_exercise = None

        if len(matches) == 1:
            selected_exercise = matches[0].title()
            print(f"Analyzing {selected_exercise}...")
            time.sleep(2)
        else:
            for i, match in enumerate(matches, start=1):
                print(f"{i}. {match}")
            try:
                choice = int(input("Did you mean one of these?(0 to quit): "))
                if choice == 0:
                    continue
                if choice < 1 or choice > len(matches):
                    print("Invalid input, please pick one of the following options.")
                    continue
                selected_exercise = matches[choice - 1].title().strip()
                print(f"Analyzing {selected_exercise}")
                time.sleep(2)
            except ValueError:
                print("Invalid input, Please input a valid number!")
                continue

        if selected_exercise is None:
            continue

        best_weight = 0
        best_reps = 0
        best_workout = None

        for workout in workouts:
            for exercise in workout["Exercises"]:
                exercise_name = exercise.get("Name", "")
                if exercise_name.title().strip() == selected_exercise:
                        for Set in exercise.get("Sets", []):
                            w = Set.get("Weight", 0)
                            r = Set.get("Reps", 0)
                            if (w, r) > (best_weight, best_reps):
                                best_weight, best_reps = w, r
                                best_workout = workout
        if best_workout == None:
            print(f"We coudnt find any data availible for {selected_exercise.title()}")
        else:
            print(f"Your PR for {selected_exercise.title()} is {best_weight}lbs x {best_reps} reps. On {best_workout['Date']}")



def main():
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
        elif Option == "4":
            Record()
        elif Option == "7":
            Quit = input("Are you sure you want to quit?(0 for no): ")
            if Quit == "0": 
                continue
            else:
                break

     
main()



    



                

