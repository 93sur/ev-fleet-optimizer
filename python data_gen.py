import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Настройки
np.random.seed(42)
vehicles = ['EV_001', 'EV_002', 'EV_003', 'EV_004', 'EV_005']
days = 7
data = []

start_date = datetime(2026, 4, 1)

for day in range(days):
    current_day = start_date + timedelta(days=day)
    
    # Имитируем цены на электричество в Германии (цены выше днем, ниже ночью)
    # В среднем от 0.20 до 0.45 EUR за кВтч
    hourly_prices = [0.30 + 0.10 * np.sin(np.pi * (h - 6) / 12) for h in range(24)]
    
    for v_id in vehicles:
        # Машина приезжает вечером (между 17:00 и 20:00)
        arrival_h = np.random.randint(17, 21)
        arrival = current_day.replace(hour=arrival_h, minute=np.random.randint(0, 59))
        
        # Машина уезжает утром (между 06:00 и 09:00 следующего дня)
        departure = arrival + timedelta(hours=np.random.randint(10, 14))
        
        # Состояние заряда (SOC)
        soc_start = np.random.randint(10, 40) # Приехала разряженной
        soc_target = 90 # Нужно зарядить до 90%
        battery_capacity = 77 # кВтч (например, как у VW ID.4)
        
        energy_needed = (soc_target - soc_start) / 100 * battery_capacity
        
        data.append({
            'vehicle_id': v_id,
            'arrival': arrival,
            'departure': departure,
            'energy_needed_kwh': round(energy_needed, 2),
            'avg_price_at_arrival': round(hourly_prices[arrival_h], 3)
        })

df = pd.DataFrame(data)
print(df.head())
# Сохраним для следующих этапов
df.to_csv('fleet_data.csv', index=False)