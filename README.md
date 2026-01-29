# Project Title
Air Quality Comparator Project

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
- Tools / libraries used (e.g., Python, pandas, matplotlib, scikit-learn)
- Steps taken: data cleaning, feature engineering, modeling
- Any assumptions or limitations

---

## Analysis & Results
- Key findings
- Tables or summary statistics
- Any models or metrics (if applicable)

---

## Visualizations
- Important charts, graphs, or plots
- Optionally include a screenshot or embed images

---

## Conclusions
- Insights drawn from the analysis
- How the results answer the problem statement

---

## Future Work
- Ideas to improve or expand the project
- Additional analyses, data sources, or models to explore

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
