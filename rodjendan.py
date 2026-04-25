import streamlit as st
import os
from PIL import Image

# 1. Podešavanje stranice
st.set_page_config(page_title="Srećan rođendan!", page_icon="🎂", layout="wide")

# CSS za ulepšavanje
st.markdown("""
    <style>
    .stApp {
        background-color: #F3E5F5;
    }
    .stButton {
        display: flex;
        justify-content: center;
        margin-top: 20vh; /* Spušta dugme na 20% visine ekrana */
    }
    .stButton > button {
        width: 280px !important;
        height: 80px !important;
        background-color: #7B1FA2 !important;
        color: white !important;
        font-size: 22px !important;
        border-radius: 50px !important;
        border: 4px solid white !important;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.2) !important;
    }
    h1 {
        text-align: center;
        color: #6A1B9A !important;
        padding-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Inicijalizacija stanja (da sajt "zapamti" da je dugme kliknuto)
if 'prikazi_sadrzaj' not in st.session_state:
    st.session_state['prikazi_sadrzaj'] = False

# 3. NASLOV
st.markdown("<h1>🎉 Srećan rođendan, kraljice! 🎂</h1>", unsafe_allow_html=True)

# 4. LOGIKA ZA DUGME
if not st.session_state['prikazi_sadrzaj']:
    # Ako još nije kliknuto, prikaži samo dugme
    if st.button('OTVORI IZNENAĐENJE 🎁'):
        st.session_state['prikazi_sadrzaj'] = True
        st.balloons()
        st.rerun()  # Osvežava stranicu da prikaže slike
else:
    # Ako je kliknuto, prikaži sve slike i poruku
    st.snow()
    st.markdown("<h2 style='text-align: center; color: #7B1FA2;'>VOLIMO TE NAJVIŠE! ❤️</h2>", unsafe_allow_html=True)

    st.write("---")
    st.success("""
    Želim ti sve najlepše, puno zdravlja, sreće i da 
    nastavimo da pravimo ovakve uspomene još dugo! ✨
    """)

    # --- OVDE IDU SLIKE (Sada će biti vidljive) ---
    try:
        glavna = Image.open('img_1.png')
        st.image(glavna, use_container_width=True)
    except:
        pass

    col_a, col_b = st.columns(2)
    with col_a:
        try:
            st.image('img.png', use_container_width=True)
        except:
            pass
    with col_b:
        try:
            st.image('img_2.png', use_container_width=True)
        except:
            pass

    st.header("📸 Galerija")
    putanja_galerija = "fotke"
    if os.path.exists(putanja_galerija):
        sve_slike = [f for f in os.listdir(putanja_galerija) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if sve_slike:
            kolone = st.columns(4)
            for i, naziv in enumerate(sve_slike):
                putanja = os.path.join(putanja_galerija, naziv)
                try:
                    img = Image.open(putanja)
                    with kolone[i % 4]:
                        st.image(img, use_container_width=True)
                except:
                    continue


