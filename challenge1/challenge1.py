class MoneyBox:
    def __init__(self, capacity):
        # Your code here
        if isinstance(capacity, int):
            self.capacity = capacity
            self.coins = 0
        else:
            print("Error: Please input capacity (integer)")

    def can_add(self, v):
        # True, if you can add v coins, False otherwise
        # Your code here
        return (self.coins + v <= self.capacity) 

    def add(self, v):
        # put v coins to moneybox
        # Your code here
        if self.can_add(v):
            self.coins += v
        else:
            print("Error: Not enough capacity")

# Test Sample
if __name__ == "__main__":

    #initialization
    print("\ninitialization:")
    myMoneyBox = MoneyBox(50)
    print(myMoneyBox.coins)

    #can_add
    print("\ncan_add:")
    print(myMoneyBox.can_add(10))
    print(myMoneyBox.can_add(100))

    #add
    print("\nadd:")
    print(myMoneyBox.coins)
    myMoneyBox.add(10)
    print(myMoneyBox.coins)

    #add (error)
    print("\nadd (error):")
    print(myMoneyBox.coins)
    myMoneyBox.add(100)
    print(myMoneyBox.coins)