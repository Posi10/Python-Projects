import time
Projects = []
def load_data():
    print("Loaading app...")
    time.sleep(3)
    try:
        with open("Project Manager V1.txt", "r") as file:
            for line in file:
                Projects.append(line.strip())
    except:
        print("Welcome to Project Manager V1💼💻📅✉️")
        time.sleep(3)
        print("To start, please choose option 1 so we can log in your hours.")

def save_data():
    print("Saving Data...")
    time.sleep(3)
    with open("Project Manager V1.txt", "w") as file:
        for Project in Projects:
            file.write(Project + "\n")

def Show_menu():
    print("\n☕︎‧₊˚⏱٠࣪⋆💻₊˚ᵎ☕︎‧₊˚⏱٠࣪⋆💻₊˚ᵎ")
    print("---Project Manager V1📝----")
    print("☕︎‧₊˚⏱٠࣪⋆💻₊˚ᵎ☕︎‧₊˚⏱٠࣪⋆💻₊˚ᵎ")
    print("\n1. Add Projects")
    print("2. View Projects")
    print("3. Mark Project Complete")
    print("4. View progress")
    print("5. Delete Last Project")
    print("6. Quit")

def Option():
    Choice = int(input("Pick an option: "))
    return Choice

def Add_Projects():
    while True:
     Project = input("Project name: ")
     Projects.append(Project)
     print("Logging Project...")
     time.sleep(3)
     print("Project logged!")
     Quit = input("Do you want to go back to menu?: ").lower()
     if Quit == "yes":
         print("Going back to menu...")
         time.sleep(3)
         break
     else:
        continue
        
        


def View_Projects():
    while True:
     if len(Projects) == 0:
        print("Loading Projects...")
        time.sleep(3)
        print("No Projects logged")
     else:
        print("Loading Projects...")
        time.sleep(3)
        print("\nProjects📁")
        for index, Project in enumerate(Projects, start=1):
            print(f"Project {index}: {Project}")
            time.sleep(30)
        Quit = input("Do you want to go back to menu?: ").lower()
        if Quit == "yes":
            print("Going back to menu...")
            time.sleep(3)
            break
        else:
            continue
                
                
    

def Mark_complete():
    while True:
     if len(Projects) == 0:
            print("Loading Projects...")
            time.sleep(3)
            print("No Projects logged")
     else:
        print("Loading Projects...")
        time.sleep(3)
        print("\nProjects📁")
        for index, Project in enumerate(Projects, start=1):
            print(f"Project {index}: {Project}")

        Pro = int(input("Pick a project by number: "))
        Choice = Pro - 1
        Mark = input(f"Do you want to mark {Choice} as complete?: ").lower()
        if Mark == "yes":
            print(f"{Choice}✅")
            time.sleep(3)
            Projects[Choice] = f"{Projects[Choice]} ✅"
            print("\nUpdated Projects📁")
            for index, Project in enumerate(Projects, start=1):
              print(f"Project {index}: {Project}")
        time.sleep(10)
        Quit = input("Do you want to go back to menu?: ").lower()
        if Quit == "yes":
         print("Going back to menu...")
         time.sleep(3)
         break
        else:
            continue
                

def choice():
    return Projects
    
def View_Progress():
    while True:
     if len(Projects) == 0:
             time.sleep(3)
             print("No projects logged")
     else:
        print("Loading Projects...")
        time.sleep(3)
        print("\nProgress tracker📊")
        time.sleep(3)
        print("Loading Progress...")
        Projects_remaining = 0
        Projects_Completed = 0
        Choice = choice()
        for Cho in Choice:
            if (Cho) == f"✅":
                Projects_Completed += 1
            else:
                Projects_remaining += 1
        Total = Projects_Completed + Projects_remaining
        Completion_rate = Projects_Completed/Total*100
        time.sleep(5)
        print(f"Projects Completed: {Projects_Completed}")
        time.sleep(1)
        print(f"Projects remaining: {Projects_remaining}")
        time.sleep(1)
        print(f"Completion rate: {Completion_rate}")
        time.sleep(20)
        Quit = input("Do you want to go back to menu?: ").lower()
        if Quit == "yes":
            print("Going back to menu...")
            time.sleep(3)
            break
        else:
           continue

def delete():
    if len(Projects) == 0:
         time.sleep(3)
         print("No projects logged")
    else:
        time.sleep(2)
        Delete = input("Are you sure you want to delete the last item?: ").lower()
        if Delete == "yes":
            print("Deleting last item...")
            save_data
            time.sleep(3)
            del Projects[-1]
            
        else:
            time.sleep(2)
            print("Ok!")

def main():
    load_data()
    while True:
        Show_menu()
        Choice = Option()
        if Choice == "1":
            Add_Projects()
        elif Choice == "2":
            View_Projects()
        elif Choice == "3":
            Mark_complete()
        elif Choice == "4":
            View_Progress()
        elif Choice == "5":
            delete()
        elif Choice == "6":
            print("Goodbye...")
            time.sleep(3)
            save_data()
            break
        else:
            print("Invalid option")

main()
    

        




        
             
             

            




    
    