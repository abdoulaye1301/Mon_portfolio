import streamlit as st

st.markdown(
    "**Dans cette page, vous pouvez consulter les différentes projets sur lesquels** "
    "**Mr Abdoulaye NDAO à participer**"
)
st.header("Projet de modélisation avec Python")
st.write("\n")

col = st.columns(2)
# =============Projets Biostatistiques=======================
for i in range(1):
    col[0].write("\n")
for i in range(6):
    col[1].write("\n")
col[0].subheader("Biostatistique")
col[0].write("\n")
col[0].write(
    """
    <p style="text-align: justify;"><B>
    Le projet de Biostatistique consiste à mettre en place un modèle de machine 
    learning ou statistique qui permet de faire un pronostique sur 
    la survenue instantanée de décès après le traitement.Pour la 
    construction de ce modèle, nous avons utiliser les données des patients 
    atteints d’accident cérébral vasculaire (AVC), traités et suivis.
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[1].image("photos/biosta.jpeg")
col[0].link_button("Plus info", url="https://projetbiostatistique.streamlit.app")

for i in range(1):
    col[0].write("\n")
for i in range(6):
    col[1].write("\n")

# ========Projet Series Temporelles=================
col[0].subheader("Série Temporelle")
col[0].write("\n")
col[1].write(
    """
    <p style="text-align: justify;"><B>
    Le projet de Biostatistique consiste à mettre en place un modèle de machine 
    learning ou statistique qui permet de faire un pronostique sur 
    la survenue instantanée de décès après le traitement.Pour la 
    construction de ce modèle, nous avons utiliser les données des patients 
    atteints d’accident cérébral vasculaire (AVC), traités et suivis.
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[0].image("photos/series temporelles.png")
col[1].link_button(
    "Plus info",
    url="",
)

# ========MODELISATION AVEC SPSS=================


# ===========ANALYSE DE DONNÉES==============
for i in range(1):
    col[0].write("\n")
for i in range(4):
    col[0].write("\n")
col[0].header("Analyse de données")

# ============Projet power BI==============
for i in range(1):
    col[0].write("\n")
for i in range(11):
    col[1].write("\n")
col[0].subheader("Analyse des ventes")
st.write("\n")
col[0].write(
    """
    <p style="text-align: justify;"><B>
    Le projet de Biostatistique consiste à mettre en place un modèle de machine 
    learning ou statistique qui permet de faire un pronostique sur 
    la survenue instantanée de décès après le traitement.Pour la 
    construction de ce modèle, nous avons utiliser les données des patients 
    atteints d’accident cérébral vasculaire (AVC), traités et suivis.
    </B></p>
    """,
    unsafe_allow_html=True,
)
for i in range(3):
    col[1].write("\n")
col[1].image("photos/ID Global Busness/Accessoire ID Global.jpg", use_column_width=True)
col[0].link_button(
    "Plus info",
    url="",
)

# =============Projet excel=============
for i in range(1):
    col[0].write("\n")
for i in range(11):
    col[1].write("\n")
col[0].subheader("Dashboard RNU avec excel")
col[0].write("\n")
col[1].write(
    """
    <p style="text-align: justify;"><B>
    Le projet de Biostatistique consiste à mettre en place un modèle de machine 
    learning ou statistique qui permet de faire un pronostique sur 
    la survenue instantanée de décès après le traitement.Pour la 
    construction de ce modèle, nous avons utiliser les données des patients 
    atteints d’accident cérébral vasculaire (AVC), traités et suivis.
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[0].image("photos/Departement de Kaffine.jpg")
col[1].link_button("Plus info", url="https://projetbiostatistique.streamlit.app")
st.write("\n")

# ===============Développement d'application===========================
for i in range(1):
    col[0].write("\n")
col[0].write(
    """<h2 align=right><FONT color="orange">Développement </FONT></h2>""",
    unsafe_allow_html=True,
)
col[1].write(
    """<h2 align=left><FONT color="orange">d'Application</FONT></h2>""",
    unsafe_allow_html=True,
)
col[1].write("\n")
# ===============Application python===========================
col[0].subheader("Application Python")
col[0].write(
    """
    <p style="text-align: justify;"><B>
    Le projet de Biostatistique consiste à mettre en place un modèle de machine 
    learning ou statistique qui permet de faire un pronostique sur 
    la survenue instantanée de décès après le traitement.Pour la 
    construction de ce modèle, nous avons utiliser les données des patients 
    atteints d’accident cérébral vasculaire (AVC), traités et suivis.
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[1].video("Videos/arithmacie.mp4", start_time=3)
col[0].link_button(
    "Plus info",
    url="https://projetbiostatistique.streamlit.app",
)
