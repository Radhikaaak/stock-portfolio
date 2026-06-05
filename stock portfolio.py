# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "MSFT": 400,
    "AMZN": 170,
    "NIFTY":340,
    "PW":100,
    "SENSEX":350,
    
}

total_value = 0
portfolio_data = []

print("=== Stock Portfolio Tracker ===")

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    stock = input("\nEnter stock name: ").upper()

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_value += investment

    portfolio_data.append(
        f"{stock} | Quantity: {quantity} | Value: ₹{investment}"
    )

print("\n===== Portfolio Summary =====")

for item in portfolio_data:
    print(item)

print("\nTotal Investment Value = ₹", total_value)

# Save report to file
file = open("portfolio_report.txt", "w")

file.write("STOCK PORTFOLIO REPORT\n")
file.write("----------------------\n")

for item in portfolio_data:
    file.write(item + "\n")

file.write(f"\nTotal Investment Value = ₹{total_value}")

file.close()

print("\nReport saved successfully in portfolio_report.txt")
input("\nplease enter to exit......")
