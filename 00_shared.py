import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 60)
pd.set_option("display.float_format", "{:,.1f}".format)

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.dpi"] = 110

MAINE_COUNTIES = [
    "Androscoggin County", "Aroostook County", "Cumberland County",
    "Franklin County", "Hancock County", "Kennebec County", "Knox County",
    "Lincoln County", "Oxford County", "Penobscot County", "Piscataquis County",
    "Sagadahoc County", "Somerset County", "Waldo County", "Washington County",
    "York County",
]

DATA_RAW = "."
DATA_PROCESSED = "data/processed"

os.makedirs(DATA_PROCESSED, exist_ok=True)
