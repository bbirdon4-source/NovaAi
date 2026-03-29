import streamlit as st
import google.generativeai as genai

# Senin aldığın API anahtarını buraya bağladık!
genai.configure(api_key="AIzaSyDLkWlueyBkqInr_IoJTS5DMnZwmzHSTGQ")

# Sayfa ayarları ve başlık
st.set_page_config(page_title="NovaAi", page_icon="", layout="centered")

# Koyu Tema ve Havalı Tasarım (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #0f141c;
        color: #ffffff;
    }
    .stTextInput>div>div>input {
        background-color: #1f2937;
        color: #ffffff;
        border: 2px solid #ff4655;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #ff4655;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff2a3a;
        color: white;
        box-shadow: 0 4px 15px rgba(255, 70, 85, 0.4);
    }
    h1 {
        color: #ff4655;
        text-align: center;
        font-family: 'Arial Black', sans-serif;
    }
    .taktik-kutusu {
        background-color: #1a2230;
        padding: 15px;
        border-left: 5px solid #ff4655;
        border-radius: 5px;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("NovaAi")
st.write("<p style='text-align: center; color: #a0aec0;'>Artık gerçek bir beynim var! Bana her şeyi sorabilirsin.</p>", unsafe_allow_html=True)

# Kullanıcıdan girdi alma
soru = st.text_input("Bana bir soru sor veya bir ajan adı yaz:")

if st.button("SİSTEMİ ÇALIŞTIR 🚀"):
    if soru:
        st.write("---")
        
        try:
            # Burada Google'ın gerçek yapay zekasına bağlanıyoruz
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # Yapay zekaya bir rol veriyoruz ki oyuncu gibi cevap versin
            komut = f"Sen bir oyuncu asistanı yapay zekasısın. Sorulan soruya bir oyuncu samimiyetiyle ve bilgisiyle cevap ver. Soru şu: {soru}"
            
            with st.spinner("Yapay zeka düşünüyor..."):
                response = model.generate_content(komut)
            
            # Gelen cevabı havalı kutumuzun içinde gösteriyoruz
            st.markdown(f"""
            <div class='taktik-kutusu'>
                <h3 style='color: #00ffaa;'>🤖 Yapay Zeka Cevabı:</h3>
                <p>{response.text}</p>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
            st.warning("Eğer hata aldıysan API anahtarın henüz aktifleşmemiş olabilir. Birkaç dakika bekleyip tekrar dene.")
            
    else:
        st.warning("Lütfen boş bırakma, bir şeyler yaz!")

# Alt bilgi
st.markdown("<br><br><p style='text-align: center; color: #4a5568;'>Bu site senin ellerinle kodlandı! 🚀</p>", unsafe_allow_html=True)
