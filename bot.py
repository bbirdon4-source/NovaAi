import streamlit as st
import requests

# API Anahtarını Streamlit Secrets'tan çekiyoruz
api_key = st.secrets["GEMINI_API_KEY"]

st.title("🤖 NovaAi Chatbot")
st.write("Sana nasıl yardımcı olabilirim?")

# 1. Sohbet Geçmişini Hafızada Tutma
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. Eski Mesajları Ekrana Yazdırma
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Kullanıcıdan Mesaj Alma (Sohbet Kutusu)
if prompt := st.chat_input("Mesajınızı buraya yazın..."):
    # Kullanıcının yazdığını ekrana bas
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Yapay zekadan cevap üretme
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Google API URL'si
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        
        headers = {'Content-Type': 'application/json'}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            response_data = response.json()
            full_response = response_data['candidates'][0]['content']['parts'][0]['text']
        except Exception as e:
            full_response = "Üzgünüm, bir hata oluştu. Lütfen Streamlit Secrets kısmındaki API anahtarınızı kontrol edin."
        
        message_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})
