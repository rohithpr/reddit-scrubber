# Reddit Scrubber

A serverless app that runs periodically on AWS Lambda to delete old comments and posts from Reddit.

## Useful commands


### Install `pre-commit`, it's hooks and run it

```sh
pip install pre-commit
pre-commit install
pre-commit run -a
```

### Install the plugin `serverless-python-requirements`

```sh
sls plugin install -n serverless-python-requirements
```

### Install pre-commit hooks

```sh
pre-commit install
```

### Deploy the application to AWS

```sh
sls deploy -v
```

### Deploy only function changes to AWS

```sh
sls deploy function -f scrubber -v
```

### Invoke function

```sh
sls invoke -f scrubber -l
```

### Tail logs

```sh
sls logs -f scrubber -t
```

### Teardown the app

```sh
sls remove
```
