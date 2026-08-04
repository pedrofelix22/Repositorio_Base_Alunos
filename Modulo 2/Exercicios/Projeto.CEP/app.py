import requests
import pandas as pd
import streamlit as st 

cep = st.sidebar.text_input("digite o cep que deseja pesquisar", icon="🔎")
st.image("https://www.bing.com/th/id/OGC.894456302a0da8007a8d01bc0f5aac2d?r=0&o=7&pid=1.7&rm=3&rurl=https%3a%2f%2fmedia2.giphy.com%2fmedia%2fv1.Y2lkPTc5MGI3NjExMXdkNW43b245bDZzODZyZmZyd2p1bzVidGFpNTZoN2ltM2hwY2lkaiZlcD12MV9naWZzX3NlYXJjaCZjdD1n%2f6y6fyAD9OIE6NvhJEu%2fgiphy.gif&ehk=tYZwFfuUxWekVmeKs5Fz%2b2R4uqdPz9TSNk3Gm5xCkyI%3d")
if st.sidebar.button("Pesquisa"):
    if len(cep) != 8:
        st.error("CEP invalido, digite sem ponto e traço e verifique os digitos ")
        st.stop()

busca = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")

if busca.status_code == 200:
        dados = busca.json()
        st.success("Endereço encontrado!")
        dados["address"]   
        dados["district"]  
        dados["city"]      
        dados["state"]     
        dados["lat"]      
        dados["lng"]   
        st.write("### 🗺️ Localização no mapa")

        local = pd.DataFrame({
            "lat": [float(dados["lat"])],
            "lon": [float(dados["lng"])]
        })

        st.map(local) 