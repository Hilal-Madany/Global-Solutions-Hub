import streamlit as st
import pdfkit
from jinja2 import Environment, FileSystemLoader
import datetime
import os

# --- PATH CONFIGURATION ---
current_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(current_dir, 'templates')

st.set_page_config(page_title="PSU Vendor Assessment", layout="wide")

# Initialize Session States
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

st.title("🏛️ Comprehensive Vendor Assessment Portal")
st.write(f"**Step {st.session_state.step} of 7: {['','General Info', 'Statutory Details', 'Organisational Soundness', 'Technical & Manufacturing', 'Quality Systems', 'Financials', 'Final Review'][st.session_state.step]}**")
st.progress(st.session_state.step / 7)

# --- STEP 1: GENERAL INFO ---
if st.session_state.step == 1:
    st.header("1. General Identification")
    st.session_state.data['name'] = st.text_input("Name of Supplier/Sub-Vendor", st.session_state.data.get('name', ''))
    st.session_state.data['reg_office'] = st.text_area("Registered Office", st.session_state.data.get('reg_office', ''))
    st.session_state.data['works_addr'] = st.text_area("Factory / Works Address", st.session_state.data.get('works_addr', ''))
    col1, col2 = st.columns(2)
    st.session_state.data['tel'] = col1.text_input("Telephone/Mobile", st.session_state.data.get('tel', ''))
    st.session_state.data['email'] = col2.text_input("Email ID", st.session_state.data.get('email', ''))
    st.button("Save & Next ➡️", on_click=next_step)

# --- STEP 2: STATUTORY DETAILS ---
elif st.session_state.step == 2:
    st.header("2. Registration Details")
    c1, c2 = st.columns(2)
    st.session_state.data['pan'] = c1.text_input("PAN/TAN NO.", st.session_state.data.get('pan', ''))
    st.session_state.data['gst'] = c2.text_input("GST / TIN NO.", st.session_state.data.get('gst', ''))
    st.session_state.data['msme_type'] = st.selectbox("Category of Industry", ["Micro", "Small", "Medium", "Large"], index=0)
    st.session_state.data['msme_no'] = st.text_input("Registration No. & Validity", st.session_state.data.get('msme_no', ''))
    
    colb, coln = st.columns(2)
    colb.button("⬅️ Back", on_click=prev_step)
    coln.button("Save & Next ➡️", on_click=next_step)

# --- STEP 3: ORGANISATIONAL ---
elif st.session_state.step == 3:
    st.header("3. Organisational Soundness")
    st.session_state.data['commence_year'] = st.text_input("Year of Commencement of Business", st.session_state.data.get('commence_year', ''))
    st.session_state.data['area'] = st.number_input("Total Covered Area (Sq. m.)", value=st.session_state.data.get('area', 0))
    st.session_state.data['power'] = st.text_input("Connected Load (kVA)", st.session_state.data.get('power', ''))
    
    st.subheader("Manpower Details")
    m1, m2, m3 = st.columns(3)
    st.session_state.data['grad_staff'] = m1.number_input("Graduate Engineers", value=st.session_state.data.get('grad_staff', 0))
    st.session_state.data['diploma_staff'] = m2.number_input("Diploma Holders", value=st.session_state.data.get('diploma_staff', 0))
    st.session_state.data['skilled_workers'] = m3.number_input("Skilled Workers", value=st.session_state.data.get('skilled_workers', 0))

    colb, coln = st.columns(2)
    colb.button("⬅️ Back", on_click=prev_step)
    coln.button("Save & Next ➡️", on_click=next_step)

# --- STEP 4: TECHNICAL ---
elif st.session_state.step == 4:
    st.header("4. Technical & Manufacturing")
    st.session_state.data['inhouse_test'] = st.radio("In-house Testing Facilities?", ["Yes", "No"], index=0)
    st.session_state.data['machinery'] = st.text_area("List of Major Machinery (Description/Capacity/Make)", st.session_state.data.get('machinery', ''))
    st.session_state.data['outsourced'] = st.text_input("If outsourced, provide details", st.session_state.data.get('outsourced', ''))
    
    colb, coln = st.columns(2)
    colb.button("⬅️ Back", on_click=prev_step)
    coln.button("Save & Next ➡️", on_click=next_step)

# --- STEP 5: QUALITY ---
elif st.session_state.step == 5:
    st.header("5. Quality System (# Scoreable)")
    st.session_state.data['iso9001'] = st.selectbox("ISO 9001 Certified?", ["Yes", "No"])
    st.session_state.data['iso14000'] = st.selectbox("ISO 14000 Certified?", ["Yes", "No"])
    st.session_state.data['q_manual'] = st.radio("Do you have written QC Manual?", ["Yes", "No"])
    st.session_state.data['traceability'] = st.radio("System for Traceability?", ["Yes", "No"])
    st.session_state.data['safety'] = st.radio("Safety measures available?", ["Yes", "No"])

    colb, coln = st.columns(2)
    colb.button("⬅️ Back", on_click=prev_step)
    coln.button("Save & Next ➡️", on_click=next_step)

# --- STEP 6: FINANCIALS ---
elif st.session_state.step == 6:
    st.header("6. Financial Soundness")
    f1, f2, f3 = st.columns(3)
    st.session_state.data['turnover_1'] = f1.number_input("Turnover Year 1 (Cr)", value=st.session_state.data.get('turnover_1', 0.0))
    st.session_state.data['turnover_2'] = f2.number_input("Turnover Year 2 (Cr)", value=st.session_state.data.get('turnover_2', 0.0))
    st.session_state.data['turnover_3'] = f3.number_input("Turnover Year 3 (Cr)", value=st.session_state.data.get('turnover_3', 0.0))
    st.session_state.data['networth'] = st.number_input("Current Net Worth (Cr)", value=st.session_state.data.get('networth', 0.0))

    colb, coln = st.columns(2)
    colb.button("⬅️ Back", on_click=prev_step)
    coln.button("Save & Next ➡️", on_click=next_step)

# --- STEP 7: FINAL REVIEW & PDF ---
elif st.session_state.step == 7:
    st.header("7. Final Review & Report Generation")
    st.write("Review all details below. If correct, generate the Assessment Form.")
    st.json(st.session_state.data)
    
    # CALCULATE COMPLIANCE SCORE
    score = 0
    if st.session_state.data.get('iso9001') == "Yes": score += 20
    if st.session_state.data.get('inhouse_test') == "Yes": score += 20
    if st.session_state.data.get('q_manual') == "Yes": score += 20
    if st.session_state.data.get('traceability') == "Yes": score += 20
    if st.session_state.data.get('turnover_3', 0) > 0: score += 20
    st.session_state.data['score'] = score

    colb, coln = st.columns(2)
    colb.button("⬅️ Edit Details", on_click=prev_step)
    
    if coln.button("📄 Generate Complete PDF Report"):
        try:
            env = Environment(loader=FileSystemLoader(template_path))
            template = env.get_template('full_report.html')
            html_out = template.render(d=st.session_state.data, date=datetime.date.today().strftime("%d/%m/%Y"))
            pdf = pdfkit.from_string(html_out, False)
            st.download_button("📥 Download Final Assessment", data=pdf, file_name="PSU_Vendor_Assessment.pdf", mime="application/pdf")
            st.success("Report Ready!")
        except Exception as e:
            st.error(f"Error: {e}")
