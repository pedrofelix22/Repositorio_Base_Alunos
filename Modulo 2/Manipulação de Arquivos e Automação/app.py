import streamlit as st
from datetime import datetime

st.title("Locadora de Veiculos")
st.title("Aluguel e venda de carros")
st.image("nova logo].png")

st.sidebar.title("patrocinador carful  força e elegancia")
carro = st.sidebar.selectbox("Selecione o carro que deseja alugar:", ["Lamborghini huracan","Hennessey Venom F5","porsche","Ferari SF90 Spider","bugatti tourbillon","Aston Martin DBS"])

valores_diarias =  {"Lamborghini huracan":10000, "Hennessey Venom F5":15000, "porsche":20000, "Ferrari SF90 Spider":100000, "bugatti tourbillon":50000, "Aston Martin DBS":60000}
valor_do_carro = {"Lamborghini huracan":2500000, "Hennessey Venom F5": 3000000 , "porsche":2600000, "Ferrari SF90 Spider":2600000, "bugatti tourbillon":50000000, "Aston Martin DBS":4600000}
st.image(f"{carro}.png", width=750)
st.subheader(f"valor da diaria: R$ {valores_diarias[carro]}")
st.subheader(f"Valor da compra: R$ {valor_do_carro[carro]}")

data_de_retirada = st.date_input("Selecione a data de retirada: ",datetime.now())
data_devolucao = st.date_input("selecione a data da devolução: ", data_de_retirada)

if st.button("Alugar"):

    dias = (data_devolucao - data_de_retirada).days
    total = dias * valores_diarias[carro]
    st.success(f"Alugando o carro por {dias} o custo total e: R$ {total}")

if st.button("Comprar"):
   
    st.success(f"Parabem por ter comprado um {carro} na nosa locadora, a sua compra total fica em {carro}")