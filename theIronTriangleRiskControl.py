capital = float(input("Enter capital: "))
percentage = float(input("Enter percentage of risk you can afford to loose in one transaction: "))
firstArmOfTriangle = capital * percentage / 100
print("Max lost you can afford which is the percentage you pasted above based on your capital:", firstArmOfTriangle)

while True:
    value = input("Buy or Sell: ")

    def fun(x):
        while x != "Buy" and x != "buy" and x != "Sell" and x != "sell":
            print("Invalid input. Please enter either 'Buy' or 'Sell'.")
            x = input("Buy or Sell: ")
        if x == "Buy" or x == "buy":
            while True:
                try:
                    enter = float(input("Enter the position rate: "))
                    takeProfit = float(input("Enter take profit value: "))
                    stopLoss = float(input("Enter stop loss value: "))
        
                    lostMoneyPerShare = enter - stopLoss
                    earnMoneyPerShare = takeProfit - enter
                    riskRatio = earnMoneyPerShare / lostMoneyPerShare
        
                    break

                except ValueError:
                    print("One or more inputs are not valid numbers. Please try again.")
        if x == "Sell" or x == "sell":
            while True:
                try:
                    enter = float(input("Enter the position rate: "))
                    takeProfit = float(input("Enter take profit value: "))
                    stopLoss = float(input("Enter stop loss value: "))

                    lostMoneyPerShare = stopLoss - enter
                    earnMoneyPerShare = takeProfit - enter
                    riskRatio = earnMoneyPerShare / lostMoneyPerShare
                    
                    break

                except ValueError:
                    print("One or more inputs are not valid numbers. Please try again.")
        secondArmOfTriangle = int(firstArmOfTriangle // lostMoneyPerShare)

        if secondArmOfTriangle == 0:
            print("You cannot afford any shares with the given parameters")
        else:

          print("The maximum amount of shares:", secondArmOfTriangle)
          print("The maximum price of transaction in $/Zl:", secondArmOfTriangle * enter)
          print("Profit/Risk ratio:", abs(riskRatio))
          print("Possible to earn:", abs(secondArmOfTriangle * (takeProfit - enter)))
          print("Possible to lose:", abs(secondArmOfTriangle * (enter - stopLoss)))
          print('Left capital after buying max amount of shares:', capital - (secondArmOfTriangle * enter))

    fun(value)
    repeat = input("Do you want to run the program again? (yes/no): ")
    if repeat.lower() != "yes":
        break

print("Program ended.")