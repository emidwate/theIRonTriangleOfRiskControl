while True:
    capital = float(input("Enter capital: "))
    percentage = float(input("Enter percentage of risk you can afford to lose in one transaction: "))
    firstArmOfTriangle = capital * percentage / 100
    print("Max loss you can afford based on your capital:", firstArmOfTriangle)

    value = input("Buy or Sell: ")

    def calculate_max_shares():
        while True:
            try:
                enter = float(input("Enter the position rate: "))
                takeProfit = float(input("Enter take profit value: "))
                stopLoss = float(input("Enter stop loss value: "))

                if stopLoss >= enter:
                    print("Stop loss must be lower than the entry price. Please try again.")
                    continue

                if takeProfit <= enter:
                    print("Take profit must be greater than the entry price. Please try again.")
                    continue

                lostMoneyPerShare = enter - stopLoss
                earnMoneyPerShare = takeProfit - enter
                riskRatio = earnMoneyPerShare / lostMoneyPerShare

                if lostMoneyPerShare > 0:
                    max_shares = min(int(firstArmOfTriangle // lostMoneyPerShare), int(capital // enter))
                    total_transaction_cost = max_shares * enter
                    return max_shares, riskRatio, earnMoneyPerShare, lostMoneyPerShare, enter, total_transaction_cost

                print("Stop loss should be less than the entry price. Please try again.")

            except ValueError:
                print("One or more inputs are not valid numbers. Please try again.")

    max_shares, risk_ratio, earn_money_per_share, lost_money_per_share, entry_price, total_cost = calculate_max_shares()

    print("The maximum amount of shares to buy:", max_shares)
    print("Profit/Risk ratio:", abs(risk_ratio))
    print("Possible to earn:", abs(max_shares * earn_money_per_share))
    print("Possible to lose:", abs(max_shares * lost_money_per_share))
    print("Total transaction cost:", total_cost)
    remaining_capital = capital - total_cost
    print('Left capital after buying max amount of shares:', remaining_capital)
    
    while True:
        another_transaction = input("Do you want to buy a different number of shares? (yes/no): ")
        if another_transaction.lower() == "yes":
            new_shares = int(input("Enter the new number of shares: "))
            new_total_transaction_cost = new_shares * entry_price
            new_remaining_capital = capital - new_total_transaction_cost

            new_earnings = new_shares * earn_money_per_share
            new_losses = new_shares * lost_money_per_share

            print("Updated results based on new number of shares:")
            print("The new amount of shares to buy:", new_shares)
            print("Total transaction cost:", new_total_transaction_cost)
            print('Left capital after buying the new amount of shares:', new_remaining_capital)
            print("Possible to earn with the new number of shares:", abs(new_earnings))
            print("Possible to lose with the new number of shares:", abs(new_losses))
        if another_transaction.lower() == "no":
            break
    
    repeat = input("Do you want to run the program again? (yes/no): ")
    if repeat.lower() != "yes":
        break

print("Program ended.")
