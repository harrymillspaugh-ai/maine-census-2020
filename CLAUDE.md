# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Data analysis project exploring Maine 2020 Census data. The primary workspace is `explore.ipynb` (Jupyter notebook), backed by three Excel source files:

- `Total Population_2020_3.xlsx` — total population by geography (state, county, municipality)
- `Counties race x ethn change 2010 to 2020.xlsx` — county-level racial/ethnic composition (Sheet1) and change 2010–2020 (sheet "Change")
- `Housing Units_2020_0.xlsx` — housing unit counts (total, occupied, vacant)

## Running the Notebook

```bash
jupyter notebook explore.ipynb
# or
jupyter lab
```

## Dependencies

```bash
pip install pandas openpyxl matplotlib seaborn jupyter
```

## Data Structure

**Population file** (`Total Population_2020_3.xlsx`, sheet `Query_Total Pop`):
- Columns: `Place`, `2010 Total Population`, `2020 Total Population`, `Percent Change` (as decimal, e.g. 0.05 = 5%)
- Rows mix state, county, and municipality — segment using `MAINE_COUNTIES` list + `"Maine"` string

**Race/ethnicity file** (`Counties race x ethn change 2010 to 2020.xlsx`):
- `Sheet1`: rows 0–15 = 2020 county snapshot; rows 17+ = 2010 data. No headers — columns renamed by position. Includes Hispanic (any race) and NH (non-Hispanic) breakdowns; groups: White, Black, AIAN, Asian, NHOPI, Other_Race, Two_Plus
- Sheet `"Change"`: rows 0–15 = absolute population change 2010–2020 per county, same positional column layout

**Housing file** (`Housing Units_2020_0.xlsx`, sheet `Query_Housing Units`):
- Row 0 = real column headers (`Geography`, `Total`, `Occupied`, `Vacant`); data starts at row 1
- Same geography mix as population file (state/county/municipality)

## Notebook Structure

The notebook (`explore.ipynb`) is organized into four sections:

1. **Total Population** — county 2010 vs 2020 bar charts; municipality top/bottom 10 growers (filtered to pop ≥ 500 in 2010)
2. **Race & Ethnicity** — diversity percentages by county; stacked composition bar chart; 2010–2020 change heatmap
3. **Housing Units** — vacancy rates by county; municipality vacancy distribution (filtered to ≥ 100 units); highlight municipalities ≥ 500 units
4. **Cross-Dataset County Summary** — merged DataFrame joining all three datasets at county level; scatter plots of population growth vs vacancy, and diversity vs vacancy

## Key Variables (cross-section dependencies)

Later sections depend on variables set earlier:
- `MAINE_COUNTIES` — defined in Section 1, reused in Section 3
- `pop_counties`, `pop_munis` — from Section 1, used in Section 4
- `diversity` — from Section 2, used in Section 4
- `housing_counties`, `state_vac` — from Section 3, used in Section 4

Run cells in order; restarting the kernel requires re-running all prior sections.
