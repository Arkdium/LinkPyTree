import streamlit as st
import base64


def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

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
                
        .css-1w6rlcb.e12sa3f30, css-17z2rne.e13vu3m50 {{
            display: block; 
            text-align: center;
            margin: 0 auto;
            width: 80%;
            
        }}

        .css-10trblm.e16nr0p30 {{
            font-weight: bold;
            text-align: center;
        }}

        p {{
            font-size: 19px;
        }}
                
        MainMenu {{
            visibility: hidden !important;
        }}
                
        footer {{
            visibility: hidden !important;
        }}
                
        header {{
            visibility: hidden !important;
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
        
       .link-button {{
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
        
        .css-nahz7x a {{
            color: white !important;
        }}       
        
        </style>     

    """, unsafe_allow_html=True)

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def st_button(icon, url, label, iconsize):
    icon_path = f'icons/{icon}.png'  # Caminho para o ícone
    
    if icon in ['linkedin', 'instagram', 'whatsapp', 'telegram', 'star']:
        # Codifica a imagem em base64
        icon_base64 = get_base64_image(icon_path)
        button_code = f'''
        <p style="text-align: center; width: 100%;">
            <a href="{url}" target="_blank" class="btn btn-outline-primary btn-lg" type="button" aria-pressed="true" style="
                display: block;  
                align-items: center; 
                justify-content: center; 
                text-decoration: none; 
                padding: 10px 20px; 
                border-radius: 8px; 
                background: linear-gradient(90deg, #4169E1, #333333);  /* Gradiente de azul royal para cinza escuro */
                color: white !important;  /* Texto sempre branco */
                width: 100%;  /* Largura total */
                font-size: 16px;  /* Tamanho do texto */
                margin: 10px 0;  /* Margem centralizada */
                text-align: center;
                border: 2px solid transparent; /* Define a borda para começar como transparente */
                background-origin: border-box;
                background-clip: padding-box, border-box;
                box-shadow: 0px 0px 0px 2px transparent;
                ">
                <img src="data:image/png;base64,{icon_base64}" width="{iconsize}" height="{iconsize}" style="margin-right: 10px;">
                {label}
            </a>
        </p>'''
    else:
        button_code = f'''
        <p style="text-align: center; width: 100%;">
            <a href="{url}" target="_blank" class="btn btn-outline-primary btn-lg" type="button" aria-pressed="true" style="
                display: block;  
                padding: 10px 20px; 
                border-radius: 8px; 
                background: linear-gradient(90deg, #4169E1, #333333);  /* Gradiente de azul royal para cinza escuro */
                color: white !important;  /* Texto sempre branco */
                text-align: center; 
                text-decoration: none; 
                width: 100%;  /* Largura total */
                font-size: 16px;  /* Tamanho do texto */
                margin: 10px 0; /* Margem centralizada */
                text-align: center;
                border: 2px solid transparent;
                background-origin: border-box;
                background-clip: padding-box, border-box;
                box-shadow: 0px 0px 0px 2px transparent;
                ">
                {label}
            </a>
        </p>'''

    st.markdown(button_code, unsafe_allow_html=True)
