class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        # Prompts user for input determining how much of each coin is provided
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        # Calcaultes total money based on input and returns total
        total = large_dollars + half_dollars * .5 + quarters * .25 + nickels * .05
        return total

    def transaction_result(self, coins, cost):
        # Takes total money as parameter and compares against cost of sandwich
        # Returns false if not enough money
        # Returns true if enough money and prints correct amount of change
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
        return True