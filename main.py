import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
months = np.array([
    "Jan", "Jan", "Jan",
    "Feb", "Feb", "Feb",
    "Mar", "Mar", "Mar",
    "Apr", "Apr", "Apr",
    "May", "May", "May",
    "Jun", "Jun", "Jun"
])
rooms = np.array(["Living Room", "Bedroom", "Kitchen"] * 6)
units = np.array([
    85, 65, 45,
    95, 70, 48,
    125, 78, 52,
    110, 75, 50,
    145, 90, 60,
    160, 95, 65
])
data = pd.DataFrame({
    "Month": months,
    "Room": rooms,
    "Units": units
})
data["Cost"] = data["Units"] * 7
def analyze(data):
    total = np.sum(data["Units"])
    cost = np.sum(data["Cost"])
    print("\nELECTRICITY CONSUMPTION ANALYZER")
    print("Total units:", total, "kWh")
    print("Estimated cost: Rs.", cost)
    print("Average usage:", round(np.mean(data["Units"]), 2), "kWh")
    monthly = data.groupby("Month", sort=False)["Units"].sum()
    print("\nMonthly usage:\n", monthly)
    highest = monthly.max()
    print("\nHighest usage month:", list(monthly[monthly == highest].index))
    print("Highest consumption:", highest, "kWh")
    print("\nMonthly percentage change:")
    print((monthly.pct_change() * 100).round(2))
    room_usage = data.groupby("Room")["Units"].sum()
    print("\nRoom-wise usage:\n", room_usage)
    print("\nRoom contribution (%):")
    print((room_usage / total * 100).round(2))
    high = data[data["Units"] > 120]
    print("\nHigh consumption records:")
    if high.empty:
        print("No unusually high consumption found.")
    else:
        print(high[["Month", "Room", "Units"]].to_string(index=False))
    saved = room_usage["Living Room"] * 0.10
    print("\nSavings from a 10% reduction:")
    print("Units saved:", round(saved, 2), "kWh")
    print("Estimated cost saved: Rs.", round(saved * 7, 2))
    print("\nElectricity-saving suggestions:")
    print("- Switch off unused lights and fans.")
    print("- Use energy-efficient LED bulbs.")
    print("- Reduce unnecessary appliance use.")
    print("- Monitor rooms with high consumption.")
    monthly.plot(kind="bar", title="Monthly Electricity Consumption")
    plt.xlabel("Month")
    plt.ylabel("Units (kWh)")
    plt.tight_layout()
    plt.savefig("monthly_consumption.png")
    plt.show()
analyze(data)