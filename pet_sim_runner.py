import pet_simulator as ps
import time


def main():
    pet_simulator()


def pet_simulator():
    print("🐾Welcome to the Virtual Pet Simulator!🐾")
    print("")
    time.sleep(1)
    pet_name = input("Enter a name for your pet: ")
    time.sleep(1)
    print("")
    print("Choose a pet type:")
    print("1. Dog 🐶")
    print("2. Cat 🐱")
    print("3. Dragon 🐉")
    pet_type = input("Enter your choice (1/2/3): ")
    time.sleep(1)
    print("")
    if pet_type == "1":
        pet = ps.Dog(50, 50, 50, pet_name)
    elif pet_type == "2":
        pet = ps.Cat(50, 50, 50, pet_name)
    elif pet_type == "3":
        pet = ps.Dragon(50, 50, 50, pet_name)

    pet.show_status()
    print("")
    actions()
    action = input("Enter your choice (1/2/3/4/5): ")
    while action != 5:
        time.sleep(1)
        print("")
        if action == "1":
            ps.Pet.feed(pet)
            pet.show_status()
            print("")
        elif action == "2":
            ps.Pet.play(pet)
            pet.show_status()
            print("")
        elif action == "3":
            ps.Pet.sleep(pet)
            pet.show_status()
            print("")
        elif action == "4":
            if pet_type == "1":
                ps.Dog.special_ability(pet)
                pet.show_status()
            elif pet_type == "2":
                ps.Cat.special_ability(pet)
                pet.show_status()
            elif pet_type == "3":
                ps.Dragon.special_ability(pet)
                pet.show_status()
            print("")
        elif action == "5":
            print("Goodbye! Thanks for playing! 🐾")
            exit()
            break
        action = input("Enter your choice (1/2/3/4/5): ")


def actions():
    print("What would you like to do? ")
    print("1. Feed 🍖")
    print("2. Play 🎾")
    print("3. Sleep 😴")
    print("4. Use Special Ability 💥")
    print("5. Exit❌")


if __name__ == "__main__":
    main()
