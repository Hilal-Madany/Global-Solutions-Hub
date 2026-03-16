# MGPS Reliability Tools
# Developed by: Syed Hilaluddin Madany

def oxygen_reserve_hours(tank_liters, level_pct, flow_lpm):
    """Calculates hours of oxygen left in a VIE tank."""
    gas_m3 = (tank_liters * (level_pct / 100) * 860) / 1000
    total_liters_gas = gas_m3 * 1000
    hours_left = total_liters_gas / (flow_lpm * 60)
    return round(hours_left, 1)

def dew_point_alert(temp):
    """Safety check for Medical Air quality."""
    if temp > -40:
        return "⚠️ ALARM: High Moisture detected! Bypass to Standby Dryer."
    return "✅ System Dry."

# Example: 10k Liter tank at 40% with 250LPM demand
print(f"O2 Remaining: {oxygen_reserve_hours(10000, 40, 250)} Hours")
