import pandas as pd

#get CSV data and turn this into a dataframe
file_path = "/workspaces/my_cv.github.io/canlyniadaur/ParcBrynBachResults - Results (All Time) (1).csv"
df = pd.read_csv(file_path)

#Get the 25 recent SBs
season_bests = df.query("Best == 'SB'")
latest_sbs = season_bests.head(25)
columns_to_remove = ['Sex', 'Age Position','Gender Position', 'Best', 'Club Record', 'Location' ]
latest_sbs = latest_sbs.drop(columns=columns_to_remove)

#Write to file

sb_html_table = latest_sbs.to_html(classes='data-table')

with open("/workspaces/my_cv.github.io/canlyniadaur/TableTemplate.html", "r") as file:
    existing_html = file.read()

# Define the placeholder element
placeholder = '<!-- INSERT_PANDAS_HTML -->'

# Replace the placeholder with the generated HTML
modified_html = existing_html.replace(placeholder, sb_html_table)

# Save the modified HTML to a file
with open('/workspaces/my_cv.github.io/canlyniadaur/ClubActivitiesSB.html', 'w') as file:
    file.write(modified_html)