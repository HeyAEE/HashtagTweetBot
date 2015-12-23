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
    print('Successfully imported praw.')
except ImportError:
    print('Uh oh! You don\'t have praw installed to access the reddit API. Install praw using the following command:\n\npip install praw\n\nand try again.')
        
from sys import exit

from pprint import PrettyPrinter
printer = PrettyPrinter()
        
def main():
    redditor = p.Reddit(user_agent='Hashtagger')
    print('Successfully created reddit UA.')
    login = []
    f = open('private/login_info','r')
    [login.append(str(line).rstrip()) for line in f]
    f.close()
    try:
        redditor.login(login[0],login[1], disable_warning=True)
        print(redditor.user)
        print('So far, so good!')
    except p.errors.InvalidUserPass:
        print("Wrong username or password. Try again!")
        exit(1)
    # So far, I have created a reddit user agent and logged in, such that I can now start listening to the reddit streams. Next step: listen to the streams so I can find Twitter linked comments.
    comments = redditor.get_comments("baseball", limit=20)
    print("pulled comments")
    print("comments:\n")
    comments_to_analyze = []
    [comments_to_analyze.append(comment.body_html) for comment in comments]
    [printer.pprint(comment) for comment in comments_to_analyze]
        
if __name__=="__main__":
    main()
