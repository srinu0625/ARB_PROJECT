import pandas as pd

file_path = r"D:\SNP_30min_1oct-15marc.csv"

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

# Initialize variables
number_of_positions = 0
num_of_trades = 0
max_profit = float('-inf')
max_loss = float('inf')
TOTAL_P_L = 0
contract_size = 50

# Iterate over each row of the DataFrame
for index, row in data.iterrows():
    try:
        # Extracting current and previous values for high and low
        current_time = row[time_column_name]
        current_high = float(row[high_column_name])
        current_low = float(row[low_column_name])

        # Initialize previous high and low on the first iteration
        if index == 0:
            prev_high = current_high
            prev_low = current_low
            continue

        # bullish candle---------------------------------------------
        if current_high > prev_high:
            if not number_of_positions:
                # Entry condition for long position
                number_of_positions += 1
                entry_price = current_high
                print("\033[32m--SNP500 LONG ENTRY-- (CH > PH)\033[0m", current_time)
                print("number_of_positions :", number_of_positions)
                print("current_high", current_high)
                print("prev_high :", prev_high)
            else:
                # Update previous high
                prev_high = current_high

        # Check for long exit condition
        if current_low < prev_low and number_of_positions:
            # Exit condition for long position
            number_of_positions -= 1
            num_of_trades += 1
            exit_price = current_low
            print("\033[32m--SNP500 LONG EXIT-- (CL < PL)\033[0m", current_time)
            print("current_low", current_low)
            print("prev_low", prev_low)
            print("number_of_positions:", number_of_positions)
            print("number_of_trades:", num_of_trades)

            # Calculate P&L
            pnl = (exit_price - entry_price) * contract_size
            TOTAL_P_L += pnl

            # Update max profit and max loss
            max_profit = max(max_profit, pnl)
            max_loss = min(max_loss, pnl)

            print("P&L for this trade:", pnl)
            print("max_profit:", max_profit)
            print("max_loss:", max_loss)

        # Update previous low
        prev_low = current_low

        # bearish candle---------------------------------------------
        if current_low < prev_low:
            if not number_of_positions:
                # Entry condition for short position
                number_of_positions -= 1
                entry_price = current_low
                print("\033[31m--SNP500 SHORT ENTRY-- (CL < PL)\033[0m", current_time)
                print("number_of_positions :", number_of_positions)
                print("current_low", current_low)
                print("prev_low :", prev_low)
            else:
                # Update previous low
                prev_low = current_low

        # Check for short exit condition
        if current_high > prev_high and number_of_positions < 0:
            # Exit condition for short position
            number_of_positions += 1
            num_of_trades += 1
            exit_price = current_high
            print("\033[31m--SNP500 SHORT EXIT-- (CH > PH)\033[0m", current_time)
            print("current_high", current_high)
            print("prev_high", prev_high)
            print("number_of_positions:", number_of_positions)
            print("number_of_trades:", num_of_trades)

            # Calculate P&L
            pnl = (entry_price - exit_price) * contract_size
            TOTAL_P_L += pnl

            # Update max profit and max loss
            max_profit = max(max_profit, pnl)
            max_loss = min(max_loss, pnl)

            print("P&L for this trade:", pnl)
            print("max_profit:", max_profit)
            print("max_loss:", max_loss)

    except Exception as e:
        print("Error processing row:", e)
    finally:
        print("---------------------------end of iteration--------------------------")

print("max_profit", max_profit)
print("max_loss", max_loss)
print("TOTAL_P_L", TOTAL_P_L)
print("num of trades:", num_of_trades)
