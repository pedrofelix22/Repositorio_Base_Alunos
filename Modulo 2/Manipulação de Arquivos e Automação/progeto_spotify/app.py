import streamlit as st 

musica = {
    "Michael Jackson":{
        "billie jean":"https://www.youtube.com/watch?v=Zi_XLOBDo_Y&list=RDZi_XLOBDo_Y&start_radio=1",
         "They Don't Care About Us":  "https://www.youtube.com/watch?v=pY90sFsB9wI&list=RDpY90sFsB9wI&start_radio=1",     
        "Thriller":"https://www.youtube.com/watch?v=IK-nOiFE6gg&list=RDIK-nOiFE6gg&start_radio=1",
},


        "Forro Boys":{
            "Baladeiro":"https://www.youtube.com/watch?v=u3JXbF3RwY0&list=RDu3JXbF3RwY0&start_radio=1",
            "Amor Virtual":"https://www.youtube.com/watch?v=6sxh45dhzDM&list=RD6sxh45dhzDM&start_radio=1",
            "Ta Todo Mundo Doido":"https://www.youtube.com/watch?v=3UXnJJJdtH0&list=RD3UXnJJJdtH0&start_radio=1",
        },
        "abertura de power rangers":{
            "abertura de power rangers s.p.d":"https://www.youtube.com/watch?v=nSrX-HDdync",
            "abertura de power rangers tempestade ninja":"https://www.youtube.com/watch?v=HZ7bY_a0UtE",
            "abertura de power rangers morfagem ferros":"https://www.youtube.com/watch?v=Iko5IUXCHSQ,",
        }


}
  


st.sidebar.image("spotify2.png")
artista = st.sidebar.selectbox("Selecione o artista",musica.keys())
musica_artista = musica [artista]

st.title(artista)
for musica in musica_artista.items():
    titulo,link = musica
    st.subheader(titulo)
    st.video(link)