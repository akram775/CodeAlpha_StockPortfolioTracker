
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOG": 170,
    "AMZN": 200
}

print("Welcome to Stock Portfolio Tracker!")

print("\nAvailable Stocks:")

for stock in stock_prices:
    print(stock, ":", "$", stock_prices[stock])
    
stock_name = input("\nEnter stock name: ").upper()

if stock_name in stock_prices:

    quantity = int(input("Enter quantity: "))

    total = stock_prices[stock_name] * quantity

    print("\nStock Name:", stock_name)
    print("Price per share: $", stock_prices[stock_name])
    print("Quantity:", quantity)
    print("Total Investment: $", total)

else:
    print("Stock not available!")
    
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOG": 170,
    "AMZN": 200
}

print("Welcome to Stock Portfolio Tracker!")

print("\nAvailable Stocks:")

for stock in stock_prices:
    print(stock, ":", "$", stock_prices[stock])

portfolio = []
total_investment = 0

stock_name = input("\nEnter stock name: ").upper()

if stock_name in stock_prices:

    quantity = int(input("Enter quantity: "))

    total = stock_prices[stock_name] * quantity

    portfolio.append({
        "name": stock_name,
        "quantity": quantity,
        "total": total
    })

    total_investment += total

    print("\nStock Name:", stock_name)
    print("Quantity:", quantity)
    print("Total:", total)

else:
    print("Stock not available!")

print("\nTotal Investment: $", total_investment)

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOG": 170,
    "AMZN": 200
}

print("Welcome to Stock Portfolio Tracker!")

print("\nAvailable Stocks:")

for stock in stock_prices:
    print(stock, ":", "$", stock_prices[stock])

portfolio = []
total_investment = 0

while True:

    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

        total = stock_prices[stock_name] * quantity

        portfolio.append({
            "name": stock_name,
            "quantity": quantity,
            "total": total
        })

        total_investment += total

        print("Stock added successfully!")
        print("Stock Total: $", total)

    else:
        print("Stock not available!")

print("\n----- YOUR PORTFOLIO -----")

for item in portfolio:
    print(item["name"], "| Quantity:", item["quantity"],
          "| Total: $", item["total"])

print("\nTotal Investment: $", total_investment)


with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("----------------------\n\n")

    for item in portfolio:
        file.write("Stock: " + item["name"] + "\n")
        file.write("Quantity: " + str(item["quantity"]) + "\n")
        file.write("Investment: $" + str(item["total"]) + "\n\n")

    file.write("Total Investment: $" + str(total_investment))

print("\nPortfolio saved successfully!")

