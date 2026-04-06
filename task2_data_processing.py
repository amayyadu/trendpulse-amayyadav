import json
import pandas as pd
import numpy as ny
#loading json file
with open(r'data\trends_20260405.json','r') as file:
    data=json.load(file)
#converting it to dataframe
df=pd.DataFrame(data)
#printing no. of rows
print(f'loaded rows : {df.shape[0]}\n')
#removing duplicates
print(f'no. of duplicates : {df["post_id"].duplicated().sum()}')
df['post_id']=df['post_id'].drop_duplicates()
df=df[df['post_id'].notna()]
print(f'After removing duplicates : {df.shape[0]}\n')
#checking if any other missing value
print(f'no. of null values : {df.isnull().sum().sum()}\n')
#changing into int
df['score'] = df['score'].astype(int)
df['num_comments'] = df['num_comments'].astype(int)
#filterin scores
df=df[df['score']>=5]
#striping title
df['title'] = df['title'].str.strip()
print(f'no. of rows after filtering scores : {df.shape[0]}\n')

file=r'data\trends_clean.csv'
df.to_csv(file, index=False)
print(f'Saved Rows: {len(df)} to {file}')

print('\nStories per categories:')
print(df['category'].value_counts().reset_index(name='count'))
