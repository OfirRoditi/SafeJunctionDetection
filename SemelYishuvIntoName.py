import pandas as pd

# Load the intersection group summary CSV
intersections_path = "C:\\Users\\ofirr\\Desktop\\3-Year\\FinalProject\\Project\\Data\\IntersectionByGroupWithRisk.csv"

# Load the Excel file that maps SEMEL_YISHUV to English city names
cities_path = "C:\\Users\\ofirr\\Desktop\\3-Year\\FinalProject\\Project\\Data\\TtransformationOfSemelIshuvIntoNames.xlsx"

# Load both files
df_intersections = pd.read_csv(intersections_path)
df_cities = pd.read_excel(cities_path)

# Merge English city names into intersection data
df_merged = df_intersections.merge(
    df_cities[["SEMEL_YISHUV", "SHEM_YISHUV_ANGLIT"]],
    on="SEMEL_YISHUV",
    how="left"
)

# Rename the column for clarity
df_merged = df_merged.rename(columns={"SHEM_YISHUV_ANGLIT": "CITY_NAME_EN"})

# Save the result to a new CSV file
output_path = "C:\\Users\\ofirr\\Desktop\\3-Year\\FinalProject\\Project\\Data\\IntersectionGroup_With_City_Names_English.csv"
df_merged.to_csv(output_path, index=False, encoding='utf-8')

print(f"✅ File saved with English city names: {output_path}")

# Preview first few rows
print(df_merged.head())
