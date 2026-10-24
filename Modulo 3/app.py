
import streamlit as st
import joblib
import os


st.set_page_config(
    page_title="Classificador de Flores Iris",
    page_icon="🌸",
    layout="centered"
)

ARQUIVO_MODELO = "modelo.joblib"


FOTOS_ESPECIES = {
    "setosa": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg",
    "versicolor": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
    "virginica": "https://upload.wikimedia.org/wikipedia/commons/3/32/Iris_virginica.jpg"
}


@st.cache_resource
def carregar_modelo():
    if not os.path.exists(ARQUIVO_MODELO):
        return None

    return joblib.load(ARQUIVO_MODELO)


try:
    dados_modelo = carregar_modelo()

    if dados_modelo is None:
        st.error(
            "Arquivo modelo.joblib não encontrado. "
            "Coloque-o na mesma pasta deste código."
        )
        st.stop()

    modelo = dados_modelo["modelo"]
    nomes_especies = dados_modelo["nomes_especies"]

except Exception as erro:
    st.error(f"Erro ao carregar o modelo: {erro}")
    st.stop()


st.title("🌸 Classificador de Flores Iris")

st.write(
    """
    Este aplicativo utiliza um modelo de Machine Learning
    já treinado para prever a espécie de uma flor Iris
    a partir de quatro medidas em centímetros.
    """
)

st.success("Modelo existente carregado com sucesso!")

st.divider()


st.header("Informe as características da flor")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Comprimento da sépala (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.1,
        step=0.1
    )

    petal_length = st.number_input(
        "Comprimento da pétala (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.4,
        step=0.1
    )

with col2:
    sepal_width = st.number_input(
        "Largura da sépala (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.5,
        step=0.1
    )

    petal_width = st.number_input(
        "Largura da pétala (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )

st.divider()


st.subheader("Dados informados")

dados_iris = {
    "Comprimento da sépala (cm)": sepal_length,
    "Largura da sépala (cm)": sepal_width,
    "Comprimento da pétala (cm)": petal_length,
    "Largura da pétala (cm)": petal_width
}

st.write(dados_iris)

if st.button("🔍 Adivinhar espécie da flor", type="primary"):

    entrada_modelo = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    try:
        previsao = int(modelo.predict(entrada_modelo)[0])
        especie = nomes_especies[previsao]
        especie = str(especie).lower()

        st.divider()
        st.subheader("🌺 Resultado da classificação")

        st.success(f"Espécie prevista: Iris {especie}")

       
        foto = FOTOS_ESPECIES.get(especie)

        if foto:
            st.image(
                foto,
                caption=f"Flor Iris {especie}",
                use_container_width=True
            )
        else:
            st.warning(
                "Não foi encontrada uma foto para esta espécie."
            )

        if hasattr(modelo, "predict_proba"):
            probabilidades = modelo.predict_proba(
                entrada_modelo
            )[0]

            confianca = float(probabilidades[previsao]) * 100

            st.metric(
                "Probabilidade estimada",
                f"{confianca:.1f}%"
            )

            st.subheader("Probabilidades por espécie")

            for i, nome in enumerate(nomes_especies):
                st.write(
                    f"Iris {nome}: "
                    f"{probabilidades[i] * 100:.1f}%"
                )

        st.caption(
            "A probabilidade é uma estimativa do modelo, "
            "não uma garantia de acerto."
        )

        with st.expander("Ver dados enviados ao modelo"):
            st.code(str(entrada_modelo), language="python")

    except Exception as erro:
        st.error(f"Erro ao realizar a previsão: {erro}")


st.divider()

st.caption(
    "Projeto didático de Machine Learning com "
    "Streamlit e Scikit-learn — Dataset Iris."
)
