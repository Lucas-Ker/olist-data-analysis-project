# src/cleaning.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs initial data cleaning on the merged dataframe.
    - Converts all timestamp columns to datetime objects.
    - (Future cleaning steps can be added here)

    Args:
        df (pd.DataFrame): The raw, merged dataframe.

    Returns:
        pd.DataFrame: The dataframe with corrected data types.
    """
    
    df_clean = df.copy()

    # Identifies all datetime columns
    datetime_cols = [
        'order_purchase_timestamp', 'order_approved_at',
        'order_delivered_carrier_date', 'order_delivered_customer_date',
        'order_estimated_delivery_date', 'shipping_limit_date',
        'review_creation_date', 'review_answer_timestamp'
    ]

    print("--- Data Cleaning Step ---")
    print("Converting timestamp columns to datetime objects...")

    # Convert each column to datetime
    for col in datetime_cols:
        if col in df_clean.columns:
            df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')
            print(f"  - Column '{col}' converted.")

    print("Data cleaning complete.")
    return df_clean