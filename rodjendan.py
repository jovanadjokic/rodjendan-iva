import streamlit as st
import os
import time
from PIL import Image

# 1. KONFIGURACIJA STRANICE
st.set_page_config(page_title="Za Ivu 💜", layout="centered")

# 2. NAPREDNI CSS
st.markdown("""
    <style>
    /* Svetlo ljubičasta pozadina za glavni deo aplikacije */
    .stApp {
        background-color: #E6E6FA; 
    }

    h1, h2, h3, p {
        color: #4B0082 !important;
        text-align: center;
        font-family: 'Segoe UI', Arial, sans-serif;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.6);
        border-radius: 20px;
        padding: 20px;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin: 20px auto;
        max-width: 500px;
    }

    div.stButton > button {
        display: block;
        margin: 0 auto !important;
        background-color: #9370DB;
        color: white !important;
        border-radius: 50px;
        border: none;
        padding: 10px 35px;
        font-size: 16px;
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #8A2BE2;
    }

    .start-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }

    .stImage img {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'korak' not in st.session_state:
    st.session_state.korak = 'start'

# --- KORAK 1: TOTALNO CRNI EKRAN ---
if st.session_state.korak == 'start':
    st.markdown("""
        <style>
        .stApp { background-color: black !important; }
        header, footer {visibility: hidden;}
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="start-wrapper">', unsafe_allow_html=True)
    if st.button('OTVORI IZNENAĐENJE 🎁'):
        st.session_state.korak = 'baloni'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- KORAK 2: BALONI / KONFETE ---
elif st.session_state.korak == 'baloni':
    st.balloons()  # Efekat slavlja
    st.markdown("<br><br><h1>SREĆAN ROĐENDAN, IVO! 🎂</h1>", unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.korak = 'slike_uvod'
    st.rerun()

# --- KORAK 3: TRI GLAVNE SLIKE (3 SEKUNDE) ---
elif st.session_state.korak == 'slike_uvod':
    glavne_slike = ['img_1.png', 'img_2.png', 'img.png']
    opisi = ["Zvezda dana! ✨", "Neke nase lepse slike! ", "Uzivaj danass!"]

    placeholder = st.empty()
    for i in range(len(glavne_slike)):
        with placeholder.container():
            st.markdown(f"<h3>{opisi[i]}</h3>", unsafe_allow_html=True)
            try:
                img = Image.open(glavne_slike[i])
                st.image(img, use_container_width=True)
                time.sleep(3)  # Smanjeno na 3 sekunde
            except:
                st.error(f"Fali slika: {glavne_slike[i]}")
                time.sleep(1)

    st.session_state.korak = 'zelje'
    st.rerun()

# --- KORAK 4: ŽELJE I GALERIJA ---
elif st.session_state.korak == 'zelje':
    st.markdown("<h1>Nešto posebno za tebe ✨</h1>", unsafe_allow_html=True)

    if st.button('Klikni za želju'):
        st.balloons()  # Zamenjene pahuljice balonima (kao konfete)
        st.session_state.pokazi_zelje = True

    if st.session_state.get('pokazi_zelje', False):
        st.markdown("""
        <div class="glass-card">
            <p>1. Sreća ✨</p>
            <p>2. Zdravlje 🍀</p>
            <p>3. Igrica 🎮</p>
            <p>4. Funko Pop figurica 🧸</p>
            <p>5. 6-ica iz Ekonomije! 📚</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("<h2>Uspomene 🎞️</h2>", unsafe_allow_html=True)

    folder_putanja = "fotke"
    if os.path.exists(folder_putanja):
        sve_fotke = [f for f in os.listdir(folder_putanja) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
        sve_fotke.sort()

        if sve_fotke:
            if 'foto_index' not in st.session_state:
                st.session_state.foto_index = 0

            trenutna_slika = sve_fotke[st.session_state.foto_index]
            st.image(Image.open(os.path.join(folder_putanja, trenutna_slika)), use_container_width=True)
            st.markdown(f"<p>Uspomena {st.session_state.foto_index + 1} od {len(sve_fotke)}</p>",
                        unsafe_allow_html=True)

            col_levo, col_desno = st.columns(2)
            with col_levo:
                if st.button("Prethodna slika"):
                    st.session_state.foto_index = (st.session_state.foto_index - 1) % len(sve_fotke)
                    st.rerun()
            with col_desno:
                if st.button("Sledeća slika"):
                    st.session_state.foto_index = (st.session_state.foto_index + 1) % len(sve_fotke)
                    st.rerun()

