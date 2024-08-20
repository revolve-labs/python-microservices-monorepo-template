FROM public.ecr.aws/lambda/python:3.12

# dnf is the package manager for Fedora
RUN dnf update -y
# RUN dnf install -y gcc python3-devel
RUN dnf clean all

RUN pip3 install --no-cache-dir --upgrade pip poetry

ENV POETRY_VIRTUALENVS_CREATE=false

# Set the working directory in the container
WORKDIR ${LAMBDA_TASK_ROOT}

# Copy the current directory contents into the container at /app
COPY . ${LAMBDA_TASK_ROOT}

RUN poetry install --no-dev

CMD ["main.lambda_handler"]
