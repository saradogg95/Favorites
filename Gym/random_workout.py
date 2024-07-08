import random

class Workout:

    def __init__(self):
        self.reset()

    def reset(self):
        self.warmup_list = [] 
        self.warmups = [] 
        self.push_list = []    
        self.push = []    
        self.pull_list = []
        self.pull = [] 
        self.legs_list = []
        self.legs = []      

    def populate_workout_lists(self):
        self.get_warmup_list()
        self.get_warmups()
        self.get_push_list()
        self.get_push_day()
        self.get_pull_list()
        self.get_pull_day()
        self.get_legs_list()
        self.get_leg_day()

    def make_workouts(self):
        self.populate_workout_lists()

    def get_warmups(self):
        """Gets random warmups"""
        for _ in range(6):
            self.warmups.append(self.get_warmup())

    def get_push_day(self):
        """Gets random push exercises"""
        for _ in range(4):
            self.push.append(self.get_push())

    def get_pull_day(self):
        """Gets random pull exercises"""
        for _ in range(4):
            self.pull.append(self.get_pull())

    def get_leg_day(self):
        """Gets random leg exercises"""
        for _ in range(4):
            self.legs.append(self.get_legs())

    def get_warmup_list(self):
        """Gets all of the warmups from the warmup file and appends them to a list"""
        with open("warmup.txt") as file:
            for warmup in file:
                warmup = warmup.strip()
                self.warmup_list.append(warmup)

    def get_warmup(self):
        """Gets a random warmup from the warmup list"""
        return random.choice(self.warmup_list)

    def get_push_list(self):
        """Gets all of the exercises from the push file and appends them to a list"""
        with open("push.txt") as file:
            for push in file:
                push = push.strip()
                self.push_list.append(push)

    def get_push(self):
        """Gets a random exercise from the push list"""
        return random.choice(self.push_list)

    def get_pull_list(self):
        """Gets all of the exercises from the pull file and appends them to a list"""
        with open("pull.txt") as file:
            for pull in file:
                pull = pull.strip()
                self.pull_list.append(pull)

    def get_pull(self):
        """Gets a random exercise from the pull list"""
        return random.choice(self.pull_list)

    def get_legs_list(self):
        """Gets all of the exercises from the legs file and appends them to a list"""
        with open("legs.txt") as file:
            for legs in file:
                legs = legs.strip()
                self.legs_list.append(legs)

    def get_legs(self):
        """Gets a random exercise from the legs list"""
        return random.choice(self.legs_list)

    def __len__(self):
        return len(self.workouts)

    def __str__(self):
        return f""


def main():
    days = ["Monday - Push", "Wednesday - Pull", "Friday - Legs"]
    workout = Workout()
    workout.make_workouts()
    # print(f"\n{days[0]}\n{workout.warmups[0]}\n{workout.warmups[1]}")
    print(f"\n{days[0]}\n{workout.push[0]}\n{workout.push[1]}\n{workout.push[2]}\n{workout.push[3]}")
    # print(f"\n{days[1]}\n{workout.warmups[2]}\n{workout.warmups[3]}")
    print(f"\n{days[1]}\n{workout.pull[0]}\n{workout.pull[1]}\n{workout.pull[2]}\n{workout.pull[3]}")
    # print(f"\n{days[2]}\n{workout.warmups[4]}\n{workout.warmups[5]}")
    print(f"\n{days[2]}\n{workout.legs[0]}\n{workout.legs[1]}\n{workout.legs[2]}\n{workout.legs[3]}\n")

if __name__ == "__main__":
    main()