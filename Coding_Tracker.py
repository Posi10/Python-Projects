import time
from datetime import datetime, timedelta
Hours = []
Session_Entries = []
Roadmap = []
Roadmap_name = None

def load_data():
   try:
      with open("Coding Tracker Pro.txt", "r") as file:
         for line in file:
            if line.strip():
               data = line.strip().split(" | ")
               if len(data) == 3:
                  timestamp_text, display_text, hours_text = data
                  try:
                     timestamp = datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S")
                  except ValueError:
                     timestamp = datetime.now()
                  session = {
                     "text": f"{display_text} l {hours_text}",
                     "datetime": timestamp,
                     "hours": int(hours_text)
                  }
                  Session_Entries.append(session)
                  Hours.append(int(hours_text))
                  print("Loading data...")
                  time.sleep(3)
   except FileNotFoundError:
      time.sleep(3)
      print("Welcome to Coding Tracker Pro!")
      time.sleep(3)
      print("To start please pick option 1 so we can load your sessions!")
      time.sleep(3)


def save_data():
   with open("Coding Tracker Pro.txt", "w") as file:
      for session in Session_Entries:
         timestamp = session["datetime"].strftime("%Y-%m-%d %H:%M:%S")
         display = session["text"].split(" l ")[0]
         hours = session["hours"]

         file.write(f"{timestamp} | {display} | {hours}\n")

def load_roadmap():
   try:
      with open(f"{Roadmap_name} Roadmap.txt", "r") as file:
         for line in file:
          Roadmap.append(line.strip())
   except:
      print("You can also pick option 4 to start creating goals!")

def save_roadmap():
   print("Saving Data...")
   time.sleep(3)
   with open(f"{Roadmap_name} Roadmap.txt", "w") as file:
           for Road in Roadmap:
               file.write(Road + "\n")





def show_menu():
   print("\n--------------")
   print("--Coding Tracker Pro")
   print("--------------------")
   print("\n1. Log Session")
   print("2. Show Session")
   print("3. Show statistics")
   print("4. Log Goals")
   print("5. See Goals")
   print("6. Quit")


def get_choice():
   return input("Pick an option: ")

def clock():
   now = datetime.now()
   date = now.strftime("%b %d, %Y")
   time = now.strftime("%I:%M %p")
   weekday = now.strftime("%A")
   return {
      "display": f"{weekday} | {date} - {time}",
      "datetime": now
   }


def weeks(session_entries=None):
   if session_entries is None:
      session_entries = Session_Entries

   if not session_entries:
      return []

   grouped_weeks = []
   current_week = None
   current_week_start = None

   for entry in session_entries:
      week_start = entry["datetime"] - timedelta(days=entry["datetime"].weekday()).date()
      if current_week is None or week_start != current_week_start:
         current_week_start = week_start
         current_week = {
            "label": f"Week {len(grouped_weeks) + 1}",
            "sessions": []
         }
         grouped_weeks.append(current_week)

      current_week["sessions"].append(entry)

   return grouped_weeks


def log_session():
   Hour = int(input("Hours coded: "))
   session_info = clock()
   session = f"{session_info['display']} l {Hour}"
   Session_Entries.append({
      "text": session,
      "datetime": session_info["datetime"],
      "hours": Hour
   })
   Hours.append(Hour)
   print("Hours logged")


def show_sessions():
   if len(Session_Entries) == 0:
      print("No hours logged")
   else:
      for week_group in weeks():
         print(week_group["label"])
         for index, session in enumerate(week_group["sessions"], start=1):
            print(f"Session {index}: {session['text']} ({session['hours']} hours)")


def show_statistics():
   if len(Hours) == 0:
      print("No hours logged")
   else:
      Average = sum(Hours) / len(Hours)
      Total = sum(Hours)
      Highest = max(Hours)
      Least = min(Hours)
      print(f"You averaged {Average} hours.")
      print(f"You coded for a total of {Total} hours.")
      print(f"The most you coded in a session was {Highest} hours.")
      print(f"the least you coded in a session was {Least} hours.")

def Goals():
   global Roadmap_name
   Goal = input("What is your goal?: ")
   Roadmap_name = Goal
   Step = input("What is the first step to that goal?: ")
   Roadmap.append(f"Goal: {Goal}")
   Roadmap.append(Step)
   while True:
     Map = input("next step?: ")
     Roadmap.append(Map)
     quit = input("Press q to quit, press any other key to add more steps: ").lower()
     if quit == "q":
        print("Go to option 5 to see your list")
        break
     else:
        continue
   Roadmap.append(Goal)
   return Goal

def Goal_list():
   if len(Roadmap) == 0:
      print("No goals logged")
   else:
    for index, Road in enumerate(Roadmap, start=1):
      print(f"step {index}: {Road}")
      
        



   

def main():
   load_data()
   load_roadmap()
   while True:
      show_menu()
      Choice = get_choice()
      if Choice == "1":
         log_session()
      elif Choice == "2":
         show_sessions()
      elif Choice == "3":
         show_statistics()
      elif Choice == "4":
         Goals()

      elif Choice == "5":
         Goal_list()

      elif Choice == "6":
         print("Goodbye")
         save_data()
         if len(Roadmap) == 0:
            None
         else: 
          save_roadmap()
         break
      else:
         print("Invalid option")

main()