# Midas Project

## Developing

To prepare the project for local development it's necessary to install the shared package in editable mode and install the dev dependencies. Run:

```
make develop
```

To sam build on a faster iteration without re-building `ServerlessDependenciesLayer`. Run:
```bash
make build-fast
# next command
sam local start-api
sam local invoke ...
```

## Running tests

```
make test
```

## Running mypy

```
make mypy
```

## Deploying code

Deploying code requires a configured AWS account and a local installation of [AWS SAM CLI](https://aws.amazon.com/serverless/sam/).

First build the project:

```
sam build
```

Then deploy it:

```
sam deploy --guided
```

The `--guided` flag is only required on the first deployment (or whevever you want to change deployment configuration).
