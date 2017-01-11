import praw
from PDFGenerator import PDFGenerator

# import imghdr, urllib, cStringIO
# import uuid
# # import urllib2
# import os, sys
#
# import urllib
#
# # from imgurpython import ImgurClient
# from subprocess import call
# import time
from praw.models import Submission


class RedditConnection(object):
    """provides a connection to reddit"""

    def __init__(self, client_tag, client_id, client_secret, redirect_uri, username, password):
        super(RedditConnection, self).__init__()
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.username = username
        self.connection = self.get_reddit(client_id, client_secret, password, username)

    def get_reddit(self, client_id, client_secret, password, username, user_agent="https://jabbari.io") -> praw.Reddit:
        return praw.Reddit(client_id=client_id, client_secret=client_secret,
                           password=password,
                           username=username, user_agent=user_agent)

    def get_posts_from_sub(self, sub_reddit, limit=None, save_to_pdf=False):
        result =  self.connection.subreddit(sub_reddit).hot(limit=limit)
        if not save_to_pdf:
            return result
        else:
            for submission in result:
                try:
                    self.post_to_pdf(submission)
                except Exception as e:
                    print(e)

    def post_to_pdf(self, submission: Submission) -> None:
        PDFGenerator()
        PDFGenerator.instance.generate_pdf(submission)
