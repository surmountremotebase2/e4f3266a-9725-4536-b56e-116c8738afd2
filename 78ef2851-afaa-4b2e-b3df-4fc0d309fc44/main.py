import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample price data
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', end='2024-02-27')
prices = np.random.normal(loc=100, scale=5, size=len(dates))
df = pd.DataFrame({'Date': dates, 'Price': prices})
df.set_index('Date', inplace=True)

# Define function to generate moving averages
def moving_average(data, window_size):
    return data.rolling(window=window_size).mean()

# Calculate short-term (fast) and long-term (slow) moving averages
short_window = 20
long_window = 50
df['Short_MA'] = moving_average(df['Price'], short_window)
df['Long_MA'] = moving_average(df['Price'], long_window)

# Generate buy/sell signals based on crossover
df['Signal'] = 0
df['Signal'][short_window:] = np.where(df['Short_MA'][short_window:] > df['Long_MA'][short_window:], 1, 0)
df['Position'] = df['Signal'].diff()

# Plotting
plt.figure(figsize=(12,6))
plt.plot(df['Price'], label='Price')
plt.plot(df['Short_MA'], label=f'Short MA ({short_window} days)')
plt.plot(df['Long_MA'], label=f'Long MA ({long_window} days)')
plt.plot(df[df['Position'] == 1].index, df['Short_MA'][df['Position'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
plt.plot(df[df['Position'] == -1].index, df['Short_MA'][df['Position'] == -1], 'v', markersize=10, color='r', lw=0, label='Sell Signal')
plt.title('Moving Average Crossover Strategy')
plt.legend()
plt.show()