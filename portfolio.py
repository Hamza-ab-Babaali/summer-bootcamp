import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🚀",yout="wide",
    initial_sid
    laebar_state="expanded"
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
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚀 My Portfolio</h1>', unsafe_allow_html=True)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Home", "👤 About", "💻 Skills", "📁 Projects", "📧 Contact"]
)

# Home Page
if page == "🏠 Home":
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("https://via.placeholder.com/400x300/1f77b4/ffffff?text=Welcome+to+My+Portfolio", use_column_width=True)
        
    st.markdown("""
    ## Welcome to My Portfolio! 👋
    
    I'm a passionate developer who loves creating innovative solutions and learning new technologies.
    This portfolio showcases my skills, projects, and experience in the world of software development.
    
    ### What I Do:
    - 🎯 **Web Development** - Building responsive and modern web applications
    - 📱 **Mobile Development** - Creating intuitive mobile experiences
    - 🤖 **Machine Learning** - Developing intelligent solutions
    - 🎨 **UI/UX Design** - Crafting beautiful user interfaces
    
    Feel free to explore the different sections using the navigation sidebar!
    """)

# About Page
elif page == "👤 About":
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://via.placeholder.com/300x400/2c3e50/ffffff?text=Profile+Photo", use_column_width=True)
    
    with col2:
        st.markdown("""
        ### Hi, I'm [Your Name] 👨‍💻
        
        I'm a dedicated software developer with a passion for creating innovative solutions that make a difference. 
        With several years of experience in the tech industry, I've worked on various projects ranging from web applications 
        to machine learning solutions.
        
        **🎓 Education:**
        - Bachelor's in Computer Science
        - Master's in Software Engineering
        
        **💼 Experience:**
        - Senior Developer at Tech Company (2020-Present)
        - Full Stack Developer at Startup (2018-2020)
        - Junior Developer at Agency (2016-2018)
        
        **🌟 What drives me:**
        - Solving complex problems with elegant solutions
        - Learning new technologies and frameworks
        - Contributing to open-source projects
        - Mentoring junior developers
        
        When I'm not coding, you can find me hiking, reading tech blogs, or experimenting with new programming languages!
        """)

# Skills Page
elif page == "💻 Skills":
    st.markdown('<h2 class="section-header">Skills & Technologies</h2>', unsafe_allow_html=True)
    
    # Programming Languages
    st.subheader("🖥️ Programming Languages")
    languages = {
        "Python": 90,
        "JavaScript": 85,
        "Java": 80,
        "C++": 75,
        "Go": 70
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
    
    # Frameworks & Tools
    st.subheader("🛠️ Frameworks & Tools")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Frontend:**
        - React.js
        - Vue.js
        - Angular
        - HTML5/CSS3
        - Bootstrap
        
        **Backend:**
        - Node.js
        - Django
        - Flask
        - Express.js
        - FastAPI
        """)
    
    with col2:
        st.markdown("""
        **Databases:**
        - PostgreSQL
        - MongoDB
        - MySQL
        - Redis
        
        **DevOps:**
        - Docker
        - Kubernetes
        - AWS
        - Git
        - CI/CD
        """)
    
    # Data Visualization
    st.subheader("📊 Data Visualization")
    
    # Sample data for skills chart
    skills_data = pd.DataFrame({
        'Category': ['Frontend', 'Backend', 'Database', 'DevOps', 'Machine Learning'],
        'Proficiency': [85, 90, 80, 75, 85]
    })
    
    fig = px.bar(skills_data, x='Category', y='Proficiency', 
                  title="Skills Proficiency by Category",
                  color='Proficiency',
                  color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)

# Projects Page
elif page == "📁 Projects":
    st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)
    
    # Project 1
    st.markdown("""
    <div class="project-card">
        <h3>🌐 E-Commerce Platform</h3>
        <p><strong>Technologies:</strong> React, Node.js, MongoDB, Stripe</p>
        <p>A full-stack e-commerce platform with user authentication, product management, shopping cart, and payment processing.</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>User registration and authentication</li>
            <li>Product catalog with search and filtering</li>
            <li>Shopping cart and checkout process</li>
            <li>Admin dashboard for inventory management</li>
            <li>Payment integration with Stripe</li>
        </ul>
        <p><a href="#" style="color: #1f77b4;">View Project →</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 2
    st.markdown("""
    <div class="project-card">
        <h3>🤖 Machine Learning Dashboard</h3>
        <p><strong>Technologies:</strong> Python, Streamlit, Scikit-learn, Plotly</p>
        <p>An interactive dashboard for data analysis and machine learning model training with real-time visualization.</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Data upload and preprocessing</li>
            <li>Interactive data visualization</li>
            <li>Model training and evaluation</li>
            <li>Real-time predictions</li>
            <li>Model performance metrics</li>
        </ul>
        <p><a href="#" style="color: #1f77b4;">View Project →</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project 3
    st.markdown("""
    <div class="project-card">
        <h3>📱 Task Management App</h3>
        <p><strong>Technologies:</strong> Flutter, Firebase, Cloud Firestore</p>
        <p>A cross-platform mobile application for task and project management with real-time collaboration features.</p>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Task creation and organization</li>
            <li>Team collaboration and sharing</li>
            <li>Real-time updates and notifications</li>
            <li>Progress tracking and analytics</li>
            <li>Offline functionality</li>
        </ul>
        <p><a href="#" style="color: #1f77b4;">View Project →</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    # GitHub Stats
    st.subheader("📈 GitHub Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Repositories", "25+")
    with col2:
        st.metric("Stars", "150+")
    with col3:
        st.metric("Forks", "50+")
    with col4:
        st.metric("Contributions", "500+")

# Contact Page
elif page == "📧 Contact":
    st.markdown('<h2 class="section-header">Get In Touch</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        ### 📞 Contact Information
        
        **📧 Email:** your.email@example.com
        
        **📱 Phone:** +1 (555) 123-4567
        
        **📍 Location:** San Francisco, CA
        
        **💼 LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com)
        
        **🐙 GitHub:** [github.com/yourusername](https://github.com)
        
        **🐦 Twitter:** [@yourusername](https://twitter.com)
        """)
    
    with col2:
        st.markdown("""
        ### 📝 Send a Message
        
        Feel free to reach out if you'd like to:
        - Discuss potential collaborations
        - Ask about my projects
        - Request a consultation
        - Just say hello! 👋
        """)
        
        # Contact form
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=150)
            submit_button = st.form_submit_button("Send Message")
            
            if submit_button:
                st.success("Thank you for your message! I'll get back to you soon.")
    
    # Availability Status
    st.subheader("🟢 Current Status")
    st.info("I'm currently available for new opportunities and collaborations!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p>© 2024 My Portfolio. Built with ❤️ using Streamlit.</p>
    <p>Last updated: """ + datetime.now().strftime("%B %d, %Y") + """</p>
</div>
""", unsafe_allow_html=True) 