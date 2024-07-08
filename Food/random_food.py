import random
from typing import Text

class Food:

    def __init__(self):
        self.reset()

    def populate_meal_lists(self):
        self.get_breakfast()
        self.get_lunch()
        self.get_dinner()
        self.get_snack()

    def reset(self):
        self.breakfast = ""
        self.breakfast_list = [
            "Hafragrautur",
            # "Kornflex",
            # "Cheerios",
            # "Special K"
            # "Chiagrautur",
            # "Honeynut cheerios",
            # "Weetos",
            # "Rice Krispies"
        ] 
        self.lunch = ""
        self.lunch_list = [
            "Grísk jógúrt með ávöxtum og múslí",
            "Brauð með banana",
            "Brauð með epli",
            "Brauð með gúrku",
            "Brauð með mysingi og banana",
            "Grilluð ostasamloka",
            "Ristað brauð með smjöri, osti og sultu",
            "Ristað brauð með avocado og eggjum",
            "Bolla með avocado og eggjum",
            "Bolla með áleggi",
            "Ristuð beygla með smjöri og osti",
            "Núðlur með eggjum, brokkolí og gulrótum",
            "Ristað brauð og hrærð egg",
            "Tortillas",
            "Smoothie skál",
            "Heimagert Maikai",
            "Kaffijógúrt með múslí"
        ]        
        self.dinner = ""
        self.dinner_list = [
            "Kjúklingapasta",
            "Pasta með rjómasósu",
            "Pylsur",
            "Pylsupasta",
            "Spaghetti bolognese",
            "Súpukássa",
            "Tortilla pizza",
            "Kjúklingabollur með hrísgrjónum og súrsætri sósu",
            "Plokkfiskur með rúgbrauði",
            "Ýsa í raspi og kartöflur",
            "Tacos",
            "Tortillas",
            "Pestó pasta",
            "Súpa",
            "Grjónagrautur",
            "Makkarónugrautur",
            "Mexíkósk kjúklingasúpa",
            "Kornflex kjúklingur",
            "Quesadillas",
            "Kjúklingasnitsel með kartöflum og brúnni sósu",
            "Pizza",
            "Ofnbakaður fiskur",
            "Kjötbúðingur með kartöflustöppu",
            "Fiskbúðingur með kartöflum",
            "Bleikar bollur með kartöflum",
            "Falafel samloka með kartöflum og grænmeti",
            "Lazy lasagna",
            "Ofnbakað pasta",
            "Kjúklingaréttur",
            "Pastaréttur",
            "Pylsu og kartöflukássa",
            "Pulled pork nachos",
            "Pulled pork samloka og kartöflur",
            "Fiskibollur og kartöflur"
        ]
        self.snack = ""
        self.snack_list = [
            "Hrökkbrauð með smjöri og osti",
            "Hrökkbrauð með hummus og eggjum",
            "Gulrætur og hummus",
            "Orkukúlur og grænt te",
            "Súkkulaði sesamstangir",
            "Kókosstykki",
            "Smoothie",
            "Flatkökur",
            "Banani",
            "Vínber",
            "Epli",
            "Pera",
            "Paprika",
            "Jarðaber",
            "Epli og hnetusmjör",
            "Poppkex",
            "Hnetumix",
            "Próteinkaka og grænt te",
            "Peanut clusters",
            "Hafrakökur",
            "Muffins"
        ]
        self.meals = []

    def make_meals(self):
        self.populate_meal_lists()
        self.get_meals()

    def get_breakfast(self):
        """Gets a random breakfast from the breakfast list"""
        self.breakfast += random.choice(self.breakfast_list)

    def get_lunch(self):
        """Gets a random lunch from the lunch list"""
        self.lunch += random.choice(self.lunch_list)

    def get_dinner(self):
        """Gets a random dinner from the dinner list"""
        self.dinner += random.choice(self.dinner_list)

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
        return f"Morgunmatur: {self.meals[0]}\nHádegismatur: {self.meals[1]}\nKvöldmatur: {self.meals[2]}\nSnarl: {self.meals[3]}\n"


def main():
    days = ["Mánudagur", "Þriðjudagur", "Miðvikudagur", "Fimmtudagur", "Föstudagur", "Laugardagur", "Sunnudagur"]
    food = Food()
    print()
    for day in range(1,8):
        print(f"Dagur {day} - {days[day-1]}:")
        food.make_meals()
        print(food)
        food.reset()

if __name__ == "__main__":
    main()