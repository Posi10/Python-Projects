# The list of workout data to run your code against:
workouts = [
    {
        "Date": "2026-02-10",
        "Exercises": [
            {
                "Name": "Bench Press",
                "Sets": [
                    {"Weight": 135, "Reps": 10},
                    {"Weight": 185, "Reps": 5}
                ]
            },
            {
                "Name": "Squat",
                "Sets": [
                    {"Weight": 225, "Reps": 5}
                ]
            }
        ]
    },
    {
        "Date": "2026-02-15",
        "Exercises": [
            {
                "Name": "Bench Press",
                "Sets": [
                    {"Weight": 200, "Reps": 1},
                    {"Weight": 185, "Reps": 6}
                ]
            }
        ]
    },
    {
        "Date": "2026-02-20",
        "Exercises": [
            {
                "Name": "Bench Press",
                "Sets": [
                    {"Weight": 200, "Reps": 3}  # This should be your final PR!
                ]
            }
        ]
    }
]

# Set this variable to choose which exercise to look up:
selected_exercise = "Bench Press"

best_workout = None
best_weight = 0
best_reps = 0
for workout in workouts:
    for exercise in workout["Exercises"]:
        if exercise.get('Name') == selected_exercise:
            for Set in exercise.get("Sets", []):
                w = Set.get('Weight', 0)
                r = Set.get('Reps', 0)
                if (w, r) > (best_weight, best_reps):
                    best_weight, best_reps = w, r
                    best_workout = workout
if best_workout == None:
        print(f"Nothing found on {selected_exercise}")
else:
        print(f"Your PR with {selected_exercise} is {best_weight}lbs x {best_reps} reps (from {best_workout['Date']})")