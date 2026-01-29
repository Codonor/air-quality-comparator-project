import streamlit as st

def run():
    st.title("Project Overview")
    st.markdown("""
    This dashboard compares air quality data from different monitoring sites in Birmingham and Bristol, UK. The data includes measurements of nitrogen oxides (NOx, NO2, NO) and ozone (O3) levels over time.
    using a subset of the Kaggle UK Air Quality dataset.

    **Objectives:**
    - Understand air quality and pollution trends  
    - Compare air quality across different sites
    - Build predictive models for air quality  
    - Provide actionable pollution insights  
    - Demonstrate a Hackathon project for Code Institute's Data Analytics course.
    """)