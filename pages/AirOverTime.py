import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

df = pd.read_csv(r"data/air_brum_bris_cleaned_dates")


df = pd.read_csv(r"data/air_brum_bris_cleaned_dates",
    parse_dates=["date"],
)
df = df.set_index("date")
st.session_state["df"] = df

@st.cache_data
def prep_df(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    d.index = pd.to_datetime(d.index)
    d = d.sort_index()


    for c in ["nox", "no2", "o3"]:
        if c in d.columns:
            d[c] = pd.to_numeric(d[c], errors="coerce")

    return d

def rolling_timeseries(site_df: pd.DataFrame, pollutant: str, mode: str, roll_window: int) -> pd.Series:
    s = site_df[pollutant].dropna()

    if mode == "Hourly (raw)":
        return s

    if mode == "Daily mean":
        return s.resample("D").mean()


    daily = s.resample("D").mean()
    return daily.rolling(window=roll_window, min_periods=max(2, roll_window // 4)).mean()

def make_fig(series: pd.Series, title: str) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=series.index,
        y=series.values,
        mode="lines",
        name=series.name if series.name else "value",
    ))
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Concentration",
        height=500,
        hovermode="x unified",
        margin=dict(l=40, r=20, t=60, b=40),
    )
    return fig


st.title("Air Quality over time")


df = prep_df(st.session_state["df"])

sites = sorted(df["site"].dropna().unique().tolist())
pollutants = [c for c in ["nox", "no2", "o3"] if c in df.columns]

left, mid, right = st.columns([1.2, 1.2, 2.2])

with left:
    site = st.selectbox("Site", sites, index=0)

with mid:
    pollutant = st.selectbox("Pollutant", pollutants, index=0)

with right:
    mode = st.radio("View", ["Hourly (raw)", "Daily mean", "Rolling mean"], horizontal=True)

# site filter
site_df = df[df["site"] == site]

# Date filter
min_date = site_df.index.min().date()
max_date = site_df.index.max().date()

date_from, date_to = st.slider(
    "Date range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
)

mask = (site_df.index >= pd.to_datetime(date_from)) & (site_df.index <= pd.to_datetime(date_to) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1))
site_df = site_df.loc[mask]

roll_window = 30
if mode == "Rolling mean":
    roll_window = st.slider("Rolling window (days)", min_value=3, max_value=90, value=30, step=1)

series = rolling_timeseries(site_df, pollutant, mode, roll_window)
series.name = pollutant.upper()

# Quick stats
c1, c2, c3, c4 = st.columns(4)
c1.metric("Mean", f"{series.mean():.2f}" if len(series) else "—")
c2.metric("Median", f"{series.median():.2f}" if len(series) else "—")
c3.metric("95th pct", f"{series.quantile(0.95):.2f}" if len(series) else "—")
c4.metric("Max", f"{series.max():.2f}" if len(series) else "—")

title = f"{pollutant.upper()} over time — {site} ({mode}{'' if mode != 'Rolling mean' else f', {roll_window}-day'})"
fig = make_fig(series, title)
st.plotly_chart(fig, use_container_width=True)

with st.expander("Notes / tips"):
    st.write(
        "- Rolling mean - Average over x daays (set with slider), better for analysing overall trends over long time periods. \n"
       " - Daily mean - average for each day, hourly time data is difficult to analyse over long time periods like this"
       
    )
