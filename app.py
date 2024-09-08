import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

def add_custom_css():
    st.markdown(
        """
        <style>
        /* Estilizando a coluna col2 com imagem de fundo */
        .col2-custom {
            position: relative;
            background-image: url('background.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100%;
        }

        /* Layer cinza sobre a imagem de fundo */
        .col2-custom::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(128, 128, 128, 0.5); /* Camada cinza com transparência */
            z-index: 1;
        }

        /* Ajustando o conteúdo da coluna col2 para estar sobre o background */
        .col2-custom > div {
            position: relative;
            z-index: 2; /* Coloca o conteúdo acima do overlay */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()

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

