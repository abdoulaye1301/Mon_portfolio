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
    Les objectifs attendus dans cette étude sont nombreux.
    Parmi lesquelles, nous pouvons citer tout d’abord, 
    l’étude de la tendance de la série en utilisant un 
    modèle linéaire simple et multiple. Ensuite de faire 
    une prédiction de la production électrique pour les 
    années à venir en utilisant les processus ARIMA et la 
    méthode de lissage exponentiel et enfin de fournir des résultats 
    fiables qui pourrons aider les décideurs à prendre des décisions éclairées 
    sur la production d’électrique.
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[0].image("static/series temporelles.png")
col[0].write(
    """
    <p style="text-align: justify;"><B>
    Dans cette étude, nous allons à modéliser les données de la 
    production électrique mensuelle d’un pays entre 1985 et 2018.
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[1].link_button(
    "Plus info",
    url="",
)

# ========MODELISATION AVEC SPSS=================


# ===========ANALYSE DE DONNÉES==============
for i in range(3):
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

col[0].write(
    """<h4 align=left><FONT color="orange">Analyse des ventes</FONT></h4>""",
    unsafe_allow_html=True,
)

col[0].write(
    """
    <p style="text-align: justify;"><B>
    Dans cette étude, l'objectif est de metter en place
    un tableau de bord pour avoir une vue globale 
    l'évolution des ventes de ID GLOBA BUSNESS. Pour
    ce fait nous avons répondu quelques questions qui sont :<br>
    1- Quelle est la dépence totale effectuée depuis l'instalation de l'entreprise ID GLOBAL BUSNESS ?<br>
    2- Quelle est la dépence effectuée après l'instalation de l'entreprise ID GLOBAL BUSNESS ?<br>
    3- Quels sont les produits les plus vendus ?<br>
    4- Quels sont les produits qui apportent plus de chiffre d'affaire ?<br>
    5- Quels est le porcentage de ventes par années ?<br>
    6- Quels sont les produits cosmétiques les plus vendus ?<br>
    </B></p>
    """,
    unsafe_allow_html=True,
)
for i in range(3):
    col[1].write("\n")
col[1].image("static/Accessoire ID Global.jpg", use_column_width=True)
col[1].write(
    """
    <p style="text-align: justify;"><B>
    7- Quels sont les produits cosmétiques qui apportent plus de chiffre d'affaire ?<br>
    8- Quels est le bénéfice totale de l'entreprise ?<br>
    9- Quels est le bénéfice des produits ?<br>
    10- Quels est le bénéfice des produits cosmétiques ?<br>
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[0].link_button(
    "Plus info",
    url="",
)

# =============Projet excel=============
for i in range(1):
    col[1].write("\n")
col[1].write(
    """<h4 align=left><FONT color="orange">Dashboard RNU Excel</FONT></h4>""",
    unsafe_allow_html=True,
)
for i in range(1):
    col[1].write("\n")
col[1].write(
    """
    <p style="text-align: justify;"><B>
    l'évolution des enquetes au près de l'ensemble des ménages des 
    quatre (4) communes du département de Kaffrine. L'objectif de ce travail est d'avoir 
    une vue globale sur la progression des enquetes au près des ménages pour mener à bien la
    réalisation du projet d'enquete dans le cadre de la mise à jours et extention
    du Registre National Unique (RNU).
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[0].image("static/Departement de Kaffine.jpg")

col[0].write(
    """
    <p style="text-align: justify;"><B>
    Ce travail consiste à mettre en place un tableau de bord qui va nous permetre de suivre en temps réel 
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[1].link_button(
    "Plus info",
    url="",
)
st.write("\n")

# ===============Développement d'application===========================

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
    Cette étude consiste à mettre en place une application Arithmanceur.
    L’arithmancie ou l’arithmomancie est une technique de divination basée 
    sur les nombres de 1 à 9.Le plus souvent, il s’agit de transformer le 
    prénom et le nom des gens en une suite de chiffres pour
    obtenir ce qu’on appelle le nombre d’expression, le nombre intime et 
    le nombre de réalisation. Chacun de ces nombres est ensuite analysé.
    Pour ce fair, nous allons faire un contrôle de saisie pour gérer les 
    entrées de l’utilisateur. Nous forcerons aussi l’utilisateur à entrer 
    une chaîne de caractère comportant uniquement
    l’alphabet latin (a - z) ou (A - Z).
    </B></p>
    """,
    unsafe_allow_html=True,
)
col[1].image("static/arithmacie.jpg")
col[1].write("\n")
col[1].link_button(
    "Plus info",
    url="",
)
