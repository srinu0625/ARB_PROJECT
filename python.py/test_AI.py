import pandas as pd

# Define your file path here
file_path = r"C:\Users\srinu\Downloads\recent download\ES_BIG_DATA_10MIN (1).csv"

try:
    data = pd.read_csv(file_path)
except Exception as e:
    print("Error loading data:", e)
    exit()

# Define column names
high_column_name = 'High'
low_column_name = 'Low'
time_column_name = 'time'

# Initialize variables
temp_high = 0
temp_low = 0
local_high = temp_high
local_low = temp_low
bull = False
bear = False
flag = False
number_of_positions = 0
num_of_trades = 0

for index, row in data.iterrows():
    try:
        # Extracting current and previous values for high and low
        current_time = row[time_column_name]
        current_high = float(row[high_column_name])
        previous_high = float(data.at[index - 1, high_column_name] if index > 0 else 0)
        current_low = float(row[low_column_name])
        previous_low = float(data.at[index - 1, low_column_name] if index > 0 else 0)

        # Update temp_high and temp_low based on conditions
        if current_high > previous_high:
            temp_high = current_high

        if current_low < previous_low:
            temp_low = current_low

        # Update local_low and local_high based on conditions
        if current_high > previous_high:
            local_low = temp_low

        if current_low < previous_low:
            local_high = temp_high

        # Print data with the default terminal color
        print(f"Time: {current_time}")
        print(f"Current High : {current_high}, Previous High : {previous_high}, local_high : {local_high}, temp_high : {temp_high}")
        print(f"Current Low : {current_low}, Previous Low : {previous_low}, local_low : {local_low}, temp_low : {temp_low}")

        # Bullish entry
        if current_high > local_high and not bear and not flag:
            number_of_positions += 1
            print("\033[32m--SNP500 LONG ENTRY-- (CH > LH)\033[0m")
            print(f"\033[32mcurrent_high: {current_high}, local_high: {local_high}\033[0m")
            print(f"\033[32mnumber_of_positions: {number_of_positions}\033[0m")
            bull = True
            flag = True

        # Bullish exit
        elif current_low < local_low and bull and flag:
            number_of_positions -= 1
            num_of_trades += 1
            print("\033[32m--SNP500 LONG EXIT-- (CL < LL)\033[0m")
            print(f"\033[32mcurrent_low: {current_low}, local_low: {local_low}\033[0m")
            print(f"\033[32mnumber_of_positions: {number_of_positions}, num_of_trades: {num_of_trades}\033[0m")
            bull = False
            flag = False

        # Bearish entry
        elif current_low < local_low and not bull and not flag:
            number_of_positions += 1
            print("\033[31m--SNP500 SHORT ENTRY-- (CL < LL)\033[0m")
            print(f"\033[31mcurrent_low: {current_low}, local_low: {local_low}\033[0m")
            print(f"\033[31mnumber_of_positions: {number_of_positions}\033[0m")
            bear = True
            flag = True

        # Bearish exit
        elif current_high > local_high and bear and flag:
            number_of_positions -= 1
            num_of_trades += 1
            print("\033[31m--SNP500 SHORT EXIT-- (CH > LH)\033[0m")
            print(f"\033[31mcurrent_high: {current_high}, local_high: {local_high}\033[0m")
            print(f"\033[31mnumber_of_positions: {number_of_positions}, num_of_trades: {num_of_trades}\033[0m")
            bear = False
            flag = False

    except Exception as e:
        print("Error:", e)

    finally:
        # Resetting text color to default after each iteration
        print("\033[0m-----------------------------End of iteration---------------------------------\033[0m")

print(f"Total number of trades: {num_of_trades}")
