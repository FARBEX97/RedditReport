class RedditPost:
    def __init__(self, submission, sub_name):
        self.submission = submission
        self.sub_name = sub_name
        self.title = self.submission.title
        self.url = self.submission.url
        self.score = self.submission.score
        self.num_comments = self.submission.num_comments
