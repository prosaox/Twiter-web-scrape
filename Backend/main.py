import tweepy,csv


header = ['name', 'description', 'location']
# Authenticate to Twitter
auth = tweepy.OAuthHandler("e0zseUEJgyZL31qXfJZB6m0zt", 
    "sifM2XFtF7jjra3m9uTT4z8gY8mdYviHMLwAu3IlHBqtbo20Vp")
auth.set_access_token("1463578925024657410-OYwNQ1hmYLUdhUcHzBm7krz9cjUuAB", 
    "HyWsXd6ZB1ySeGazfuJzFfUACaRwqr5jNEGaMkSmrVoqa")

api = tweepy.API(auth, wait_on_rate_limit=True)

name="MikezGarcia"
# user = api.get_user(screen_name=name)
# count = user.followers_count
# print("User details:")
# print(user.screen_name)
# print(user.description)
# print(user.location)
# data=[]
# print(name + " has " + str(count) + " followers.")
# for follower in tweepy.Cursor(api.get_followers,screen_name=name).items(count):
#     x=[follower.name,follower.description,follower.location]
#     data.append(x)


c = tweepy.Cursor(api.get_follower_ids, screen_name = name)
ids = []
for x in c.items():
    ids.append(x)

with open('results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Description", "Location"])
    for x in ids:
        user = api.get_user(user_id=x)
        writer.writerow([user.screen_name, user.description, user.location])