capital = float(input("Enter capital in $/Zl: "))
percentage = float(input("Enter percentage risk, less than 2%: "))
result = capital * percentage / 100
print("Max lost you can afford which is the percentage you pasted according to the method:", result)

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

        maxShares = int(capital // enter)
        outcome = int(result // score)
        maxOutcome = min(outcome, maxShares)

        if maxOutcome == 0:
            print("You cannot afford any shares with the given parameters")
        else:
            print("The maximum amount of shares:", maxOutcome)
            print("The maximum price of transaction in $/Zl:", maxOutcome * enter)
            print("Risk ratio:", devide)
            print("Possible to earn:", abs(maxOutcome * (takeProfit - enter)))
            print("Possible to lose:", abs(maxOutcome * (enter - stopLoss)))
            print('Left capital after buying max:', capital - (maxOutcome * enter))

    fun(value)
    repeat = input("Do you want to run the program again? (yes/no) ")
    if repeat.lower() != "yes":
        break

print("Program ended.")
