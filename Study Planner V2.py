import time
Days = []
def load_data():
    try:
        with open("Study Tracker V2.txt", "r") as file:
            for line in file:
                try:
                 Days.append(int(line.strip()))
                except ValueError:
                    print("Enter a valid Integar")
    except FileNotFoundError:
        time.sleep(3)
        print("Welcome to Study Planner V2✎ᝰ.📓📚💻✍🏼💯")
        print("to start, please choose option 1 so we can log in the hours you plan to study for.")

def save_data():
    with open("Study Tracker V2.txt", "w") as file:
        for Hours in Days:
            file.write(str(Hours) + "\n")

def show_menu():
    print("\n-------------")
    print("--Study Planner V2📚")
    print("---------------")
    print("\n1. Add Study Goal")
    print("2. Check Goal")
    print("3. View Study Plan")
    print("4. View Statistics")
    print("5. AI Study Coach")
    print("6. Delete Last Goal")
    print("7. Quit")

def Option():
    Choice = input("Pick an option: ")
    return Choice

def Log_Goals():
    Hours = int(input("Hours you plan to study for today: "))
    Days.append(Hours)
    print("Analyzing Hours...")
    save_data()
    time.sleep(3)
    print("Hours logged")

def Check_Goal():
    if len(Days) == 0:
        print("Loading Goal Checker..")
        time.sleep(3)
        print("No hours logged")
        return
    print("\nGoal Tracker📊")
    for planned in Days:
        print(f"You wanted to study for {planned} hours.")
        try:
            check = int(input("How many hours did you study for: "))
        except ValueError:
            print("Invalid input — skipping this entry.")
            continue
        if check >= planned:
            print("Goal met✅!")
        else:
            print("Goal not met❌.")

def View_Plan():
    if len(Days) == 0:
        print("Loading Planner...")
        time.sleep(3)
        print("No hours logged")
        return
    print("Loading Planner... ")
    time.sleep(1)
    print("\nYour Plan🗓️")
    time.sleep(1)
    print("There will be a check mark for the days you completed your goal and x for the days you didnt.")
    time.sleep(1)
    for index, Hour in enumerate(Days, start=1):
        print(f"Day {index}: {Hour} hours")

def View_statistics():
    if len(Days) == 0:
     print("Loading statistics...")
     time.sleep(3)
     print("No hours logged")
    else:
        print("Loading statistics")
        time.sleep(3)
        print("\nPlan statistics")
        Total = sum(Days)
        Average = sum(Days)/len(Days)
        Highest = max(Days)
        Lowest = min(Days)
        Total_Days = len(Days)
        print(f"Your total planned hours are{Total} hours.")
        time.sleep(2)
        print(f"Your average planned hours are {Average} hours of studying per day.")
        time.sleep(2)
        print(f"The most you want to study in a day is {Highest}.")
        time.sleep(2)
        print(f"You least you want to study in a day is {Lowest} hours.")
        time.sleep(2)
        print(f"You want this over the course of {Total_Days} Days.")
        time.sleep(2)
        print(f"These are your goals, work hard so you can acheive them!🎯🔥💪🏻")

def Coach():
    if len(Days) == 0:
     print("Loading ChatGpt...")
     time.sleep(3)
     print("No hours logged")
    else:
     print("Loading ChatGpt...")
     time.sleep(3)
     Average = sum(Days)/len(Days)
     if Average >= 5:
        return"You are setting the bar high, I believe you can handle it!💪🏻"
     elif Average >= 3:
        return"You have amazing goals. If you stay consistent in this you can go far💯⚡"
     elif Average >= 1:
        return"You are setting realistic goals, theres no shame in that, tiny study sessions over the course of a few weeks or months compound into something much bigger!📈"

def Ai(Coach):
    return(f"ChatGpt: {Coach}")

def delete():
    if len(Days) == 0:
         time.sleep(3)
         print("No hours logged")
    else:
        time.sleep(2)
        Delete = input("Are you sure you want to delete the last item?: ").lower()
        if Delete == "yes":
            print("Deleting last item...")
            save_data
            time.sleep(3)
            del Days[-1]
            
        else:
            time.sleep(2)
            print("Ok!")




def main():
    load_data()
    while True:
        show_menu()
        Choice = Option()
        if Choice == "1":
            Log_Goals()
        elif Choice == "2":
            Check_Goal()
        elif Choice == "3":
            View_Plan()
        elif Choice == "4":
            View_statistics()
        elif Choice == "5":
            Coa = Coach()
            ChatGpt = Ai(Coa)
            print(ChatGpt)
        elif Choice == "6":
            delete()
        elif Choice == "7":
            print("Goodbye")
            save_data()
            time.sleep(3)
            break
        else:
            print("Invalid option")

main()



          

    

            
        