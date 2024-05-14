import pandas as pd
import datetime

file_path = r"D:\surya sir.csv"

# Load the data
try:
    data = pd.read_csv(file_path)
except Exception as e:
    print("Error loading data:", e)
    exit()

# Assuming the column names
Date_Time_ = 'DateTime'
Price_name = 'Price'
Volume_name = 'Volume'
ExchTime_name = 'ExchTime'

# Initialize variables
current_minute = None
avg_trade_price = 0
total_volume = 0
num_of_lines = 0
Date_Time = 0
curr_high = float('-inf')
curr_low = float('inf')
curr_close = 0
timeSlot = 15  # Assuming time slot is 15 minutes

# Iterate over each row of the DataFrame
for index, row in data.iterrows():
    try:
        # Extracting values
        Price = row[Price_name]
        Volume = row[Volume_name]
        ExchTime = row[ExchTime_name]
        Date_Time = row[Date_Time_]

        # Split ExchTime into hours, minutes, and seconds
        hour, minute, second = map(int, ExchTime.split('.'))

        # Initialize tm_struct as datetime object
        tm_struct = datetime.datetime.now()

        # Check if it's a new minute
        if minute != current_minute:
            # Print candlestick for the previous minute
            if current_minute is not None:
                print("Time:", tm_struct)
                print("Open:", curr_open)
                print("High:", curr_high)
                print("Low:", curr_low)
                print("Close:", curr_close)
                print('----------------------------')

            # Reset variables for the new minute
            current_minute = minute
            curr_open = Price
            curr_high = Price
            curr_low = Price
            curr_close = Price
            total_volume = 0

        # Update high and low prices
        if Price > curr_high:
            curr_high = Price
        if Price < curr_low:
            curr_low = Price

        # Check if it's the end of a candlestick interval
        if tm_struct.minute % timeSlot == 0 and tm_struct.minute != minute:
            curr_close = Price
            tm_struct = datetime.datetime.now()

        # Calculate average trade price for the previous minute
        if current_minute is not None:
            if total_volume != 0:
                avg_trade_price = total_trade_value / total_volume
                avg_trade_price_rounded = round(avg_trade_price, 2)
                print(f"Avg_trade_price : {current_minute}: {avg_trade_price_rounded}")
                print('----------------------------')
            else:
                print(f"No trades occurred in minute {current_minute}")

            if avg_trade_price > curr_high:
                curr_high = avg_trade_price
                print("curr_high :", curr_high)
            if avg_trade_price < curr_low:
                curr_low = avg_trade_price
                print("curr_Low :", curr_low)

            if tm_struct.minute % timeSlot == 0:
                curr_close = avg_trade_price
                print("curr_close :", curr_close)

            # Reset variables for the new minute
            tm_struct = datetime.datetime.now()
            total_trade_value = 0
            total_volume = 0

        # Accumulate trade value and volume
        total_trade_value += Price * Volume
        total_volume += Volume

    except Exception as e:
        print("Error:", e)
