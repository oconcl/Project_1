import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv('results.csv')

# ensure the Date colume is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# set the Data column as the index
df.set_index('Date', inplace=True)

# display the first 5 rows
print(df.head())

# calculate the average volume
average_volume = df['volume'].mean()
print(f"The average volume is: {average_volume}")

# find the day with the highest volume
max_volume_day = df[df['volume'] == df['volume'].max()]
print(f"The day with the highest volume is: {max_volume_day.index[0]} with a volume of {max_volume_day['volume'].iloc[0]}")

# find the day with the lowest volume
min_volume_day = df[df['volume'] == df['volume'].min()]
print(f"The day with the lowest volume is: {min_volume_day.index[0]} with a volume of {min_volume_day['volume'].iloc[0]}")

# yearly volume summary
yearly_volume = df.resample('YE')['volume'].sum()
print("Yearly Volume Summary:")
print(yearly_volume)


# Plotting the trading volume
plt.figure(figsize=(14, 7))
plt.plot(df.index, df['volume'], label='Daily Trading Volume', color='blue')
plt.title('Tesla (TSLA) Daily Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.show()

# Yearly Volume Plot
plt.figure(figsize=(10, 5))
yearly_volume.plot(kind='bar')
plt.title('Tesla (TSLA) Yearly Trading Volume Summary')
plt.xlabel('Year')
plt.ylabel('Total Volume')
plt.xticks(rotation=45)
plt.show()


# Calculate the 30-day average and standard deviation of the volume\
df['30d_avg_volume'] = df['volume'].rolling(window=30).mean()
df['30d_std_volume'] = df['volume'].rolling(window=30).std()
df['volume_spike'] = df['volume'] > (df['30d_avg_volume'] + 2 * df['30d_std_volume'])

# Filter days with volume spikes
volume_spikes_df = df[df['volume_spike']]

df['daily_price_change_pct'] = df['close'].pct_change() * 100

# Average price change on days with volume spikes
avg_price_change_on_spikes = df[df['volume_spike']]['daily_price_change_pct'].mean()

# Average price change on all days
avg_price_change_all_days = df['daily_price_change_pct'].mean()

print(f"Average price change on days with volume spikes: {avg_price_change_on_spikes}%")
print(f"Average price change on all days: {avg_price_change_all_days}%")


# Plot daily volume and highlight volume spikes
plt.figure(figsize=(14,7))
plt.bar(df.index, df['volume'], color='lightgray', label='Daily Volume')
plt.bar(volume_spikes_df.index, volume_spikes_df['volume'], color='red', label='Volume Spike')

# Plot daily price change percentage on a secondary axis
plt.twinx()
plt.plot(df.index, df['daily_price_change_pct'], color='blue', label='Daily Price Change %', alpha=0.5)

plt.title('Volume Spikes and Daily Price Changes for Tesla (TSLA)')
plt.legend(loc='upper left')
plt.show()
