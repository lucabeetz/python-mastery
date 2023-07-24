def portfolio_cost(filename: str) -> float:
    with open(filename) as f:
        total_cost = 0
        for line in f:
            parts = line.split()
            try:
                num_shares = int(parts[1])
                price = float(parts[2])
                total_cost += num_shares * price
            except ValueError as e:
                print(f"Couldn't parse: {line.strip()}\nReason: {e}")
    return total_cost


print(portfolio_cost("Data/portfolio3.dat"))
