# 75000 ids/15 min + 18000 lookup/15mins
import tweepy,csv


header = ['name', 'description', 'location']
# Authenticate to Twitter
auth = tweepy.OAuthHandler("e0zseUEJgyZL31qXfJZB6m0zt", 
    "sifM2XFtF7jjra3m9uTT4z8gY8mdYviHMLwAu3IlHBqtbo20Vp")
auth.set_access_token("1463578925024657410-OYwNQ1hmYLUdhUcHzBm7krz9cjUuAB", 
    "HyWsXd6ZB1ySeGazfuJzFfUACaRwqr5jNEGaMkSmrVoqa")

api = tweepy.API(auth, wait_on_rate_limit=True)

name="vietnam_idol"
user = api.get_user(screen_name=name)
counts = user.followers_count

c = tweepy.Cursor(api.get_follower_ids, screen_name = name,count=5000)
ids = []
for x in c.items():
    ids.append(x)
print(len(ids))
count=0
list=[]
with open('results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Description", "Location"])
    for x in ids:
        count+=1
        if count==100:
            list.append(x)
            user = api.lookup_users(user_id=list[0:99])
            for i in range(len(user)):
                writer.writerow([user[i].screen_name, user[i].description, user[i].location])
            list=[]
            count=0
        else:
            list.append(x)