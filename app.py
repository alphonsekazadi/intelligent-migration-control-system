import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Configuration de la page
st.set_page_config(layout="wide", page_title="Contrôle Migratoire DGM Mbujimayi")

# CSS intégré
st.markdown("""
    <style>
        /* Fond général */
        body, .stApp {
            background-color: whitesmoke;
            color: black;
        }

        /* Titres en orange */
        h1, h2, h3, h4 {
            color: orange;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #1e1e1e;
            color: white;
        }

        /* Boutons */
        button {
            background-color: orange !important;
            color: black !important;
            font-weight: bold;
            padding: 2em;
            border: none !important;
            border-radius: 4px;
        }

        button:hover {
            background-color: #ff9900 !important;
            color: white !important;
        }

        /* Metrics */
        [data-testid="metric-container"] {
            background-color: #222;
            border-radius: 0.5rem;
            padding: 1rem;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Chargement du modèle et des données
model = joblib.load("model_risque.pkl")
encoders = joblib.load("encoders.pkl")
target_encoder = joblib.load("target_encoder.pkl")
df = pd.read_csv("donnees_migratoires_mbujimayi.csv")

# Sidebar
with st.sidebar:
    st.markdown("## À propos du système")
    st.markdown("Ce système utilise l'intelligence artificielle pour évaluer automatiquement le risque des voyageurs entrant à Mbujimayi.")
    st.markdown("---")
    st.button("Recharger les données")
    st.button("Voir statistiques globales")
    st.button("Documentation")
    st.markdown("---")
    st.write("**Développé par** : Un groupe d'étudiants de L3 LMD INFORMATIQUE. Année 2025")

# Titre principal
st.markdown("<h1>Système Intelligent de Contrôle Migratoire - DGM Mbujimayi</h1>", unsafe_allow_html=True)

# Onglets
tab1, tab2, tab3 = st.tabs(["Tableau de Bord", "Contrôle des Voyageurs", "Gestion des Données"])

# ----------- Onglet 1 : Tableau de Bord --------------
with tab1:
    st.markdown("<h2>Statistiques Globales</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Nombre total de voyageurs", len(df))
    col2.metric("Risque élevé (%)", f"{(df['niveau_risque']=='Élevé').mean()*100:.1f}%")
    col3.metric("Pays le plus fréquent", df['pays_origine'].mode()[0])

    st.plotly_chart(
        px.pie(df, names='niveau_risque', title="Répartition des niveaux de risque"),
        use_container_width=True
    )

    st.plotly_chart(
        px.histogram(df, x="pays_origine", color="niveau_risque", barmode="group",
                     title="Voyageurs par pays et niveau de risque"),
        use_container_width=True
    )

# ----------- Onglet 2 : Contrôle des Voyageurs --------------
with tab2:
    st.markdown("<h2>Analyser un voyageur</h2>", unsafe_allow_html=True)
    with st.form("formulaire"):
        age = st.slider("Âge", 18, 70, 30)
        sexe = st.selectbox("Sexe", encoders['sexe'].classes_)
        pays = st.selectbox("Pays d'origine", encoders['pays_origine'].classes_)
        raison = st.selectbox("Raison du voyage", encoders['raison_voyage'].classes_)
        provenance = st.selectbox("Ville de provenance", encoders['provenance'].classes_)
        destination = st.selectbox("Ville de destination", encoders['destination'].classes_)
        papiers_valides = st.checkbox("Papiers valides ?", value=True)
        casier = st.checkbox("Casier judiciaire ?", value=False)

        submit = st.form_submit_button("Analyser")

    if submit:
        input_data = {
            "age": age,
            "sexe": encoders['sexe'].transform([sexe])[0],
            "pays_origine": encoders['pays_origine'].transform([pays])[0],
            "raison_voyage": encoders['raison_voyage'].transform([raison])[0],
            "provenance": encoders['provenance'].transform([provenance])[0],
            "destination": encoders['destination'].transform([destination])[0],
            "papiers_valides": int(papiers_valides),
            "casier_judiciaire": int(casier),
        }
        df_input = pd.DataFrame([input_data])
        prediction = model.predict(df_input)[0]
        risque = target_encoder.inverse_transform([prediction])[0]

        color = {"Faible": "green", "Moyen": "orange", "Élevé": "red"}[risque]
        st.markdown(f"### Niveau de risque : <span style='color:{color}'>{risque}</span>", unsafe_allow_html=True)

        # Informations complémentaires
        st.markdown("#### Informations complémentaires")
        st.write("**Âge :**", age)
        st.write("**Sexe :**", sexe)
        st.write("**Pays d'origine :**", pays)
        st.write("**Ville de provenance :**", provenance)
        st.write("**Ville de destination :**", destination)
        st.write("**Raison du voyage :**", raison)
        st.write("**Papiers valides :**", "Oui" if papiers_valides else "Non")
        st.write("**Casier judiciaire :**", "Oui" if casier else "Non")

# ----------- Onglet 3 : Données --------------
with tab3:
    st.markdown("<h2>Jeu de Données Utilisé</h2>", unsafe_allow_html=True)
    st.dataframe(df.head(100), use_container_width=True)
    st.download_button("Télécharger CSV", df.to_csv(index=False), file_name="donnees_migratoires.csv")

    if st.button("Autres informations"):
        st.warning("Ce système est conçu dans le cadre du projet tutoré 3")

