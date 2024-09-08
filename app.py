import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
with col2:
    st.markdown('<div class="col2-custom">', unsafe_allow_html=True)
    col2.image(Image.open('dp.png'))
    st.markdown('</div>', unsafe_allow_html=True)

st.header('Jullie Canejo 🫶🏻')

st.info('Motorista TVDE no Porto.')

icon_size = 45

st_button('instagram', 'https://www.instagram.com/ju.uberporto?igsh=MWQ3b3o2emxneWV3eg==', 'Me segue no Insta!', icon_size)
st_button('whatsapp', 'wa.me/351932676539', 'Fale comigo no Whatsapp', icon_size)
st_button('star', 'https://chat.whatsapp.com/HczP5bUqL1l7YtIwE1LMkF', 'Donzelas no Volante 🚘', icon_size)
#st_button('telegram', 't.me/', 'Fale comigo no Telegram', icon_size)
#st_button('linkedin', 'https://www.linkedin.com/in/', 'Follow me on LinkedIn', icon_size)

