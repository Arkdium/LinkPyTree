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
                
        .center-text {{
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            background-color: #f0f8ff;  /* Cor de fundo similar ao st.info */
            border-left: 5px solid #00acc1;  /* Bordar lateral semelhante ao st.info */
            border-radius: 5px;
            color: #000000;  /* Cor do texto */
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


# style="display: flex; align-items: center;">
#def load_css():
#    with open("style.css") as f:
#        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
#    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

#def st_button(icon, url, label, iconsize):
#    if icon == 'youtube':
#        button_code = f'''
#        <p>
#            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
#                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-youtube" viewBox="0 0 16 16">
#                    <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
#                </svg>  
#                {label}
#            </a>
#        </p>'''
#    elif icon == 'twitter':
#        button_code = f'''
#        <p>
#        <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
#            <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-twitter" viewBox="0 0 16 16">
#                <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
#            </svg>
#            {label}
#        </a>
#        </p>'''
#    elif icon == 'linkedin':
#        button_code = f'''
#        <p>
#            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
#                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
#                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
#                </svg>
#                {label}
#            </a>
#        </p>''' 
#    elif icon == 'medium':
#        button_code = f'''
#        <p>
#            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
#                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-medium" viewBox="0 0 16 16">
#                    <path d="M9.025 8c0 2.485-2.02 4.5-4.513 4.5A4.506 4.506 0 0 1 0 8c0-2.486 2.02-4.5 4.512-4.5A4.506 4.506 0 0 1 9.025 8zm4.95 0c0 2.34-1.01 4.236-2.256 4.236-1.246 0-2.256-1.897-2.256-4.236 0-2.34 1.01-4.236 2.256-4.236 1.246 0 2.256 1.897 2.256 4.236zM16 8c0 2.096-.355 3.795-.794 3.795-.438 0-.793-1.7-.793-3.795 0-2.096.355-3.795.794-3.795.438 0 .793 1.699.793 3.795z"/>
#                </svg>
#                {label}
#            </a>
#        </p>'''
#    elif icon == 'newsletter':
#        button_code = f'''
#        <p>
#            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
#                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16">
#                    <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z"/>
#                </svg>
#                {label}
#            </a>
#        </p>'''
#    elif icon == 'cup':
#        button_code = f'''
#        <p>
#            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
#                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-cup-fill" viewBox="0 0 16 16">
#                    <path d="M1 2a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v1h.5A1.5 1.5 0 0 1 16 4.5v7a1.5 1.5 0 0 1-1.5 1.5h-.55a2.5 2.5 0 0 1-2.45 2h-8A2.5 2.5 0 0 1 1 12.5V2zm13 10h.5a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.5-.5H14v8z"/>
#                </svg>
#                {label}
#            </a>
#        </p>'''
#    elif icon == 'instagram':
#        button_code = f'''
#        <p>
#            <a href="{url}" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
#                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" fill="currentColor" class="bi bi-instagram" viewBox="0 0 16 16">
#                    <path d="M8 0C5.792 0 5.556.01 4.71.048 3.86.087 3.281.214 2.775.445A4.512 4.512 0 0 0 1.6 1.6c-.23.506-.358 1.085-.397 1.935C1.165 4.556 1.155 4.792 1.155 8c0 3.208.01 3.444.048 4.29.04.85.166 1.429.398 1.935.231.506.537.912 1.035 1.41.498.498.904.803 1.41 1.034.506.23 1.085.357 1.935.398C4.556 14.835 4.792 14.845 8 14.845c3.208 0 3.444-.01 4.29-.048.85-.041 1.429-.168 1.935-.398.506-.231.912-.537 1.41-1.035.498-.498.803-.904 1.034-1.41.23-.506.358-1.085.398-1.935.038-.846.048-1.082.048-4.29 0-3.208-.01-3.444-.048-4.29-.04-.85-.166-1.429-.398-1.935a4.512 4.512 0 0 0-1.035-1.41c-.498-.498-.904-.803-1.41-1.034-.506-.23-1.085-.357-1.935-.398C11.444.165 11.208.155 8 .155zm0 1.563c2.978 0 3.253.01 4.399.048.781.029 1.205.137 1.485.23.46.15.787.329 1.131.673.344.344.523.671.673 1.131.093.28.2.704.23 1.485.038 1.146.048 1.421.048 4.399s-.01 3.253-.048 4.399c-.029.781-.137 1.205-.23 1.485a3.052 3.052 0 0 1-.673 1.131 3.053 3.053 0 0 1-1.131.673c-.28.093-.704.2-1.485.23-1.146.038-1.421.048-4.399.048s-3.253-.01-4.399-.048c-.781-.029-1.205-.137-1.485-.23a3.052 3.052 0 0 1-1.131-.673 3.052 3.052 0 0 1-.673-1.131c-.093-.28-.2-.704-.23-1.485-.038-1.146-.048-1.421-.048-4.399s.01-3.253.048-4.399c.029-.781.137-1.205.23-1.485a3.052 3.052 0 0 1 .673-1.131 3.052 3.052 0 0 1 1.131-.673c.28-.093.704-.2 1.485-.23 1.146-.038 1.421-.048 4.399-.048zm0 3.844a4.155 4.155 0 1 0 0 8.31 4.155 4.155 0 0 0 0-8.31zm0 1.563a2.592 2.592 0 1 1 0 5.184 2.592 2.592 0 0 1 0-5.184zm5.056-1.41a1.005 1.005 0 1 0 0 2.01 1.005 1.005 0 0 0 0-2.01z"/>
#                </svg>
#                {label}
#            </a>
#        </p>'''
    
#    elif icon == 'whatsapp':
#        button_code = f'''
#        <p>
#            <a href="{url}" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
#                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16">
#                    <path d="M13.601 2.326A7.898 7.898 0 0 0 8.002.004a7.906 7.906 0 0 0-6.114 12.849L.862 15.5l2.722-.715a7.906 7.906 0 0 0 4.417 1.3h.003a7.899 7.899 0 0 0 7.875-7.899 7.857 7.857 0 0 0-2.278-5.86zm-.597 9.288c-.264.734-1.33 1.351-1.83 1.436-.466.075-1.04.106-1.678-.106a8.12 8.12 0 0 1-1.822-.93 7.367 7.367 0 0 1-2.462-2.43 5.943 5.943 0 0 1-1.21-3.125c-.012-.88.23-1.543.325-1.775.267-.625.977-.961 1.383-.99.36-.025.72-.005.957.044.27.056.58-.093.906.686.334.812.557 1.19.686 1.381.155.225.132.4-.028.61-.143.19-.298.335-.448.516-.137.166-.29.348-.132.63.155.285.688 1.144 1.476 1.851.994.888 1.837 1.175 2.125 1.31.21.1.467.075.618-.106.164-.186.7-.77.885-1.034.178-.26.365-.224.61-.136.27.095 1.427.673 1.672.794.246.12.41.18.472.284.075.12.075.69-.19 1.426z"/>
#                </svg>
#                {label}
#            </a>
#        </p>'''

#    elif icon == 'telegram':
#        button_code = f'''
#        <p>
#            <a href="{url}" class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
#                <svg xmlns="http://www.w3.org/2000/svg" width="{iconsize}" height="{iconsize}" fill="currentColor" class="bi bi-telegram" viewBox="0 0 16 16">
#                    <path d="M16 1.538c-.5.216-1.04.37-1.6.438a5.422 5.422 0 0 0 2.378-3.065c-.527.313-1.103.539-1.707.66A2.705 2.705 0 0 0 8.688 1.078a2.757 2.757 0 0 0-4.865 1.885 7.81 7.81 0 0 1-5.719-2.905 2.755 2.755 0 0 0 .852 3.676 2.712 2.712 0 0 1-1.248-.344v.034c0 1.288.926 2.36 2.163 2.603a2.765 2.765 0 0 1-1.246.048 2.757 2.757 0 0 0 2.571 1.914 5.512 5.512 0 0 1-3.41 1.178A7.79 7.79 0 0 0 4.21 15a7.797 7.797 0 0 0 7.825-7.825c0-.119-.003-.238-.009-.355A5.57 5.57 0 0 0 16 1.538z"/>
#                </svg>
#                {label}
#            </a>
#        </p>'''


#    elif icon == '':
#        button_code = f'''
#        <p>
#            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
#                {label}
#            </a>
#        </p>'''
#    return st.markdown(button_code, unsafe_allow_html=True)