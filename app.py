import streamlit as st
import time
from mindmatch_ai import MindMatchEngine

engine = MindMatchEngine()
st.set_page_config(page_title="OMNI Sovereign Ecosystem", layout="wide")

# --- GHOST PROTOCOL TOGGLE ---
st.sidebar.title("🛡️ OMNI Sovereign")
ghost_mode = st.sidebar.toggle("Activate Ghost Protocol")

# CSS for Visibility and Theme
if ghost_mode:
    st.markdown("<style>.stApp { background-color: #000000; color: #00FF41 !important; }</style>", unsafe_allow_html=True)
    accent = "#ff3131"
else:
    st.markdown("<style>.stApp { background-color: #0E1117; color: white; }</style>", unsafe_allow_html=True)
    accent = "#3b82f6"

st.markdown(f"""
    <style>
    .main-card {{ background-color: #1c1f26; padding: 20px; border-radius: 15px; border: 1px solid {accent}; margin-bottom: 10px; }}
    .stButton>button {{ background-color: #1E3A8A; color: white; width: 100%; border-radius: 10px; }}
    label, h1, h2, h3 {{ color: white !important; }}
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'step' not in st.session_state: st.session_state.step = 0

# --- 1. LOGIN / SIGNUP ---
if not st.session_state.auth:
    st.title("🛡️ OMNI Sovereign Access")
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab2:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        role = st.radio("Join as:", ["User", "Therapist"], horizontal=True)
        name = st.text_input("Full Name")
        email = st.text_input("Email/ID")
        pwd = st.text_input("Password", type="password")
        if st.button("Create Identity"):
            st.session_state.auth = True
            st.session_state.user = {"name": name, "role": role}
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with tab1:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.text_input("Username")
        st.text_input("Password", type="password", key="l_pwd")
        if st.button("Login"):
            st.session_state.auth = True
            st.session_state.user = {"name": "Verified User", "role": "User"}
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 2. DASHBOARD ---
else:
    user = st.session_state.user
    st.sidebar.success(f"User: {user['name']}")
    if st.sidebar.button("Logout"):
        st.session_state.auth = False
        st.session_state.step = 0
        st.rerun()

    if user['role'] == "Therapist":
        st.header("👨‍⚕️ Clinician Revenue & Mesh Chat")
        col_c, col_a = st.columns([2, 1])
        with col_a:
            st.subheader("Revenue Audit")
            split = engine.get_revenue_split(150)
            st.metric("Net Payout", f"${split['net']:.2f}")
            st.json(split['breakdown'])
        with col_c:
            st.subheader("Client P2P Chat")
            st.chat_input("Reply to client...")

    else: # USER JOURNEY
        st.header("🧠 MindMatch AI Clinical Journey")
        
        if st.session_state.step == 0:
            prompt = st.chat_input("Workload ya kisi aur maslay ke bare mein likhein...")
            if prompt:
                st.markdown(f'<div class="main-card"><b>You:</b> {prompt}<br><br><b>OMNI AI:</b> {engine.get_calming_msg(prompt)}</div>', unsafe_allow_html=True)
                if st.button("Start Assessment ➡️"):
                    st.session_state.step = 1
                    st.rerun()

        elif st.session_state.step == 1:
            st.markdown('<div class="main-card">', unsafe_allow_html=True)
            st.subheader("Clinical Matrix Assessment")
            s1 = st.slider("Workload Stress", 1, 10, 5)
            s2 = st.slider("Mood Level", 1, 10, 5)
            if st.button("Analyze & Match"):
                st.session_state.match = engine.match_logic(s1 + s2)
                st.session_state.step = 2
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state.step == 2:
            match = st.session_state.match
            st.success(f"Match Found: {match['name']}")
            col_l, col_r = st.columns([1, 1])
            with col_l:
                st.markdown(f"""
                <div class="main-card">
                    <h3>{match['name']}</h3>
                    <p>{match['degree']}</p>
                    <p><b>Match:</b> {match['match']}%</p>
                    <p><b>Rate:</b> ${match['rate']}</p>
                </div>
                """, unsafe_allow_html=True)
            with col_r:
                st.subheader("Direct Secure Chat")
                st.chat_input("Message your therapist...")
