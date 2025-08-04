import streamlit as st
import json
from PIL import Image

# Load French content
with open("content_fr.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Load profile image
profile_image = Image.open("profile.jpg")

# Page config
st.set_page_config(page_title=f"{data['about']['name']} | Portfolio Développeur", layout="wide")

# Sidebar Navigation
st.sidebar.image(profile_image, width=150)
st.sidebar.title(f"Portfolio de {data['about']['name']}")
tabs = ["Présentation", "À propos", "Éducation", "Certifications", "Projets", "Compétences", "Langues", "Loisirs", "LeetCode"]
selected_tab = st.sidebar.radio("Navigation", tabs)

# --- Présentation ---
if selected_tab == "Présentation":
    st.title("👋 Bienvenue !")
    st.write(data.get("overview", ""))

# --- À propos ---
elif selected_tab == "À propos":
    st.title("👤 À propos de moi")
    st.image(profile_image, width=200)
    st.markdown(f"*Nom:* {data['about']['name']}")
    st.markdown(f"*Email:* {data['about']['email']}")
    st.write(data['about']['description'])
    st.markdown("---")
    st.subheader("Mes objectifs")
    st.write(data['about']['goals'])

# --- Éducation ---
elif selected_tab == "Éducation":
    st.title("🎓 Éducation")
    for edu in data['education']:
        st.subheader(edu['institution'])
        st.write(f"*Diplôme:* {edu['degree']}")
        st.write(f"*Année:* {edu['year']}")
        st.markdown("---")

# --- Certifications ---
elif selected_tab == "Certifications":
    st.title("📜 Certifications")
    for cert in data['certifications']:
        st.subheader(cert['title'])
        st.write(f"Émis par : *{cert['issuer']}*")
        st.write(f"Année : {cert['year']}")
        if cert.get("link"):
            st.markdown(f"[🔗 Voir la certification]({cert['link']})")
        st.markdown("---")

# --- Projets ---
elif selected_tab == "Projets":
    st.title("🛠 Projets")
    for project in data['projects']:
        st.subheader(project['title'])
        st.write(project['description'])
        if project.get("link"):
            st.markdown(f"[🔗 Lien du projet]({project['link']})")
        st.markdown("---")
    st.markdown("### 🔗 Tous mes projets sur GitHub")
    st.markdown("[GitHub Profile](https://github.com/hamza)")

# --- Compétences ---
elif selected_tab == "Compétences":
    st.title("💼 Compétences")
    st.subheader("Langages & Outils")
    st.write(", ".join(data['skills']['languages']))
    st.subheader("Stack Technique")
    st.write(", ".join(data['skills']['tech_stack']))

# --- Langues ---
elif selected_tab == "Langues":
    st.title("🌍 Langues")
    for lang in data['languages']:
        st.write(f"- {lang}")

# --- Loisirs ---
elif selected_tab == "Loisirs":
    st.title("🎯 Loisirs et Intérêts")
    for hobby in data['hobbies']:
        st.write(f"- {hobby}")

# --- LeetCode ---
elif selected_tab == "LeetCode":
    st.title("🧩 Problèmes LeetCode résolus")
    st.write(f"Nombre total de problèmes résolus : *{data['leetcode']['count']}*")
    st.markdown(f"[🔗 Voir mes solutions LeetCode sur GitHub]({data['leetcode']['link']})")

