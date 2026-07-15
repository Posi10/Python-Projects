import time
from datetime import datetime, timedelta
Hours = []
Session_Entries = []
Roadmap = []
Goal_Title = ""
def load_data():
   try:
      with open("Coding Tracker Pro.txt", "r", encoding="utf-8") as file:
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
   with open("Coding Tracker Pro.txt", "w", encoding="utf-8") as file:
      for session in Session_Entries:
         timestamp = session["datetime"].strftime("%Y-%m-%d %H:%M:%S")
         display = session["text"].split(" l ")[0]
         hours = session["hours"]

         file.write(f"{timestamp} | {display} | {hours}\n")

def clean_roadmap_item(item):
   cleaned = item.strip()
   while True:
      if cleaned.startswith("Step ") and ": " in cleaned:
         prefix, _, remainder = cleaned.partition(": ")
         if prefix.split()[-1].isdigit():
            cleaned = remainder
            continue
      return cleaned


def load_roadmap():
   try:
      with open("Roadmap.txt", "r", encoding="utf-8") as file:
         for line in file:
            item = clean_roadmap_item(line)
            if item:
               Roadmap.append(item)
   except FileNotFoundError:
      print("You can also pick option 4 to start creating goals!")


def save_roadmap():
   print("Saving Data...")
   time.sleep(3)
   with open("Roadmap.txt", "w", encoding="utf-8") as file:
      for road in Roadmap:
         file.write(f"{road}\n")
           





def show_menu():
   print("\n--------------")
   print("--Coding Tracker Pro")
   print("--------------------")
   print("\n1. Log Session(List 1)")
   print("2. Show Session")
   print("3. Show statistics")
   print("4. Log Goals(List 2)")
   print("5. See Goals")
   print("6. Check completed Goals")
   print("7. Progress bar")
   print("8. Delete item")
   print("9. Quit")


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
      week_start = (
         entry["datetime"] - timedelta(days=entry["datetime"].weekday())
      ).date()
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
      print("Sessions💻")
      for week_group in weeks():
         print(week_group["label"])
         for index, session in enumerate(week_group["sessions"], start=1):
            print(f"Session {index}: {session['text']} ({session['hours']} hours)")


def show_statistics():
   if len(Hours) == 0:
      print("No hours logged")
   else:
      print("\nStatistics📊")
      Average = sum(Hours) / len(Hours)
      Total = sum(Hours)
      Highest = max(Hours)
      Least = min(Hours)
      print(f"You averaged {Average} hours.")
      print(f"You coded for a total of {Total} hours.")
      print(f"The most you coded in a session was {Highest} hours.")
      print(f"the least you coded in a session was {Least} hours.")


def Goals():
   global Goal_Title
   if len(Roadmap) == 0:
        Goal = input("What is your goal? (0 to quit): ")
        if Goal == "0": return
        
        Goal_Title = f"Goal: {Goal}"
        Step = input("What is the first step to that goal? (0 to quit): ")
        if Step == "0": return
        
        Roadmap.append(Step)
        
        while True:
            Map = input("Next step? (0 to quit): ")
            if Map == "0":
                break
            if Map.strip():
                Roadmap.append(Map)
                
        print("Saving Roadmap...")
        time.sleep(1)
        save_roadmap()
        print("Go to option 5 to see your list\nRoadmap Saved")
   else:
        print("\nGoals🎯")
        while True:
            Go = input("Do you want to add more goals? (0 to quit): ").lower()
            if Go == "0":
                break
            while True:
                Map = input("Next step? (0 to quit): ")
                if Map == "0":
                    print("Saving data...")
                    save_roadmap()
                    break
                if Map.strip():
                    Roadmap.append(Map)

             

def Goal_list():
    if len(Roadmap) == 0:
        print("No goals logged")
        return

    print("\nGoal Roadmap🎯")
    if Goal_Title:
        print(Goal_Title)
    
    # Clean 1-to-1 mapping because Roadmap only contains steps now
    for index, road in enumerate(Roadmap, start=1):
        print(f"{index}. {road}")

def Progress_bar():
   if len(Roadmap) == 0:
      print("No goals logged")
   else:
      Completed = sum(1 for road in Roadmap[1:] if "✅" in road)
      Complete = "🟩"
      Complete_20 = "🟩"*2
      Complete_30 = "🟩"*3
      Complete_40 = "🟩"*4
      Complete_50 = "🟩"*5
      Complete_60 = "🟩"*6
      Complete_70 = "🟩"*7
      Complete_80 = "🟩"*8
      Complete_90 = "🟩"*9
      Complete_100 = "🟩"*10
      Total = len(Roadmap[1:])
      Percentage = Completed / Total * 100
      if Percentage >= 100:
         Bar = Complete_100
      elif Percentage >= 90:
         Bar = f"{Complete_90}⬜"
      elif Percentage >= 80:
         Bar = f"{Complete_80}⬜⬜"
      elif Percentage >= 70:
         Bar = f"{Complete_70}⬜⬜⬜"
      elif Percentage >= 60:
         Bar = f"{Complete_60}⬜⬜⬜⬜"
      elif Percentage >= 50:
         Bar = f"{Complete_50}⬜⬜⬜⬜⬜"
      elif Percentage >= 40:
         Bar = f"{Complete_40}⬜⬜⬜⬜⬜⬜"
      elif Percentage >= 30:
         Bar = f"{Complete_30}⬜⬜⬜⬜⬜⬜⬜"
      elif Percentage >= 20:
         Bar = f"{Complete_20}⬜⬜⬜⬜⬜⬜⬜⬜"
      elif Percentage >= 10:
         Bar = f"{Complete}⬜⬜⬜⬜⬜⬜⬜⬜⬜"
      else:
         Bar = "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
      for Road in Roadmap:
         if "✅" in Road:
            Complete + Bar
         else:
            None
   Response = ""
   if Percentage == 100:
       Response = ("You made it to your goal!🎉🎊🥳🥳")
   elif Percentage >= 80:
       Response = ("You are so close, you got this!👊")
   elif Percentage >= 51:
       Response = ("Your more than halfway there, Keep going!🔥")
   elif Percentage >= 40:
       Response = ("You have made some serious progress, keep pushing!💪")
   elif Percentage >= 20:
       Response = ("Progress is progress — stay consistent!📈")
   elif Percentage >= 1:
       Response = ("You’ve started, and that matters. Keep working!🚀")
   Progress = Bar
   print("-------Progress Bar📶-----")
   print(f"{Progress}  Goal {Percentage:.2f}% completed")
   print(Response)




def Check():
   if len(Roadmap) == 0:
            print("No goals logged")
            return
   print("\nGoal Roadmap🎯")
   print(Roadmap[0])
    
   for index, Road in enumerate(Roadmap[1:], start=1):
            print(f"{index}. {Road}")
    
   while True:
            try:
                Option = int(input("\nWhich step did you complete? (0 to quit): "))
    
                if Option == 0:
                    break
    
                if Option < 1 or Option >= len(Roadmap):
                    print("Invalid step.")
                    continue
    
                if "✅" in Roadmap[Option]:
                    print("That step is already complete!")
                else:
                    Roadmap[Option] += " ✅"
                    print("Step marked complete!")
    
            except ValueError:
                print("Please enter a number.")
def delete():
   Option = int(input("Which list do you want to delete items from list 1/2:  "))
   if Option == 1:
     if len(Hours) == 0:
         time.sleep(3)
         print("No projects logged")
         return
     else:
        time.sleep(2)
        print("\nSessions💻")
        for index, Hour in enumerate(Hours, start=1):
           print(f"{index}. {Hour}")
        while True:
         try:
            Delete = int(input("\nWhich session would you like to delete (0 to quit): "))

            if Delete == 0:
                print("Leaving...")
                time.sleep(3)
                break

            if Delete < 1 or Delete > len(Hours):
                print("Invalid step.")
                continue

            removed_item = Hours.pop(Delete - 1)
            print(f"Deleting: {removed_item}")
            time.sleep(3)
            save_roadmap()
            break

         except ValueError:
            print("Please enter a number.")
   elif Option == 2:
       if len(Hours) == 0:
                time.sleep(3)
                print("No projects logged")
                return
       else:
         time.sleep(2)
         print("\nGoal Roadmap🎯")
         for index, road in enumerate(Roadmap, start=1):
                  print(f"{index}. {road}")
         while True:
            try:
              Delete = int(input("\nWhich step would you like to delete (0 to quit): "))
       
              if Delete == 0:
               print("Leaving...")
               time.sleep(3)
               break
       
              elif Delete < 1 or Delete > len(Roadmap):
                       print("Invalid step.")
                       continue
       
              removed_item = Roadmap.pop(Delete - 1)
              print(f"Deleting: {removed_item}")
              time.sleep(3)
              save_roadmap()
              break
            except ValueError:
                           print("Please enter a number.")
         

       


            
        

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
         Check()
      elif Choice == "7":
         Progress_bar()
      elif Choice == "8":
         delete()
      elif Choice == "9":
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