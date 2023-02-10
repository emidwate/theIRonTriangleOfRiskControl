repeat_count = int(input("How many times do you want to pass the price? "))

prices = []

for i in range(repeat_count):
    price = float(input("Enter the price: "))
    prices.append(price)

average_price = sum(prices) / len(prices)

print("The average market noise is", average_price)