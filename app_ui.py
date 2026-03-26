
import streamlit as st
import requests
import json

st.set_page_config(page_title="Human Performance OS", layout="wide")

BACKEND_URL = st.secrets.get("BACKEND_URL", "http://localhost:8000")
API_KEY = "demo-key"

st.title("🚀 Human Performance OS")
st.markdown("---")

# Metrics Input
col1, col2 = st.columns(2)
with col1:
    sleep = st.slider("Sleep Hours (0-10)", 0.0, 10.0, 7.5)
    focus = st.slider("Focus Hours (0-10)", 0.0, 10.0, 4.0)
with col2:
    energy = st.slider("Energy Level (0-10)", 0.0, 10.0, 6.0)
    consistency = st.slider("Habit Consistency (0-1)", 0.0, 1.0, 0.8)

if st.button("🧠 Calculate Performance", type="primary"):
    payload = {
        "sleep_hours": sleep,
        "focus_hours": focus,
        "energy_level": energy,
        "habit_consistency": consistency
    }
    
    try:
        response = requests.post(
            f"{BACKEND_URL}/evaluate",
            headers={"X-API-Key": API_KEY, "Content-Type": "application/json"},
            json=payload,
            timeout=5
        )
        data = response.json()
        
        # Dashboard
        col_score, col_rec = st.columns([1, 2])
        with col_score:
            st.metric("Performance Score", f"{data['performance_score']}/10")
            # Gauge Chart
            st.image("https://via.placeholder.com/300x200/00ff00/000000?text=Gauge+Here")  # Placeholder; use streamlit-gauge in prod
            
        with col_rec:
            st.markdown("### 🤖 AI Recommendation")
            st.markdown(data['recommendation'])
        
        # Security View
        with st.expander("🔒 Security View - Encrypted Data"):
            st.code(data['encrypted_data'])
            st.info("Your behavioral data is AES-256 encrypted, ensuring Zero-Trust sovereignty.")
            
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("Ensure backend is running at http://localhost:8000")

st.markdown("---")
st.caption("👨‍💻 Production-Ready Autonomous Performance Engine")
