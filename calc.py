import pandas as pd
import os

def calculate_savings(row):
    prices = {h: (0.40 if 17 <= h <= 21 else 0.22) for h in range(24)}
    arrival_h = row["arrival"].hour
    duration = int((row["departure"] - row["arrival"]).total_seconds() // 3600)

    # Dumb
    dumb_cost = row["energy_needed_kwh"] * prices[arrival_h]
    # Smart
    smart_cost = row["energy_needed_kwh"] * 0.22 # simplest version

    return pd.Series([dumb_cost, smart_cost])

if os.path.exists("fleet_data.csv"):
    df = pd.read_csv("fleet_data.csv", parse_dates=["arrival", "departure"])
    df[["dumb_cost_eur", "smart_cost_eur"]] = df.apply(calculate_savings, axis=1)
    df["savings_eur"] = df["dumb_cost_eur"] - df["smart_cost_eur"]
    df.to_csv("fleet_data_optimized.csv", index=False)
    print("--- DONE! File created! ---")
else:
    print("--- ERROR: fleet_data.csv not found! ---")