import requests
import time
import pandas as pd
import json 
import datetime
#header
headers = {"User-Agent": "TrendPulse/1.0"}
#categories
categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}
counts = {cat: 0 for cat in categories}
#Fetching story ID from url 
url='https://hacker-news.firebaseio.com/v0/topstories.json'
id_response=requests.get(url)
id_response=(id_response.json()[0:500])
#fetching story by providing story id in url 2 link and storing stories in list called stories
stories=[]
for id in id_response:
    try:
        print(id)
        url2=f'https://hacker-news.firebaseio.com/v0/item/{id}.json'
        story_response=(requests.get(url2,headers=headers).json())
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if story_response:
            # Add the Current time
            story_response['collected_at'] = cur_time
            stories.append(story_response)
    #continuing if failed to fetch
    except Exception as e:
        print(f"Failed to fetch story IDs: {e}")
        continue
#categorizing each story
final_data = []
for category_name, keywords in categories.items():
    for story in stories:
        title = story.get('title', '').lower()
        #25 stories per category
        if counts[category_name] < 25:
            for word in keywords:
                if word.lower() in title:
                    story['category']= category_name
                    #all the field of our future dataframe
                    param = {
                            "post_id": story.get('id'),
                            "title": story.get('title'),
                            "category": category_name,
                            "score": story.get('score'),
                            "num_comments": story.get('descendants', 0),
                            "author": story.get('by'),
                            "collected_at": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        }
                    final_data.append(param)
                    counts[category_name] += 1
                    break
    #sleep between switching from each category 
    time.sleep(2)        
#converting it to dataframe
df=pd.DataFrame(final_data)
print(df)
#creating a json file
name=r'data\trends_20260405.json'
with open(name, "w") as f:
    json.dump(final_data, f, indent=4)
print(f"Successfully saved {len(final_data)} stories at {name}")