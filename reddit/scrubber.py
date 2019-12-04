import configparser
import datetime

import praw

# TODO: Move to config file
MAX_COMMENT_AGE = datetime.timedelta(**{"days": 2})


def scrub_reddit():
    client = _get_reddit_client()
    me = _get_current_user(client)
    _delete_comments(me)


def _get_reddit_client():
    config = configparser.ConfigParser()
    config.read("credentials.ini")
    credentials = {
        key: config["reddit-scrubber"][key] for key in config["reddit-scrubber"]
    }
    return praw.Reddit(**credentials)


def _get_current_user(client):
    return client.user.me()


def _get_user_comments(user):
    return user.comments.new()


def _is_of_deletable_age(comment):
    epoch = comment.created_utc
    now = datetime.datetime.now(datetime.timezone.utc)
    comment_time = datetime.datetime(
        1970, 1, 1, tzinfo=datetime.timezone.utc
    ) + datetime.timedelta(seconds=epoch)
    comment_age = now - comment_time
    if comment_age > MAX_COMMENT_AGE:
        return True
    return False


def _is_deletable_comment(comment):
    # TODO: Add other criteria for deletion
    if _is_of_deletable_age(comment):
        return True
    return False


def _delete_comments(user):
    # TODO: Delete comments instead of just printing them
    comments = _get_user_comments(user)
    deletable = []
    for comment in comments:
        if _is_deletable_comment(comment):
            deletable.append(comment)

    print(deletable)
