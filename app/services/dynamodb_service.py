import logging
from typing import List

import boto3
from botocore.exceptions import ClientError
from types_boto3_dynamodb import DynamoDBClient

from app.config import env_vars
from app.models.models import InsertData

logger = logging.getLogger(__name__)
MAX_GET_SIZE = 100  # Amazon DynamoDB rejects a get batch larger than 100 items.


class AWSDynamoDBService:
    """
    Example class to return mock / stubbed data.
    """

    def __init__(
        self,
        dynamodb_table: str,
        dynamodb_client: DynamoDBClient = boto3.client(
            service_name="dynamodb", region_name=env_vars.AWS_REGION
        ),
    ):
        self.table = dynamodb_table
        self.client = dynamodb_client

    def add_data(self, data: InsertData):
        try:
            self.client.put_item(
                TableName=self.table,
                Item={
                    "DateReceived": {"S": str(data.DateReceived)},
                    "UUID": {"S": data.UUID},
                },
            )
        except ClientError as exception:
            logger.error(
                f"Couldn't get data from {self.table} table, due to error code: {exception.response['Error']['Code']}, with error message: {exception.response['Error']['Message']}"
            )
            raise

    def get_all_items(self) -> List[dict]:
        try:
            response = self.client.scan(TableName=self.table)
        except ClientError as exception:
            logger.error(
                f"Couldn't get data from {self.table} table, due to error code: {exception.response['Error']['Code']}, with error message: {exception.response['Error']['Message']}"
            )
            raise
        else:
            return response["Items"] if "Items" in response else []

    def update_data(self, data: InsertData):
        try:
            response = self.client.update_item(
                TableName=self.table,
                Key={
                    "DateReceived": {"S": str(data.DateReceived)},
                    "UUID": {"S": data.UUID},
                },
                ReturnValues="UPDATED_NEW",
            )
        except ClientError as exception:
            logger.error(
                f"Couldn't get data from {self.table} table, due to error code: {exception.response['Error']['Code']}, with error message: {exception.response['Error']['Message']}"
            )
            raise
        else:
            return response["Attributes"]

    def delete_data(self, data: InsertData):
        try:
            self.client.delete_item(
                TableName=self.table,
                Key={
                    "DateReceived": {"S": str(data.DateReceived)},
                    "UUID": {"S": data.UUID},
                },
            )
        except ClientError as exception:
            logger.error(
                f"Couldn't get data from {self.table} table, due to error code: {exception.response['Error']['Code']}, with error message: {exception.response['Error']['Message']}"
            )
            raise
