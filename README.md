# Maine Municipal Housing Vulnerability Analysis
> Census-based housing vulnerability analysis for Maine municipalities, built to support nonprofit resource allocation decisions.

---

## Overview

This project analyzes U.S. Census data to identify and classify Maine municipalities by their housing vulnerability profile. The goal is to help organizations like **Maine Needs** direct limited housing and service resources toward communities with the greatest structural need — and away from communities that appear distressed on the surface but aren't.

The analysis distinguishes between four distinct community types, separating genuine decline from seasonal vacancy patterns that are often misread as crisis.

---

## Motivation

Maine's housing landscape is deeply uneven. Coastal towns with high vacancy rates are often thriving — their empty homes are second residences, not abandoned ones. Meanwhile, inland towns with similar vacancy numbers are quietly hollowing out: residents leaving, tax bases shrinking, services degrading.

Applying the same policy lens to both types of communities wastes resources. This project builds a data-driven segmentation framework to prevent that misallocation.

---

## Methodology

### Data Sources
- U.S. Census Bureau — 2020 Decennial Census (Housing Units, Population)
- American Community Survey (ACS) 5-Year Estimates
- Maine-specific municipal shapefiles and administrative data

### Segmentation Framework

Each municipality with at least 200 housing units is classified into one of four segments:

| Segment | Description |
|---|---|
| **Hollowing Out** | Sustained population decline + structural vacancy unexplained by seasonal demand |
| **Resort Town** | High vacancy rate that is predominantly seasonal in character |
| **Healthy Growth** | Population growth with manageable vacancy levels |
| **Stagnant** | High structural vacancy, flat population — at risk of tipping toward hollowing |

### Key Metrics
- **Structural Vacancy Rate** — vacancy not attributable to seasonal or temporary factors
- **Hollowing Score** — composite index combining population decline trajectory and structural vacancy severity
- **Seasonal Rate** — share of vacancy explained by second-home and tourism demand
- **Affordability Signal** — municipalities growing in population but accumulating structural vacancy (early displacement indicator)

---

## Key Findings

- A significant share of Maine municipalities exhibit the "Hollowing Out" pattern — a self-reinforcing cycle where population loss leaves behind housing stock that can't attract buyers, depressing tax revenue and degrading services further.
- A clear **geographic divide** separates coastal resort towns (high vacancy, healthy economy) from inland decline towns (high vacancy, negative population trajectory). These require entirely different interventions.
- A counterintuitive **affordability signal** emerges in growing municipalities with above-average structural vacancy — suggesting displacement of lower-income households rather than abandonment.
- A substantial **stagnant middle tier** is at risk of tipping toward hollowing over the next decade and warrants preventive investment now.

---

## Recommendations for Nonprofits

1. **Concentrate** direct housing assistance (rehabilitation grants, weatherization, emergency repair) in top-quintile "Hollowing Out" municipalities — prioritizing towns where structural vacancy exceeds 25% and population decline exceeded 5%.
2. **Pilot preventive programs** in "Stagnant" municipalities before hollowing accelerates — specifically where structural vacancy is above median but population loss is under 3%.
3. **Do not deploy** scarce housing-supply dollars in "Resort Town" municipalities without first disaggregating who the seasonal units serve. The correct intervention is production of affordable year-round units, not vacancy remediation.

---

## Project Structure

```
maine-census-2020/
│
├── data/processed/          # Cleaned and merged census datasets
├── 00_shared.py             # Shared utilities and constants
├── 01_population.ipynb      # Population trend analysis
├── 02_race_ethnicity.ipynb  # Demographic composition analysis
├── 03_housing.ipynb         # Housing stock and vacancy analysis
├── 04_cross_dataset.ipynb   # Cross-dataset merging and feature engineering
├── 05_vacancy_classification.ipynb  # Municipal segmentation model + narrative output
└── CLAUDE.md                # AI assistant context file
```

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/harrymillspaugh-ai/maine-census-2020.git
cd maine-census-2020

# Install dependencies
pip install -r requirements.txt

# Open notebooks in order
jupyter notebook
```

Run notebooks `01` through `05` sequentially — each builds on the outputs of the previous.

---

## Tools & Libraries

- **Python 3.13** — core language
- **Pandas** — data manipulation and aggregation
- **NumPy** — numerical computing
- **Jupyter Notebook** — interactive analysis environment
- **Matplotlib / Seaborn** — data visualization
- **Census / ACS APIs** — data sourcing

---

## Author

**Harry Millspaugh**
Data Science Graduate Student, University of Virginia
[GitHub](https://github.com/harrymillspaugh-ai)

---

*Built as part of an applied data science project exploring how public Census data can support nonprofit decision-making in rural and semi-rural housing markets.*
