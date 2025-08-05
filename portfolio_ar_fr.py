import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Portfolio - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    .skill-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .project-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border: 1px solid #e9ecef;
    }
    .education-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    .tab-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚀 Portfolio - Portfolio</h1>', unsafe_allow_html=True)

# Language selector
language = st.sidebar.selectbox(
    "🌍 Language / Langue:",
    ["Français", "العربية"]
)

# Navigation tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Accueil / الرئيسية", "🎓 Éducation / التعليم", "💻 Compétences / المهارات", "📁 Projets / المشاريع"])

# Home Tab
with tab1:
    if language == "Français":
        st.markdown("""
        ## Bienvenue dans mon Portfolio! 👋
        
        Je suis un développeur passionné qui aime créer des solutions innovantes et apprendre de nouvelles technologies.
        Ce portfolio présente mes compétences, projets et expérience dans le monde du développement logiciel.
        
        ### Ce que je fais:
        - 🎯 **Développement Web** - Création d'applications web responsives et modernes
        - 📱 **Développement Mobile** - Création d'expériences mobiles intuitives
        - 🤖 **Machine Learning** - Développement de solutions intelligentes
        - 🎨 **Conception UI/UX** - Création d'interfaces utilisateur belles
        
        N'hésitez pas à explorer les différentes sections en utilisant les onglets ci-dessus!
        """)
    else:
        st.markdown("""
        ## مرحباً بكم في ملفي الشخصي! 👋
        
        أنا مطور شغوف يحب إنشاء حلول مبتكرة وتعلم تقنيات جديدة.
        يعرض هذا الملف مهاراتي ومشاريعي وخبرتي في عالم تطوير البرمجيات.
        
        ### ما أقوم به:
        - 🎯 **تطوير الويب** - بناء تطبيقات ويب متجاوبة وحديثة
        - 📱 **تطوير الجوال** - إنشاء تجارب جوال بديهية
        - 🤖 **التعلم الآلي** - تطوير حلول ذكية
        - 🎨 **تصميم واجهات المستخدم** - إنشاء واجهات جميلة
        
        لا تتردد في استكشاف الأقسام المختلفة باستخدام علامات التبويب أعلاه!
        """)

# Education Tab
with tab2:
    if language == "Français":
        st.markdown('<h2 class="section-header">🎓 Formation et Éducation</h2>', unsafe_allow_html=True)
        
        # 3AC Education
        st.markdown("""
        <div class="education-card">
            <h3>🏫 3ème Année Collégiale (3AC)</h3>
            <p><strong>Établissement:</strong> Collège Technique</p>
            <p><strong>Spécialisation:</strong> Sciences Mathématiques</p>
            <p><strong>Année:</strong> 2023-2024</p>
            <p><strong>Modules principaux:</strong></p>
            <ul>
                <li>Mathématiques avancées</li>
                <li>Sciences physiques</li>
                <li>Informatique et programmation</li>
                <li>Langues étrangères</li>
            </ul>
            <p><strong>Projets réalisés:</strong></p>
            <ul>
                <li>Projet de programmation en Python</li>
                <li>Présentation sur les algorithmes</li>
                <li>Projet de mathématiques appliquées</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional Education
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📚 Formation Continue
            
            **Cours en ligne:**
            - Python pour débutants (Coursera)
            - Introduction à Git et GitHub (Udemy)
            - Structures de données en Python (edX)
            
            **Certifications:**
            - Python Programming Certificate
            - Git Fundamentals
            - Data Structures & Algorithms
            """)
        
        with col2:
            st.markdown("""
            ### 🎯 Objectifs Académiques
            
            **Court terme:**
            - Maîtriser les frameworks web
            - Développer des projets complexes
            - Contribuer à des projets open source
            
            **Long terme:**
            - Spécialisation en IA/ML
            - Création d'une startup tech
            - Mentorat de jeunes développeurs
            """)
    
    else:
        st.markdown('<h2 class="section-header">🎓 التعليم والتكوين</h2>', unsafe_allow_html=True)
        
        # 3AC Education in Arabic
        st.markdown("""
        <div class="education-card">
            <h3>🏫 السنة الثالثة إعدادي (3AC)</h3>
            <p><strong>المؤسسة:</strong> ثانوية تقنية</p>
            <p><strong>التخصص:</strong> العلوم الرياضية</p>
            <p><strong>السنة الدراسية:</strong> 2023-2024</p>
            <p><strong>المواد الرئيسية:</strong></p>
            <ul>
                <li>الرياضيات المتقدمة</li>
                <li>العلوم الفيزيائية</li>
                <li>الإعلاميات والبرمجة</li>
                <li>اللغات الأجنبية</li>
            </ul>
            <p><strong>المشاريع المنجزة:</strong></p>
            <ul>
                <li>مشروع برمجة بلغة Python</li>
                <li>عرض حول الخوارزميات</li>
                <li>مشروع الرياضيات التطبيقية</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional Education in Arabic
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📚 التكوين المستمر
            
            **الدورات عبر الإنترنت:**
            - Python للمبتدئين (Coursera)
            - مقدمة في Git و GitHub (Udemy)
            - هياكل البيانات في Python (edX)
            
            **الشهادات:**
            - شهادة برمجة Python
            - أساسيات Git
            - هياكل البيانات والخوارزميات
            """)
        
        with col2:
            st.markdown("""
            ### 🎯 الأهداف الأكاديمية
            
            **قصيرة المدى:**
            - إتقان أطر عمل الويب
            - تطوير مشاريع معقدة
            - المساهمة في مشاريع مفتوحة المصدر
            
            **طويلة المدى:**
            - التخصص في الذكاء الاصطناعي
            - إنشاء شركة تقنية ناشئة
            - إرشاد المطورين الشباب
            """)

# Skills Tab
with tab3:
    if language == "Français":
        st.markdown('<h2 class="section-header">💻 Compétences Techniques</h2>', unsafe_allow_html=True)
        
        # Programming Languages
        st.subheader("🖥️ Langages de Programmation")
        languages = {
            "Python": 90,
            "JavaScript": 75,
            "HTML/CSS": 80,
            "SQL": 70,
            "Java": 65
        }
        
        for lang, level in languages.items():
            st.markdown(f"""
            <div class="skill-card">
                <strong>{lang}</strong>
                <div style="background-color: #e9ecef; height: 20px; border-radius: 10px; margin-top: 5px;">
                    <div style="background-color: #1f77b4; height: 20px; border-radius: 10px; width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Tools & Technologies
        st.subheader("🛠️ Outils et Technologies")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🔄 Version Control:**
            - Git (Avancé)
            - GitHub (Maîtrise complète)
            - GitLab (Intermédiaire)
            
            **📊 Structures de Données:**
            - Listes et tuples
            - Dictionnaires et sets
            - Piles et files
            - Arbres et graphes
            - Algorithmes de tri
            """)
        
        with col2:
            st.markdown("""
            **🐍 Python Libraries:**
            - NumPy et Pandas
            - Matplotlib et Seaborn
            - Streamlit et Flask
            - Tkinter (GUI)
            - Requests (API)
            
            **🛠️ Outils de Développement:**
            - VS Code / PyCharm
            - Jupyter Notebook
            - Postman (API testing)
            - Docker (Basics)
            """)
        
        # Skills Visualization
        st.subheader("📊 Visualisation des Compétences")
        
        skills_data = pd.DataFrame({
            'Catégorie': ['Python', 'Git/GitHub', 'Structures de Données', 'Web Dev', 'Machine Learning'],
            'Niveau': [90, 85, 80, 75, 70]
        })
        
        fig = px.bar(skills_data, x='Catégorie', y='Niveau', 
                      title="Niveau de Maîtrise par Compétence",
                      color='Niveau',
                      color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)
    
    else:
        st.markdown('<h2 class="section-header">💻 المهارات التقنية</h2>', unsafe_allow_html=True)
        
        # Programming Languages in Arabic
        st.subheader("🖥️ لغات البرمجة")
        languages = {
            "Python": 90,
            "JavaScript": 75,
            "HTML/CSS": 80,
            "SQL": 70,
            "Java": 65
        }
        
        for lang, level in languages.items():
            st.markdown(f"""
            <div class="skill-card">
                <strong>{lang}</strong>
                <div style="background-color: #e9ecef; height: 20px; border-radius: 10px; margin-top: 5px;">
                    <div style="background-color: #1f77b4; height: 20px; border-radius: 10px; width: {level}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Tools & Technologies in Arabic
        st.subheader("🛠️ الأدوات والتقنيات")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🔄 التحكم في الإصدارات:**
            - Git (متقدم)
            - GitHub (إتقان كامل)
            - GitLab (متوسط)
            
            **📊 هياكل البيانات:**
            - القوائم والمتتاليات
            - القواميس والمجموعات
            - المكدسات والطوابير
            - الأشجار والرسوم البيانية
            - خوارزميات الترتيب
            """)
        
        with col2:
            st.markdown("""
            **🐍 مكتبات Python:**
            - NumPy و Pandas
            - Matplotlib و Seaborn
            - Streamlit و Flask
            - Tkinter (واجهات)
            - Requests (API)
            
            **🛠️ أدوات التطوير:**
            - VS Code / PyCharm
            - Jupyter Notebook
            - Postman (اختبار API)
            - Docker (أساسيات)
            """)
        
        # Skills Visualization in Arabic
        st.subheader("📊 تصور المهارات")
        
        skills_data = pd.DataFrame({
            'الفئة': ['Python', 'Git/GitHub', 'هياكل البيانات', 'تطوير الويب', 'التعلم الآلي'],
            'المستوى': [90, 85, 80, 75, 70]
        })
        
        fig = px.bar(skills_data, x='الفئة', y='المستوى', 
                      title="مستوى الإتقان حسب المهارة",
                      color='المستوى',
                      color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)

# Projects Tab
with tab4:
    if language == "Français":
        st.markdown('<h2 class="section-header">📁 Mes Projets</h2>', unsafe_allow_html=True)
        
        # XO Game Project
        st.markdown("""
        <div class="project-card">
            <h3>🎮 Jeu XO (Tic-Tac-Toe)</h3>
            <p><strong>Technologies:</strong> Python, Tkinter, Streamlit</p>
            <p>Un jeu de morpion interactif avec interface graphique moderne et fonctionnalités avancées.</p>
            <p><strong>Fonctionnalités principales:</strong></p>
            <ul>
                <li>Interface graphique avec Tkinter</li>
                <li>Version web avec Streamlit</li>
                <li>Détection automatique du gagnant</li>
                <li>Bouton de redémarrage</li>
                <li>Design responsive et moderne</li>
                <li>Animations et effets visuels</li>
            </ul>
            <p><strong>Code source:</strong> <a href="#" style="color: #1f77b4;">Voir sur GitHub →</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Guessing Game Project
        st.markdown("""
        <div class="project-card">
            <h3>🎯 Jeu de Devinettes</h3>
            <p><strong>Technologies:</strong> Python, Random, Input/Output</p>
            <p>Un jeu de devinettes interactif où l'utilisateur doit deviner un nombre avec des indices.</p>
            <p><strong>Fonctionnalités principales:</strong></p>
            <ul>
                <li>Génération aléatoire de nombres</li>
                <li>Système de points et de vies</li>
                <li>Indices intelligents (plus grand/plus petit)</li>
                <li>Historique des tentatives</li>
                <li>Différents niveaux de difficulté</li>
                <li>Interface en ligne de commande</li>
            </ul>
            <p><strong>Code source:</strong> <a href="#" style="color: #1f77b4;">Voir sur GitHub →</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Mini Bank Project
        st.markdown("""
        <div class="project-card">
            <h3>🏦 Mini Banque Python</h3>
            <p><strong>Technologies:</strong> Python, SQLite, Classes, OOP</p>
            <p>Une application bancaire simplifiée avec gestion des comptes, transactions et historique.</p>
            <p><strong>Fonctionnalités principales:</strong></p>
            <ul>
                <li>Création et gestion de comptes bancaires</li>
                <li>Opérations de dépôt et retrait</li>
                <li>Transferts entre comptes</li>
                <li>Historique des transactions</li>
                <li>Base de données SQLite</li>
                <li>Interface utilisateur en ligne de commande</li>
                <li>Système de sécurité basique</li>
            </ul>
            <p><strong>Code source:</strong> <a href="#" style="color: #1f77b4;">Voir sur GitHub →</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Project Statistics
        st.subheader("📈 Statistiques des Projets")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Projets", "3")
        with col2:
            st.metric("Lignes de Code", "500+")
        with col3:
            st.metric("Technologies", "5+")
        with col4:
            st.metric("Heures de Dev", "50+")
    
    else:
        st.markdown('<h2 class="section-header">📁 مشاريعي</h2>', unsafe_allow_html=True)
        
        # XO Game Project in Arabic
        st.markdown("""
        <div class="project-card">
            <h3>🎮 لعبة XO (إكس أو)</h3>
            <p><strong>التقنيات:</strong> Python, Tkinter, Streamlit</p>
            <p>لعبة إكس أو تفاعلية مع واجهة رسومية حديثة وميزات متقدمة.</p>
            <p><strong>الميزات الرئيسية:</strong></p>
            <ul>
                <li>واجهة رسومية مع Tkinter</li>
                <li>إصدار ويب مع Streamlit</li>
                <li>اكتشاف تلقائي للفائز</li>
                <li>زر إعادة تشغيل</li>
                <li>تصميم متجاوب وحديث</li>
                <li>رسوم متحركة وتأثيرات بصرية</li>
            </ul>
            <p><strong>الكود المصدري:</strong> <a href="#" style="color: #1f77b4;">عرض على GitHub →</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Guessing Game Project in Arabic
        st.markdown("""
        <div class="project-card">
            <h3>🎯 لعبة التخمين</h3>
            <p><strong>التقنيات:</strong> Python, Random, Input/Output</p>
            <p>لعبة تخمين تفاعلية حيث يجب على المستخدم تخمين رقم مع تلميحات.</p>
            <p><strong>الميزات الرئيسية:</strong></p>
            <ul>
                <li>توليد أرقام عشوائية</li>
                <li>نظام النقاط والحياة</li>
                <li>تلميحات ذكية (أكبر/أصغر)</li>
                <li>سجل المحاولات</li>
                <li>مستويات صعوبة مختلفة</li>
                <li>واجهة سطر الأوامر</li>
            </ul>
            <p><strong>الكود المصدري:</strong> <a href="#" style="color: #1f77b4;">عرض على GitHub →</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Mini Bank Project in Arabic
        st.markdown("""
        <div class="project-card">
            <h3>🏦 بنك مصغر بلغة Python</h3>
            <p><strong>التقنيات:</strong> Python, SQLite, Classes, OOP</p>
            <p>تطبيق بنكي مبسط مع إدارة الحسابات والمعاملات والسجل.</p>
            <p><strong>الميزات الرئيسية:</strong></p>
            <ul>
                <li>إنشاء وإدارة الحسابات البنكية</li>
                <li>عمليات الإيداع والسحب</li>
                <li>التحويلات بين الحسابات</li>
                <li>سجل المعاملات</li>
                <li>قاعدة بيانات SQLite</li>
                <li>واجهة مستخدم سطر الأوامر</li>
                <li>نظام أمان أساسي</li>
            </ul>
            <p><strong>الكود المصدري:</strong> <a href="#" style="color: #1f77b4;">عرض على GitHub →</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Project Statistics in Arabic
        st.subheader("📈 إحصائيات المشاريع")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("المشاريع", "3")
        with col2:
            st.metric("أسطر الكود", "500+")
        with col3:
            st.metric("التقنيات", "5+")
        with col4:
            st.metric("ساعات التطوير", "50+")

# Footer
st.markdown("---")
if language == "Français":
    st.markdown(f"""
    <div style="text-align: center; color: #666; padding: 2rem 0;">
        <p>© 2024 Mon Portfolio. Créé avec ❤️ en utilisant Streamlit.</p>
        <p>Dernière mise à jour: {datetime.now().strftime("%B %d, %Y")}</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div style="text-align: center; color: #666; padding: 2rem 0;">
        <p>© 2024 ملفي الشخصي. تم إنشاؤه بـ ❤️ باستخدام Streamlit.</p>
        <p>آخر تحديث: {datetime.now().strftime("%B %d, %Y")}</p>
    </div>
    """, unsafe_allow_html=True) 