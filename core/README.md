# Class RedditReport

* filename (string): the name of the output file, not including file extension. e.g.: "my_report", not "my_report.pdf"
* reddit_user(RedditUser): instance of the Reddit user account which will be used as interface with the RedditAPI through ```praw``` Python library.
* subs_list(list): list of strings containing the subreddits' names to include in the Report.
* lines_per_sub(integer): number of lines per subreddit to generate in the Report.
* report_data(dictionary): Report data stored in a dictionary of lists.
* order_posts_by(string): one of three values = 'new', 'hot', 'top'.