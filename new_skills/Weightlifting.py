import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

# Exercise data with options and variations
exercises = {
    "Strength": {
        "Barbell Squats": {
            "Sets": 3,
            "Reps": 5,
            "Weight": "Heavy"
        },
        "Barbell Bench Press": {
            "Sets": 3,
            "Reps": 5,
            "Weight": "Heavy"
        },
        "Barbell Deadlifts": {
            "Sets": 1,
            "Reps": 5,
            "Weight": "Heavy"
        },
        "Dumbbell Goblet Squats": {
            "Sets": 3,
            "Reps": 8,
            "Weight": "Moderate"
        },
        "Dumbbell Chest Press": {
            "Sets": 3,
            "Reps": 8,
            "Weight": "Moderate"
        },
        "Dumbbell Romanian Deadlifts": {
            "Sets": 3,
            "Reps": 8,
            "Weight": "Moderate"
        },
        "Bodyweight Squats": {
            "Sets": 3,
            "Reps": 10,
            "Weight": "Bodyweight"
        },
        "Push-ups": {
            "Sets": 3,
            "Reps": 10,
            "Weight": "Bodyweight"
        },
        "Bodyweight Lunges": {
            "Sets": 3,
            "Reps": 10,
            "Weight": "Bodyweight"
        }
    },
    "Muscle Mass": {
        "Barbell Squats": {
            "Sets": 3,
            "Reps": 8,
            "Weight": "Moderate"
        },
        "Barbell Bench Press": {
            "Sets": 3,
            "Reps": 8,
            "Weight": "Moderate"
        },
        "Barbell Rows": {
            "Sets": 3,
            "Reps": 8,
            "Weight": "Moderate"
        },
        "Dumbbell Lunges": {
            "Sets": 3,
            "Reps": 10,
            "Weight": "Moderate"
        },
        "Dumbbell Chest Flyes": {
            "Sets": 3,
            "Reps": 10,
            "Weight": "Moderate"
        },
        "Dumbbell Rows": {
            "Sets": 3,
            "Reps": 10,
            "Weight": "Moderate"
        },
        "Bodyweight Squats": {
            "Sets": 3,
            "Reps": 12,
            "Weight": "Bodyweight"
        },
        "Push-ups": {
            "Sets": 3,
            "Reps": 12,
            "Weight": "Bodyweight"
        },
        "Inverted Rows": {
            "Sets": 3,
            "Reps": 12,
            "Weight": "Bodyweight"
        }
    },
    "General Fitness": {
        "Barbell Squats": {
            "Sets": 3,
            "Reps": 10,
            "Weight": "Moderate"
        },
        "Barbell Overhead Press": {
            "Sets": 3,
            "Reps": 10,
            "Weight": "Moderate"
        },
        "Barbell Romanian Deadlifts": {
            "Sets": 3,
            "Reps": 10,
                        "Weight": "Moderate"
        },
        "Dumbbell Step-ups": {
            "Sets": 3,
            "Reps": 12,
            "Weight": "Light to moderate"
        },
        "Dumbbell Shoulder Press": {
            "Sets": 3,
            "Reps": 12,
            "Weight": "Light to moderate"
        },
        "Dumbbell Romanian Deadlifts": {
            "Sets": 3,
            "Reps": 12,
            "Weight": "Light to moderate"
        },
        "Bodyweight Squats": {
            "Sets": 3,
            "Reps": 15,
            "Weight": "Bodyweight"
        },
        "Push-ups": {
            "Sets": 3,
            "Reps": 15,
            "Weight": "Bodyweight"
        },
        "Mountain Climbers": {
            "Sets": 3,
            "Reps": 15,
            "Weight": "Bodyweight"
        }
    }
}

def generate_schedule():
    goal = goal_var.get()
    days_per_week = int(days_var.get())
    available_equipment = equipment_var.get()

    # Generate schedule based on user input
    schedule = "Your Weightlifting Program Schedule:\n\n"

    for day in range(1, days_per_week + 1):
        schedule += "Day " + str(day) + ":\n"

        if goal in exercises:
            available_exercises = exercises[goal]
            selected_exercises = []

            for exercise, details in available_exercises.items():
                if available_equipment in exercise or "Bodyweight" in exercise:
                    selected_exercises.append((exercise, details))

            for exercise, details in selected_exercises:
                sets = details["Sets"]
                reps = details["Reps"]
                weight = details["Weight"]

                schedule += f"Exercise: {exercise} - {sets} sets of {reps} reps ({weight} weight)\n"

            schedule += "\n"

    # Display the schedule in a messagebox
    messagebox.showinfo("Weightlifting Program Schedule", schedule)

# Create the main GUI window
window = tk.Tk()
window.title("Weightlifting Program Generator")

# Create the goal selection label and dropdown menu
goal_label = tk.Label(window, text="Choose your goal:")
goal_label.pack()
goal_var = tk.StringVar(window)
goal_var.set("Strength")
goal_dropdown = tk.OptionMenu(window, goal_var, *exercises.keys())
goal_dropdown.pack()

# Create the days per week selection label and entry field
days_label = tk.Label(window, text="Number of training days per week:")
days_label.pack()
days_var = tk.StringVar(window)
days_entry = tk.Entry(window, textvariable=days_var)
days_entry.pack()

# Create the available equipment selection label and checkboxes
equipment_label = tk.Label(window, text="Available equipment:")
equipment_label.pack()
equipment_var = tk.StringVar()
barbell_checkbox = tk.Checkbutton(window, text="Barbell", variable=equipment_var, onvalue="Barbell")
barbell_checkbox.pack()
dumbbells_checkbox = tk.Checkbutton(window, text="Dumbbells", variable=equipment_var, onvalue="Dumbbells")
dumbbells_checkbox.pack()
bodyweight_checkbox = tk.Checkbutton(window, text="Bodyweight", variable=equipment_var, onvalue="Bodyweight")
bodyweight_checkbox.pack()

# Create the generate schedule button
generate_button = tk.Button(window, text="Generate Schedule", command=generate_schedule)
generate_button.pack()

# Start the GUI event loop
window.mainloop()