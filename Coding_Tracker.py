import time
from datetime import datetime
Hours = []

def load_data():
   try:
      with open("Coding Tracker Pro.txt", "r") as file:
         for line in file:
            if line.strip():
               Hours.append(int(line.strip()))
   except FileNotFoundError:
      time.sleep(3)
      print("Welcome to Coding Tracker V2!")
      time.sleep(3)
      print("To start please pick option 1 so we can load your sessions!")


def save_data():
   with open("Coding Tracker Pro.txt", "a") as file:
      for Hour in Hours:
         file.write(str(Hour) + "\n")


def show_menu():
   print("\n--------------")
   print("--Coding Tracker Pro")
   print("--------------------")
   print("\n1. Log Session")
   print("2. Show Session")
   print("3. Show statistics")
   print("4. Quit")


def get_choice():
   return input("Pick an option: ")

def clock():
   now = datetime.now()
   date = now.strftime("%b %d, %Y")
   time = now.strftime("%I :%M %p")
   session = f"{date} - {time}"
   return session


def log_session():
   Hour = int(input("Hours coded: "))
   time = clock()
   session = f"{time} l {Hour}"
   Hours.append(session)
   print("Hours logged")


def show_sessions():
   if len(Hours) == 0:
      print("No hours logged")
   else:
      for index, session in enumerate(Hours, start=1):
         print(f"Session {index}: {session} Hours coding")


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


def main():
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
         print("Goodbye")
         save_data()
         break
      else:
         print("Invalid option")

main()