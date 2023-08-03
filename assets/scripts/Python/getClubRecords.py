import pandas as pd
import re

# get CSV data and turn it into a dataframe
file_path = "src\ParcBrynBachResults.csv"
df = pd.read_csv(file_path)

# Function to convert time strings to timedelta format
def convert_time(time_str):
    try:
        return pd.to_timedelta(time_str)
    except ValueError:
        time_parts = re.split(r'[:\.]', time_str)
        time_parts = list(map(int, time_parts))
        hours, minutes, seconds, milliseconds = 0, 0, 0, 0
        if len(time_parts) == 1:  # Check if it's in .ss format
            seconds = int(time_parts[0])
        elif len(time_parts) == 2:  # Check if it's in m:ss format
            minutes, seconds = time_parts
        elif len(time_parts) == 3:  # Check if it's in mm:ss format or m:ss.000 format
            if '.' in time_str:  # Check if it's in m:ss.000 format
                minutes, seconds, milliseconds = time_parts
            else:  # It's in mm:ss format
                minutes, seconds = time_parts
        elif len(time_parts) == 4:  # Check if it's in h:mm:ss, hh:mm:ss, or mm:ss.000 format
            if '.' in time_str:  # Check if it's in mm:ss.000 format
                minutes, seconds, milliseconds = time_parts[1:]
            else:  # It's in h:mm:ss or hh:mm:ss format
                hours, minutes, seconds = time_parts
        else:
            raise ValueError("Invalid time format: " + time_str)

        return pd.Timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)


# Convert 'Time' column to timedelta format
df['Time'] = df['Time'].apply(convert_time)

# Filter records where 'Club Record' is 'Y', distance is in the specified list, and Age Category is not 'Male' or 'Female'
distances = ['Mile', '3000', '5K', '10K', 'HM', 'Mar', 'parkrun']
filtered_df = df[(df['Distance'].isin(distances)) & (~df['Age Category'].isin(['Male', 'Female']))]

# Find the all-time records for each distance, gender, and age category
all_time_records = filtered_df.groupby(['Distance', 'Sex', 'Age Category'])['Time'].idxmin()

# Create a new DataFrame with the all-time records
all_time_df = filtered_df.loc[all_time_records].copy()

 # Reset the index of the new DataFrame
all_time_df.reset_index(drop=True, inplace=True)

# Remove the days component from the timedelta values
all_time_df['Time'] = all_time_df['Time'].dt.total_seconds().apply(pd.to_datetime, unit='s').dt.strftime('%H:%M:%S.%f').str.rstrip('0').str.rstrip('.')

# Strip out the hours component when it's zero
all_time_df['Time'] = all_time_df['Time'].apply(lambda x: x[3:] if x.startswith('00:') else x)

# Drop unwanted columns
columns_to_remove = ['Sex', 'Age Position', 'Gender Position', 'Best', 'Club Record', 'Location']
all_time_df.drop(columns_to_remove, axis=1, inplace=True)

# Read the HTML template
with open("pages/canlyniadaur/TableTemplate.html", "r") as file:
    existing_html = file.read()

# Define the placeholder element
placeholder = '<!-- INSERT_PANDAS_HTML -->'

# Get unique distances
unique_distances = all_time_df['Distance'].unique()

# Generate HTML tables for each distance group
for distance in unique_distances:
    # Filter data for the current distance
    distance_df = all_time_df[all_time_df['Distance'] == distance].copy()

    # Remove the 'Distance' column
    distance_df.drop('Distance', axis=1, inplace=True)

    # Generate HTML table
    html_table = distance_df.to_html(classes='data-table')

    # Modify HTML template
    modified_html = existing_html.replace(placeholder, html_table)

    # Save HTML to a file
    file_name = f"pages/canlyniadaur/ClubRecords_{distance}.html"
    with open(file_name, 'w') as file:
        file.write(modified_html)