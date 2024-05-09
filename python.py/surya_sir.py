from tokenize import String
import pandas as pd

file_path = r"C:\Users\srinu\Desktop\TimeAndSalesGCcv1-20190101-20240426.csv.gz"

# Load the data
try:
    data = pd.read_csv(file_path)
except Exception as e:
    print("Error loading data:", e)
    exit()

# Assuming the column names for high and low are 'High' and 'Low'
Alias_name = 'Alias_Underlying_RIC'
Domain_name = 'Domain_name'
Date_Time_ = 'Date-Time'
GMTOffset_name = 'GMTOffset'
Type_name = 'Type'
Price_name = 'Price'
Volume_name = 'Volume'
BidPrice_price = 'BidPrice'
BidSize_price = 'BidSize'
AskPrice_price = 'AskPrice'
AskSize_price = 'AskSize'
ExchTime_price = 'ExchTime'

 # Iterate over each row of the DataFrame
for index, row in data.iterrows():
    # adding a check point  to not process the balck or nan values in excel
        try:
            # Extracting current and previous values for high and low
            Alias_Underlying_RIC = row[Alias_Underlying_RIC]
            Domain = String(row[Domain])
            Date_Time = row[Date_Time]
            GMTOffset = row[GMTOffset]
            Type = String(row[Type])
            Price = row[Price]
            Volume = row[Volume]
            BidPrice = row[BidPrice]
            BidSize = row[BidSize]
            AskPrice = row[AskPrice]
            AskSize = row[AskSize]
            ExchTime = row[ExchTime]

            print("Time:", Date_Time)
            print('Alias_Underlying_RIC:',Alias_Underlying_RIC,'Domain:',Domain,'GMTOffset_name:',GMTOffset_name,'Type:',Type,
            'Price:',Price,'Volume:',Volume,'BidPrice:',BidPrice,'BidSize:',BidSize,'AskPrice:',AskPrice,'AskSize:',AskPrice,
            'ExchTime:',ExchTime)
            print('-----------------------------------------------------------------------------------------------------------------')
          
        except Exception as e:
                print("Error:", e)
        finally:
                print("-----------------------------------End of iteration-------------------------------------")