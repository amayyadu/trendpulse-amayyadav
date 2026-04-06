import pandas as pd
import numpy as np
df=pd.read_csv(r'data\trends_clean.csv')
print(f'loaded data : {df.shape}\n')
#printing first 5 rows 
print(df.head(),'\n')
#printing average score and average comments
print(f"Average score : {df['score'].mean().round(2)}\nAverage comments : {df['num_comments'].mean().round(2)}")
#ny functioning
num_imp=np.array(df['score'])
mean=np.mean(df['score'])
median=np.median(df['score'])
sd=num_imp.std()
scr_max=num_imp.max()
scr_min=num_imp.min()
#printing ny stats
print(f'\n-------NumPy Stats-----\nMean Score : {mean}\nMedian Score : {median}\nStandard Deviation : {sd}\nMax Score : {scr_max}\nMin Score : {scr_min}\n-------------------\n')
#finding all the categories with max frequency  
cat=np.array(df['category'])
cats,count=(np.unique(cat,return_counts=True))
max_count = np.max(count)
idx=np.where(count==max_count)
print(f'Most stories in : {cats[idx]} = {count[idx][0]}')
#printing all story titles with max comments
com=np.array(df['num_comments'])
max_com=np.max(com)
idx=np.where(com==max_com)
for i in idx:
    story_title = df["title"].values[i]
    print(f'Most commented story : {story_title} = {max_com} comments')
#adding new column engagement
df['engagement']=df['num_comments']/(df['score']+ 1)
#adding new column is_popular
df['is_popular']=df['score'] > mean
#saving it to file named trends_analysed.csv
file=r'data\trends_analysed.csv'
df.to_csv(file, index=False)
#printing confirmation message
print(f'Saved to {file}')