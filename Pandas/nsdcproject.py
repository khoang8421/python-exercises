import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =========================
# GREEN + EGGWHITE THEME WITH GRADIENT
# =========================

plt.rcParams.update({
    # Warm background
    "figure.facecolor": "#FFF8E7",   # soft eggwhite
    "axes.facecolor": "#FFF3D6",     # light warm vanilla
    "savefig.facecolor": "#FFF8E7",

    # Grid
    "axes.grid": True,
    "grid.color": "#EAD7B7",
    "grid.linestyle": "--",
    "grid.alpha": 0.6,

    # Text colors
    "text.color": "#3A5A40",
    "axes.labelcolor": "#3A5A40",
    "xtick.color": "#4F6F52",
    "ytick.color": "#4F6F52",

    "axes.titleweight": "bold",
    "axes.titlesize": 15,
    "axes.labelsize": 11,

    "lines.linewidth": 2
})

# =========================
# LOAD DATA
# =========================

df = pd.read_csv(r"C:\Kyle VSCode 2026\Pandas\main-data.csv", sep=";")

# =========================
# AI SECTORS
# =========================

ai_sectors = df[
    ["518200", "519130", "541511", "541512", "334413",
     "517110", "517210"]
]

ai_sector_names = {
    "518200": "Data Centers",
    "519130": "Web Search & Platforms",
    "541511": "Computer Programming",
    "541512": "Computer Systems Design",
    "334413": "Semiconductor Manufacturing",
    "517110": "Wired Telecom.",
    "517210": "Wireless Telecom."
}

ai_mean = ai_sectors.mean()
ai_mean_named = ai_mean.rename(index=ai_sector_names)
ai_sorted = ai_mean_named.sort_values(ascending=True)

# Create light-to-dark green gradient by value
ai_colors = plt.cm.Greens(np.linspace(0.4, 0.8, len(ai_sorted)))

graph = ai_sorted.plot(
    kind="barh",
    color=ai_colors
)

for bar in graph.patches:
    bar.set_edgecolor("#3A5A40")
    bar.set_linewidth(1.2)
    bar.set_alpha(0.9)

plt.title("CO₂ Emissions from AI-Related Sectors")
plt.ylabel("CO₂ Emissions (kgCO2e per USD)")
plt.xlabel("Industry (Related to AI)")

graph.bar_label(graph.containers[0], fmt="%.2f",
                label_type="center",
                color="#1B4332",
                fontsize=9)

plt.axvline(ai_sorted.mean(),
            color="#2D6A4F",
            linestyle="--",
            linewidth=2)

plt.subplots_adjust(left=0.4)
plt.show()

# =========================
# HEAVY INDUSTRY
# =========================

high_emission_sectors = df[
    ["221100", "211000", "212100", "324110", "325110",
     "331110", "327310", "484000", "481000", "562000"]
]

high_emission_sector_names = {
    "221100": "Electric Power Gen.",
    "211000": "Oil & Gas Extraction",
    "212100": "Coal Mining",
    "324110": "Petrol Refineries",
    "325110": "Petrochemicals",
    "331110": "Iron & Steel Mills",
    "327310": "Cement Manufacturing",
    "484000": "Truck Transportation",
    "481000": "Air Transportation",
    "562000": "Waste Management"
}

industry_mean = high_emission_sectors.mean()
industry_mean_named = industry_mean.rename(index=high_emission_sector_names)
industry_sorted = industry_mean_named.sort_values(ascending=True)

industry_colors = plt.cm.Greens(np.linspace(0.4, 0.8, len(industry_sorted)))

graph = industry_sorted.plot(
    kind="barh",
    color=industry_colors
)

for bar in graph.patches:
    bar.set_edgecolor("#3A5A40")
    bar.set_linewidth(1.2)
    bar.set_alpha(0.9)

plt.title("CO₂ Emissions from Major Industrial Sectors")
plt.ylabel("CO₂ Emissions (kgCO2e per USD)")
plt.xlabel("Sector Names")

graph.bar_label(graph.containers[0], fmt="%.2f",
                label_type="center",
                color="#1B4332",
                fontsize=8)

plt.axvline(industry_sorted.mean(),
            color="#2D6A4F",
            linestyle="--",
            linewidth=2)

plt.subplots_adjust(left=0.4)
plt.show()

# =========================
# COMPARISON GRAPH
# =========================

ai_value = ai_mean.mean()
industry_value = industry_mean.mean()

comparison_df = pd.DataFrame(
    {
        "Average CO₂ Intensity (kgCO2e per USD)": [
            ai_value,
            industry_value
        ]
    },
    index=["AI Sectors", "Heavy Industry"]
)

# Use gradient for two bars
comparison_colors = plt.cm.Greens(np.linspace(0.5, 0.75, 2))

graph = comparison_df.plot(
    kind="barh",
    color=comparison_colors
)

for bar in graph.patches:
    bar.set_edgecolor("#3A5A40")
    bar.set_linewidth(1.2)
    bar.set_alpha(0.9)

plt.title("Average CO₂ Intensity: AI vs Heavy Industry")
plt.ylabel("CO₂ Emissions (kgCO2e per USD)")

graph.bar_label(graph.containers[0], fmt="%.2f",
                label_type="center",
                color="#1B4332",
                fontsize=10)

plt.subplots_adjust(left=0.25)
plt.show()