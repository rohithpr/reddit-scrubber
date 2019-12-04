import json

import reddit


def main(event, context):
    reddit.scrub_reddit()


if __name__ == "__main__":
    main({}, {})
