import streamlit as st

st.markdown(
    """<p style="text-align: justify;"><B>Dans cette page, vous pouvez consulter 
    les différentes projets sur lesquels</B></p>""",
    unsafe_allow_html=True,
)
st.write(
    """<h2 align=center><FONT color="orange">Réalisation des projets avec Python</FONT></h2>""",
    unsafe_allow_html=True,
)
st.write("\n")

col = st.columns(2)
# =============Projets Biostatistiques=======================
for i in range(1):
    col[0].write("\n")
for i in range(6):
    col[1].write("\n")
col[0].write(
    """<h4 align=left><FONT color="orange">Biostatistique</FONT></h4>""",
    unsafe_allow_html=True,
)
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
col[1].image("static/biosta.jpeg")
col[0].link_button("Plus info", url="https://projetbiostatistique.streamlit.app")

for i in range(3):
    col[0].write("\n")
for i in range(1):
    col[1].write("\n")

# ========Projet Series Temporelles=================
col[1].write(
    """<h4 align=left><FONT color="orange">Série Temporelle</FONT></h4>""",
    unsafe_allow_html=True,
)
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
col[0].image("static/series temporelles.png")
col[1].link_button(
    "Plus info",
    url="",
)

# ========MODELISATION AVEC SPSS=================


# ===========ANALYSE DE DONNÉES==============
for i in range(1):
    col[1].write("\n")
for i in range(1):
    col[0].write("\n")
col[0].write(
    """<h2 align=right><FONT color="orange">Analyse de</FONT></h2>""",
    unsafe_allow_html=True,
)
col[1].write(
    """<h2 align=left><FONT color="orange">données</FONT></h2>""",
    unsafe_allow_html=True,
)
# ============Projet power BI==============
for i in range(1):
    col[0].write("\n")
col[0].write(
    """<h4 align=left><FONT color="orange">Analyse des ventes</FONT></h4>""",
    unsafe_allow_html=True,
)
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
col[1].image("static/ID Global Busness/Accessoire ID Global.jpg", use_column_width=True)
col[0].link_button(
    "Plus info",
    url="",
)

# =============Projet excel=============
col[0].write("\n")
for i in range(1):
    col[1].write("\n")
col[1].write(
    """<h4 align=left><FONT color="orange">Dashboard RNU Excel</FONT></h4>""",
    unsafe_allow_html=True,
)
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
col[0].image("static/Departement de Kaffine.jpg")
col[1].link_button("Plus info", url="https://projetbiostatistique.streamlit.app")
st.write("\n")

# ===============Développement d'application===========================
for i in range(3):
    col[0].write("\n")
col[0].write(
    """<h2 align=right><FONT color="orange">Développement </FONT></h2>""",
    unsafe_allow_html=True,
)
col[1].write(
    """<h2 align=left><FONT color="orange">d'Application</FONT></h2>""",
    unsafe_allow_html=True,
)
for i in range(4):
    col[1].write("\n")
# ===============Application python===========================
col[0].write(
    """<h4 align=left><FONT color="orange">Application Python</FONT></h4>""",
    unsafe_allow_html=True,
)
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
