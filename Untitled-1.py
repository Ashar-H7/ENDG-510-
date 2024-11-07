import pandas as pd # in case of error, install pnadas using: pip install pandas
import os
import random

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')
for x in range(500):

    
    new_data = {
    'Temp': random.randint(0, 70),
    'Humd':  random.randint(0,200),
    'Label': 0
    }
    df = df.append(new_data, ignore_index=True)
    # Step 3: Save the DataFrame to a new CSV file

print(os.getcwd())
df.to_csv("data1.csv", index=False)
