# pip install pandas numpy scikit-learn yfinance

# This code does the following:
# Downloads historical stock price data for the given symbol and date range using Yahoo Finance.
# Preprocesses the data by adding date-related features such as year, month, day, and weekday.
# Splits the data into training and testing sets.
# Trains a simple linear regression model on the training data.
# Makes predictions on the testing data and calculates the Root Mean Squared Error (RMSE) as a measure of model performance.
# Plots the actual vs. predicted stock prices to visualize the model's performance.
# (c) Manikandan 2017

import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Define the stock symbol and date range for historical data
symbol = "AAPL"  # Example: Apple Inc.
start_date = "2010-01-01"
end_date = "2021-12-31"

# Download historical stock data from Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

# Prepare the data for predictive analytics
data['Date'] = data.index
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day
data['Weekday'] = data['Date'].dt.weekday

# Create a feature matrix (X) and target variable (y)
X = data[['Year', 'Month', 'Day', 'Weekday']]
y = data['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate the Root Mean Squared Error (RMSE) as a measure of model performance
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error (RMSE): {rmse}")

# Plot actual vs. predicted stock prices
plt.figure(figsize=(12, 6))
plt.plot(data.index[-len(y_test):], y_test, label="Actual Price")
plt.plot(data.index[-len(y_test):], y_pred, label="Predicted Price")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title(f"{symbol} Stock Price Prediction")
plt.legend()
plt.show()

