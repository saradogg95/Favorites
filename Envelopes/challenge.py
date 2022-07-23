import random

class Envelopes:
    def __init__(self):
        self.goal = 5050
        self.rate = 137
        self.saved = self.get_saved_from_file()
        self.number_of_envelopes_total = 100
        self.number_of_envelopes_used = self.get_number_of_envelopes_from_file()
        self.chosen_envelope = 0
        self.generated = self.get_generated_state()
        self.envelopes = []
        self.random_number = 0

    def calculate(self):
        self.get_random_envelope()
        self.add_saved_to_file()

    def get_generated_state(self):
        f = open("generated.txt", "r")
        return f.read().strip()

    def generate_envelopes(self):
        if self.generated == "False":
            print("\nWelcome to the envelope challenge!")
            f = open("envelopes.txt", "w+")
            f.writelines( "%s\n" % item for item in [x for x in range(1, 101)] )
            f2 = open("generated.txt", "w+")
            f2.write("True")
        print("\nWelcome back to the envelope challenge!")
        self.get_envelopes()

    def get_envelopes(self):
        f = open("envelopes.txt", "r")
        for line in f:
            self.envelopes.append(int(line.strip()))

    def get_random_number(self):
        self.random_number = random.randint(0, self.number_of_envelopes_total - self.number_of_envelopes_used)

    def get_random_envelope(self):
        self.get_random_number()
        self.chosen_envelope = self.envelopes[self.random_number]
        print(f"\nEnvelope {self.chosen_envelope} has been randomly chosen!\n")
        choice = input(f"Can you save this ${self.chosen_envelope} or ~{self.rate * self.chosen_envelope:,.0f}kr this week? y/n ")
        if choice == "y":
            self.saved += self.chosen_envelope
            self.remove_used_envelope()
            self.number_of_envelopes_used += 1
            self.add_number_of_envelopes_to_file()
    
    def remove_used_envelope(self):
        self.envelopes.remove(self.chosen_envelope)
        f = open("envelopes.txt", "w+")
        f.writelines( "%s\n" % item for item in self.envelopes )


    def add_saved_to_file(self):
        f = open("saved.txt", "w+")
        f.write(str(self.saved))
        f.close()

    def get_saved_from_file(self):
        f = open("saved.txt", "r")
        return int(f.readline().strip())

    def add_number_of_envelopes_to_file(self):
        f = open("num_of_envelopes.txt", "w+")
        f.write(str(self.number_of_envelopes_used))
        f.close()

    def get_number_of_envelopes_from_file(self):
        f = open("num_of_envelopes.txt", "r")
        return int(f.readline().strip())

    def get_remaining(self):
        return self.goal - int(self.saved)

    def __str__(self):
        return f"\nStarting goal: ${self.goal} --- ~{self.rate * self.goal:,.0f}kr\nSaved so far: ${self.saved} --- ~{self.rate * self.saved:,.0f}kr\nRemaining: ${self.get_remaining()} --- ~{self.rate * self.get_remaining():,.0f}kr\n"

if __name__ == "__main__":
   challenge = Envelopes()
   challenge.generate_envelopes()
   while True:
    challenge.calculate()
    print(challenge)
    choice = input("Would you like to pick another envelope right now? y/n ")
    if choice != "y":
        print("\nNo problem! Seeya later!\n")
        break