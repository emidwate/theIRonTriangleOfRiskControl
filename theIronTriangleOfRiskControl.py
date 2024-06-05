while True:
    try:
        capital = float(input("Enter capital: "))
        percentage = float(input("Enter percentage of risk you can afford to lose in one transaction: "))
        first_arm_of_triangle = capital * percentage / 100
    except ValueError:
        print("Please enter a number")
        continue

    while True:
        transaction_type = input("Buy or Sell: ")

        if transaction_type.lower() not in ["buy", "sell"]:
            print("Please enter either buy or sell")
            continue
        else:
            def calculate_max_shares():
                while True:
                    try:
                        enry_price = float(input("Enter the position rate: "))
                        if enry_price > capital:
                            print("You can not buy shares that are greater than your capital")
                            continue

                        take_profit = float(input("Enter take profit value: "))
                        stop_loss = float(input("Enter stop loss value: "))

                        if transaction_type.lower() == 'buy':
                            if stop_loss >= enry_price:
                                print("Stop loss must be lower than the entry price. Please try again.")
                                continue

                            elif take_profit <= enry_price:
                                print("Take profit must be greater than the entry price. Please try again.")
                                continue
                        else:
                            if stop_loss <= enry_price:
                                print("Stop loss must be higher than the entry price. Please try again.")
                                continue

                            elif take_profit >= enry_price:
                                print("Take profit must be lower than the entry price. Please try again.")
                                continue

                        lost_money_per_share = abs(enry_price - stop_loss)
                        earn_money_per_share = abs(take_profit - enry_price)
                        risk_ratio = earn_money_per_share / lost_money_per_share

                        max_shares = int(first_arm_of_triangle // lost_money_per_share)
                        max_total_transaction_cost = max_shares * enry_price

                        return max_shares, risk_ratio, earn_money_per_share, lost_money_per_share, enry_price, max_total_transaction_cost

                    except ValueError:
                        print("One or more inputs are not valid numbers. Please try again.")

            max_shares, risk_ratio, earn_money_per_share, lost_money_per_share, entry_price, max_total_transaction_cost = calculate_max_shares()

            print("Max loss you can afford based on your capital:", first_arm_of_triangle)
            print("The maximum amount of shares to buy:", max_shares)
            print("Profit/Risk ratio:", abs(risk_ratio))
            print("Possible to earn:", abs(max_shares * earn_money_per_share))
            print("Possible to lose:", abs(max_shares * lost_money_per_share))
            print("Total transaction cost:", max_total_transaction_cost)

            remaining_capital = capital - max_total_transaction_cost

            print('Left capital after buying max amount of shares:', remaining_capital)

        while True:
            another_transaction = input("Do you want to buy a different number of shares? (yes/no): ")

            if another_transaction.lower() not in ['yes', 'no']:
                print("Please enter either yes or no")

            elif another_transaction.lower() == 'yes':
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
            else:
                break
        break

    repeat = input("Do you want to run the program again? (yes/no): ")

    if repeat.lower() != "yes":
        break

print("Program ended.")