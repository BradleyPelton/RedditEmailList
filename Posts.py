""" HOW TO EXECUTE: RUN THE FOLLOWING COMMAND
c:\Users\mavri\AppData\Local\Programs\Python\Python36>python c:\users\mavri\desktop\Redditproject\firstfile.py
""" 



reddit = praw.Reddit(client_id, client_secret,user_agent, username, password)

subred = reddit.subreddit("learnpython")
new = subred.new(limit = 10)


for i in new:
    print(i.title)




print("reached this point")
