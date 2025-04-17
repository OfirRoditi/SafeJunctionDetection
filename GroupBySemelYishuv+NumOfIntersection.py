import pandas as pd

# Load the filtered urban accident dataset
df = pd.read_csv("C:\\Users\\ofirr\\Desktop\\3-Year\\FinalProject\\Project\\Data\\Filtered_Urban_Accidents.csv")

# Clean and convert intersection ID column
df["ZOMET_IRONI"] = pd.to_numeric(df["ZOMET_IRONI"], errors="coerce")
df = df.dropna(subset=["ZOMET_IRONI"])
df["ZOMET_IRONI"] = df["ZOMET_IRONI"].astype(int)

# Clean and convert city code column
df["SEMEL_YISHUV"] = pd.to_numeric(df["SEMEL_YISHUV"], errors="coerce")
df = df.dropna(subset=["SEMEL_YISHUV"])
df["SEMEL_YISHUV"] = df["SEMEL_YISHUV"].astype(int)

# Group by unique intersection key: intersection ID + city code
df_grouped = df.groupby(["ZOMET_IRONI", "SEMEL_YISHUV"]).agg(
    total_rows=("pk_teuna_fikt", "count"),
    total_accidents=("pk_teuna_fikt", "nunique"),
    fatal_accidents=("HUMRAT_TEUNA", lambda x: (x == 1).sum()),
    severe_accidents=("HUMRAT_TEUNA", lambda x: (x == 2).sum()),
    light_accidents=("HUMRAT_TEUNA", lambda x: (x == 3).sum()),
    accident_ids=("pk_teuna_fikt", lambda x: ", ".join(map(str, sorted(set(x)))))
).reset_index()

# Save the result to a CSV file
output_path = "C:\\Users\\ofirr\\Desktop\\3-Year\\FinalProject\\Project\\Data\\Intersection_By_Zomet_And_Yishuv.csv"
df_grouped.to_csv(output_path, index=False, encoding="utf-8")
print(f"✅ Final grouped summary saved to: {output_path}")

# # Preview the result
# print(df_grouped.head())
