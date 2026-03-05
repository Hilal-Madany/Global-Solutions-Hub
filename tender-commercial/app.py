import streamlit as st
import os
from jinja2 import Environment, FileSystemLoader
import datetime

# --- PATH CONFIG ---
current_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(current_dir, 'templates')

# --- JINJA ENVIRONMENT ---
# This looks for 'full_report.html' inside the 'templates' folder
env = Environment(loader=FileSystemLoader(template_path))

# ... (Previous segments for data entry remain the same) ...

# --- FINAL SEGMENT: PREVIEW & PRINT ---
if st.session_state.step == 7:
    st.header("7. Final Review & Official Report")
    
    # Calculate Final Score
    score = 0
    if st.session_state.data.get('iso9001') == "Yes": score += 25
    if st.session_state.data.get('inhouse_test') == "Yes": score += 25
    if st.session_state.data.get('q_manual') == "Yes": score += 25
    if st.session_state.data.get('safety') == "Yes": score += 25
    st.session_state.data['score'] = score

    # RENDER THE REPORT
    try:
        template = env.get_template('full_report.html')
        report_html = template.render(
            d=st.session_state.data, 
            date=datetime.date.today().strftime("%d/%m/%Y")
        )
        
        # Display the report on screen
        st.markdown("### Report Preview")
        st.divider()
        
        # This renders your "Perfect Format" HTML inside the app
        st.components.v1.html(report_html, height=800, scrolling=True)
        
        st.info("💡 **To Print:** Right-click the report above and select 'Print', or use 'Ctrl + P' in your browser.")
        
    except Exception as e:
        st.error(f"Template Error: Ensure 'full_report.html' is inside the 'templates' folder. Error: {e}")
