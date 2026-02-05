import streamlit as st
import time
from mindmatch_ai import MindMatchEngine

engine = MindMatchEngine()

# --- FORCING DARK THEME & CONTRAST ---
st.set_page_config(page_title="OMNI Sovereign Ecosystem", layout="wide")

st.markdown("""
    <style>
    /* Main Background - Thoda Dark Grey taake white text dikhe */
    .stApp { background-color: #121417; color: #ffffff; }
    
    /* Input Labels ko hamesha white rakhega */
    label { color: #ffffff !important; font-weight: bold; }
    
    /* Auth Container - Dark Blueish Background */
    .auth-container { 
        background-color: #1e2229; 
        padding: 40px; 
        border-radius: 20px; 
        border: 1px solid #3d4452;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    /* Tabs and Radio buttons styling */
    .stTabs [data-baseweb="tab-list"] { background-color: transparent; }
    .stTabs [data-baseweb="tab"] { color: #ffffff; }
    
    /* Custom Buttons */
    .stButton>button { 
        border-radius: 12px; 
        height: 3.5em; 
        background-color: #1E3A8A; 
        color: white; 
        font-weight: bold; 
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🛡️ OMNI Sovereign")
if st.sidebar.toggle("Activate Ghost Protocol"):
    st.markdown("<style>.stApp { background-color: #000000; color: #ff3131 !important; }</style>", unsafe_allow_html=True)
    st.sidebar.error("GHOST MESH ENCRYPTION ACTIVE")

# --- LOGIN / SIGN UP FLOW ---
if 'auth' not in st.session_state:
    st.title("🌐 OMNI Global Access")
    
    # Separation Tabs
    auth_tab1, auth_tab2 = st.tabs(["🔒 Secure Login", "📝 Create Account (Sign Up)"])

    with auth_tab2:
        st.subheader("Start Your Sovereign Journey")
        role = st.radio("I want to register as a:", ["User / Client", "Therapist / Provider"], horizontal=True)
        
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        if role == "Therapist / Provider":
            with col1:
                t_name = st.text_input("Full Legal Name", placeholder="Dr. Adyan")
                t_degree = st.selectbox("Degree", ["MD Psychiatrist", "PhD Clinical Psych", "PsyD", "LCSW"])
                t_license = st.text_input("Medical License Number")
            with col2:
                t_exp = st.number_input("Years of Experience", 1, 50)
                t_rate = st.number_input("Session Rate ($)", 150)
                t_pwd = st.text_input("Create Sovereign Password", type="password", key="t_pass")
            
            st.info("💡 A mandatory $149.99 vetting fee is required for Clinical Matrix activation.")
            if st.button("Complete Provider Registration"):
                st.session_state.auth = True
                st.session_state.user = {"name": t_name, "role": "Therapist", "rate": t_rate}
                st.rerun()

        else: # User Registration
            with col1:
                u_name = st.text_input("Full Name")
                u_email = st.text_input("Email Address")
            with col2:
                u_dob = st.date_input("Date of Birth")
                u_pwd = st.text_input("Password", type="password", key="u_pass")
            
            st.write("---")
            st.multiselect("Main Focus Area", ["Anxiety", "Trauma", "Depression", "Work Stress"])
            
            if st.button("Initialize Sovereign Account"):
                st.session_state.auth = True
                st.session_state.user = {"name": u_name, "role": "User"}
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with auth_tab1:
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        st.subheader("Welcome Back")
        st.text_input("Email / Sovereign ID")
        st.text_input("Secure Password", type="password", key="l_pass")
        if st.button("Enter Ecosystem"):
            st.session_state.auth = True
            st.session_state.user = {"name": "Demo User", "role": "User"}
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARDS ---
else:
    # (Baqi dashboard ka code wahi rahega jo pehle diya tha)
    st.header(f"Welcome, {st.session_state.user['name']}")
    if st.sidebar.button("Logout"):
        del st.session_state.auth
        st.rerun()
