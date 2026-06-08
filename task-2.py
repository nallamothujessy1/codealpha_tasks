# task-2 : Stock Portfolio Tracker
# Portfolio = The information you want to keep.
# CSV file = The notebook/file where you store that information.

# Hardcoded stock prices
# dictionary using to stored stock:prices like "key:value"
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# input/output to know how many stocks user wants to invest
n = int(input("\nHow many different stocks do you own? "))

portfolio = {}

for i in range(n):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
        total_investment += stock_prices[stock_name] * quantity
    else:
        print("Stock not available in tracker.")

print("\n----- Portfolio Summary -----")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock} | Quantity: {quantity} | Value: ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Save result to a text file
# file handling 

with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-----------------\n")
    
    # basic arithmetic operation
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock} | Quantity: {quantity} | Value: ${value}\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

    print("\nPortfolio saved successfully in 'portfolio.txt'")
