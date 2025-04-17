import pandas as pd
import matplotlib.pyplot as plt

# Load the merged data (with city names and risk scores)
merged_df = pd.read_csv("C:\\Users\\ofirr\\Desktop\\3-Year\\FinalProject\\Project\\Data\\IntersectionGroup_With_City_Names_English.csv")

# 1. Top Cities by Risk Score (Average Risk Score per City)
city_risk_avg = merged_df.groupby('CITY_NAME_EN')['risk_score'].mean().sort_values(ascending=False).head(10)

# Create a bar plot for the top 10 cities with the highest average risk score
plt.figure(figsize=(10,6))
city_risk_avg.plot(kind='bar', color='skyblue')
plt.title("Top 10 Cities by Average Risk Score")
plt.xlabel("City")
plt.ylabel("Average Risk Score")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# 2. Risk Score Distribution (Histogram)
plt.figure(figsize=(10,6))
merged_df['risk_score'].plot(kind='hist', bins=20, color='orange', edgecolor='black')
plt.title("Risk Score Distribution")
plt.xlabel("Risk Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 3. Top 10 Intersections with Highest Risk Scores
top_intersections = merged_df[['ZOMET_IRONI', 'risk_score']].sort_values(by='risk_score', ascending=False).head(10)

# Create a bar plot for the top 10 intersections with the highest risk score
plt.figure(figsize=(10,6))
plt.bar(top_intersections['ZOMET_IRONI'].astype(str), top_intersections['risk_score'], color='green')
plt.title("Top 10 Intersections by Risk Score")
plt.xlabel("Intersection ID")
plt.ylabel("Risk Score")
plt.tight_layout()
plt.show()
