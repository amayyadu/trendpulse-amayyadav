import matplotlib.pyplot as plt
import pandas as pd
#Reading Csv file
df=pd.read_csv(r'data\trends_analysed.csv')
#resizing area as the content is too large
plt.figure(figsize=(13,6)) 
#ploting and formating horizontal bar graph (ScoreXStory Title)
plt.barh(df.sort_values('score',ascending=False)['title'].head(10).apply(lambda x: x[:47] + '...' if len(x) > 50 else x),(df.sort_values('score',ascending=False)['score'].head(10)))
plt.xlabel('Score')
plt.ylabel('Story Title')
plt.title('Top 10 Stories by Score')
plt.tight_layout()
plt.subplots_adjust(left=0.33) 
plt.savefig(r'outputs/chart1_top_stories.png') 
a=plt.show()
#ploting and formating default bar graph of category count
plt.bar(df['category'].unique(),df['category'].value_counts())
plt.xlabel('Ctegory')
plt.ylabel('Count')
plt.title('Category Count')
plt.savefig('outputs/chart2_categories.png') 
b=plt.show()
#ploting and formating scatter graph
#select the story score and comments which is not popular  
plt.scatter(df[df['is_popular']==0]['score'], 
            df[df['is_popular']==0]['num_comments'], 
            c='skyblue', label='Not Popular')
#select the story score and comments which is popular  
plt.scatter(df[df['is_popular']==1]['score'], 
            df[df['is_popular']==1]['num_comments'], 
            c='orange', label='Popular')
plt.title('Score vs Comments')
plt.xlabel('score')
plt.ylabel('num_comments')
#adding legend
plt.legend(title="Status")
plt.savefig('outputs/chart3_scatter.png') 
c=plt.show()

#showing all the graphs by subplot
plt.figure(figsize=(16, 10)) 
#graph 1 (bottom)
plt.subplot(2,3,5)
plt.barh(df.sort_values('score',ascending=False)['title'].head(10).apply(lambda x: x[:47] + '...' if len(x) > 50 else x),(df.sort_values('score',ascending=False)['score'].head(10)))
plt.xlabel('Score')
plt.ylabel('Story Title')
plt.title('Top 10 Stories by Score')
#graph 2(top right)
plt.subplot(2, 3, 3)
plt.bar(df['category'].unique(),df['category'].value_counts())
plt.title('Category Count')
#rotating to avoid overlap
plt.xticks(rotation=25, ha='right')
plt.xlabel('Ctegory')
plt.ylabel('Category Count')
#graph 3(top left)
plt.subplot(2,3,1)
plt.scatter(df[df['is_popular']==0]['score'], 
            df[df['is_popular']==0]['num_comments'], 
            c='skyblue', label='Not Popular')
plt.scatter(df[df['is_popular']==1]['score'], 
            df[df['is_popular']==1]['num_comments'], 
            c='orange', label='Popular')
plt.title('Score vs Comments')
plt.xlabel('score')
plt.ylabel('num_comments')
plt.legend(title="Status")
#formating all graph clubbed chart
plt.subplots_adjust(left=0.63)
plt.suptitle("TrendPulse Dashboard", fontsize=16)
plt.tight_layout(pad=4.0)
plt.subplots_adjust(left=0.05, right=0.95, top=0.90, bottom=0.1, wspace=0.3, hspace=0.4)
plt.savefig('outputs/dashboard.png')
plt.show()
