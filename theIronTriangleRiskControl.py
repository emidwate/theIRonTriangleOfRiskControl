capital = float(input("Enter capital in $/Zl: "))
percentage = float(input("Enter percentage risk, less than 2%: "))
result = capital * percentage / 100

while True:
    value = input("Buy or Sell: ")

    def fun(x):
        while x != "Buy" and x != "buy" and x != "Sell" and x != "sell":
            print("Invalid input. Please enter either 'Buy' or 'Sell'.")
            x = input("Buy or Sell: ")
        if x == "Buy" or x == "buy":
            enter = float(input("Enter the position rate: "))
            takeProfit = float(input("Enter take profit value: "))
            stopLoss = float(input("Enter stop loss value: "))
            score = enter - stopLoss
            devide = (takeProfit - enter) / score
        if x == "Sell" or x == "sell":
            enter = float(input("Enter the position rate: "))
            takeProfit = float(input("Enter take profit value: "))
            stopLoss = float(input("Enter stop loss value: "))
            score = stopLoss - enter
            devide = (enter - takeProfit) / score

        outcome = result // score
        maxPrice = outcome * enter
        print("The maximum amount of shares:", outcome)
        print("The maximum price of transaction in $/Zl:", maxPrice)
        print("Risk ratio:", devide)
        print("Possible to earn:", abs(outcome * (takeProfit - enter)))
        print("Approximately to lost:", result)

    fun(value)
    repeat = input("Do you want to run the program again? (yes/no) ")
    if repeat.lower() != "yes":
        break

print("Program ended.")
