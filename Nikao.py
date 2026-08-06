import time
import json
Trips = []

def load_data():
    global Trips
    print("Loading data...")
    time.sleep(3)
    try:
        with open("Trips.json", "r") as file:
            Trips = json.load(file)
    except FileNotFoundError:
        print("Welcome to Workout tracker!")
        time.sleep(2)
        print("To start, please pick option 1 to log your workouts!")
        time.sleep(1)

def save_data():
    print("Saving data...")
    time.sleep(3)
    try:
        with open("Trips.json", "w") as file:
            json.dump(Trips, file, indent=4)
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
    print("Here you can log in your workouts!")
    time.sleep(2)
    print("if you ever want to quit, just press 0!")
    time.sleep(1)

    Date = input("Date: ")
    if Date == "0": return

    Store = input("Store name: ")
    if Store == "0": return

    current_trip = {
        "Date": Date,
        "Store": Store,
        "Recipies": []
    }

    while True:
        Name = input("Recipie name: ")
        if Name == "0": break

        Ingredients = {
            "Name": Name,
            "ingredients": []
        }
        while True:
            Ingredient_count = int(input("Amount of Items: "))
            for index in range(1, Ingredient_count + 1):
                Ingredient = input(f"Ingredient {index}: ")
                Ingredients["ingredients"].append(Ingredient)
            current_trip["Recipies"].append(Ingredients)
            quit = input("Do you want to add more recipies?(0 for no, any key for yes): ")
            if quit == "0":
                Trips.append(current_trip)
                save_data()
                break
            else:
                if current_trip["Recipies"]:
                    Trips.append(current_trip)
                    save_data()

Create()
                

        
        

        
     
        
