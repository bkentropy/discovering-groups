import praw
import config 

auth = config.auth
reddit = praw.Reddit(
    client_id=auth["client_id"],
    client_secret=auth["client_secret"],
    password=auth["password"],
    user_agent=auth["user_agent"],
    username=auth["username"]
)

# reddit.subreddit('test').submit("Hello worlllllld", url="https://reddit.com")
# submission = reddit.submission(url="https://www.reddit.com/r/test/comments/5vg5d8")
# submission.reply("Super rad")
# for s in reddit.front.hot(limit=256):
#    print(s.score)

prog = reddit.subreddit('programming')

# this gets 25 ish posters
user_dict = {}

submissions = [sub for sub in prog.hot(limit=25)]
for sub in submissions:
    user_dict[sub.author] = {}

for sub in submissions:
    top_lvl_cmts = [cmt for cmt in sub.comments]

def usernameToTitle(submissions):
    return [{"username": sub.author.name, "title": sub.title}
            for sub in submissions]

untotitle = username(submissions)

