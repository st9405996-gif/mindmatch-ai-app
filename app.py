import streamlit as st
from mindmatch_ai import MindMatchEngine

engine = MindMatchEngine()
st.set_page_config(page_title="OMNI Sovereign", layout="wide")

# Force Dark Mode CSS
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .chat-bubble { background-color: #1c1f26; padding: 20px; border-radius: 15px; border-left: 5px solid #3b82f6; margin-top: 10px; }
    .auth-card { background-color: #1c1f26; padding: 20px; border-radius: 15px; border: 1px solid #3b82f6; margin-top: 20px; }
    label { color: #3b82f6 !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Session States
if 'step' not in st.session_state: st.session_state.step = 0
if 'auth' not in st.session_state: st.session_state.auth = False

# --- SIMPLE AUTH ---
if not st.session_state.auth:
    st.title("🛡️ OMNI Sovereign Login")
    with st.container():
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.text_input("Username / Email", key="user_login")
        st.text_input("Password", type="password")
        if st.button("Access Ecosystem"):
            st.session_state.auth = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN FLOW ---
else:
    st.sidebar.title("🛡️ OMNI Sovereign")
    if st.sidebar.button("Logout"):
        st.session_state.auth = False
        st.session_state.step = 0
        st.rerun()

    # Step 0: Language-Adaptive Chat
    if st.session_state.step == 0:
        st.header("🧠 MindMatch AI Intake")
        prompt = st.chat_input("Write your feelings here (English ya Hinglish)...")
        
        if prompt:
            st.markdown('<div class="chat-bubble">', unsafe_allow_html=True)
            st.write(f"**You:** {prompt}")
            response = engine.get_calming_msg(prompt)
            st.write(f"**OMNI AI:** {response}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.write("---")
            if st.button("Start Assessment / Assessment Shuru Karein ➡️"):
                st.session_state.step = 1
                st.rerun()

    # Step 1: Clinical Matrix
    elif st.session_state.step == 1:
        st.header("📋 Clinical Assessment")
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        s1 = st.slider("Workload/Stress Level (1-10)", 1, 10, 5)
        s2 = st.slider("Sleep/Rest Quality (1-10)", 1, 10, 5)
        if st.button("Generate Sovereign Match"):
            st.session_state.match = engine.match_logic(s1 + s2)
            st.session_state.step = 2
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # Step 2: Match Result & P2P Chat
    elif st.session_state.step == 2:
        match = st.session_state.match
        st.success("🎯 Match Found / Match Mil Gaya Hai!")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f"""
            <div class="auth-card">
                <h3>{match['name']}</h3>
                <p><b>Expertise:</b> {match['degree']}</p>
                <p><b>Match Score:</b> {match['match']}%</p>
                <button style="width:100%; padding:10px; background:#1E3A8A; color:white; border:none; border-radius:5px;">Book Session</button>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.subheader("Secure P2P Chat")
            st.write("Ab aap apne therapist se baat kar sakte hain.")
            st.chat_input("Type a message to your therapist...")
