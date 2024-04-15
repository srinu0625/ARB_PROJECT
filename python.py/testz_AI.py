def print_colored(text, value):
    if value >= 0:
        print(text + "\x1b[32m" + str(value) + "\x1b[0m")  # Green color
    else:
        print(text + "\x1b[31m" + str(value) + "\x1b[0m")  # Red color

# Example usage:
max_profit = 100
max_loss = -50
TOTAL_P_L = 75
num_of_trades = 20
positive_pnl = 200
negative_pnl = -100
total_long_pnl = 150
total_short_pnl = -75

print_colored("        max_profit:", max_profit)
print_colored("          max_loss:", max_loss)
print_colored("         TOTAL_P_L:", TOTAL_P_L)
print_colored("     num of trades:", num_of_trades)
print_colored("total_positive_pnl: ", positive_pnl)
print_colored("total_negative_pnl: ", negative_pnl)
print_colored("   total_long_pnl :", total_long_pnl)
print_colored("  total_short_pnl :", total_short_pnl)
