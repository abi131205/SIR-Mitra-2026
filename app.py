import streamlit as st
import os
import requests
from dotenv import load_dotenv

# 1. Page Configuration (Must be first)
st.set_page_config(page_title="SIR-Mitra 2026", page_icon="🗳️", layout="centered")

# 2. Setup
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 3. UI Language Dictionary
lang_options = {
    "English": {"title": "SIR-Mitra: Election Assistant", "info": "Identify the correct form for voter registration, deletion, or correction.", "input": "Ask about your Voter ID..."},
    "Tamil": {"title": "SIR-Mitra: தேர்தல் உதவியாளர்", "info": "பதிவு, நீக்கம் அல்லது திருத்தத்திற்கான சரியான படிவத்தைக் கண்டறியவும்.", "input": "உங்கள் கேள்வியைக் கேட்கவும்..."},
    "Hindi": {"title": "SIR-Mitra: चुनाव सहायक", "info": "पंजीकरण, विलोपन या सुधार के लिए सही फॉर्म की पहचान करें।", "input": "अपने वोटर आईडी के बारे में पूछें..."},
    "Malayalam": {"title": "SIR-Mitra: തിരഞ്ഞെടുപ്പ് സഹായി", "info": "രജിസ്ട്രേഷൻ, തിരുത്തൽ എന്നിവയ്ക്കുള്ള ശരിയായ ഫോം കണ്ടെത്തുക.", "input": "ചോദിക്കൂ..."},
    "Telugu": {"title": "SIR-Mitra: ఎన్నికల సహాయకుడు", "info": "రిజిస్ట్రేషన్ లేదా దిద్దుబాటు కోసం సరైన ఫారమ్‌ను గుర్తించండి.", "input": "అడగండి..."},
    "Kannada": {"title": "SIR-Mitra: ಚುನಾವಣಾ ಸಹಾಯಕ", "info": "ನೋಂದಣಿ ಅಥವಾ ತಿದ್ದುಪಡಿಗಾಗಿ ಸರಿಯಾದ ಫಾರ್ಮ್ ಅನ್ನು ಗುರುತಿಸಿ.", "input": "ಕೇಳಿ..."},
    "Bengali": {"title": "SIR-Mitra: নির্বাচনী সহকারী", "info": "নিবন্ধন বা সংশোধনের জন্য সঠিক ফর্মটি চিহ্নিত করুন।", "input": "জিজ্ঞাসা করুন..."}
}

# 4. Sidebar - Standard components to avoid "Invisible Text"
with st.sidebar:
    st.title("🗳️ SIR-Mitra 2026")
    st.divider()
    selected_lang = st.selectbox("Select Language / மொழியைத் தேர்ந்தெடுக்கவும்", list(lang_options.keys()))
    st.info("2026 Special Intensive Revision (SIR) National Support")

# 5. Language Reload Logic
if "current_lang" not in st.session_state:
    st.session_state.current_lang = selected_lang

if st.session_state.current_lang != selected_lang:
    st.session_state.messages = []
    st.session_state.current_lang = selected_lang
    st.rerun()

ui = lang_options[selected_lang]

# 6. Main Body - Official Look using Standard Containers
st.header(f"{ui['title']}")
st.caption("Election Commission of India | भारत निर्वाचन आयोग")

with st.expander("ℹ️ How to use / எப்படிப் பயன்படுத்துவது", expanded=True):
    st.write(ui["info"])

# 7. Multilingual Chat Logic
def chat_with_mitra(user_input, language):
    system_logic = (
        f"You are 'SIR-Mitra', a professional 2026 Election Assistant for India. "
        f"Language: {language}. Logic: Form 6 (New), Form 7 (Remove), Form 8 (Correction). "
        f"Provide direct advice and respond ONLY in {language}."
    )
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    payload = {"contents": [{"parts": [{"text": f"{system_logic}\n\nUser: {user_input}"}]}]}
    try:
        response = requests.post(url, json=payload)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "System error. Please refresh."

# 8. Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input(ui["input"]):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = chat_with_mitra(prompt, selected_lang)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})