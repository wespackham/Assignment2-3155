import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Class instances created here
# Including: resources, recipes, an instance of SandwichMaker, and an instance of Cashier
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    # Rens until false
    while True:
        # Takes user input and functionality follows based on input
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")

        if choice == "off":
            # Ends program
            break
        elif choice == "report":
            # Prints data
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounce(s)")
        elif choice in ["small", "medium", "large"]:
            # Initiates sandwich making logic based on size input
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])

if __name__=="__main__":
    main()
