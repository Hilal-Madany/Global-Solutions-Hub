import streamlit as st
import math
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Universal Filter SME Tool", page_icon="⚙️", layout="wide")

# --- CUSTOM CSS FOR INDUSTRIAL UI ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e0e0e0; }
    .sme-header { background: linear-gradient(90deg, #004e92 0%, #000428 100%); padding: 25px; border-radius: 15px; color: white; text-align: center; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("""
    <div class="sme-header">
        <h1>📜 Universal Pleated Element Design Tool</h1>
        <p>Industrial & EPC Consultant | 14+ Yrs Experience | #AskAndWeSolve</p>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR: ENGINEERING INPUTS ---
st.sidebar.header("🛠️ 1. Geometry Specs")
u_unit = st.sidebar.radio("Unit System", ["Metric (mm)", "Imperial (inch)"])
u_label = "mm" if u_unit == "Metric (mm)" else "in"

od = st.sidebar.number_input(f"Outer Diameter ({u_label})", value=100.0 if u_unit == "Metric (mm)" else 4.0)
length = st.sidebar.number_input(f"Element Length ({u_label})", value=500.0 if u_unit == "Metric (mm)" else 20.0)

st.sidebar.header("🧩 2. Pleat Configuration")
n_pleats = st.sidebar.number_input("Total Pleat Count", value=65)
p_depth = st.sidebar.slider(f"Pleat Depth ({u_label})", 5.0, 50.0, 15.0)

st.sidebar.header("🌊 3. Process Fluid")
fluid = st.sidebar.selectbox("Select Medium", ["Water (High Flux)", "Fuel/Diesel (Medium Flux)", "Lube Oil (Low Flux)", "Gas/Air (High Velocity)"])

# SME Flux Mapping (m3/h/m2)
flux_map = {"Water (High Flux)": 15.0, "Fuel/Diesel (Medium Flux)": 8.0, "Lube Oil (Low Flux)": 3.0, "Gas/Air (High Velocity)": 25.0}
design_flux = flux_map[fluid]

# --- CALCULATION ENGINE (Standardized to m2) ---
# Conversion to mm for math consistency
conv = 25.4 if u_unit == "Imperial (inch)" else 1.0
od_mm = od * conv
len_mm = length * conv
depth_mm = p_depth * conv

# Formulas
area_mm2 = n_pleats * 2 * depth_mm * len_mm
area_m2 = area_mm2 / 1_000_000
area_sqft = area_m2 * 10.764
capacity_m3h = area_m2 * design_flux
circumference = math.pi * od_mm
pitch = circumference / n_pleats if n_pleats > 0 else 0

# --- MAIN DASHBOARD DISPLAY ---
st.subheader("📊 Performance Analytics")
c1, c2, c3, c4 = st.columns(4)

c1.metric("Effective Area", f"{area_m2:.3f} m²" if u_unit == "Metric (mm)" else f"{area_sqft:.2f} ft²")
c2.metric("Flow Capacity", f"{capacity_m3h:.2f} m³/hr")
c3.metric("Pleat Pitch", f"{pitch:.2f} mm")
c4.metric("Design Flux", f"{design_flux} LMH")



# --- SME VALIDATION & FEASIBILITY ---
st.divider()
st.markdown("### 🛠️ SME Manufacturing Compliance")

status = "APPROVED"
remarks = "Design parameters are within standard manufacturing tolerances."

if pitch < 1.8:
    status = "REJECTED"
    remarks = f"Pleat pitch ({pitch:.2f}mm) is below 1.8mm. Element will blind quickly and backwash will be ineffective."
    st.error(f"❌ **{status}**: {remarks}")
elif depth_mm > (od_mm * 0.35):
    status = "CAUTION"
    remarks = "Pleat depth is too high relative to OD. Potential for internal core collapse or pleat bunching."
    st.warning(f"⚠️ **{status}**: {remarks}")
else:
    st.success(f"✅ **{status}**: {remarks}")

# --- COMPREHENSIVE TECHNICAL REPORT ---
report = f"""--------------------------------------------------
INDUSTRIAL FILTER TECHNICAL DATA SHEET
--------------------------------------------------
Generated: {datetime.now().strftime('%d-%b-%Y %H:%M')}
SME Consultant: Syed Hilaluddin Madany
--------------------------------------------------
EQUIPMENT SPECS:
- OD: {od} {u_label}
- Length: {length} {u_label}
- Pleat Count: {n_pleats}
- Pleat Depth: {p_depth} {u_label}

CALCULATED PERFORMANCE:
- Total Surface Area: {area_m2:.4f} m2 ({area_sqft:.2f} sqft)
- Fluid Type: {fluid}
- Design Flux: {design_flux} m3/h/m2
- Rated Capacity: {capacity_m3h:.2f} m3/hr
- Mechanical Pitch: {pitch:.2f} mm

VALIDATION STATUS: {status}
REMARKS: {remarks}
--------------------------------------------------
Note: This report is generated based on 14+ years of
Industrial EPC standards. #AskAndWeSolve
--------------------------------------------------
"""

with st.expander("📝 View Full Technical Audit"):
    st.code(report)

st.download_button("📥 Download PDF Report (Text)", data=report, file_name=f"Filter_SME_Report_{od}x{length}.txt")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Industrial Consultant | #NoToRacism | Python-Enabled Engineering</p>", unsafe_allow_html=True)
