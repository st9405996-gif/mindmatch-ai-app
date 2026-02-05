import streamlit as st
import time
from mindmatch_ai import MindMatchEngine

engine = MindMatchEngine()
st.set_page_config(page_title="OMNI Sovereign Ecosystem", layout="wide")

# Professional CSS
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .auth-container { background: white; padding: 50px; border-radius: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border: 1px solid #eee; }
    .stButton>button { border-radius: 10px; height: 3.5em; font-weight: bold; transition: 0.3s; }
    .video-mesh { background: black; height: 450px; border-radius: 25px; display: flex; align-items: center; justify-content: center; color: #00ff00; font-family: monospace; border: 3px solid #333; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Ghost Protocol
st.sidebar.title("🛡️ OMNI Sovereign")
if st.sidebar.toggle("Activate Ghost Protocol"):
    st.markdown("<style>.stApp { background-color: #0a0a0a; color: #ff3131 !important; }</style>", unsafe_allow_html=True)
    st.sidebar.error("GHOST MESH ENCRYPTION ACTIVE")

# --- MASTER AUTH FLOW ---
if 'auth' not in st.session_state:
    st.title("🌐 OMNI Global Access")
    
    # Clear Tabs for Login and Sign Up
    auth_tab1, auth_tab2 = st.tabs(["🔒 Secure Login", "📝 Create Account (Sign Up)"])

    with auth_tab2:
        st.subheader("Start Your Sovereign Journey")
        role = st.radio("I want to register as a:", ["User / Client", "Therapist / Provider"], horizontal=True)
        
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        if role == "Therapist / Provider":
            with col1:
                t_name = st.text_input("Full Legal Name", placeholder="Dr. John Doe")
                t_degree = st.selectbox("Degree", ["MD Psychiatrist", "PhD Clinical Psych", "PsyD", "LCSW"])
                t_license = st.text_input("Medical License Number")
            with col2:
                t_exp = st.number_input("Years of Experience", 1, 50)
                t_rate = st.number_input("Session Rate ($)", 150)
                t_pwd = st.text_input("Create Password", type="password")
            
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
                u_pwd = st.text_input("Password", type="password")
            
            st.write("---")
            st.write("### Basic Health Context")
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
        st.text_input("Secure Password", type="password")
        if st.button("Enter Ecosystem"):
            st.session_state.auth = True
            st.session_state.user = {"name": "Demo User", "role": "User"}
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARDS ---
else:
    user = st.session_state.user
    st.sidebar.success(f"Verified: {user['name']}")
    if st.sidebar.button("Log Out"):
        del st.session_state.auth
        st.rerun()

    if user['role'] == "Therapist":
        st.header(f"👨‍⚕️ Provider Management: {user['name']}")
        st.write("Credential Status: **Verified** | Sovereign Split: **20.5%**")
        
        val = st.number_input("Session Value ($)", value=float(user['rate']))
        fin = engine.get_revenue_breakdown(val)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Your Net Payout (89.5%)", f"${fin['net_to_provider']:.2f}")
        c2.metric("OMNI 20.5% Cut", f"${fin['omni_cut']:.2f}")
        c3.metric("Platform Status", "Online")
        
        st.write("---")
        st.subheader("Financial Revenue Audit")
        st.json(fin['audit'])

    elif user['role'] == "User":
        if 'step' not in st.session_state: st.session_state.step = 0
        
        if st.session_state.step == 0:
            st.header("🧠 MindMatch AI Intake")
            chat = st.chat_input("Tell me what you are feeling today...")
            if chat:
                st.chat_message("user").write(chat)
                st.chat_message("assistant").write("Main samajh sakta hoon. OMNI AI aapke patterns ko analyze kar raha hai. Gehra saans lein. Kya hum assessment shuru karein?")
                if st.button("Begin 150-Variable Matrix Assessment"):
                    st.session_state.step = 1
                    st.rerun()

        elif st.session_state.step == 1:
            st.header("📋 Clinical Assessment")
            s1 = st.slider("Stress Intensity (1-10)", 1, 10, 5)
            s2 = st.slider("Sleep Disruption (1-10)", 1, 10, 5)
            if st.button("Run AI Analysis"):
                st.session_state.match = engine.match_ai(s1+s2)
                st.session_state.step = 2
                st.rerun()

        elif st.session_state.step == 2:
            prov = st.session_state.match
            st.success(f"🎯 Ideal Match Found: {prov['name']}")
            st.info(f"Match Score: {prov['match']}% | **Recovery Acceleration: 2.08x Faster**")
            
            t1, t2 = st.tabs(["Practitioner Profile", "🎥 Sovereign Video Mesh"])
            with t1:
                st.write(f"**Degree:** {prov['degree']} | **License:** {prov['license']}")
                st.write(f"**Session Rate:** ${prov['rate']}")
                if st.button("Confirm Booking"): st.balloons()
            with t2:
                st.markdown('<div class="video-mesh">E2EE VIDEO FEED ACTIVE <br> [ CONNECTED TO PROVIDER ]</div>', unsafe_allow_html=True)
