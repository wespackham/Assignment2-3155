
class SandwichMaker:
    # Constructor takes resources to keep track of ingredient list
    def __init__(self, resources):
        self.machine_resources = resources

    # Checks resources to ensure enough ingredients for sandwich
    def check_resources(self, ingredients):
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    # Subtracts appropriate amount of resources based on sandwich size
    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")