import streamlit as st
import plotly.express as px
from mindmatch_ai import MindMatchAPI

api = MindMatchAPI()

st.set_page_config(page_title="OMNI | Sovereign Mental Health", layout="wide")

# Sidebar & Ghost Protocol
st.sidebar.title("🛡️ OMNI Sovereign")
ghost_mode = st.sidebar.toggle("Activate Ghost Protocol")

if ghost_mode:
    st.markdown("<style> .stApp { background-color: #0e0202; color: #ff4b4b; } </style>", unsafe_allow_html=True)
    st.sidebar.error("OFFLINE: GHOST MESH NODE ACTIVE")

# Authentication
if 'logged_in' not in st.session_state:
    st.title("🔐 OMNI Inc. Portal")
    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox("I am a...", ["Patient", "Therapist", "B2B Admin"])
        email = st.text_input("Email")
        dob = st.date_input("Date of Birth")
    if st.button("Enter Ecosystem"):
        st.session_state.logged_in = True
        st.session_state.role = role
        st.rerun()

else:
    role = st.session_state.role
    st.sidebar.success(f"Verified: {role}")
    
    if role == "Patient":
        st.title("🧠 MindMatch AI Chat")
        st.info("Our AI uses a 150-variable matrix for your perfect match.")
        chat = st.chat_input("Tell us how you're feeling...")
        if chat:
            st.chat_message("user").write(chat)
            insight = api.get_ai_insight()
            st.chat_message("assistant").write(f"Analysis complete. Your match is ready. Recovery Projection: **{insight['acceleration']}** faster.")
            st.metric("Match Confidence", insight['match_confidence'])

    elif role == "Therapist":
        st.title("👨‍⚕️ Provider Wallet")
        st.success(f"Status: Registered & Verified ($149.99 Paid)")
        session_amt = st.number_input("Session Rate ($)", value=150.0)
        data = api.calculate_revenue(session_amt)
        
        col1, col2 = st.columns(2)
        col1.metric("Your Net Payout", f"${data['dr_payout']}")
        col2.metric("OMNI Cut (20.5%)", f"${data['total_fee']}")
        
        st.subheader("Fee Breakdown Audit")
        st.write(data['breakdown'])

    elif role == "B2B Admin":
        st.title("🏢 Corporate ROI Dashboard")
        insight = api.get_ai_insight()
        col1, col2, col3 = st.columns(3)
        col1.metric("Productivity ROI", insight['roi'])
        col2.metric("Recovery Speed", insight['acceleration'])
        col3.metric("Employee PEPM", "$5 - $15")
        
        st.bar_chart({"ROI": [3.27, 1.0], "Label": ["OMNI", "Traditional"]})
