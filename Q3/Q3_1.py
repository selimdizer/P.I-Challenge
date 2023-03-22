import pandas as pd
import re

# Read the data
df = pd.read_csv('Q3\Q3.csv')
pattern = r'<[a-zA-Z]+>(https?://[\w\.]+)</[a-zA-Z]+>'


# Define a function to extract the pure URL based on device type and the given pattern
def extract_url(access_link):

    # Search for the pattern in the access link
    match = re.search(pattern, access_link)
    if match:
        return match.group(1)
    else:
        return None

# Apply the function to the DataFrame to create a new column with the pure URL
df['Pure_URL'] = df.apply(lambda x: extract_url(x['Stats_Access_Link']), axis=1)

# Save the updated DataFrame to a new CSV file
df.to_csv('Q3\Q3_Result.csv', index=False)
    


