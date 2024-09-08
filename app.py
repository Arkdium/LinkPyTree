import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Jullie Canejo 🫶🏻')

st.info('Motorista TVDE no Porto.')

icon_size = 50

st_button('instagram', 'https://instagram.com/ju.uber.pt', 'Me segue no Insta!', icon_size)
st_button('whatsapp', 'wa.me/351932676539', 'Fale comigo no Whatsapp', icon_size)
st_button('whatsapp', 'wa.me/351932676539', 'Entre para nosso grupo exclusivo de Meninas TVDE', icon_size)
st_button('telegram', 't.me/chamaotiao_bot', 'Fale comigo no Telegram', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/', 'Follow me on LinkedIn', icon_size)

