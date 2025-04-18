# pet.py
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []  # Bonus: List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Prevent hunger from going below 0
        self.happiness = min(10, self.happiness + 1)  # Cap happiness at 10

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Prevent energy from exceeding 10

    def play(self):
        self.energy = max(0, self.energy - 2)  # Prevent energy from going below 0
        self.happiness = min(10, self.happiness + 2)  # Cap happiness at 10
        self.hunger = min(10, self.hunger + 1)  # Cap hunger at 10

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")


    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")        
