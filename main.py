# main.py
from pet import Pet

def main():
    # Create a pet object
    my_pet = Pet("Bold")

    # Test methods
    my_pet.get_status()
    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.get_status()

    # Test bonus features
    my_pet.train("Dance")
    my_pet.train("Order")
    my_pet.train("Roll over")
    my_pet.train("Sit")
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
