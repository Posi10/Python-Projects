from datetime import datetime, timedelta

reading_sessions = [
    {"Date": "September 1, 2026", "Book": "Atomic Habits", "Minutes": 30},
    {"Date": "September 2, 2026", "Book": "The Hobbit", "Minutes": 45},
    {"Date": "September 4, 2026", "Book": "Atomic Habits", "Minutes": 60},
    {"Date": "September 6, 2026", "Book": "The Hobbit", "Minutes": 25},
    {"Date": "September 7, 2026", "Book": "Atomic Habits", "Minutes": 50}
]

weeks = {}

seen = set()
for sesh in reading_sessions:
    d = datetime.strptime(sesh.get("Date"), "%B %d, %Y").date()

    Monday = d - timedelta(days=d.weekday())

    if Monday not in weeks:
        weeks[Monday] = []
    weeks[Monday].append(sesh)

for Monday, item in weeks.items():
    Minutes = 0
    Books = 0
    for session in item:
        Minutes += session["Minutes"]
        if session["Book"]:
         Books += 1
    print(f"{Monday} - {Monday + timedelta(days=6)}-- Sessions:{Books}   Minutes read: {Minutes}")
    