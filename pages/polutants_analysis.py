 import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def run():
    st.title("Sensor Level Diagnostics")

    df = pd.read_csv("data/rul_predictions_fd001.csv")

        # --- Plotly sensor chart ---
    st.markdown(f"### {selected_sensor} Over Time (Interactive)")
    fig_sensor = px.line(
        engine_data,
        x="cycle",
        y="smooth",
        title=f"{selected_sensor} (Smoothed)",
        markers=True
    )
    st.plotly_chart(fig_sensor, use_container_width=True)

    # --- Summary statistics ---
    st.markdown("### Summary Statistics")
    st.write(engine_data[selected_sensor].describe())

    # --- Correlation heatmap ---
    st.markdown("### Sensor Correlation Heatmap")

    corr = df[sensor_cols].corr()

    fig_heatmap = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Sensor Correlation Matrix"
    )

    st.plotly_chart(fig_heatmap, use_container_width=True)