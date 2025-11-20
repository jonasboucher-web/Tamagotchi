import time
import random

class Pet:
    def __init__(self, name="Tama"):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.cleanliness = 50

    def feed(self):
        self.hunger = min(100, self.hunger + 20)
        print(f"{self.name} enjoyed the meal!")

    def play(self):
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 10)
        print(f"{self.name} had fun playing!")

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        print(f"{self.name} is sleeping peacefully.")

    def clean(self):
        self.cleanliness = min(100, self.cleanliness + 25)
        print(f"{self.name} is now sparkling clean!")

    def update_stats(self):
        self.hunger = max(0, self.hunger - random.randint(1, 5))
        self.energy = max(0, self.energy - random.randint(1, 3))
        self.happiness = max(0, self.happiness - random.randint(1, 4))
        self.cleanliness = max(0, self.cleanliness - random.randint(1, 2))

    def get_mood(self):
        if self.hunger < 20 or self.energy < 20:
            return "hungry/tired"
        elif self.happiness < 30:
            return "sad"
        elif self.cleanliness < 20:
            return "dirty"
        else:
            return "happy"

# Game Loop
pet = Pet("PyPet")

while True:
    print("\n--- Pet Status ---")
    print(f"Name: {pet.name}")
    print(f"Hunger: {pet.hunger}")
    print(f"Energy: {pet.energy}")
    print(f"Happiness: {pet.happiness}")
    print(f"Cleanliness: {pet.cleanliness}")
    print(f"Mood: {pet.get_mood()}")

    action = input("What do you want to do? (feed, play, sleep, clean, exit): ").lower()

    if action == "feed":
        pet.feed()
    elif action == "play":
        pet.play()
    elif action == "sleep":
        pet.sleep()
    elif action == "clean":
        pet.clean()
    elif action == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid action.")

    pet.update_stats()
    time.sleep(2) # Simulate time passing