'''HashtagTweetBot.py - Making Reddit a hashtaggier place

        The goals for HashtagTweetBot are as follows:
        1. Reply to existing bot comments with links to the hashtags in their tweets.
        2. Reply to existing bot comments, hyperlinking the hashtags in their tweets to Twitter.
        3. Pull tweets directly from Twitter, including the hashtag link in the tweet.

---

Progress log:

12/22/15 - Initial development. Created basic directory structure. Can now .gitignore login info and any other file in the private folder while leaving the private folder intact. Also, can pull login info from a file in the private folder. Username is on first line. Password is on second line.
'''

try:
    import praw as p
except ImportError:
    print('Uh oh! You don\'t have praw installed to access the reddit API. Install praw using the following command:\n\npip install praw\n\nand try again.')
        
from sys import exit
        
def main():
    redditor = p.Reddit(user_agent='Hashtagger')
    print('test')
    login = []
    f = open('private/login_info','r')
    [login.append(str(line).rstrip()) for line in f]
    try:
        redditor.login(login[0],login[1])
        print(redditor.user())
    except praw.errors.InvalidUserPass:
        print("Wrong username. Try again!")
        sys.exit(1)
        
if __name__=="__main__":
    main()
