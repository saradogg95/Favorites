import random

class Workout:

    def __init__(self):
        self.reset()

    def populate_workout_lists(self):
        self.get_warmup_list()
        self.get_exercise_list()

    def reset(self):
        self.warmup = ""
        self.warmup_list = [] 
        self.exercise = ""
        self.exercise_list = []        
        self.workouts = []

    def make_workouts(self):
        self.populate_workout_lists()
        self.get_workouts()

    def get_warmup_list(self):
        """Gets all of the warmups from the warmup file and appends them to a list"""
        with open("warmup.txt") as file:
            for warmup in file:
                warmup = warmup.strip()
                self.warmup_list.append(warmup)

    def get_warmup(self):
        """Gets a random warmup from the warmup list"""
        self.warmup += random.choice(self.warmup_list)

    def get_exercise_list(self):
        """Gets all of the exercises from the exercise file and appends them to a list"""
        with open("exercise.txt") as file:
            for exercise in file:
                exercise = exercise.strip()
                self.exercise_list.append(exercise)

    def get_exercise(self):
        """Gets a random exercise from the exercise list"""
        self.exercise += random.choice(self.exercise_list)

    def get_workouts(self):
        """Gets a random warmup and exercise"""
        for i in range(5):
            self.get_warmup()
            self.workouts.append(self.warmup)
            self.warmup = ""
            self.get_exercise()
            self.workouts.append(self.exercise)
            self.exercise = ""
        return self.workouts

    def __len__(self):
        return len(self.workouts)

    def __str__(self):
        return f"Warmups:\n{self.workouts[0]}\n{self.workouts[2]}\n{self.workouts[4]}\n{self.workouts[6]}\n{self.workouts[8]}\n\nExercises:\n{self.workouts[1]}\n{self.workouts[3]}\n{self.workouts[5]}\n{self.workouts[7]}\n{self.workouts[9]}\n"


def main():
    days = ["Monday", "Wednesday"]
    workout = Workout()
    for day in days:
        workout.make_workouts()
        print(f"{day}:\n{workout}")
        workout.reset()

if __name__ == "__main__":
    main()