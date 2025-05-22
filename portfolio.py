import streamlit as st
from streamlit.components.v1 import html

# Set page config
st.set_page_config(
    page_title="Kashish Bhasin - Business Analyst Intern Application",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .header {
            font-size: 2.5em;
            color: #FFC0CB;
            border-bottom: 2px solid #FFC0CB;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .section-header {
            font-size: 1.8em;
            color: #FFC0CB;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        .highlight {
            background-color: #E37383;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .skill-item {
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }
        .cta-button {
            background-color: #E0115F !important;
            color: white !important;
            font-weight: bold !important;
            padding: 10px 20px !important;
            border-radius: 5px !important;
            margin-top: 30px !important;
        }
        .project-card {
            border-left: 4px solid #FFC0CB;
            padding-left: 15px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="header">Kashish Bhasin</div>', unsafe_allow_html=True)
    st.markdown('**Aspiring Business Analyst | Data-Driven Problem Solver**')
    st.markdown('*BTech in Computer Science with AI/ML specialization with hands-on projects in data analysis, process optimization, and AI automation*')

with col2:
    st.write("")  # Empty for layout balance

# Navigation Sidebar
with st.sidebar:
    st.markdown("## Navigation")
    nav_option = st.radio("", ["About Me", "Skills", "Projects", "Why LithionPower?", "Contact"])
    
    st.markdown("---")
    st.markdown("### Application Progress")
    progress = st.progress(0)
    if nav_option == "About Me":
        progress.progress(20)
    elif nav_option == "Skills":
        progress.progress(40)
    elif nav_option == "Projects":
        progress.progress(60)
    elif nav_option == "Why LithionPower?":
        progress.progress(80)
    else:
        progress.progress(100)

# About Me Section
if nav_option == "About Me":
    st.markdown('<div class="section-header">About Me</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
        <ul>
            <li>Pursuing BTech in Computer Science Engineering with AI/ML specialization at Manipal University Jaipur (CGPA: 9.29)</li>
            <li>Strong analytical skills demonstrated through multiple internships (DRDO, IIM Bangalore) and AI projects with measurable impact</li>
            <li>Eager to apply my technical skills in Python, data analysis, and process optimization to business challenges</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Education")
    with st.expander("View Education Details"):
        st.markdown("""
        - **BTech in Computer Science Engineering - AI/ML**  
          *Manipal University Jaipur* | Sept 2022 - Present  
          CGPA: 9.29 | Relevant Coursework: Machine Learning, NLP, Data Mining, Algorithms, DBMS
        
        - **Lotus Valley International School, Noida**  
          Class 12: 93.8% | Class 10: 94.6%
        """)

# Skills Section
elif nav_option == "Skills":
    st.markdown('<div class="section-header">Skills</div>', unsafe_allow_html=True)
    
    st.markdown("### Technical Tools")
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.markdown('<div class="skill-item">✅ <strong>Python</strong> <em>(Advanced)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Core skill for data analysis and automation")
        
        st.markdown('<div class="skill-item">✅ <strong>SQL</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Essential for database querying and analysis")
        
        st.markdown('<div class="skill-item">✅ <strong>Excel</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Fundamental for business reporting and analysis")
    
    with tech_col2:
        st.markdown('<div class="skill-item">✅ <strong>Tableau</strong> <em>(Basic)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Data visualization and dashboard creation")
        
        st.markdown('<div class="skill-item">✅ <strong>PowerPoint</strong> <em>(Intermediate)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Presentation of business insights")
        
        st.markdown('<div class="skill-item">✅ <strong>Microsoft Azure AI</strong> <em>(Basic)</em></div>', unsafe_allow_html=True)
        st.caption("Relevance: Cloud-based AI solutions for business problems")
    
    st.markdown("### Soft Skills")
    soft_col1, soft_col2 = st.columns(2)
    
    with soft_col1:
        st.markdown('<div class="skill-item">✅ <strong>Analytical Thinking</strong></div>', unsafe_allow_html=True)
        st.caption("Relevance: Critical for business problem-solving")
        
        st.markdown('<div class="skill-item">✅ <strong>Process Mapping</strong></div>', unsafe_allow_html=True)
        st.caption("Relevance: Essential for workflow optimization")
    
    with soft_col2:
        st.markdown('<div class="skill-item">✅ <strong>Communication</strong></div>', unsafe_allow_html=True)
        st.caption("Relevance: Key for stakeholder management")
        
        st.markdown('<div class="skill-item">✅ <strong>Agile Methodology</strong></div>', unsafe_allow_html=True)
        st.caption("Relevance: Important for project management")

# Projects Section
elif nav_option == "Projects":
    st.markdown('<div class="section-header">Projects</div>', unsafe_allow_html=True)
    
    project_option = st.selectbox(
        "Select a project to view details:",
        ["AI-Powered Resume Analysis System", "Web Scraping Tool for IIM Bangalore", "RAG System for DRDO"]
    )
    
    if project_option == "AI-Powered Resume Analysis System":
        st.markdown("""
        <div class="project-card">
            <h4>AI-Powered Resume Analysis System</h4>
            <p><strong>Problem:</strong> Manual resume screening is time-consuming and inconsistent</p>
            <p><strong>Solution:</strong> Built an AI system using Python, Streamlit, and Google Gemini API for automated resume analysis</p>
            <p><strong>Impact:</strong> Improved keyword matching accuracy to 65% through user feedback and data analytics</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif project_option == "Web Scraping Tool for IIM Bangalore":
        st.markdown("""
        <div class="project-card">
            <h4>Web Scraping Tool for IIM Bangalore</h4>
            <p><strong>Problem:</strong> Manual data extraction was inefficient for large datasets</p>
            <p><strong>Solution:</strong> Developed a Python-based web scraping tool with 92% accuracy</p>
            <p><strong>Impact:</strong> Automated extraction of 7-9 Cr beneficiary records, reducing processing time by 50%</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif project_option == "RAG System for DRDO":
        st.markdown("""
        <div class="project-card">
            <h4>RAG System for DRDO Procurement Manual</h4>
            <p><strong>Problem:</strong> Inefficient document retrieval in large manuals</p>
            <p><strong>Solution:</strong> Developed a Retrieval-Augmented Generation system using LangChain and ChromaDB</p>
            <p><strong>Impact:</strong> Improved document retrieval efficiency by 70% and reduced search time by 50%</p>
        </div>
        """, unsafe_allow_html=True)

# Why LithionPower Section
elif nav_option == "Why LithionPower?":
    st.markdown('<div class="section-header">Why LithionPower?</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
        <p>Your focus on <strong>operational efficiency</strong> in the energy sector aligns perfectly with my experience in:</p>
        <ul>
            <li>Process optimization (reducing manual processing time by 50% at IIM Bangalore)</li>
            <li>Data-driven decision making (delivered analytical reports improving strategic alignment by 23%)</li>
            <li>AI-powered automation (developed systems that improved efficiency by 35-40% in multiple projects)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### How I Can Contribute")
    
    with st.expander("Process Optimization"):
        st.markdown("""
        - Experience redesigning workflows at Arogo AI and IIM Bangalore
        - Strong background in identifying inefficiencies and implementing solutions
        - Technical skills to automate repetitive tasks and processes
        """)
    
    with st.expander("Data Analysis & Reporting"):
        st.markdown("""
        - Built data pipelines that reduced processing time by 50%
        - Created dashboards and reports that improved decision-making
        - Experience with both technical and business stakeholders
        """)
    
    with st.expander("Technical Implementation"):
        st.markdown("""
        - Hands-on experience implementing AI/ML solutions in real-world scenarios
        - Ability to bridge the gap between technical teams and business needs
        - Quick learner able to adapt to new tools and technologies
        """)

# Contact Section
else:
    st.markdown('<div class="section-header">Contact</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="line-height: 2;">
        <p>📧 <strong>Email:</strong> kashishbhasinn@gmail.com</p>
        <p>🔗 <strong>LinkedIn:</strong> <a href="https://linkedin.com/in/kashish-bhasin" target="_blank">linkedin.com/in/kashish-bhasin</a></p>
        <p>📱 <strong>Phone:</strong> (+91) 9811149303</p>
        <p>💻 <strong>GitHub:</strong> <a href="https://github.com/kashishbhasinn" target="_blank">github.com/kashishbhasinn</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Availability")
    st.markdown("""
    - Immediately available for internship opportunities
    - Flexible with work arrangements (remote/hybrid/onsite)
    - Committed to contributing from Day 1 with minimal ramp-up time
    """)

# "Hire Me" CTA Button
if st.button("Hire Me!", key="hire_me", help="Click to show your interest"):
    st.success("Ready to contribute from Day 1! 🚀")
    st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
    <p>© 2025 Kashish Bhasin</p>
</div>
""", unsafe_allow_html=True)
