import streamlit as st
import pandas as pd
import plotly.express as px

def run():
    st.title("Insights & Recommendations")

    # --- Load feature importance ---
    fi = pd.read_csv("data/feature_importance_fd001.csv")

    st.markdown("### Feature Importance (Random Forest Regressor)")
    fig = px.bar(
        fi,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance",
        height=600
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Interpretation:**  
    - Features at the top contribute most to predicting NOx levels  
    - Low importance features may be redundant  
    - High importance features are strong candidates for monitoring  
    """)

        # --- Additional insights ---
    st.markdown("### Key Insights")
    st.write("""
    - Random Forest identifies key features influencing NOx levels
    - Temperature and pressure-related sensors are highly predictive
    - Some sensors show minimal impact and could be deprioritised

    ### Recommendations        
    - Regularly review model performance and retrain as needed
    - Explore feature engineering to enhance predictive power  
    - Consider integrating real-time sensor data for live predictions



    ### Next Steps
    - Expand to other sensor sites in the dataset.
    - Try Gradient Boosting or XGBoost models for better performance.
   

    """)
