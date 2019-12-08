# Reddit Scrubber

A Python 3 - [serverless](https://serverless.com/) app that runs periodically on AWS Lambda to delete old content of yours from Reddit.


## Architecture and Overview

This project is built using the [serverless](https://serverless.com/) framework. The application stack is deployed with the help of a CloudFormation template - some of which is defined it the `serverless.yml` file.

A CloudWatch Scheduled Event triggers the Lambda function periodically at an interval as defined in `serverless.yml`. `handler.py:main` is the entry point for the execution of this app.

The user's credentials are read from the file `credentials.ini`, to instantiate a [PRAW](https://github.com/praw-dev/praw) object which is used to communicate with Reddit.

Configuration of when and which content to delete are read from the file `config.yaml`. Some default rules are hardcoded (all content older than 7 days) in the codebase to ensure that the application can be deployed with minimal configuration.


## Getting started

- Install `serverless`, `serverless-python-requirements` and `docker` (it is a requirement for the plugin to work correctly). These, and many other useful commands can be found in `docs/help.md`.
- Copy the contents of `example-credentials.ini` to `credentials.ini` and fill it in. If this is your first time using a PRAW based app, [PRAW documentation](https://praw.readthedocs.io/en/latest/getting_started/configuration.html) will help you configure the file. This file name has been added to `.gitignore` so that you don't have to worry about accidentally adding your credentials to git history.
- Copy the contents of `example-config.yaml` to `config.yaml` and extend it to set up your own rules on when content should be deleted.
- Deploy the app using the command `sls deploy -v`.


## Potential Future Enhancements

- Store metrics of content deleted
- Send a periodic email notification with these metrics
