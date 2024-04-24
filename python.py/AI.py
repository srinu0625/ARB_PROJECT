import pandas as pd
import time

file_path = r"D:\nq daily.csv"

# Load the data
try:
    data = pd.read_csv(file_path)
except Exception as e:
    print("Error loading data:", e)
    exit()

# Print column names to verify
print("Column names:", data.columns)
print("Column names:", data.columns[1])
print("1st row", data.iloc[0].tolist())

# Assuming the column names for high and low are 'High' and 'Low'
high_column_name = 'High'
low_column_name = 'Low'
time_column_name = 'Date (GMT)'

# local high and local low 
local_high = 0
local_low = 0

# flag 
flag = False

# num of positions 
number_of_positions = 0

# num of trades
num_of_trades = 0

# P&L calculation
entry_price = 0
exit_price = 0
contract_size = 20

# defining tick size
tick_val = 0.25

# maxloss maxprofit
max_loss = float('inf')
max_profit = float('-inf')

# total p&l
TOTAL_P_L = 0

# total long and short pnl
total_long_pnl = 0
total_short_pnl = 0
positive_pnl = 0
negative_pnl = 0
risk = 5000
max_num_lots = 5

# Iterate over each row of the DataFrame
for index, row in data.iterrows():
    # adding a check point to not process the black or nan values in excel
    if pd.notna(row[time_column_name]) and pd.notna(row[high_column_name]) and pd.notna(row[low_column_name]):
        try:
            # Extracting current and previous values for high and low
            current_time = row[time_column_name]
            current_high = float(row[high_column_name])
            previous_high = float(data.at[index - 1, high_column_name])
            current_low = float(row[low_column_name])
            previous_low = float(data.at[index - 1, low_column_name])

            # Case 1: Update local high and low
            if current_high > previous_high:
                local_high = current_high
            if current_low < previous_low:
                local_low = current_low

            # Printing data
            print("Time:", current_time)
            print("Current High:", current_high, "Previous High:", previous_high, "Local High:", local_high)
            print("Current Low:", current_low, "Previous Low:", previous_low, "Local Low:", local_low)

            # Bullish candle
            max_loss_for_trade = (local_high - local_low) * contract_size
            if current_high > local_high and local_high != 0 and local_low != 0 and not flag:
                if max_loss_for_trade > risk:
                    print("\033[93m Max loss exceeds RISK. Skipping trade.\033[0m")
                    continue  # Skip this trade
                num_of_lots = min(risk / max_loss_for_trade, max_num_lots)
                if num_of_lots >= 5:
                    num_of_trades += 1
                entry_price = local_high + (tick_val * 2)
                print("\033[32m--SNP500 LONG ENTRY-- (CH > LH)\033[0m")
                print("Entry Price:", entry_price)
                print("Number of Lots:", num_of_lots)
                flag = True

            if current_low < local_low and flag:
                number_of_positions -= 1
                exit_price = local_low - (tick_val * 2)
                print("\033[32m--SNP500 LONG EXIT-- (CL < LL)\033[0m")
                print("Exit Price:", exit_price)
                print("Number of Positions:", number_of_positions)
                print("Number of Trades:", num_of_trades)
                flag = False

                # Calculate P&L
                pnl = (exit_price - entry_price) * num_of_lots * contract_size
                TOTAL_P_L += pnl
                total_long_pnl += pnl
                integer_pnl = float(pnl)

                # Update max loss and max profit
                max_profit = max(max_profit, pnl)
                max_loss = min(max_loss, pnl)

                # Add to total positive or negative P&L based on the result
                if pnl >= 0:
                    positive_pnl += pnl
                else:
                    negative_pnl += pnl

                print("P&L for this trade:", round(integer_pnl, 2))
                print("Max Profit:", round(max_profit, 2))
                print("Max Loss:", round(max_loss, 2))
                print("Number of Lots:", round(num_of_lots))
                continue

        except Exception as e:
            print("Error:", e)

        finally:
            print("-----------------------------End of iteration---------------------------------")

# Print summary
max_loss_color = "\033[31m" if max_loss < 0 else "\033[32m"
max_profit_color = "\033[31m" if max_profit < 0 else "\033[32m"
positive_pnl_color = "\033[31m" if positive_pnl < 0 else "\033[32m"
negative_pnl_color = "\033[31m" if negative_pnl < 0 else "\033[32m"
total_long_pnl_color = "\033[31m" if total_long_pnl < 0 else "\033[32m"
total_short_pnl_color = "\033[31m" if total_short_pnl < 0 else "\033[32m"
TOTAL_P_L_colour = "\033[31m" if TOTAL_P_L < 0 else "\033[32m"

print("Max Profit:", max_profit_color, round(max_profit, 2), "\033[0m")
print("Max Loss:", max_loss_color, round(max_loss, 2), "\033[0m")
print("Positive P&L:", positive_pnl_color, round(positive_pnl, 2), "\033[0m")
print("Negative P&L:", negative_pnl_color, round(negative_pnl, 2), "\033[0m")
print("Total Long P&L:", total_long_pnl_color, round(total_long_pnl, 2), "\033[0m")
print("Total Short P&L:", total_short_pnl_color, round(total_short_pnl, 2), "\033[0m")
print("Total P&L:", TOTAL_P_L_colour, round(TOTAL_P_L, 2), "\033[0m")
print("Number of Trades:", num_of_trades)
