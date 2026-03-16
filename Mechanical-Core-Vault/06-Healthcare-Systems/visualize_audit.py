import pandas as pd
import matplotlib.pyplot as plt

def generate_trend_chart(csv_file):
    # Step 1: Find the line where the actual data starts
    data_start_row = 0
    with open(csv_file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if "Date" in line and "T1 %" in line:
                data_start_row = i
                break
    
    # Step 2: Load the data starting from that row
    df = pd.read_csv(csv_file, skiprows=data_start_row, encoding='utf-8')
    
    # Clean up column names (removes hidden spaces)
    df.columns = df.columns.str.strip()
    
    # Step 3: Plotting
    plt.figure(figsize=(12, 6))
    
    # Oxygen Tank 1 (Blue for Liquid)
    plt.plot(df['Date'], df['T1 %'], label='Tank 1 (Duty) %', color='#0000FF', marker='o', linewidth=2)
    # Oxygen Tank 2 (Green for Standby/Medical)
    plt.plot(df['Date'], df['T2 %'], label='Tank 2 (Standby) %', color='#008000', linestyle='--', marker='s')
    
    # Safety Thresholds (HTM 02-01 Standards)
    plt.axhline(y=40, color='orange', linestyle=':', label='Low Alarm (40%)', linewidth=2)
    plt.axhline(y=20, color='red', linestyle='-', label='Critical Refill (20%)', linewidth=2)
    
    # Formatting the "Boardroom" view
    plt.title(f'MGPS Operational Reliability Trend\n{csv_file}', fontsize=14, fontweight='bold')
    plt.xlabel('Audit Date', fontweight='bold')
    plt.ylabel('Tank Storage Level (%)', fontweight='bold')
    plt.ylim(0, 105) # Keeps the scale consistent
    plt.legend(loc='upper right')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.xticks(rotation=45)
    
    # Step 4: Save & Show
    plt.tight_layout()
    plt.savefig('MGPS_Consumption_Trend.png', dpi=300) # Higher quality for LinkedIn
    print("📈 Success! Chart saved as: MGPS_Consumption_Trend.png")

if __name__ == "__main__":
    try:
        generate_trend_chart('MGPS_Audit_Report.csv')
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Tip: Make sure the CSV file is not open in Excel.")