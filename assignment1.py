def calculate_surcharge(ship_mode):
    if ship_mode == "Same Day":
        surcharge = 0.2
    elif ship_mode == "First Class":
        surcharge = 0.1
    elif ship_mode == "Standard Class":
        surcharge = 0.05
    else:
        surcharge = 0
    return surcharge

def calculate_total_cost(ship_mode, sales, profit):
    surcharge = calculate_surcharge(ship_mode)
    total_cost = (sales - profit) * (1 + surcharge)
    return total_cost

def main():
    ship_mode = input("Enter the ship mode (Same Day/First Class/Standard Class): ")
    sales = float(input("Enter the total sales amount: "))
    profit = float(input("Enter the profit amount: "))

    total_cost = calculate_total_cost(ship_mode, sales, profit)
    print("Total Cost:", total_cost)

if __name__ == "__main__":
    main()
