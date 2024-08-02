from itertools import count
import random

class Chimera:
    def __init__(self, head, body, limbs, wings, tail, name, level, hunger, energy, experience, health):
        self.head = head
        self.body = body
        self.limbs = limbs
        self.wings = wings
        self.tail = tail
        self.name = name

        self.level = level  # Now represents both level and age
        self.hunger = hunger
        self.energy = energy
        self.experience = experience
        self.health = health

    def feed(self, food_amount):
        if food_amount < 0:
            print(f"Cannot feed a negative amount of food to {self.name}.")
            return

        # Check inventory for available food
        if not Inventory.use_food(food_amount):
            print(f"Not enough food to feed {self.name}. Please check the food inventory.")
            return
        
        self.hunger += food_amount  # Increase hunger indicating more fullness
        if self.hunger > 100:
            print(f"{self.name} has been overfed and died!")
            self.health = 0
            return  # Chimera dies from overfeeding, no need to proceed further

        self.energy += food_amount  # Increase energy by the same amount
        if self.energy > 100:
            self.energy = 100  # Cap the energy at 100 to prevent overcharging

        # If hunger goes into the negative (which shouldn't normally happen if food_amount is always positive)
        if self.hunger < 0:
            print(f"{self.name} is starving due to an error and has died!")
            self.health = 0
            return

        print(f"{self.name} was fed {food_amount} units of food.")
        print(f"Energy is now {self.energy}. Hunger is now {self.hunger}.")


    def sleep(self):
        try:
            duration = int(input("Enter how long the chimera should sleep (1-10): "))
            if 1 <= duration <= 10:
                health_gain = duration * 10
                hunger_loss = duration * 10
                self.health = min(100, self.health + health_gain)  # Cap health at 100
                self.hunger -= hunger_loss  # Reduce hunger based on sleep duration

                # Check if hunger goes below zero and the chimera dies from starvation during sleep
                if self.hunger < 0:
                    print(f"{self.name} has starved to death during sleep!")
                    self.health = 0  # Set health to 0 to indicate death
                    return

                print(f"{self.name} has slept for {duration} hours, restoring {health_gain} health and reducing hunger by {hunger_loss}.")
            else:
                print("Invalid input. Sleep duration must be between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")



    def train(self):
        experience_gained = self.energy
        self.experience += experience_gained
        health_depletion = 100 - self.energy  # Health depletion inversely proportional to energy
        self.health = max(0, self.health - health_depletion)

        self.hunger = max(0, self.hunger - self.energy)  # Prevent hunger from going below 0
        
        if self.health <= 0:
            print(f"{self.name} has died from exhaustion after training.")
            return

        self.energy = 0  # Deplete all energy after training
        print(f"{self.name} trained and gained {experience_gained} experience points. Health depleted by {health_depletion} points.")
        
        while self.experience >= self.experience_to_level_up():
            self.level_up()


    def experience_to_level_up(self):
        return 100 * (self.level + 1)

    def level_up(self):
        self.level += 1
        self.experience -= self.experience_to_level_up()
        if self.experience < 0:
            self.experience = 0  # Ensure experience does not go negative
        print(f"{self.name} has leveled up! New level: {self.level}")

    def is_dead(self):
        return self.health <= 0
    

    def display_info(self):
        print("Chimera Information:", self.name)
        print("Head:", self.head)
        print("Body:", self.body)
        print("Limbs:", self.limbs)
        print("Wings:", self.wings)
        print("Tail:", self.tail)
        print("Level (Age):", self.level)
        print("Hunger:", self.hunger)
        print("Energy:", self.energy)
        print("Experience:", self.experience)
        print("Health:", self.health)
    
    def display_condition(self):
        print("Level (Age):", self.level)
        print("Hunger:", self.hunger)
        print("Energy:", self.energy)
        print("Experience:", self.experience)
        print("Health:", self.health)

        
class Inventory:
    food = 1000

    @staticmethod
    def add_food(amount):
        Inventory.food += amount
        print(f"Added {amount} food to inventory. Total food: {Inventory.food}")

    @staticmethod
    def use_food(amount):
        if Inventory.food >= amount:
            Inventory.food -= amount
            print(f"Used {amount} food from inventory. Remaining food: {Inventory.food}")
            return True
        else:
            print("Not enough food in inventory.")
            return False

    @staticmethod
    def display_food():
        print(f"Total food in inventory: {Inventory.food}")            


class ChimeraBuilder:

    chimeras=[]
    animal = ["Wolf", "Lion", "Bear", "Eagle", "Stork", "Swan", "Snake", "Turtle", "Crocodile", "Shark", "Dolphin", "Octopus", "Frog", "Axolotl", "Caecilian", "Spider", "Beetle", "Moth", "Elephant", "Rhino", "Horse", "Whale", "Lobster", "Snail", "Scorpion", "Wasp", "Giraffe", "Ostrich", "Lizard", "Salamander", "Glaucus", "Centipede", "Swan", "Peafowl", "Bat", "Skunk"]
    headOption = ["Wolf", "Lion", "Bear", "Eagle", "Stork", "Swan", "Snake", "Turtle", "Crocodile", "Shark", "Dolphin", "Octopus", "Frog", "Axolotl", "Caecilian", "Spider", "Beetle", "Moth", "Elephant", "Rhino", "Horse"]
    bodyOption = ["Wolf", "Lion", "Bear","Snake", "Turtle", "Crocodile", "Shark", "Whale", "Lobster", "Snail", "Scorpion", "Wasp", "Elephant", "Horse", "Giraffe"]
    limbOption = ["Wolf", "Lion", "Bear", "Eagle", "Ostrich","Turtle", "Crocodile", "Lizard", "Shark", "Octopus", "Lobster", "Frog", "Salamander", "Glaucus", "Spider", "Centipede", "Beetle", "Elephant","Rhino", "Horse"]
    wingOption = ["Eagle","Swan", "Peafowl", "Wasp", "Moth", "Beetle", "Bat"]
    tailOption = ["Wolf", "Lion", "Skunk", "Eagle", "Ostrich", "Peafowl", "Snake", "Crocodile", "Lizard", "Whale", "Shark", "Lobster", "Scorpion", "Wasp", "Elephant", "Horse"]

    #Chimera Building
    @staticmethod
    def build_chimera():
        print("Choose a head from the following options:")
        for index, option in enumerate(ChimeraBuilder.headOption, start=1):
            print(f"{index}. {option}", end='    ')
        head = ChimeraBuilder.headOption[ChimeraBuilder.validate_choice(len(ChimeraBuilder.headOption))]

        print("\nChoose a body from the following options:")
        for index, option in enumerate(ChimeraBuilder.bodyOption, start=1):
            print(f"{index}. {option}", end='    ')
        body = ChimeraBuilder.bodyOption[ChimeraBuilder.validate_choice(len(ChimeraBuilder.bodyOption))]

        print("\nChoose limbs from the following options:")
        for index, option in enumerate(ChimeraBuilder.limbOption, start=1):
            print(f"{index}. {option}", end='    ')
        limbs = ChimeraBuilder.limbOption[ChimeraBuilder.validate_choice(len(ChimeraBuilder.limbOption), zero_allowed=True)]

        print("\nChoose wings from the following options:")
        for index, option in enumerate(ChimeraBuilder.wingOption, start=1):
            print(f"{index}. {option}", end='    ')
        wings = ChimeraBuilder.wingOption[ChimeraBuilder.validate_choice(len(ChimeraBuilder.wingOption), zero_allowed=True)]

        print("\nChoose a tail from the following options:")
        for index, option in enumerate(ChimeraBuilder.tailOption, start=1):
            print(f"{index}. {option}", end='    ')
        tail = ChimeraBuilder.tailOption[ChimeraBuilder.validate_choice(len(ChimeraBuilder.tailOption), zero_allowed=True)]

        name = input("Give it a name (required): ")
        return Chimera(head, body, limbs, wings, tail, name, 0, 0, 0, 0, 100)
    
    @staticmethod
    def validate_choice(options_count, zero_allowed=False):
        while True:
            try:
                choice = int(input("\nEnter the number corresponding to your choice: ")) - 1
                if zero_allowed and choice == -1:
                    return None
                elif 0 <= choice < options_count:
                    return choice
                else:
                    print("Invalid choice, please select a valid number.")
            except ValueError:
                print("Invalid input, please enter a number.")
    
    # C1 = Chimera("Stork", "Snake", "Centipede", "Bat", "Ostrich", "Ashley", 5, 0, 0, 0, 100)
    # C2 = Chimera("Dolphin", "Whale", "Octopus", "Wasp", "Lobster", "Beach", 5, 0, 0, 0, 100)
    # C3 = Chimera("Axolotl", "Horse", "Salamander", "Eagle", "Lizard", "Cutie", 5, 0, 0, 0, 100)
    # C4 = Chimera("Caecilian", "Turtle", "Frog", "Peafowl", "Shark", "Damon", 5, 0, 0, 0, 100)
    # C5 = Chimera("Lion", "Snail", "Glaucus", "Beetle", "Scorpion", "Escanor", 5, 0, 0, 0, 100)
    # C6 = Chimera("Wolf", "Giraffe", "Spider", "Moth", "Crocodile", "Felix", 5, 0, 0, 0, 100)
    # C7 = Chimera("Bear", "Elephant", "Rhino", "Swan", "Skunk", "Gunter", 5, 0, 0, 0, 100)

    # chimeras.append(C1)
    # chimeras.append(C2)
    # chimeras.append(C3)
    # chimeras.append(C4)
    # chimeras.append(C5)
    # chimeras.append(C6)
    # chimeras.append(C7)
    
#Removing Dead Chimeras.
def remove_dead_chimeras():
        original_count = len(ChimeraBuilder.chimeras)
        ChimeraBuilder.chimeras = [chimera for chimera in ChimeraBuilder.chimeras if not chimera.is_dead()]
        removed_count = original_count - len(ChimeraBuilder.chimeras)
        print(f"Removed {removed_count} dead chimeras from the list.")


#Welcoming Message 
def welcome_message():
    print("Welcome to the Chimera game!")
    print("In this game, you will create and take care of chimeras.")
    print("You can feed, put to sleep, or entertain your chimeras to help them grow.")
    print("Let's get started!")
    print("")
    #Create a Chimera using the ChimeraBuilder
    chimera_builder = ChimeraBuilder()
    new_chimera = chimera_builder.build_chimera()
    ChimeraBuilder.chimeras.append(new_chimera)
    new_chimera.display_info()     

#Checking Chimera
def check_chimera():
    while True:
        if not ChimeraBuilder.chimeras:
            print("No chimeras available.")
            return

        print("\nChimera Catalog:")
        for index, chimera in enumerate(ChimeraBuilder.chimeras, start=1):
            print(f"{index}. {chimera.name}")

        print(f"{len(ChimeraBuilder.chimeras) + 1}. Go back")

        try:
            choice = int(input("Enter the number corresponding to the chimera you want to check or go back: "))
            if choice == len(ChimeraBuilder.chimeras) + 1:
                return  # User chooses to go back
            elif 1 <= choice <= len(ChimeraBuilder.chimeras):
                selected_chimera = ChimeraBuilder.chimeras[choice - 1]
                Chimera.display_info(selected_chimera)
                return
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

        

#Chimera interactig method
def interact_with_chimera():
    while True:  # This allows returning to the chimera selection phase
        print("\nSelect a chimera to interact with:")
        for index, chimera in enumerate(ChimeraBuilder.chimeras, start=1):
            print(f"{index}. {chimera.name} (Level: {chimera.level}, Health: {chimera.health})")
        print(f"{len(ChimeraBuilder.chimeras) + 1}. Go back to main menu")  # Back option

        try:
            choice = int(input("Enter the number of the chimera or go back: ")) - 1
            if choice == len(ChimeraBuilder.chimeras):
                return  # Back to main menu
            elif 0 <= choice < len(ChimeraBuilder.chimeras):
                selected_chimera = ChimeraBuilder.chimeras[choice]
            else:
                print("Invalid selection. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        while True:  # Nested loop for actions on selected chimera
            if selected_chimera.health <= 0:  # Check if chimera has died before proceeding
                print(f"{selected_chimera.name} is no longer with us. Returning to selection...")
                break

            print(f"\nSelected Chimera: {selected_chimera.name}")
            print(f"Level: {selected_chimera.level}")
            print(f"Hunger: {selected_chimera.hunger}")
            print(f"Energy: {selected_chimera.energy}")
            print(f"Health: {selected_chimera.health}")
            print(f"Experience: {selected_chimera.experience}/{selected_chimera.experience_to_level_up()}")

            print("\nWhat would you like to do with this chimera?")
            print("1. Feed")
            print("2. Put to sleep")
            print("3. Train")
            print("4. Release")
            print("5. Go back to chimera selection")
            
            action = input("Choose an option (1-5): ")

            if action == '1':
                Inventory.display_food()
                food_amount = int(input(f"Enter the amount of food to feed {selected_chimera.name}: "))
                selected_chimera.feed(food_amount)
                remove_dead_chimeras()
                if selected_chimera.health <= 0:
                    continue
                
            elif action == '2':
                selected_chimera.sleep()
                remove_dead_chimeras()
                if selected_chimera.health <= 0:
                    continue
                
            elif action == '3':
                selected_chimera.train()
                remove_dead_chimeras()
                if selected_chimera.health <= 0:
                    continue
                
            elif action == '4':
                ChimeraBuilder.chimeras.remove(selected_chimera)
                print(f"{selected_chimera.name} has been released.")
                break  # Exit the action loop as chimera is no longer there
            
            elif action == '5':
                break  # Go back to chimera selection
            
            else:
                print("Invalid option selected.")

            if selected_chimera.health > 0:
                selected_chimera.display_condition()  # Display updated info


def breed():
    # Filter chimeras that are eligible for breeding
    eligible_chimeras = [chimera for chimera in ChimeraBuilder.chimeras if chimera.level >= 5]
    if len(eligible_chimeras) < 2:
        print("Not enough chimeras of level 5 or higher to breed.")
        return

    print("\nSelect two chimeras to breed:")
    for index, chimera in enumerate(eligible_chimeras, start=1):
        print(f"{index}. {chimera.name} (Level: {chimera.level}")

    # User selects two chimeras to breed
    try:
        first_choice = int(input("Enter the number for the first chimera: ")) - 1
        second_choice = int(input("Enter the number for the second chimera: ")) - 1

        if first_choice == second_choice:
            print("Cannot breed a chimera with itself. Please select two different chimeras.")
            return

        parent1 = eligible_chimeras[first_choice]
        parent2 = eligible_chimeras[second_choice]
    except (ValueError, IndexError):
        print("Invalid selection. Please select valid numbers from the list.")
        return

    # Creating the offspring
    offspring_head = random.choice([parent1.head, parent2.head])
    offspring_body = random.choice([parent1.body, parent2.body])
    offspring_limbs = random.choice([parent1.limbs, parent2.limbs])
    offspring_wings = random.choice([parent1.wings, parent2.wings])
    offspring_tail = random.choice([parent1.tail, parent2.tail])
    offspring_name = input("Enter a name for the offspring: ")

    # Add the new chimera to the list
    new_chimera = Chimera(offspring_head, offspring_body, offspring_limbs, offspring_wings, offspring_tail, offspring_name, 0, 0, 0, 0, 100)
    ChimeraBuilder.chimeras.append(new_chimera)
    print(f"New chimera {offspring_name} created with Head: {offspring_head}, Body: {offspring_body}, Limbs: {offspring_limbs}, Wings: {offspring_wings}, Tail: {offspring_tail}.")


#Hunting method
def hunt():
    if not ChimeraBuilder.chimeras:
        print("No chimeras available to hunt with.")
        return

    # Selecting a chimera to go hunting
    print("\nSelect a chimera to go hunting with:")
    for index, chimera in enumerate(ChimeraBuilder.chimeras, start=1):
        print(f"{index}. {chimera.name} (Level: {chimera.level}, Health: {chimera.health})")
    print(f"{len(ChimeraBuilder.chimeras) + 1}. Go back to main menu")

    choice = int(input("Choose your chimera or return to main menu: "))
    if choice == len(ChimeraBuilder.chimeras) + 1:
        return  # Return to main menu
    elif 1 <= choice <= len(ChimeraBuilder.chimeras):
        selected_chimera = ChimeraBuilder.chimeras[choice - 1]
    else:
        print("Invalid selection.")
        return
    
    # Initial wild chimera generation
    wild_chimera = generate_wild_chimera()

    while True:
        print(f"\nA wild chimera appears! Level: {wild_chimera.level}")
        print(f"Composition: Head: {wild_chimera.head}, Body: {wild_chimera.body}, Limbs: {wild_chimera.limbs}, Wings: {wild_chimera.wings}, Tail: {wild_chimera.tail}")

        print("\nChoose your action:")
        print("1. Kill")
        print("2. Capture")
        print("3. Run")
        print("4. Return Home")
        action = input("Enter your choice: ")

        if action == '1':
            kill_chimera(selected_chimera, wild_chimera)
            if selected_chimera.health <= 0:
                print(f"{selected_chimera.name} has died.")
                break  # Break loop if chimera dies
            wild_chimera = generate_wild_chimera()  # Generate new wild chimera after action
        elif action == '2':
            capture_chimera(selected_chimera, wild_chimera)
            if selected_chimera.health <= 0:
                print(f"{selected_chimera.name} has died.")
                break  # Break loop if chimera dies
            wild_chimera = generate_wild_chimera()  # Generate new wild chimera after action
        elif action == '3':
            selected_chimera.energy = max(0, selected_chimera.energy - 10)  # Reduce energy by 10 for running
            if selected_chimera.energy > 0:
                wild_chimera = generate_wild_chimera()  # Generate new wild chimera if still has energy
                print(f"Ran away successfully! Energy left: {selected_chimera.energy}")
            else:
                print(f"{selected_chimera.name} is too exhausted to continue.")
                break  # Break loop if no energy left
        elif action == '4':
            return  # Return to main menu
        else:
            print("Invalid option. Please choose again.")

        print(f"After action - Health: {selected_chimera.health}, Energy: {selected_chimera.energy}")



# Generates wild chimeras
def generate_wild_chimera():
    head = random.choice(ChimeraBuilder.headOption)
    body = random.choice(ChimeraBuilder.bodyOption)
    limbs = random.choice(ChimeraBuilder.limbOption)
    wings = random.choice(ChimeraBuilder.wingOption)
    tail = random.choice(ChimeraBuilder.tailOption)
    level = random.randint(1, 10)
    return Chimera(head, body, limbs, wings, tail, "Wild Chimera", level, 10, 10, 0, 10)

#Attacking wild Chimeras
def engage_chimera(selected_chimera, wild_chimera):
    if selected_chimera.level > wild_chimera.level:
        diff = selected_chimera.level - wild_chimera.level
        health_depletion = max(0, 100 - diff * 10)
        selected_chimera.health -= health_depletion
        selected_chimera.energy = max(0, selected_chimera.energy - 20)
        selected_chimera.hunger = max(0, selected_chimera.hunger - 20)
        return True  # Chimera survives
    elif selected_chimera.level == wild_chimera.level:
        if random.random() < 0.5:  # 50% chance for user's chimera to win
            selected_chimera.health = 1  # Set health to 1 if chimera barely wins
            return True  # Chimera survives
        else:
            selected_chimera.health = 0  # Chimera dies if it loses
            return False  # Chimera does not survive
    else:
        selected_chimera.health = 0  # Chimera dies if the wild's level is higher
        return False  # Chimera does not survive

def kill_chimera(selected_chimera, wild_chimera):
    if engage_chimera(selected_chimera, wild_chimera):
        food_collected = 100 * wild_chimera.level
        print(f"{selected_chimera.name} successfully killed the wild chimera, health now {selected_chimera.health}. Collected {food_collected} food.")
        Inventory.add_food(food_collected)
    else:
        print(f"{selected_chimera.name} was defeated by the wild chimera and has died.")

def capture_chimera(selected_chimera, wild_chimera):
    survived = engage_chimera(selected_chimera, wild_chimera)
    if survived and selected_chimera.health > 0:
        # Only prompt for a name if the chimera survived and did not die in the engagement
        print("The wild chimera has been succesfully captured!")
        new_name = input("Enter a name for your new chimera: ")
        wild_chimera.name = new_name
        ChimeraBuilder.chimeras.append(wild_chimera)
        print(f"{new_name} has been added to your list of chimeras.")
    elif not survived:
        print(f"{selected_chimera.name} was defeated by the wild chimera and could not capture it.")
    else:
        print(f"{selected_chimera.name} is too weak to capture the wild chimera.")


#Removes dead chimeras
def remove_dead_chimeras():
        original_count = len(ChimeraBuilder.chimeras)
        ChimeraBuilder.chimeras = [chimera for chimera in ChimeraBuilder.chimeras if not chimera.is_dead()]
        removed_count = original_count - len(ChimeraBuilder.chimeras)
        if removed_count:
            print(f"Removed {removed_count} dead chimeras from the game.")

def main():
    welcome_message()
    chimeras = []
    while True:
        print("")
        Inventory.display_food()
        print("")
        print("\nOptions:")
        print("1. Chimera Catalog")
        print("2. Interact with Chimera")
        print("3. Breed Chimeras")
        print("4. Hunt")
        print("5. How to play")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                check_chimera()
            elif choice == 2:
                if not ChimeraBuilder.chimeras:
                    print("No chimeras available.")
                else:
                    interact_with_chimera()
            elif choice == 3:
                if not ChimeraBuilder.chimeras:
                    print("No chimeras available.")
                else:
                    breed()
            elif choice == 4:
                if not ChimeraBuilder.chimeras:
                    print("No chimeras available.")
                else:
                    hunt()
            elif choice == 5:
                pass
            elif choice == 6:
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid option. Please choose again.")

            remove_dead_chimeras()

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
    

    
