from turtle import position
import pandas as pd
import time

file_path = r"C:\Users\srinu\Downloads\recent download\ES_BIG_DATA_10MIN (1).csv"

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
time_column_name = 'time'
# temp column names
temp_high = 0
temp_low = 0
# local column names
local_high = temp_high
local_low = temp_low

bull = False
bear = False
flag = False

# num of positions 
number_of_positions=0

# num of trades
num_of_trades=0

# max_loss and max_profit
max_loss=0
max_profit=0

# Iterate over each row of the DataFrame
for index, row in data.iterrows():
    try:
        # Extracting current and previous values for high and low
        current_time = row[time_column_name]
        current_high = float(row[high_column_name])
        previous_high = float(data.at[index - 1, high_column_name] if index > 0 else 0)
        current_low = float(row[low_column_name])
        previous_low = float(data.at[index - 1, low_column_name] if index > 0 else 0)

         # case 1------------------------------------------------------------------------------------
        if current_high > previous_high:
            temp_high = current_high
            print("if one ","TH :",temp_high,"CH :",current_high)

        if current_low < previous_low:
            temp_low = current_low
        # case 2------------------------------------------------------------------------------------
        if current_high > previous_high:
            local_low = temp_low

        if current_low < previous_low:
            local_high = temp_high

        # Printing data
        print("Time:", current_time)
        print("Current High :", current_high, "Previous High :", previous_high, "local_high :", local_high
              , "temp_high :", temp_high)
        print("Current Low :", current_low, "Previous Low :", previous_low, "local_low :", local_low
              , "temp_low :", temp_low)
    

        # bullish candle---------------------------------------------------------------------------
        if current_high > local_high and not bear and not flag:
            number_of_positions +=1
            print("\033[32m--SNP500 LONG ENTRY-- (CH > LH)\033[0m") # ANSI escape codes for this color coding to work
            print("current_high : ",current_high),print("local_high : ",local_high)
            print("number_of_positions : ",number_of_positions)
            bull = True
            flag = True
            continue

        if current_low < local_low and bull and flag:
            number_of_positions -=1
            num_of_trades+=1
            print("\033[32m--SNP500 LONG EXIT-- (CL < LL)\033[0m") # ANSI escape codes for this color coding to work
            print("current_low :",current_low),print("local_low :",local_low)
            print("number_of_positions : ",number_of_positions),print("num_of_trades = ",num_of_trades)
            bull = False
            flag = False
            continue

        # bearish candle-------------------------------------------------------------------------
        if current_low < local_low and not bull and not flag:
            number_of_positions +=1
            print("\033[31m--SNP500 SHORT ENTRY-- (CL < LL)\033[0m") # ANSI escape codes for this color coding to work
            print("current_low :",current_low)
            print("local_low :",local_low),print("number_of_positions : ",number_of_positions)
            bear = True
            flag = True
            continue

        if current_high > local_high and bear and flag:
            number_of_positions -=1
            num_of_trades +=1
            print("\033[31m--SNP500 SHORT EXIT-- (CH > LH)\033[0m") #  ANSI escape codes for this color coding to work 
            print("current_high :",current_high), print("local_high :",local_high),
            print("number_of_positions : ",number_of_positions),print("num_of_trades = ",num_of_trades)
            bear = False
            flag = False
            continue
    
    except Exception as e:
        print("Error:", e)

    finally:
        print("-----------------------------End of iteration---------------------------------")

print(num_of_trades)

