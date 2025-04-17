# Load driver profiles and scoring logic
import pandas as pd

# Use relative paths to load files from the "Data" folder
drivers_df = pd.read_csv("Data/Simulated_50_Drivers_Only.csv")
scoring_logic_df = pd.read_excel("Data/Driver_Risk_Scoring_Logic_Table.xlsx")


# Clean and prepare score values
scoring_logic_df["Score"] = scoring_logic_df["Score"].astype(str).str.replace(r"\+", "", regex=True).astype(int)

# Scoring function based on dynamic rules from Excel
def dynamic_score_driver(driver, rules_df):
    total_score = 0
    # Loop Through Each Feature Group
    for feature in rules_df["Feature"].unique():
        feature_rules = rules_df[rules_df["Feature"] == feature]
        value = driver[feature]

        for _, rule in feature_rules.iterrows():
            condition = rule["Condition"]
            score = rule["Score"]

            # Age
            if feature == "age":
                if condition == "18–20" and 18 <= value <= 20:
                    total_score += score
                elif condition == "21–24" and 21 <= value <= 24:
                    total_score += score
                elif condition == "25–29" and 25 <= value <= 29:
                    total_score += score
                elif condition == "30–65" and 30 <= value <= 65:
                    total_score += score
                elif condition == "66+" and value > 65:
                    total_score += score

            # Experience
            elif feature == "experience_years":
                if condition == "< 2" and value < 2:
                    total_score += score
                elif condition == "2–5" and 2 <= value <= 5:
                    total_score += score
                elif condition == "> 5" and value > 5:
                    total_score += score

            # KM per year
            elif feature == "average_km_per_year":
                if condition == "> 15,000" and value > 15000:
                    total_score += score
                elif condition == "10,000–15,000" and 10000 <= value <= 15000:
                    total_score += score
                elif condition == "1000-6000" and 1000 <= value < 6000:
                    total_score += score
                elif condition == "< 6,000" and value < 6000:
                    total_score += score

            # Driving license type
            elif feature == "driving_license_type":
                license_count = len(str(value).split(','))
                if "1 license" in condition and license_count == 1:
                    total_score += score
                elif "Multiple" in condition and license_count > 1:
                    total_score += score

            # Professional driver
            elif feature == "is_professional_driver":
                if str(value).lower() in str(condition).lower():
                    total_score += score

    return total_score

# Apply to all drivers
# axis=1 = Each row
drivers_df["driver_risk_score"] = drivers_df.apply(lambda row: dynamic_score_driver(row, scoring_logic_df), axis=1)

# Optional: save to CSV
drivers_df.to_csv("Scored_Drivers.csv", index=False)
