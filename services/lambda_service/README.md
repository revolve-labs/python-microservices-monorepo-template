# Lambda Service

## Description
Python Lambda on Docker

## Pre-requirements
1. [Taskfile](https://taskfile.dev/): Improved version of Makefile
2. [Docker](https://www.docker.com/): Containers
3. [Pyenv](https://github.com/pyenv/pyenv-installer) & pyenv-virtualenv
4. [Python 3.12+](https://www.python.org/)

### Available tasks with Taskfile
```bash
task -l  # list of tasks with descriptions
task -a  # list of all tasks
```

## Setup - Development
### 1. Setup AWS CLI Credentials
1. Use `aws configure` to setup your AWS CLI credentials. Set:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_SESSION_TOKEN`
   - `AWS_DEFAULT_REGION`
2. Create a new profile for the project (name: `<profile-name>`)
   - The profile name is used in various scripts in `Taskfile.yml` 
3. Set the `AWS_PROFILE` env variable to `<profile-name>`
   ```bash
   export AWS_PROFILE=<profile-name>
   ```
### 2. Prepare virtual environment
```bash
task pyenv-create
pyenv activate <service_name>
task pyenv-setup
```

### 3. Run Lambda Locally
Note: `<service_name>` virtual environment must be active
```bash
python -m main.lambda_handler
```

### 3. Run Unit Tests
1. Download the pytest (unit-tests) environment vars
```bash
task get-env -- pytest
```

2. Run the tests
```bash
task pytest
```