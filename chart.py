# 23f2003651@ds.study.iitm.ac.in

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Generate synthetic data
# -----------------------------
np.random.seed(42)

channels = ['Email', 'Phone', 'Live Chat', 'Social Media']
data = []

for channel in channels:
    if channel == 'Email':
        # Email responses are slightly slower on average
        response_times = np.random.lognormal(mean=2.5, sigma=0.5, size=200)
    elif channel == 'Phone':
        # Phone responses are faster
        response_times = np.random.lognormal(mean=1.5, sigma=0.4, size=200)
    elif channel == 'Live Chat':
        # Live Chat is fast and consistent
        response_times = np.random.lognormal(mean=1.2, sigma=0.3, size=200)
    else:  # Social Media
        # Social media is somewhat variable
        response_times = np.random.lognormal(mean=2.0, sigma=0.6, size=200)
    
    for rt in response_times:
        data.append({'Channel': channel, 'ResponseTimeMinutes': rt})

df = pd.DataFrame(data)

# -----------------------------
# Seaborn styling
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # presentation-ready text sizes
palette = sns.color_palette("Set2")

# -----------------------------
# Create violinplot
# -----------------------------
plt.figure(figsize=(8, 8))  # corresponds to 512x512 pixels at 64 dpi
sns.violinplot(
    x='Channel', 
    y='ResponseTimeMinutes', 
    data=df, 
    palette=palette,
    inner='quartile',  # show quartiles inside the violin
    cut=0  # limit violin tails to the min/max
)
plt.title("Customer Support Response Time Distribution by Channel")
plt.ylabel("Response Time (minutes)")
plt.xlabel("Support Channel")

# -----------------------------
# Save figure
# -----------------------------
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()
