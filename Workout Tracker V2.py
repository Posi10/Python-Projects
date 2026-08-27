import time
import json
import difflib

workouts = []

def load_data():
    global workouts
    print("Loading data...")
    time.sleep(2)
    try:
        with open("workouts.json", "r") as file:
            workouts = json.load(file)
    except FileNotFoundError:
        print("Welcome to Workout Tracker!")
        time.sleep(2)
        print("To start, pick option 1 and log a workout!")
        time.sleep(1)

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
   print("7. Quit")


def choice():
   Option = input("Pick an option: ")
   return Option


def Create():
   print("Here you can log your workouts!")
   time.sleep(2)
   print("If you ever want to quit, just press 0!")

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

      try:
         Set_count = int(input("Sets: "))
         if Set_count == 0: return
      except ValueError:
         print("Invalid input, please enter a valid number!")
         continue
      for i in range (1, Set_count +1):
         print(f"Set {i}: ")
         try:
          Weight = int(input("Weight: "))
          if Weight == 0: return

          Reps = int(input("Reps: "))
          if Reps == 0: return
         except ValueError:
          print("Invalid input, please enter a valid number!")
          continue
         Set = {
            "Weight": Weight,
            "Reps": Reps
         }
         Exercise["Sets"].append(Set)
      current_workout["Exercises"].append(Exercise)
      quit = input("Do you want to add more exercises?(0 for no, any key for yes): ")
      if quit == "0":
         print("If you want to see your workouts, go to workout history!")
         print("Leaving...")
         time.sleep(2)
         if current_workout["Exercises"]:
            workouts.append(current_workout)
            return
      else:
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
               print(f"   Set {i}: {s['Weight']}lbs x {s['Reps']} ")
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
         print(f"Set {i}: {s['Weight']}lbs x {s['Reps']} reps")
         Total_reps += s["Reps"]

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
         selected_exercise_name = matches[0].title()
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
             selected_exercise_name = matches[Pick - 1].title()
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
      elif Choice == "7":
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


         
                    
        
                     




    

             
                 
            

             
        

    
          

           
   

         
         
    

