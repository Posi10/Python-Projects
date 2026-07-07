Hours = []
hour = int(input("Hours coded today: "))
Hours.append(hour)
with open("Coding Tracker.txt", "w") as file:
    for hour in Hours:
     file.write(str(hour) + "\n")

with open("Coding Tracker.txt", "r") as file:
   for line in file:
      Hours.append(int(line.strip()))

print(Hours)
