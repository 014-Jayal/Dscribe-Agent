# streamlit_app.py

import streamlit as st
import json
from tools.patient_loader import load_patient_folder
from agents.discharge_agent import initialize_state, run_agent

# Page Config: Clean and professional
st.set_page_config(
    page_title="Agentic Discharge Summary",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    try:
        with open("assets/style.css", "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass # Fails silently if CSS is missing, using default styles

load_css()

# Header Section
st.markdown("""
<div class="dashboard-header">
    <div class="dashboard-title">Agentic Clinical Summary</div>
    <div class="dashboard-subtitle">Automated, evidence-grounded discharge summarization with strict safety guardrails and medication reconciliation.</div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### Process Control")
    patient_folder = st.text_input("Patient Data Directory", "patient_data")
    run_agent_button = st.button("Initialize Agent Loop", type="primary", use_container_width=True)
    
    st.markdown("---")
    st.markdown("### System Guardrails")
    st.markdown("- **Fabrication:** Disabled")
    st.markdown("- **Conflict Detection:** Active")
    st.markdown("- **Source Grounding:** Enforced")

# Main Execution
if run_agent_button:
    with st.spinner("Executing ReAct Agent Loop..."):
        # Load and process
        pages = load_patient_folder(patient_folder)
        state = initialize_state(patient_id="patient_1", pages=pages)
        state = run_agent(state)
        
        # Extract variables from state
        summary = state.get("extracted_data", {})
        trace = state.get("trace_log", [])
        clinical = summary.get("clinical_summary", {})
        review_flags = summary.get("review_flags", [])
        
        # Calculate KPI Metrics
        source_count = sum(len(v.get("sources", [])) for v in clinical.values() if isinstance(v, dict))
        confidences = [v.get("confidence", 0) for v in clinical.values() if isinstance(v, dict) and v.get("confidence", 0) > 0]
        avg_confidence = round(sum(confidences) / len(confidences) * 100, 1) if confidences else 0

        # Render KPIs
        col1, col2, col3, col4 = st.columns(4)
        
        kpi_html = """
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """
        
        with col1:
            st.markdown(kpi_html.format(label="Total Steps", value=len(trace)), unsafe_allow_html=True)
        with col2:
            st.markdown(kpi_html.format(label="Safety Flags", value=len(review_flags)), unsafe_allow_html=True)
        with col3:
            st.markdown(kpi_html.format(label="Evidence Sources", value=source_count), unsafe_allow_html=True)
        with col4:
            st.markdown(kpi_html.format(label="Avg Confidence", value=f"{avg_confidence}%"), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Main Content Tabs
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "Clinical Overview", 
            "Detailed Summary", 
            "Medications & Safety", 
            "Evidence Grounding", 
            "Agent Observability"
        ])

        with tab1:
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f"""
                <div class="summary-card">
                    <div class="summary-title">Principal Diagnosis</div>
                    <div class="summary-content">{clinical.get('principal_diagnosis', {}).get('value', 'Pending')}</div>
                </div>
                """, unsafe_allow_html=True)
            with col_b:
                st.markdown(f"""
                <div class="summary-card">
                    <div class="summary-title">Discharge Condition</div>
                    <div class="summary-content">{clinical.get('discharge_condition', {}).get('value', 'Pending')}</div>
                </div>
                """, unsafe_allow_html=True)
                
            st.markdown(f"""
            <div class="summary-card">
                <div class="summary-title">Follow-up Instructions</div>
                <div class="summary-content">{clinical.get('follow_up', {}).get('value', 'Pending')}</div>
            </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown(f"""
            <div class="summary-card">
                <div class="summary-title">Hospital Course</div>
                <div class="summary-content">{clinical.get('hospital_course', {}).get('value', 'Pending')}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="summary-card">
                <div class="summary-title">Pending Results</div>
                <div class="summary-content">{', '.join(clinical.get('pending_results', {}).get('value', []))}</div>
            </div>
            """, unsafe_allow_html=True)

        with tab3:
            if review_flags:
                st.markdown("### Critical Safety Flags")
                for flag in review_flags:
                    st.markdown(f'<div class="alert-card">{flag}</div>', unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### Medication Reconciliation")
            
            med_recon = summary.get("medication_reconciliation", {})
            col_med1, col_med2 = st.columns(2)
            
            with col_med1:
                st.markdown("**Added at Discharge:**")
                for med in med_recon.get("added", []):
                    st.markdown(f"- {med.title()}")
            with col_med2:
                st.markdown("**Removed at Discharge:**")
                for med in med_recon.get("removed", []):
                    st.markdown(f"- {med.title()}")

        with tab4:
            st.markdown("### Source Grounding Audit")
            audit_data = []
            for field, data in clinical.items():
                if isinstance(data, dict):
                    sources = data.get("sources", [])
                    source_str = ", ".join([f"{s['document']} (p.{s['page']})" for s in sources]) if sources else "None"
                    audit_data.append({
                        "Clinical Field": field.replace("_", " ").title(),
                        "Confidence": f"{data.get('confidence', 0) * 100:.0f}%",
                        "Source Documents": source_str
                    })
            
            st.dataframe(audit_data, use_container_width=True, hide_index=True)

        with tab5:
            st.markdown("### Dynamic Agent Execution Trace")
            for step in trace:
                status_color = "#dcfce7" if step['status'] == 'success' else "#fef2f2"
                text_color = "#166534" if step['status'] == 'success' else "#991b1b"
                
                st.markdown(f"""
                <div class="trace-card">
                    <div class="trace-step-header">
                        <span class="trace-step-number">Step {step['step']}</span>
                        <span class="trace-status" style="background: {status_color}; color: {text_color};">
                            {step['status'].upper()}
                        </span>
                    </div>
                    <div class="trace-action">Tool Invoked: {step['action']}</div>
                    <div class="trace-reasoning"><strong>Reasoning:</strong> {step['reasoning']}</div>
                </div>
                """, unsafe_allow_html=True)