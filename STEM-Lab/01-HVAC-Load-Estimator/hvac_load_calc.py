# ==========================================================
# Project: Mech-Flow HVAC Load Estimator
# Author: Syed Hilaluddin Madany (hilalmadany.com)
# Purpose: STEM Demonstration of Mechanical Logic in Python
# ==========================================================

def calculate_hvac_load():
    print("--- Industrial HVAC Load Estimator ---")
    
    # 1. User Inputs (The 'Techno' part)
    try:
        area = float(input("Enter Room Area (sq. ft): "))
        occupants = int(input("Number of Occupants: "))
        equipment_wattage = float(input("Total Equipment Wattage (Watts): "))
        
        # 2. Engineering Constants (The 'Mechanical' part)
        # Base cooling load: ~20 BTU per sq. ft.
        # Human heat: ~400 BTU per person
        # Equipment heat: Wattage * 3.41
        
        area_load = area * 20
        occupant_load = occupants * 400
        equipment_load = equipment_wattage * 3.41
        
        total_btu = area_load + occupant_load + equipment_load
        tonnage = total_btu / 12000  # 1 Ton = 12,000 BTU/hr
        
        # 3. Output the Result
        print("\n" + "="*30)
        print(f"Total Cooling Required: {total_btu:.2 dream} BTU/hr")
        print(f"Recommended Tonnage: {tonnage:.2f} TR")
        print("="*30)
        print("Note: This is a preliminary estimate based on standard loads.")

    except ValueError:
        print("Error: Please enter valid numerical data.")

if __name__ == "__main__":
    calculate_hvac_load()
