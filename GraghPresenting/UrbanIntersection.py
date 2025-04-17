import pandas as pd
import matplotlib.pyplot as plt

# Load the grouped data
df_grouped = pd.read_csv("C:\\Users\\ofirr\\Desktop\\3-Year\\FinalProject\\Project\\Data\\IntersectionGroup_By_Zomet_And_Yishuv.csv")

# Sort by total_accidents and show top 5
top_5 = df_grouped.sort_values(by="total_accidents", ascending=False).head(5)
print("🔝 Top 5 Intersections with Most Accidents:")
print(top_5[["ZOMET_IRONI", "SEMEL_YISHUV", "total_accidents", "fatal_accidents", "severe_accidents", "light_accidents"]])

# === 📊 Visualization 1: Top 10 Intersections with Most Accidents ===
top_10 = df_grouped.sort_values(by="total_accidents", ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_10["ZOMET_IRONI"].astype(str), top_10["total_accidents"], color='skyblue')
plt.title("Top 10 Intersections by Number of Accidents")
plt.xlabel("Intersection ID")
plt.ylabel("Total Accidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === 📊 Visualization 2: Injury Breakdown in Top 5 Intersections ===
plt.figure(figsize=(10, 6))
bar_width = 0.25
x = range(len(top_5))

plt.bar([i - bar_width for i in x], top_5["fatal_accidents"], width=bar_width, label="Fatal")
plt.bar(x, top_5["severe_accidents"], width=bar_width, label="Severe")
plt.bar([i + bar_width for i in x], top_5["light_accidents"], width=bar_width, label="Light")

plt.xticks(ticks=x, labels=top_5["ZOMET_IRONI"].astype(str), rotation=45)
plt.xlabel("Intersection ID")
plt.ylabel("Number of People Injured")
plt.title("Injury Breakdown in Top 5 Intersections")
plt.legend()
plt.tight_layout()
plt.show()

# === Optional: 📊 Pie Chart of Severity Distribution Across All Data ===
severity_totals = df_grouped[["fatal_accidents", "severe_accidents", "light_accidents"]].sum()
plt.figure(figsize=(6, 6))
plt.pie(severity_totals, labels=["Fatal", "Severe", "Light"], autopct="%1.1f%%", startangle=140)
plt.title("Overall Injury Severity Distribution")
plt.axis("equal")
plt.show()
