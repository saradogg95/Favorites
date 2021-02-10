import random

class Food:

    def __init__(self):
        self.breakfast = ""
        self.breakfast_list = [] 
        self.lunch = ""
        self.lunch_list = []        
        self.dinner = ""
        self.dinner_list = []
        self.snack = ""
        self.snack_list = []
        self.meals = []

    def populate_meal_lists(self):
        self.get_breakfast_list()
        self.get_breakfast()
        self.get_lunch_list()
        self.get_lunch()
        self.get_dinner_list()
        self.get_dinner()
        self.get_snack_list()
        self.get_snack()

    def reset(self):
        self.breakfast = ""
        self.breakfast_list = [] 
        self.lunch = ""
        self.lunch_list = []        
        self.dinner = ""
        self.dinner_list = []
        self.snack = ""
        self.snack_list = []
        self.meals = []

    def make_meals(self):
        self.populate_meal_lists()
        self.get_meals()

    def get_breakfast_list(self):
        """Gets all of the meals from the breakfast file and appends them to a list"""
        with open("breakfast.txt") as file:
            for breakfast in file:
                breakfast = breakfast.strip()
                self.breakfast_list.append(breakfast)

    def get_breakfast(self):
        """Gets a random breakfast from the breakfast list"""
        self.breakfast += random.choice(self.breakfast_list)

    def get_lunch_list(self):
        """Gets all of the meals from the lunch file and appends them to a list"""
        with open("lunch.txt") as file:
            for lunch in file:
                lunch = lunch.strip()
                self.lunch_list.append(lunch)

    def get_lunch(self):
        """Gets a random lunch from the lunch list"""
        self.lunch += random.choice(self.lunch_list)

    def get_dinner_list(self):
        """Gets all of the meals from the dinner file and appends them to a list"""
        with open("dinner.txt") as file:
            for dinner in file:
                dinner = dinner.strip()
                self.dinner_list.append(dinner)

    def get_dinner(self):
        """Gets a random dinner from the dinner list"""
        self.dinner += random.choice(self.dinner_list)

    def get_snack_list(self):
        """Gets all of the meals from the snack file and appends them to a list"""
        with open("snack.txt") as file:
            for snack in file:
                snack = snack.strip()
                self.snack_list.append(snack)

    def get_snack(self):
        """Gets a random snack from the snack list"""
        self.snack += random.choice(self.snack_list)

    def get_meals(self):
        """Gets a random breakfast, lunch, dinner and a snack"""
        self.meals.append(self.breakfast)
        self.meals.append(self.lunch)
        self.meals.append(self.dinner)
        self.meals.append(self.snack)
        return self.meals

    def __len__(self):
        return len(self.meals)

    def __str__(self):
        return f"Breakfast: {self.meals[0]}\nLunch: {self.meals[1]}\nDinner: {self.meals[2]}\nSnack: {self.meals[3]}\n"


def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    food = Food()
    for day in range(1,8):
        print(f"Day {day} - {days[day-1]}:")
        food.make_meals()
        print(food)
        food.reset()

if __name__ == "__main__":
    main()