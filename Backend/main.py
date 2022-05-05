import tweepy,csv


header = ['name', 'description', 'location']
# Authenticate to Twitter
auth = tweepy.OAuthHandler("e0zseUEJgyZL31qXfJZB6m0zt", 
    "sifM2XFtF7jjra3m9uTT4z8gY8mdYviHMLwAu3IlHBqtbo20Vp")
auth.set_access_token("1463578925024657410-OYwNQ1hmYLUdhUcHzBm7krz9cjUuAB", 
    "HyWsXd6ZB1ySeGazfuJzFfUACaRwqr5jNEGaMkSmrVoqa")

api = tweepy.API(auth, wait_on_rate_limit=True)

name="vietnam_idol"
# user = api.get_user(screen_name=name)

# print("User details:")
# print(user.screen_name)
# print(user.description)
# print(user.location)

c = tweepy.Cursor(api.get_followers, screen_name=name)
count = 0
for follower in c.items():
    count += 1
print(name + " has " + str(count) + " followers.")
for follower in tweepy.Cursor(api.get_followers,screen_name=name).items(count):
    print(follower.name)
    print(follower.description)
    print(follower.location)
    # print()

# with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write multiple rows
#     writer.writerows(data)
# c = tweepy.Cursor(api.get_follower_ids, screen_name = 'vietnam_idol')
# ids = []
# for page in c.pages():
#      ids.append(page)

