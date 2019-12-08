This is a list of some useful commands for easy reference.


### Install `pre-commit`, it's hooks and run it

```sh
pip install pre-commit  # Install it on your machine
pre-commit install  # Install hooks for the project
pre-commit run -a  # Run the hooks manually
```

### Install the plugin `serverless-python-requirements`

```sh
sls plugin install -n serverless-python-requirements
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
