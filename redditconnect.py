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

def getTopLevelComment(submissions):
    top_lvl_cmts = []
    for sub in submissions:
        top_lvl_cmt = [cmt for cmt in sub.comments]
        top_lvl_cmts.append(top_lvl_cmt)
    return top_lvl_cmts


def getUsers(submissions):
    return [{"username": sub.author.name, "title": sub.title}
            for sub in submissions]

def main():
    # Example use
    prog = reddit.subreddit('programming')

    # this will get 25 posters
    submissions = [sub for sub in prog.hot(limit=25)]

    #user_dict = getUsers(submissions)
    #print("User name to title hash")
    #print(user_dict)

    # this actually produces an array of arrays 
    # that contain comment ids it looks like
    # [Comment(id='dtyuazw'), Comment(id='dtxqs3d')], [Comment(id='dtxkhdc'),
    # Comment(id='dtxjmoe')], [Comment(id='dtyoivu')],
    # [Comment(id='dty8zyf')], [], [], [], [], [Comment(id='dtxigt3'),
    # Comment(id='dtxz8fu')], [Comment(id='dty823n')],
    # [Comment(id='dtyb1qx')], [], []]
    toplvl = getTopLevelComment(submissions)
    print('Top level comments of all of the submissions:')
    print(toplvl)

if __name__ == "__main__":
    main()
