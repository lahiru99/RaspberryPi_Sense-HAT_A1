import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Connect to the database
conn = sqlite3.connect('../TaskA/data.db')
cursor = conn.cursor()

# Fetch data for line plot
cursor.execute("SELECT timestamp, temperature, humidity FROM th_data")
data = cursor.fetchall()

timestamps = [entry[0] for entry in data]
temperatures = [entry[1] for entry in data]
humidities = [entry[2] for entry in data]

# Line Plot
plt.figure(figsize=(14, 7))
plt.plot(timestamps, temperatures, label="Temperature", color='red')
plt.plot(timestamps, humidities, label="Humidity", color='blue')

# Displaying the actual temperature and humidity values on the graph
for i, (time, temp, humid) in enumerate(data):
    if i % (len(timestamps) // 10) == 0:  # to avoid overcrowding, only display every 10th value (or adjust as needed)
        plt.text(time, temp, f"{temp:.2f}", ha='left', va='bottom', color='red')
        plt.text(time, humid, f"{humid:.2f}", ha='left', va='top', color='blue')

plt.xlabel("Timestamp")
plt.ylabel("Values")
plt.title("Temperature and Humidity over Time")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../TaskB/temperature_humidity_lineplot.png')

# Fetch data for bar plots
cursor.execute("SELECT temperature_category, COUNT(*) FROM th_data GROUP BY temperature_category")
temp_data = cursor.fetchall()

cursor.execute("SELECT humidity_category, COUNT(*) FROM th_data GROUP BY humidity_category")
humidity_data = cursor.fetchall()

temp_categories = [item[0] for item in temp_data]
temp_counts = [item[1] for item in temp_data]
humidity_categories = [item[0] for item in humidity_data]
humidity_counts = [item[1] for item in humidity_data]

print("Temperature Data:", temp_data)
print("Humidity Data:", humidity_data)


# Plotting Temperature Categories
if temp_categories and temp_counts:
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    bars = sns.barplot(x=temp_categories, y=temp_counts)
    plt.xlabel("Temperature Categories")
    plt.ylabel("Count")
    plt.title("Distribution of Temperature Categories")

    # Displaying the actual count above each bar
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2. - 0.2,
                 bar.get_height() + 0.5,
                 int(bar.get_height()),
                 ha='center',
                 color='black')
    
    plt.tight_layout()
    plt.savefig('../TaskB/temperature_barplot.png')


# Bar Plot for humidity categories using Matplotlib
plt.figure(figsize=(10, 6))
bars = plt.bar(humidity_categories, humidity_counts, color='cyan')
plt.xlabel("Humidity Categories")
plt.ylabel("Count")
plt.title("Distribution of Humidity Categories")

# Displaying the actual count above each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', color='black')
    
plt.tight_layout()
plt.savefig('../TaskB/humidity_barplot.png')


conn.close()
