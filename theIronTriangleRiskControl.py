# first arm
capital = float(input("Enter capital in $/Zl: "))
percentage = float(input("Enter percentage risk, less then 2%: "))
result = capital * percentage / 100
print(result, "$/Zl")

# second arm
value = input("Buy or Sell: ")


def fun(x):
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

    # third arm
    outcome = result // score
    maxPrice = outcome * enter
    print("The maximum amount of shares:", outcome)
    print("The maximum price of transaction in $/Zl:", maxPrice)
    print("Risk ratio:", devide)


fun(value)
