import pandas as pd
import numpy as np
# Load the electricity dataset
data = pd.read_csv("data/electricity_data.csv")
# Calculate the estimated cost for each room
data["Estimated_Cost"] = (
    data["Units_kWh"] * data["Rate_per_kWh"]
)
# Calculate total electricity usage and cost
total_units = np.sum(data["Units_kWh"])
total_cost = np.sum(data["Estimated_Cost"])
# Display the results
print("ELECTRICITY CONSUMPTION ANALYZER")
print(f"Total electricity used: {total_units} kWh")
print(f"Total estimated cost: Rs. {total_cost}")
print("\nAverage monthly usage by room:")
room_average = data.groupby("Room")["Units_kWh"].mean()
print(room_average)
# Find the month with the highest electricity usage
monthly_usage = data.groupby("Month")["Units_kWh"].sum()
highest_month = monthly_usage.idxmax()
highest_usage = monthly_usage.max()
print("\nHighest Electricity Usage")
print(f"Month: {highest_month}")
print(f"Electricity used: {highest_usage} kWh")
# Find the room with the highest total electricity usage
room_usage = data.groupby("Room")["Units_kWh"].sum()
highest_room = room_usage.idxmax()
highest_room_usage = room_usage.max()
print("\nHighest Electricity Usage by Room")
print(f"Room: {highest_room}")
print(f"Total usage: {highest_room_usage} kWh")
# Calculate each room's percentage of total usage
room_percentage = (room_usage / total_units) * 100
print("\nElectricity Usage by Room (%)")
for room, percentage in room_percentage.items():
    print(f"{room}: {percentage:.2f}%")
    # Flag unusually high electricity usage
usage_threshold = 120
high_usage = data[data["Units_kWh"] > usage_threshold]
print("\nUnusually High Electricity Usage")
if high_usage.empty:
    print("No unusually high usage found.")
else:
    print(high_usage[["Month", "Room", "Units_kWh"]].to_string(index=False))
    # Estimate savings from reducing electricity usage by 10%
reduction_percentage = 10
possible_savings_units = total_units * reduction_percentage / 100
possible_savings_cost = total_cost * reduction_percentage / 100
print("\nEstimated Savings Plan")
print(f"Usage reduction target: {reduction_percentage}%")
print(f"Possible electricity savings: {possible_savings_units:.1f} kWh")
print(f"Possible cost savings: Rs. {possible_savings_cost:.2f}")
# Give simple electricity-saving suggestions
print("\nElectricity Conservation Suggestions")
if highest_room == "Living Room":
    print("- Switch off lights and fans when not needed.")
    print("- Avoid leaving televisions and other devices on standby.")
if highest_usage > 250:
    print("- Review electricity usage during the highest-consumption month.")
print("- Use energy-efficient LED bulbs.")
print("- Run appliances only when needed.")
print("- Compare monthly usage to track improvements.")

# Calculate month-to-month change in electricity usage
monthly_change = monthly_usage.sort_index().pct_change() * 100
print("\nMonthly Electricity Usage Change")
for month, change in monthly_change.items():
    if pd.isna(change):
        print(f"{month}: No previous month for comparison")
    else:
        print(f"{month}: {change:+.2f}%")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Create a chart of monthly electricity usage
monthly_usage = monthly_usage.sort_index()
plt.figure(figsize=(8, 5))
plt.plot(
    monthly_usage.index,
    monthly_usage.values,
    marker="o"
)
plt.title("Monthly Electricity Consumption")
plt.xlabel("Month")
plt.ylabel("Electricity Used (kWh)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_consumption.png")
plt.show()
