import pandas as pd

# Load your files
grouped_df = pd.read_csv("Data/IntersectionGroup_By_Zomet_And_Yishuv.csv")
acc_df = pd.read_csv("Data/H20231041AccData.csv")

# Define relevant columns for infrastructure-related features
selected_columns = [
    "ZOMET_IRONI", "SEMEL_YISHUV",
    "RAMZOR", "HUMRAT_TEUNA", "SUG_TEUNA", "ZURAT_DEREH", "HAD_MASLUL", "RAV_MASLUL",
    "MEHIRUT_MUTERET", "TKINUT", "ROHAV", "SIMUN_TIMRUR", "TEURA", "BAKARA", "MEZEG_AVIR", "PNE_KVISH"
]

# Filter the accident data to only those columns, and drop rows missing ZOMET_IRONI
acc_df_filtered = acc_df[selected_columns].dropna(subset=["ZOMET_IRONI"])
acc_df_filtered["ZOMET_IRONI"] = acc_df_filtered["ZOMET_IRONI"].astype(int)

# Group and aggregate relevant features by intersection + city
intersection_features = acc_df_filtered.groupby(["ZOMET_IRONI", "SEMEL_YISHUV"]).agg({
    "RAMZOR": lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    "SUG_TEUNA": lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    "ZURAT_DEREH": lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    "HAD_MASLUL": lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    "RAV_MASLUL": lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    "MEHIRUT_MUTERET": "mean",
    "TKINUT": lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    "ROHAV": "mean",
    "SIMUN_TIMRUR": lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    "TEURA": lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    "BAKARA": lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    "MEZEG_AVIR": lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    "PNE_KVISH": lambda x: x.mode().iloc[0] if not x.mode().empty else None
}).reset_index()

# Merge with your existing grouped intersection table
merged_df = grouped_df.merge(intersection_features, on=["ZOMET_IRONI", "SEMEL_YISHUV"], how="left")

# Save it if you want
# merged_df.to_csv("Data/IntersectionGroup_With_Infrastructure_Features.csv", index=False, encoding="utf-8-sig")
