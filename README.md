# Air Quality Comparator Project
Air Quality Comparator Project - Bristol and Birmingham. Comparing air pollution in two bristol sites and two birmingham sites

---

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Problem Statement](#problem-statement)
- [Methodology](#methodology)
- [Analysis & Results](#analysis--results)
- [Visualizations](#visualizations)
- [Conclusions](#conclusions)
- [Future Work](#future-work)
- [Setup & Run](#setup--run)
- [Team / Contributors](#team--contributors)

---

## Project Overview
Using data from Bristol and Birmingham, satellite data and ground data are compared in order to ascertain if there is sufficient correlation to infer ground levels from satellite data.

---

## Datasets
- 2 sources of data were obtained. 1 kaggle dataset as described below
- Satellite data was 
- Source: [Link to dataset](https://www.kaggle.com/datasets/airqualityanthony/uk-defra-aurn-air-quality-data-2015-2023)
- Description: .csv, 1.86GB, contains ground measurement data for UK air pollution between 2015 and 2023. It includes several pollutants including Carbon Monoxide, Nitrogen Oxides, Nitrogen Dioxide, Nitric Oxide, Ozone, and Sulphur Dioxide.

- Licensing is stated as other, with no further information in the description.

---

## Problem Statement
- We are attempting to discover whether open source satellite data is sufficiently correlated with collected ground data for air pollution. If this is the case, we can infer what the ground readings would be from satellite data, reducing the need for ground instrument readings, thus reducing the associated cost.


---


## Methodology

- Collected and cleaned ground-based air pollution data using Python, NumPy, and pandas.
- Attempted to scrape and collate Copernicus satellite data for comparison, but coverage was insufficient, so the project focus shifted to ground measurements.
- Performed data profiling to inspect distributions and completeness of key variables.
- Engineered features and ran a machine learning model using scikit-learn.
- Built interactive dashboards with Tableau and Streamlit to visualise spatial and temporal pollution patterns.
- Key limitation: limited satellite data restricted cross-source comparisons.


---

## Analysis & Results

- **Seasonal trends:** Pollutant levels are higher during winter months, consistent with reduced dispersion and meteorological factors.  
- **Site type differences:** The NO₂/NOx ratio is higher at roadside locations, reflecting fresher traffic emissions compared to background sites.  
- **Impact of COVID-19:** Overall air pollution dropped significantly in 2020 due to reduced activity, and has been gradually increasing since, though levels have not returned to pre-2019 values.  
- **Summary statistics:** Key metrics and averages were calculated for each city and site type, highlighting spatial and temporal variations.  
- **Visualizations:** Dashboards in Tableau and Streamlit illustrate these patterns with maps, time series, and comparative scatter plots.  


---

## Visualizations
### Annual mean pollutants
![Annual mean pollutants](images/avg_pollutants_year.png)

### Monthly Median Pollutants
![Monthly Median Pollutants](images/monthly_median_pollutants.png)

---

## Conclusions

- **Seasonal and site-type insights:** Pollutant levels are consistently higher during winter months, and roadside locations show higher NO₂/NOx ratios, reflecting fresher traffic emissions compared to background sites.  
- **Impact of COVID-19:** Air pollution dropped significantly in 2020 due to reduced activity, and has been gradually increasing since, though levels have not returned to pre-2019 values.  
- **Spatial patterns:** Mapping revealed hotspots within each city, highlighting areas where interventions could be most effective.  
- **Answering the problem statement:** By combining ground-based measurements, temporal analysis, and pollutant ratios, the project identifies both when and where air pollution is worst, and how traffic-related sources influence local air quality.  

**Key takeaway:** Focused analysis of NO, NO₂, and NOx, supported by dashboards and summary statistics, provides actionable insights into urban air quality trends, while limitations in satellite data emphasize the importance of robust ground monitoring.

---

## Future Work

- **Expand satellite data integration:** Gather more complete Copernicus or other satellite datasets to compare with ground measurements and explore long-term trends.  
- **Include additional pollutants:** Incorporate PM2.5, PM10, O₃, and SO₂ where data coverage allows, to provide a fuller picture of urban air quality.  
- **Meteorological analysis:** Investigate the impact of temperature, wind speed, and wind direction on pollutant dispersion using statistical or ML models.  
- **Advanced modeling:** Apply predictive models (e.g., time series forecasting or spatial interpolation) to estimate pollutant levels at unmonitored locations.  
- **Interactive dashboards:** Enhance Streamlit or Tableau dashboards with user-driven filters for sites, dates, and pollutants for more exploratory analysis.  
- **Policy-focused insights:** Use hotspot identification and seasonal trends to suggest targeted interventions for urban air quality improvement.


---

## Setup & Run
**Requirements:**
- Python version
- Libraries (`pip install -r requirements.txt`)

**Instructions:**
```bash
git clone <repo_url>
cd project-folder
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
# Run notebooks or scripts
```
---

## Team / Contributors
- Storm Harland
- Mohammed Sarki
- Conor O'Brien
- Ben 