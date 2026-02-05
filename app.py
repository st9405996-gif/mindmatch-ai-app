import streamlit as st
import time
from mindmatch_ai import MindMatchEngine

# Initialize the engine
engine = MindMatchEngine()

st.set_page_config(page_title="OMNI Sovereign", layout="wide")

# --- UI GHOST PROTOCOL ---
ghost_active = st.sidebar.toggle("Activate Ghost Protocol")

if ghost_active:
    st.markdown("<style>.stApp { background-color: #000000; color: #00FF41 !important; }</style>", unsafe_allow_html=True)
    theme_clr = "#ff3131"
else:
    st.markdown("<style>.stApp { background-color: #0E1117; color: white; }</style>", unsafe_allow_html=True)
    theme_clr = "#3b82f6"

st.markdown(f"""
    <style>
    .auth-card, .chat-box, .status-card {{ 
        background-color: {"#050505" if ghost_active else "#1c1f26"}; 
        padding: 20px; border-radius: 15px; border: 1px solid {theme_clr}; margin-bottom: 15px;
    }}
    label, h1, h2, h3, p {{ color: white !important; }}
    .stButton>button {{ background-color: #1E3A8A; color: white; border-radius: 10px; width: 100%; border: none; }}
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATES ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'step' not in st.session_state: st.session_state.step = 0
if 'p2p_chat' not in st.session_state: st.session_state.p2p_chat = []

# --- 1. LOGIN & REGISTRATION ---
if not st.session_state.auth:
    st.title("🛡️ OMNI Global Access")
    t1, t2 = st.tabs(["🔒 Secure Login", "📝 Create Account"])
    
    with t2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        role = st.radio("I am a:", ["User / Client", "Therapist / Provider"], horizontal=True)
        col1, col2 = st.columns(2)
        with col1:
            u_name = st.text_input("Full Name")
            u_reg_id = st.text_input("Email / ID")
        with col2:
            if "Therapist" in role:
                u_license = st.text_input("License Number")
                st.caption("Registration Fee: $149.99")
            u_pwd = st.text_input("Password", type="password")
        if st.button("Complete Sign Up"):
            st.session_state.auth = True
            st.session_state.user = {"name": u_name, "role": "User" if "User" in role else "Therapist", "rate": 150}
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with t1:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.text_input("Sovereign ID", key="log_id")
        st.text_input("Password", type="password", key="log_pass")
        if st.button("Enter OMNI"):
            st.session_state.auth = True
            st.session_state.user = {"name": "Demo User", "role": "User", "rate": 150}
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- 2. MAIN DASHBOARDS ---
else:
    user = st.session_state.user
    st.sidebar.title(f"Verified: {user['name']}")
    if st.sidebar.button("Logout"):
        st.session_state.auth = False
        st.rerun()

    if user['role'] == "Therapist":
        st.header("👨‍⚕️ Clinician Earnings & P2P Chat")
        col_chat, col_audit = st.columns([2, 1])
        with col_chat:
            st.subheader("Direct Client Messages")
            st.markdown('<div class="chat-box">', unsafe_allow_html=True)
            for m in st.session_state.p2p_chat:
                st.write(f"**{m['role']}:** {m['content']}")
            st.markdown('</div>', unsafe_allow_html=True)
            if p_input := st.chat_input("Reply to client..."):
                st.session_state.p2p_chat.append({"role": "Therapist", "content": p_input})
                st.rerun()
        with col_audit:
            st.subheader("Revenue Audit")
            rev = engine.get_revenue_split(user['rate'])
            st.metric("Your Net (89.5%)", f"${rev['net']:.2f}")
            st.json(rev['breakdown'])

    elif user['role'] == "User":
        st.header("🧠 Sovereign Health Journey")
        if st.session_state.step == 0:
            st.subheader("Clinical AI Chat")
            prompt = st.chat_input("How are you feeling?")
            if prompt:
                st.chat_message("user").write(prompt)
                # Corrected function call here
                response = engine.get_calming_msg(prompt)
                st.chat_message("assistant").write(response)
                if st.button("Start AI Assessment"):
                    st.session_state.step = 1
                    st.rerun()
        
        elif st.session_state.step == 1:
            st.markdown('<div class="auth-card">', unsafe_allow_html=True)
            st.subheader("Clinical Assessment")
            s1 = st.slider("Stress Level", 1, 10, 5)
            s2 = st.slider("Mood Stability", 1, 10, 5)
            if st.button("Match with Provider"):
                st.session_state.match = engine.match_logic(s1+s2)
                st.session_state.step = 2
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state.step == 2:
            doc = st.session_state.match
            st.success(f"Match Found: {doc['name']}")
            c_chat, c_status = st.columns([2, 1])
            with c_chat:
                st.subheader(f"Chat with {doc['name']}")
                st.markdown('<div class="chat-box">', unsafe_allow_html=True)
                for m in st.session_state.p2p_chat:
                    st.write(f"**{m['role']}:** {m['content']}")
                st.markdown('</div>', unsafe_allow_html=True)
                if u_input := st.chat_input("Message therapist..."):
                    st.session_state.p2p_chat.append({"role": "User", "content": u_input})
                    st.rerun()
            with c_status:
                st.markdown(f'<div class="status-card"><b>Ghost Mode:</b> {"ACTIVE" if ghost_active else "Standard"}</div>', unsafe_allow_html=True)
