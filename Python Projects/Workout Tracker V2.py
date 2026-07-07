import time
Sessions = []
def load_data():
    try:
        with open("Workout Tracker V2.txt", "r") as file:
            for line in file:
                Sessions.append(int(line.strip()))
    except FileNotFoundError:
        print("Welcome to Workout Tracker V2💥🏋‍♀🧘🏽‍♀️🔥💪🏼")
        print("To start, pick option 1 so we can log your sessions per week ")

def save_data():
    with open("Workout Tracker V2.txt", "w") as file:
        for Sesh in Sessions:
            file.write(str(Sesh) + "\n")

def Show_menu():
    print("\n---------------------")
    print("--Workout Tracker V2💪🏼---")
    print("-----------------------")
    print("\n1. Log sessions")
    print("2. View Workouts")
    print("3. View Statistics")
    print("4. Coach Feedback")
    print("5. Quit")

def Option():
     Choice = input("Pick an option: ")
     return Choice

def Log_sessions():
    Sesh = int(input("Workouts done this week: "))
    Sessions.append(Sesh)
    print("Analyzing Consisteny...")
    time.sleep(3)
    save_data()
    print("Workouts logged")

def View_Workouts():
    if len(Sessions) == 0:
        print("Loading sessions...")
        time.sleep(3)
        print("No sessions logged")
    else:
        print("Loading sessions...")
        time.sleep(3)
        print("\nWorkout History📖")
        for index, Sesh in enumerate(Sessions, start=1):
            print(f"Week {index}: {Sesh} Workouts")

def View_statistics():
    if len(Sessions) == 0:
            print("Loading statistics...")
            time.sleep(3)
            print("No sessions logged")
    else:
        Total = sum(Sessions)
        Average = sum(Sessions)/len(Sessions)
        Highest = max(Sessions)
        Least = min(Sessions)
        print("Loading Statistics...")
        time.sleep(3)
        print("\nWorkout Statistics📊")
        print(f"You have had a total of {Total} workouts since you first started.")

        print(f"You average {Average} workouts per week")

        print(f"The most you have worked out in a week is {Highest} sessions")

        print(f"The least you have worked out in a week is {Least} sessions")


def Coach_Feedback():
    if len(Sessions) == 0:
                print("Loading sessions...")
                time.sleep(3)
                print("No sessions logged")
    else:
         Average = sum(Sessions)/len(Sessions)
         if Average >= 7:
              return("That is really good and consistent, although you should make sure you dont overdue it by adding in some rest days😁!")
         elif Average >= 5:
              return("This is perfect! You workout consistent enough that you'll make progress and will still get enough rest👌!")
    
         elif Average >= 3:
              return("This is the bare minimum! You workout enough to keep your body healthy. Just make sure you stay consistent📈!")
         else:
              return("Good, but you could workout a little more.")

def Ai(Coach_Feedback):
     return(f"Ai: {Coach_Feedback()}")

def main():
     load_data()
     while True:
          Show_menu()
          Choice = Option()

          if Choice == "1":
               Log_sessions()
          elif Choice == "2":
               View_Workouts()
          elif Choice == "3":
               View_statistics()
          elif Choice == "4":
               ChatGPT = Ai(Coach_Feedback)
               print(ChatGPT)
          elif Choice == "5":
               print("Goodbye")
               save_data()
               break
          else:
               print("Invalid option")

main()


        


         


