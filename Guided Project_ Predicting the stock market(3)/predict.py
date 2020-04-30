import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('sphist.csv')
data['Date'] = pd.to_datetime(data['Date'])
data['date-after-04-01-2015'] = data['Date'] > datetime(year=2015,month=4,day=1)
data = data.sort_values('Date',ascending=True)
# print(data.head())

# Average price for past five days
mean_5_day = data['Close'].rolling(center=False,window=5).mean()
mean_5_day = mean_5_day.shift(1)
data['5 Day Average'] = mean_5_day

# Average price for past thirty days
mean_30_day = data['Close'].rolling(center=False,window=30).mean()
mean_30_day = mean_30_day.shift(1)
data['30 Day Average'] = mean_30_day

# Average price for past 365 days
mean_365_day = data['Close'].rolling(center=False,window=365).mean()
mean_365_day = mean_365_day.shift(1)
data['365 Day Average'] = mean_365_day

# Ratio between Average 5 day price and average 365 day price
data['Ratio of 5 day to 365 day price'] = mean_5_day / mean_365_day

# Standard deviation of 5 day price
std_5_day = data['Close'].rolling(center=False,window=5).std()
std_5_day = std_5_day.shift(1)
data['5 Day Standard deviation'] = std_5_day

# Standard deviation of 365 day price
std_365_day = data['Close'].rolling(center=False,window=365).std()
std_365_day = std_5_day.shift(1)
data['365 Day Standard deviation'] = std_365_day

# Ratio of between Standard Deviation of 5 day price and 365 day price
data['Ratio of 5 day standard deviation to 365 day standard deviation'] = std_5_day / std_365_day

# Average volume over last 5 days
avg_vol_5_day = data['Volume'].rolling(center=False,window=5).mean()
avg_vol_5_day = avg_vol_5_day.shift(1)
data['Average 5 day volume'] = avg_vol_5_day

# Average volume over last 365 days
avg_vol_365_day = data['Volume'].rolling(center=False,window=365).mean()
avg_vol_365_day = avg_vol_365_day.shift(1)
data['Average 365 day volume'] = avg_vol_365_day

# print(data.head(20))
data = data[data['Date'] >= datetime(year=1951,month=1,day=3)]
data = data.dropna(axis=0)

# Generate the training and testing dataframes
train = data[data['Date'] < datetime(year=2013,month=1,day=1)]
test = data[data['Date'] >= datetime(year=2013,month=1,day=1)]

# Generating linear regression model
features = ['5 Day Average','365 Day Average','Ratio of 5 day to 365 day price','5 Day Standard deviation','Ratio of 5 day standard deviation to 365 day standard deviation','Average 5 day volume','Average 365 day volume']

target = 'Close'
lr = LinearRegression()
lr.fit(train[features],train[target])
predictions = lr.predict(test[features])

# Calculate mean aboslute error
mae = mean_absolute_error(test['Close'],predictions)
print(mae)

