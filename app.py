import streamlit as st
import time
from mindmatch_ai import MindMatchEngine

engine = MindMatchEngine()

# Force Dark Mode and High Contrast CSS
st.set_page_config(page_title="OMNI Sovereign", layout="wide")

st.markdown("""
    <style>
    /* Pure Dark Background for Visibility */
    .stApp {
        background-color: #0E1117 !important;
        color: #FFFFFF !important;
    }
    
    /* Input Labels Visibility */
    label, p, span, h1, h2, h3 {
        color: #FFFFFF !important;
    }

    /* Auth Card Styling - Solid contrast */
    .auth-card {
        background-color: #1c1f26;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #2d323e;
        margin-bottom: 20px;
    }

    /* Fixing Input Box Colors */
    input {
        background-color: #262730 !important;
        color: white !important;
    }
    
    /* Premium Button */
    .stButton>button {
        background-color: #1E3A8A !items;
        color: white !important;
        border-radius: 8px;
        width: 100%;
        border: 1px solid #3b82f6;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🛡️ OMNI Sovereign")
ghost = st.sidebar.toggle("Activate Ghost Protocol")
if ghost:
    st.markdown("<style>.stApp { background-color: #000000 !important; color: #ff3131 !important; }</style>", unsafe_allow_html=True)

# --- MASTER FLOW ---
if 'auth' not in st.session_state:
    st.title("🌐 OMNI Global Access Portal")
    
    # Tabs for clear separation
    t1, t2 = st.tabs(["🔒 Secure Login", "📝 Create Account"])

    with t2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        role = st.selectbox("Register as:", ["User / Client", "Therapist / Provider"])
        
        col1, col2 = st.columns(2)
        if role == "Therapist / Provider":
            with col1:
                t_name = st.text_input("Full Name (Clinician)")
                t_degree = st.selectbox("Highest Degree", ["MD", "PhD", "PsyD", "LCSW"])
            with col2:
                t_license = st.text_input("Medical License Number")
                t_pwd = st.text_input("Create Password", type="password", key="reg_t_pwd")
            
            st.info("💡 Clinical Vetting Fee: $149.99 (Billed later)")
            if st.button("Complete Provider Sign Up"):
                st.session_state.auth = True
                st.session_state.user = {"name": t_name, "role": "Therapist"}
                st.rerun()
        
        else: # User Registration
            with col1:
                u_name = st.text_input("Full Name")
                u_email = st.text_input("Email Address")
            with col2:
                u_dob = st.date_input("Date of Birth")
                u_pwd = st.text_input("Password", type="password", key="reg_u_pwd")
            
            if st.button("Initialize Sovereign Identity"):
                st.session_state.auth = True
                st.session_state.user = {"name": u_name, "role": "User"}
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with t1:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.subheader("Sign In to Ecosystem")
        st.text_input("Email / ID", key="log_email")
        st.text_input("Password", type="password", key="log_pwd")
        if st.button("Login"):
            st.session_state.auth = True
            st.session_state.user = {"name": "User", "role": "User"}
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- POST-LOGIN DASHBOARD ---
else:
    user = st.session_state.user
    st.sidebar.success(f"Verified: {user['name']}")
    if st.sidebar.button("Log Out"):
        del st.session_state.auth
        st.rerun()

    # Yahan Dashboard Content shuru hota hai
    st.header(f"Welcome, {user['name']} 👋")
    
    if user['role'] == "Therapist":
        st.subheader("Clinician Earnings & Audit")
        # Dashboard metrics
        c1, c2 = st.columns(2)
        c1.metric("Revenue Split", "20.5%")
        c2.metric("Network Status", "Sovereign Active")
        
    elif user['role'] == "User":
        st.subheader("🧠 MindMatch AI Clinical Intake")
        st.write("How can OMNI help you today?")
        # AI Intake Flow...
        st.chat_input("Tell us about your symptoms...")
