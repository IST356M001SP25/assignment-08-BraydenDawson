import pandas as pd
import streamlit as st

def top_locations(violations_df: pd.DataFrame, threshold=1000) -> pd.DataFrame:
    # Group by 'location' and sum the 'amount' column
    grouped = violations_df.groupby('location', as_index=False)['amount'].sum()
    # Filter only locations where the total amount is >= threshold
    filtered = grouped[grouped['amount'] >= threshold]
    return filtered


def top_locations_mappable(violations_df: pd.DataFrame, threshold=1000) -> pd.DataFrame:
    # Get the top locations with high total fines
    top = top_locations(violations_df, threshold)
    # Drop duplicate location rows with their lat/lon
    location_coords = violations_df[['location', 'lat', 'lon']].drop_duplicates()
    # Merge the top locations with the coordinate data
    merged = pd.merge(top, location_coords, on='location', how='left')
    # Reorder the columns
    return merged[['location', 'lat', 'lon', 'amount']]


def tickets_in_top_locations(violations_df: pd.DataFrame, threshold=1000) -> pd.DataFrame:
    # Get list of top locations
    top_df = top_locations(violations_df, threshold)
    top_locs = top_df['location'].unique()

    # Standardize column naming if needed
    if 'hour' in violations_df.columns and 'hourofday' not in violations_df.columns:
        violations_df = violations_df.rename(columns={'hour': 'hourofday'})

    # Filter only tickets at top locations
    filtered = violations_df[violations_df['location'].isin(top_locs)].copy()

    # Reorder to match expected columns in test
    expected_columns = ['location', 'ticket_number', 'issued_date', 'description', 'status',
                        'dayofweek', 'hourofday', 'lat', 'lon', 'count', 'amount']
    filtered = filtered[expected_columns]

    return filtered



if __name__ == '__main__':
    # Load the input dataset
    df = pd.read_csv('./cache/final_cuse_parking_violations.csv')
    
    # Generate all 3 transformed datasets
    top_locs_df = top_locations(df)
    mappable_df = top_locations_mappable(df)
    filtered_tickets_df = tickets_in_top_locations(df)

    # Save the outputs to CSV
    top_locs_df.to_csv('./cache/top_locations.csv', index=False)
    mappable_df.to_csv('./cache/top_locations_mappable.csv', index=False)
    filtered_tickets_df.to_csv('./cache/tickets_in_top_locations.csv', index=False)
