import json
import sys

import boto3
import fakeredis
import pytest

from moto import mock_aws

"""
These are general fixtures that can be used across multiple lambdas.
All generic mocked AWS Services and resources should be defined here.
"""
# TODO: Make this be loaded from a .env file
# TODO: How can we make the lambdas use config.py?
MOCK_ENV_VARS = {
    "AWS_ACCESS_KEY_ID": "dummy-access-key-id",
    "AWS_SECRET_ACCESS_KEY": "dummy-secret-access-key",
    "AWS_DEFAULT_REGION": "us-west-2",
    "ENVIRONMENT": "LOCAL",
    "DB_HOST": "localhost",
}


# region AWS Mocks
@pytest.fixture
def mock_dynamodb():
    """Sample Fixture that mocks DynamoDB 'MHS Config Table'"""
    # Table definition
    table_definition = {
        'TableName': MOCK_ENV_VARS["DYBAMODB_NAME"],
        'KeySchema': [{'AttributeName': 'USER_ID', 'KeyType': 'HASH'}],
        'AttributeDefinitions': [{'AttributeName': 'USER_ID', 'AttributeType': 'S'}],
        'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    }
    # Use "with" context manager which enables the best integration between fixtures and moto
    with mock_aws():
        # Create a mocked DynamoDB resource
        dynamodb = boto3.resource('dynamodb', region_name=MOCK_ENV_VARS["AWS_DEFAULT_REGION"])
        # Create the table
        table = dynamodb.create_table(**table_definition)
        # Returns the table object which will be temporary during the execution of the test
        yield table


@pytest.fixture
def mock_redis(monkeypatch):
    """Mock Redis globally across all functions."""
    # Create a fakeredis instance
    fake_redis = fakeredis.FakeStrictRedis()

    # Use monkeypatch to replace the redis.Redis class with fakeredis.FakeStrictRedis
    # This means any instantiation of redis.Redis will actually return a fakeredis instance
    monkeypatch.setattr("redis.Redis", lambda *args, **kwargs: fake_redis)
    # If we use a Redis connection pool, we might also need to mock it
    monkeypatch.setattr("redis.ConnectionPool", lambda *args, **kwargs: fakeredis.FakeConnectionPool())


@pytest.fixture
def mock_s3_buckets():
    """Fixture that mocks S3 buckets"""
    with mock_aws():
        s3 = boto3.resource('s3', region_name=MOCK_ENV_VARS["AWS_DEFAULT_REGION"])
        # Create the bucket as per environment variable with the correct location constraint
        bucket = s3.create_bucket(
            Bucket=MOCK_ENV_VARS["S3_BUCKET_NAME"],
            CreateBucketConfiguration={
                'LocationConstraint': MOCK_ENV_VARS["AWS_DEFAULT_REGION"]
            }
        )
        yield bucket

# endregion


@pytest.fixture(autouse=True)
def shared_lib():
    """Adds Shared Libraries to sys.path for import accessibility."""
    # Path to the lambda layers code
    models_shared_lib = "../../shared/shared_lib/models"

    # Add paths to sys.path for import accessibility
    sys.path.insert(0, models_shared_lib)

    yield

    # Cleanup if necessary
    sys.path.remove(models_shared_lib)
