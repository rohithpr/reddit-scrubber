import configparser
import datetime

import praw

from .rule_builder import build_ruleset
from .utils import normalize_sub_name


def scrub_reddit():
    ruleset = build_ruleset()
    client = _get_reddit_client()
    me = _get_current_user(client)
    comments = _get_user_comments(me)
    _delete_comments(comments, ruleset)


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


def _get_comment_age(created_at, now):
    comment_time = datetime.datetime(
        1970, 1, 1, tzinfo=datetime.timezone.utc
    ) + datetime.timedelta(seconds=created_at)
    comment_age = now - comment_time
    return comment_age


def _is_deletable_age(created_at, now, rule):
    age = _get_comment_age(created_at, now)
    if age.days > rule["max_age_days"]:
        return True
    return False


def _get_rule(sub, ruleset):
    rule = ruleset.get(sub, ruleset["default"])
    return rule


def _get_has_skip_delete_pattern(text, rule):
    if rule["skip_delete_pattern"]:
        return rule["skip_delete_pattern"] in text
    return False


def _is_deletable_comment(comment, ruleset):
    # TODO: Add other criteria for deletion
    rule = _get_rule(normalize_sub_name(comment.subreddit.display_name), ruleset)

    if _get_has_skip_delete_pattern(comment.body, rule):
        return False

    now = datetime.datetime.now(datetime.timezone.utc)
    if _is_deletable_age(comment.created_utc, now, rule):
        return True

    return False


def _delete_comments(comments, ruleset):
    # TODO: Check if there's a way to process these comments oldest first.
    for comment in comments:
        if _is_deletable_comment(comment, ruleset):
            comment.delete()
