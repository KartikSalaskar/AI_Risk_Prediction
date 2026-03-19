import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import os

def preprocess_data():
    # get project root directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    input_path = os.path.join(
        base_dir, "data", "raw", "supply_chain_data.csv"
    )
    output_path = os.path.join(
        base_dir, "data", "processed", "cleaned_data.csv"
    )

    df = pd.read_csv(input_path)

    print("Raw data shape:", df.shape)
    print(df.head())

    # encode risk level
    le = LabelEncoder()
    df["risk_level"] = le.fit_transform(df["risk_level"])

    # scale features
    scaler = StandardScaler()
    features = df.drop("risk_level", axis=1)
    scaled_features = scaler.fit_transform(features)

    processed_df = pd.DataFrame(
        scaled_features, columns=features.columns
    )
    processed_df["risk_level"] = df["risk_level"]

    processed_df.to_csv(output_path, index=False)
    print("Processed data saved at:", output_path)

if __name__ == "__main__":
    preprocess_data()
