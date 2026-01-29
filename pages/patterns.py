import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Patterns", layout="wide")
st.title("Patterns: Daily + Seasonal + Heatmaps")


df = st.session_state["df"].copy()
df.index = pd.to_datetime(df.index)
df = df.sort_index()

# Ensure numeric
for c in ["nox", "no2", "o3"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

sites = sorted(df["site"].dropna().unique().tolist())
pollutants = [c for c in ["nox", "no2", "o3"] if c in df.columns]

#Sidebar controls
st.sidebar.header("Controls")
pollutant = st.sidebar.selectbox("Pollutant", pollutants, index=0)
site_mode = st.sidebar.radio("Sites", ["One site", "Compare all sites"], horizontal=False)

if site_mode == "One site":
    site = st.sidebar.selectbox("Site", sites, index=0)
    dff = df[df["site"] == site]
    site_label = site
else:
    dff = df.copy()
    site_label = "All sites"

# Date range
min_date = dff.index.min().date()
max_date = dff.index.max().date()
date_from, date_to = st.sidebar.slider(
    "Date range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
)
mask = (dff.index >= pd.to_datetime(date_from)) & (
    dff.index <= pd.to_datetime(date_to) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)
)
dff = dff.loc[mask].dropna(subset=[pollutant])

# Add time features
dff = dff.assign(
    hour=dff.index.hour,
    month=dff.index.month,
    month_name=dff.index.strftime("%b"),
)

# tabs
tab1, tab2, tab3 = st.tabs(["Daily cycle", "Seasonal cycle", "Hour × Month heatmap"])

#TAB 1: Daily cycle
with tab1:
    st.subheader("Daily cycle (average by hour of day)")

    if site_mode == "One site":
        diurnal = dff.groupby("hour")[pollutant].mean().reset_index()
        fig = px.line(diurnal, x="hour", y=pollutant, markers=True)
        fig.update_layout(
            xaxis_title="Hour of day",
            yaxis_title="Concentration",
            title=f"{pollutant.upper()} diurnal cycle — {site_label}",
            hovermode="x unified",
        )
        st.plotly_chart(fig, use_container_width=True)

    else:
        diurnal = dff.groupby(["site", "hour"])[pollutant].mean().reset_index()
        fig = px.line(diurnal, x="hour", y=pollutant, color="site")
        fig.update_layout(
            xaxis_title="Hour of day",
            yaxis_title="Concentration",
            title=f"{pollutant.upper()} diurnal cycle — compare sites",
            hovermode="x unified",
        )
        st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "Tip: NOx/NO2 often show rush-hour peaks, as it's mostly coming from cars"
    )

# TAB 2: Seasonal cycle
with tab2:
    st.subheader("Seasonal cycle (average by month)")

    # Keep months ordered 1..12
    month_order = list(range(1, 13))
    month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    if site_mode == "One site":
        seasonal = dff.groupby("month")[pollutant].mean().reindex(month_order).reset_index()
        seasonal["month_name"] = month_names
        fig = px.line(seasonal, x="month_name", y=pollutant, markers=True)
        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Concentration",
            title=f"{pollutant.upper()} seasonal cycle — {site_label}",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        seasonal = (
            dff.groupby(["site", "month"])[pollutant].mean()
            .reset_index()
        )
        seasonal["month_name"] = seasonal["month"].map({i: month_names[i-1] for i in month_order})
        fig = px.line(seasonal, x="month_name", y=pollutant, color="site")
        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Concentration",
            title=f"{pollutant.upper()} seasonal cycle — compare sites",
        )
        st.plotly_chart(fig, use_container_width=True)

# TAB 3: Hour × Month heatmap - I thought this might be intersting, not sure how useful it actually is
with tab3:
    st.subheader("Hour × Month heatmap (mean concentration)")

    heat_site_mode = st.radio(
        "Heatmap scope",
        ["Use current selection", "Pick a single site (recommended for heatmap)"],
        horizontal=True,
    )

    if heat_site_mode == "Pick a single site (recommended for heatmap)":
        hs = st.selectbox("Heatmap site", sites, index=0)
        hdf = df[df["site"] == hs].copy()
        hdf.index = pd.to_datetime(hdf.index)
        hdf = hdf.sort_index()
        hdf = hdf.loc[
            (hdf.index >= pd.to_datetime(date_from))
            & (hdf.index <= pd.to_datetime(date_to) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1))
        ]
        hdf[pollutant] = pd.to_numeric(hdf[pollutant], errors="coerce")
        hdf = hdf.dropna(subset=[pollutant])
        hdf = hdf.assign(hour=hdf.index.hour, month=hdf.index.month)
        heat_title_site = hs
    else:
        hdf = dff.copy()
        heat_title_site = site_label

    pivot = (
        hdf.groupby(["hour", "month"])[pollutant]
        .mean()
        .unstack("month")
        .reindex(index=range(0, 24), columns=range(1, 13))
    )

    # Prettifying axes
    pivot.columns = month_names
    pivot.index = [f"{h:02d}:00" for h in pivot.index]

    fig = px.imshow(
        pivot,
        aspect="auto",
        labels=dict(x="Month", y="Hour of day", color="Mean"),
        title=f"{pollutant.upper()} mean by hour & month — {heat_title_site}",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.caption("This compresses years of data into a single graphic")

