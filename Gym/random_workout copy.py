import random

class Workout:

    def __init__(self):
        self.reset()

    def populate_workout_lists(self):
        self.get_warmup_list()
        self.get_push_list()
        self.get_pull_list()
        self.get_legs_list()

    def reset(self):
        self.warmup = ""
        self.warmup_list = [] 
        self.exercise = ""
        self.push = []        
        self.pull = []  
        self.legs = []      
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


    def get_push_list(self):
        """Gets all of the exercises from the push file and appends them to a list"""
        with open("push.txt") as file:
            for push in file:
                push = push.strip()
                self.push.append(push)

    def get_push(self):
        """Gets a random exercise from the push list"""
        self.exercise += random.choice(self.push)

    def get_pull_list(self):
        """Gets all of the exercises from the pull file and appends them to a list"""
        with open("pull.txt") as file:
            for pull in file:
                pull = pull.strip()
                self.pull.append(pull)

    def get_pull(self):
        """Gets a random exercise from the pull list"""
        self.exercise += random.choice(self.pull)

    def get_legs_list(self):
        """Gets all of the exercises from the legs file and appends them to a list"""
        with open("legs.txt") as file:
            for legs in file:
                legs = legs.strip()
                self.legs.append(legs)

    def get_legs(self):
        """Gets a random exercise from the legs list"""
        self.exercise += random.choice(self.legs)

    def get_workouts(self):
        """Gets random warmups"""
        for i in range(5):
            self.get_warmup()
            self.workouts.append(self.warmup)
            self.warmup = ""
            self.workouts.append(self.exercise)
            self.exercise = ""
        return self.workouts

    def __len__(self):
        return len(self.workouts)

    def __str__(self):
        return f"Warmups:\n{self.workouts[0]}\n{self.workouts[2]}\n{self.workouts[4]}\n{self.workouts[6]}\n{self.workouts[8]}\n\nExercises:\n{self.workouts[1]}\n{self.workouts[3]}\n{self.workouts[5]}\n{self.workouts[7]}\n{self.workouts[9]}\n"


def main():
    days = ["Monday - Push", "Wednesday - Pull", "Friday - Legs"]
    workout = Workout()
    for day in days:
        workout.make_workouts()
        print(f"{day}:\n{workout}")
        workout.reset()

if __name__ == "__main__":
    main()