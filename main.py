import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("data/electricity_data.csv")
data["Estimated_Cost"] = data["Units_kWh"] * data["Rate_per_kWh"]
total_units = np.sum(data["Units_kWh"])
total_cost = np.sum(data["Estimated_Cost"])
print("\nELECTRICITY CONSUMPTION ANALYZER")
print("Total electricity used:", round(total_units, 2), "kWh")
print("Total estimated cost: Rs.", round(total_cost, 2))
print("\nAverage Usage by Room:")
print(data.groupby("Room")["Units_kWh"].mean().round(2))
monthly_usage = data.groupby("Month")["Units_kWh"].sum()
highest_month = monthly_usage.idxmax()
print("\nHighest Usage Month:", highest_month)
print("Usage:", round(monthly_usage.max(), 2), "kWh")
room_usage = data.groupby("Room")["Units_kWh"].sum()
highest_room = room_usage.idxmax()
print("\nHighest Usage Room:", highest_room)
print("Usage:", round(room_usage.max(), 2), "kWh")
print("\nRoom-wise Usage Percentage:")
for room, units in room_usage.items():
    percentage = (units / total_units) * 100 if total_units else 0
    print(room, ":", round(percentage, 2), "%")
print("\nUnusually High Usage (over 120 kWh):")
high_usage = data[data["Units_kWh"] > 120]
if high_usage.empty:
    print("No unusually high usage found.")
else:
    print(high_usage[["Month", "Room", "Units_kWh"]].to_string(index=False))
savings_units = total_units * 0.10
savings_cost = total_cost * 0.10
print("\nEstimated Savings from a 10% Reduction:")
print("Electricity saved:", round(savings_units, 2), "kWh")
print("Estimated cost saved: Rs.", round(savings_cost, 2))
print("\nElectricity Saving Suggestions:")
print("- Switch off lights and fans when not in use.")
print("- Use energy-efficient LED bulbs.")
print("- Avoid leaving appliances on unnecessarily.")
print("- Monitor rooms with high electricity consumption.")
print("\nMonthly Usage Changes (%):")
print((monthly_usage.pct_change() * 100).round(2))
monthly_usage.plot(
    kind="bar",
    title="Monthly Electricity Consumption",
    ylabel="Electricity Used (kWh)",
    xlabel="Month"
)
plt.tight_layout()
plt.savefig("monthly_consumption.png")
plt.show()
