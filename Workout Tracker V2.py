import time
import json
import difflib
from datetime import datetime, timedelta

workouts = []

def load_data():
    global workouts
    print("Loading data...")
    time.sleep(2)
    try:
        with open("workouts.json", "r") as file:
            data = json.load(file)
        if not isinstance(data, list):
           print("Invalid data format. Starting fresh.")
           workouts = []
        else:
           workouts = data
    except FileNotFoundError:
        print("Welcome to Workout Tracker!")
        time.sleep(2)
        print("To start, pick option 1 and log a workout!")
        time.sleep(1)
    except json.JSONDecodeError:
       print("Workout data could not be read. Starting with an empty workout list.")
       workouts = []

def save_data():
   print("Saving data...")
   time.sleep(2)
   try:
      with open("workouts.json", "w") as file:
         json.dump(workouts, file, indent=4)
   except Exception as error:
      print(f"Error saving file: {error}")

def menu():
   print("\n---Workout Tracker---")
   print("1. Log Workout")
   print("2. Workout History")
   print("3. Suggestions")
   print("4. Personal Record")
   print("5. Statistics")
   print("6. Weekly Chart")
   print("7. Manage/Delete Data")
   print("8. Quit")


def choice():
   Option = input("Pick an option: ")
   return Option


def Create():
   print("Here you can log your workouts!")
   time.sleep(2)
   print("If you ever want to quit, just press 0!")

   while True:
    Date = input("Date (Month DD, YYYY): ")

    if Date == "0":
        return

    try:
        datetime.strptime(Date, "%B %d, %Y")
        break
    except ValueError:
        print("Invalid date. Please use the format: Month DD, YYYY")

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
            if Set_count <= 0:
               print("Please enter at least one set.")
               continue
            break
         except ValueError:
            print("Invalid input, please enter a valid number!")

      for i in range(1, Set_count + 1):
         print(f"Set {i}: ")
         while True:
            try:
               Weight = int(input("Weight: "))
               if Weight <= 0:
                  print("Weight must be greater than 0.")
                  continue

               Reps = int(input("Reps: "))
               if Reps <= 0:
                  print("Reps must be greater than 0.")
                  continue
               break
            except ValueError:
               print("Invalid input, please enter a valid number!")

         Set = {
            "Weight": Weight,
            "Reps": Reps
         }
         Exercise["Sets"].append(Set)

      current_workout["Exercises"].append(Exercise)
      quit = input("Do you want to add more exercises?(0 for no, any key for yes): ")
      if quit == "0":
         print("If you want to see your workouts, go to workout history!")
         if current_workout["Exercises"]:
            workouts.append(current_workout)
            save_data()
            return
      
      
      continue


def History():
   if len(workouts) == 0:
      print("No workouts logged, choose option 1 and log a workout!")
   else:
      print("\n---Workout History---")
      for workout in workouts:
         print(f"{workout['Date']} | {workout['Group']}")
         for exercise in workout["Exercises"]:
            print(f"  {exercise['Name']}")
            for i, s in enumerate(exercise["Sets"], start=1):
                  weight = s.get("Weight", "N/A")
                  reps = s.get("Reps", "N/A")
                  print(f"   Set {i}: {weight}lbs x {reps} ")

def Delete():
      if not workouts:
         print("No workouts logged, choose option 1 and log a workout!")
         return

      print("\n---Manage Workouts---")
      for index, workout in enumerate(workouts, start=1):
         date = workout.get("Date") or "No date"
         print(f"{index}. {date} | {workout.get('Group', 'No group')}")

      try:
         workout_choice = int(input("Choose a workout (0 to quit): "))
      except ValueError:
         print("Invalid input, please enter a valid number!")
         return

      if workout_choice == 0:
         return
      if workout_choice < 1 or workout_choice > len(workouts):
         print("Invalid input, please pick one of the listed workouts!")
         return

      selected_workout = workouts[workout_choice - 1]
      print("1. Delete entire workout")
      print("2. Delete an exercise")
      print("3. Delete a set")
      print("4. Delete the workout date")
      print("5. Delete a set's weight")
      print("6. Delete a set's reps")
      print("0. Cancel")

      try:
         action = int(input("What would you like to delete? "))
      except ValueError:
         print("Invalid input, please enter a valid number!")
         return

      if action == 0:
         return
      if action == 1:
         workouts.pop(workout_choice - 1)
      elif action == 4:
         selected_workout.pop("Date", None)
      elif action in (2, 3, 5, 6):
         exercises = selected_workout.get("Exercises", [])
         if not exercises:
            print("This workout has no exercises.")
            return

         for index, exercise in enumerate(exercises, start=1):
            print(f"{index}. {exercise.get('Name', 'Unnamed exercise')}")
         try:
            exercise_choice = int(input("Choose an exercise (0 to quit): "))
         except ValueError:
            print("Invalid input, please enter a valid number!")
            return
         if exercise_choice == 0:
            return
         if exercise_choice < 1 or exercise_choice > len(exercises):
            print("Invalid input, please pick one of the listed exercises!")
            return

         selected_exercise = exercises[exercise_choice - 1]
         if action == 2:
            exercises.pop(exercise_choice - 1)
         else:
            sets = selected_exercise.get("Sets", [])
            if not sets:
               print("This exercise has no sets.")
               return
            for index, set_data in enumerate(sets, start=1):
               weight = set_data.get("Weight", "N/A")
               reps = set_data.get("Reps", "N/A")
               print(f"{index}. {weight}lbs x {reps} reps")
            try:
               set_choice = int(input("Choose a set (0 to quit): "))
            except ValueError:
               print("Invalid input, please enter a valid number!")
               return
            if set_choice == 0:
               return
            if set_choice < 1 or set_choice > len(sets):
               print("Invalid input, please pick one of the listed sets!")
               return

            if action == 3:
               sets.pop(set_choice - 1)
            elif action == 5:
               sets[set_choice - 1].pop("Weight", None)
            else:
               sets[set_choice - 1].pop("Reps", None)
      else:
         print("Invalid input, please choose one of the listed actions!")
         return

      save_data()
      print("The selected data was deleted.")
      print()

def Suggestions():
   if len(workouts) == 0:
    print("No workouts logged, choose option 1 and log a workout!")
    return

   print("\n---Suggestions---")
   time.sleep(2)
   print("Here you can get suggestions from our ai for your workouts!")
   time.sleep(1)
   print("Pick a workout by number to get suggestions for that workout!(0 to quit)")

   while True:
      for i, workout in enumerate(workouts, start=1):
         print(f"{i}. {workout['Date']} | {workout['Group']}")
      try:
         Pick = int(input("Pick an option by number: "))
         if Pick == 0:
             print("Leaving...")
             time.sleep(1)
             return
         if Pick < 1 or Pick > len(workouts):
             print("Invalid input, please pick one of the following options!")
             continue
         selected_workout = workouts[Pick - 1]
      except ValueError:
         print("Invalid input, please enter a valid number!")
         continue

      print(f"Workout selected: {selected_workout['Date']} | {selected_workout['Group']}")
      if not selected_workout["Exercises"]:
         print("This workout has no exercises logged yet.")
         return

      for index, exercise in enumerate(selected_workout["Exercises"], start=1):
         print(f"{index}. {exercise['Name']}")

      try:
         Choice = int(input("Pick an exercise by number: "))
         if Choice < 1 or Choice > len(selected_workout["Exercises"]):
             print("Invalid input, please pick one of the following options!")
             continue
      except ValueError:
         print("Invalid input, please enter a valid number!")
         continue

      selected_exercise = selected_workout["Exercises"][Choice - 1]
      print(f"You chose: {selected_exercise['Name']}")

      if not selected_exercise["Sets"]:
         print("This exercise has no set data yet.")
         return

      Total_reps = 0
      for i, s in enumerate(selected_exercise["Sets"], start=1):
         weight = s.get("Weight", "N/A")
         reps = s.get("Reps", 0)
         print(f"Set {i}: {weight}lbs x {reps} reps")
         Total_reps += reps

      Average = Total_reps / len(selected_exercise["Sets"])
      if Average >= 12:
         print("That is great that you can lift that amount of weight with that much reps. But with working out, it is better to up the weight when you get to a certain amount of reps. That is called progressive overload. I would suggest you up the weight by at least 5lbs.")
      elif Average <= 5:
         print("It is amazing that you can lift that weight. But it may be a little too heavy for your form. Try lowering the weight and focusing on control and technique.")
      else:
         print("Honestly your great where you're at right now. Just remember once it starts feeling easy, progressive overload.")
      return

def Record():
   if len(workouts) == 0:
       print("No workouts logged, choose option 1 and log a workout!")
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

      matches = difflib.get_close_matches(user.title(), [name.title() for name in all_exercise_names], n=3, cutoff=0.5)

      if len(matches) == 0:
         print("Sorry! We couldn't find any matches.")
         continue

      if len(matches) == 1:
         selected_exercise_name = matches[0]
         print(f"Analyzing {selected_exercise_name}...")
         time.sleep(2)
      else:
         for i, match in enumerate(matches, start=1):
             print(f"{i}. {match}")

         try:
             Pick = int(input("Did you mean any of these?(0 to quit): "))
             if Pick == 0:
                 return
             if Pick < 1 or Pick > len(matches):
                 print("Invalid input, please pick one of the following options.")
                 continue
             selected_exercise_name = matches[Pick - 1]
         except ValueError:
             print("Invalid input, please enter a valid number!")
             continue

      best_weight = 0
      best_reps = 0
      best_workout = None

      for workout in workouts:
         for exercise in workout["Exercises"]:
            if exercise.get("Name", "").title().strip() == selected_exercise_name:
                for set_data in exercise.get("Sets", []):
                    w = set_data.get("Weight", 0)
                    r = set_data.get("Reps", 0)
                    if (w, r) > (best_weight, best_reps):
                        best_weight, best_reps = w, r
                        best_workout = workout

      if best_workout is None:
         print(f"No data available for {selected_exercise_name}")
      else:
         print(f"Your PR for {selected_exercise_name} is {best_weight}lbs x {best_reps} reps. On {best_workout['Date']}")
         time.sleep(10)
      return

def Statistics():
   if len(workouts) == 0:
      print("No workouts logged. Choose option 1 to log a workout")
      return
   else:
    groups = set()

    while True:
      Muscles = []
      for workout in workouts:
         name = workout.get("Group", "")
         if name:
            groups.add(name)

      muscles = sorted(groups)

      if not muscles:
         print("No valid muscle groups found.")
         return
         
      
      for index, muscle in enumerate(Muscles, start=1):
         print(f"{index}. {muscle} group")
      try: 
       Pick = int(input("Pick an option: "))

       if Pick < 1 or Pick > len(Muscles):
         print("Invalid input, please pick one of the following options.")
         continue
      except ValueError:
         print("Invalid input, please enter a valid number!")
         continue

      
      else:
         Selected_group = muscles[Pick - 1]
         print(f"You picked {Selected_group}")

         Total_sets = 0
         Total_weight = 0
         Total_reps = 0
         Total_volume = 0
         Average_weight = 0
         Average_reps = 0

         print("Analyzing")
         time.sleep(3)

         for workout in workouts:
            if Selected_group.strip().casefold() == workout["Group"]:
               for exercise in workout["Exercises"]:
                  for set in exercise["Sets"]:
                     # per-set aggregation using safe getters
                     Total_sets += 1
                     reps = set.get('Reps', 0)
                     weight = set.get('Weight', 0)
                     Total_reps += reps
                     Total_weight += weight

                     
                     Total_volume += weight * reps

         
         if Total_sets:
            Average_weight = Total_weight / Total_sets
            Average_reps = Total_reps / Total_sets
         else:
            Average_weight = 0
            Average_reps = 0

         print(f"\nStatistics: {Selected_group}")
         print(f"1. Total Sets: {Total_sets}")
         print(f"2. Total Reps: {Total_reps}")
         print(f"3. Total Volume: {Total_volume} lbs")
         print(f"4. Average Weight: {Average_weight:.2f}")
         print(f"5. Average reps per set: {Average_reps:.2f}")

def Chart():
   print("---Weekly Workout chart---")
   print()

   def workout_volume(workout):
      total = 0
      for exercise in workout.get("Exercises", []):
         for s in exercise.get("Sets", []):
            w = s.get("Weight", 0)
            r = s.get("Reps", 0)
            total += w * r
      return total

   weeks = {}

   for workout in workouts:
      try:
       d = datetime.strptime(workout["Date"], "%B %d, %Y").date()
      except (KeyError, TypeError, ValueError):
       continue

      Monday = d - timedelta(days=d.weekday())

      if Monday not in weeks:
             weeks[Monday] = []

      weeks[Monday].append(workout)


   sorted_weeks = sorted(weeks.keys(), reverse=True)


   week_summaries = []
   for i, monday in enumerate(sorted_weeks, start=1):
      Sunday = monday + timedelta(days=6)
      week_workouts = weeks[monday]
      week_total_volume = sum(workout_volume(w) for w in week_workouts)
      print(f"{i}. {monday} - {Sunday} : {len(week_workouts)} workout(s), {week_total_volume} lbs total volume")
      week_summaries.append((monday, week_workouts)) 
   try:
    Pick = int(input("Pick a week by number: "))
   except ValueError:
      print("Invalid input, please pick a valid number")
      return

   if Pick == 0:
      return
   if Pick < 1 or Pick > len(week_summaries):
      print("Please pick one of the following options")
   else:
      selected_week = week_summaries[Pick - 1]

      for week in week_summaries:
         if week == selected_week:
                  for workout in selected_week[1]:
                     print(f"{workout['Date']} | {workout['Group']}")
                     for exercise in workout["Exercises"]:
                        print(f"  {exercise['Name']}")
                        for i, s in enumerate(exercise["Sets"], start=1):
                           weight = s.get("Weight", "N/A")
                           reps = s.get("Reps", "N/A")
                           print(f"   Set {i}: {weight}lbs x {reps} ")
                  print()
                     



def main():
   load_data()
   while True:
      menu()
      Choice = choice()
      if Choice == "1":
         Create()
      elif Choice == "2":
         History()
      elif Choice == "3":
         Suggestions()
      elif Choice == "4":
         Record()
      elif Choice == "5":
         Statistics()
      elif Choice == "6":
         Chart()
      elif Choice == "7":
         Delete()
      elif Choice == "8":
         quit = input("Are you sure you want to quit?(0 for no): ")
         if quit == "0":
            continue
         else:
            print("Goodbye...")
            time.sleep(3)
            break
      else:
         print("Invalid option, please pick one of the following.")

main()

