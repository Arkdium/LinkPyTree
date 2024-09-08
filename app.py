import streamlit as st
from st_functions import st_button, load_css, get_base64_image
from PIL import Image

def add_custom_css():
    # Caminho da imagem de fundo
    background_image_base64 = get_base64_image("background.jpg")  # Substitua pelo caminho correto da sua imagem
    
    st.markdown(f"""
        <style>
        /* Ajuste de margens e alinhamento */
        .css-12oz5g7.egzxvld2 {{
            padding-top: 0px;
        }}

        .css-1v0mbdj.etr89bj1 {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            min-width: 180px;
            max-width: 40%;
        }}

        .css-10trblm.e16nr0p30 {{
            font-weight: bold;
            text-align: center;
        }}

        p {{
            font-size: 19px;
        }}

        MainMenu {{
            visibility: hidden;
        }}
        footer {{
            visibility: hidden;
        }}
        header {{
            visibility: hidden;
        }}

        /* Aplicando a imagem de fundo em base64 */
        .stApp {{
            background-image: url("data:image/jpeg;base64,{background_image_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            border-radius: 10px;
            padding: 20px;
            height: 100%;
            overflow: hidden;        
        }}
        
       link-button {{
            display: block;
            align-items: center;
            justify-content: center;
            text-decoration: none !important;
            color: white !important;
            padding: 10px 20px;
            border-radius: 8px;
            background: linear-gradient(90deg, #4169E1, #333333);
            width: 100%;
            font-size: 16px;
            margin: 10px 0;
            text-align: center;
            border: 2px solid transparent;
            background-origin: border-box;
            background-clip: padding-box, border-box;
            box-shadow: 0px 0px 0px 2px transparent;
        }}

        .link-button:link {{
            color: white !important;  /* Cor para links não visitados */
        }}

        .link-button:visited {{
            color: #999999 !important;  /* Cor para links visitados */
        }}

        .link-button:hover {{
            color: #FFD700 !important;  /* Cor ao passar o mouse */
        }}

        .link-button:active {{
            color: #FF4500 !important;  /* Cor ao clicar */
        }}

        </style>
    """, unsafe_allow_html=True)

# Função para carregar e aplicar o CSS
add_custom_css()

#load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Jullie Canejo 🫶🏻')

st.info('Motorista TVDE no Porto.')

icon_size = 45

st_button('instagram', 'https://www.instagram.com/ju.uberporto?igsh=MWQ3b3o2emxneWV3eg==', 'Me segue no Insta!', icon_size)
st_button('whatsapp', 'wa.me/351932676539', 'Fale comigo no Whatsapp', icon_size)
st_button('star', 'https://chat.whatsapp.com/HczP5bUqL1l7YtIwE1LMkF', 'Donzelas no Volante 🚘', icon_size)
#st_button('telegram', 't.me/', 'Fale comigo no Telegram', icon_size)
#st_button('linkedin', 'https://www.linkedin.com/in/', 'Follow me on LinkedIn', icon_size)
