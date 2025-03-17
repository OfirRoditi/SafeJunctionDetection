import pandas as pd
import os  # Import os module to check file existence

# Define the full file paths
accidents_file = "C:\\Users\\ofirr\\Desktop\\3-Year\\FinalProject\\Project\\Data\\H20231041AccData.csv"
involved_file = "C:\\Users\\ofirr\\Desktop\\3-Year\\FinalProject\\Project\\Data\\H20231041InvData.csv"
output_file = "C:\\Users\\ofirr\\Desktop\\3-Year\\FinalProject\\Project\\Data\\Merged_Accident_Data.csv"

try:
    # Load the data into pandas DataFrames
    print("Loading data files...")
    accidents_df = pd.read_csv(accidents_file, encoding="utf-8")
    involved_df = pd.read_csv(involved_file, encoding="utf-8")
    print("Files loaded successfully!")

    # Merging datasets
    print("Merging data...")
    merged_df = accidents_df.merge(involved_df, on="pk_teuna_fikt", how="inner")
    merged_df = merged_df.drop_duplicates()
    print(f"Merged dataset contains {merged_df.shape[0]} rows and {merged_df.shape[1]} columns.")

    # Saving the merged dataset
    merged_df.to_csv(output_file, index=False, encoding="utf-8")
    
    # Debug print to check if file is created
    if os.path.exists(output_file):
        print(f"✅ Merged file successfully created: {output_file}")
    else:
        print("❌ Error: Merged file was NOT created!")

except Exception as e:
    print(f"⚠️ An error occurred: {e}")
