# Initialize variables outside of the loops
current_high1 = 0
local_high1 = 0
local_low1 = 0
local_high2 = 0

# Iterate over each row of the daily DataFrame (data1)
for index1, row1 in data1.iterrows():
    # Check if the row has valid data
    if pd.notna(row1[time_column_name]) and pd.notna(row1[high_column_name]) and pd.notna(row1[low_column_name]):
        # Extract the current date from the daily data
        current_date1 = row1[time_column_name].split()[0]

        # Iterate over each row of the hourly DataFrame (data2)
        for index2, row2 in data2.iterrows():
            # Check if the row has valid data
            if pd.notna(row2[time_column_name]) and pd.notna(row2[high_column_name]) and pd.notna(row2[low_column_name]):
                # Extract the current date from the hourly data
                current_date2 = row2[time_column_name].split()[0]

                # If the hourly data date matches the daily data date
                if current_date2 == current_date1:
                    # Update values for high and low from data1
                    current_high1 = float(row1[high_column_name])
                    current_low1 = float(row1[low_column_name])

                    # Update values for high and low from data2
                    current_high2 = float(row2[high_column_name])
                    current_low2 = float(row2[low_column_name])

                    # Rest of your code here
