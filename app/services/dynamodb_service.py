import logging
from datetime import datetime
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
    Encapsulates an Amazon DynamoDB table
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
        """
        Add data to a table.
        :param data:
        """
        try:
            self.client.put_item(
                TableName=self.table,
                Item={
                    "DateReceived": {"S": str(data.DateReceived)},
                    "UUID": {"S": data.UUID},
                    "Message": {"S": data.Message},
                },
            )
        except ClientError as exception:
            logger.error(
                f"Couldn't get data from {self.table} table, due to error code: {exception.response['Error']['Code']}, with error message: {exception.response['Error']['Message']}"
            )
            raise

    def get_all_items(self) -> List[dict]:
        """
        Get items stored within the table.
        :return:
        """
        try:
            response = self.client.scan(TableName=self.table)
        except ClientError as exception:
            logger.error(
                f"Couldn't get data from {self.table} table, due to error code: {exception.response['Error']['Code']}, with error message: {exception.response['Error']['Message']}"
            )
            raise
        else:
            return response["Items"] if "Items" in response else []

    def update_data(self, data: InsertData) -> dict:
        """
        Update an existing data in the table.
        :param data:
        :return: Updated attributes.
        """
        try:
            response = self.client.update_item(
                TableName=self.table,
                Key={
                    "DateReceived": {"S": str(data.DateReceived)},
                    "UUID": {"S": data.UUID},
                },
                UpdateExpression="set Message = :r",
                ExpressionAttributeValues={":r": {"S": str(data.Message)}},
                ConditionExpression="attribute_exists(Message) OR Message <> :r",
                ReturnValues="UPDATED_NEW",
            )
        except ClientError as exception:
            logger.error(
                f"Couldn't get data from {self.table} table, due to error code: {exception.response['Error']['Code']}, with error message: {exception.response['Error']['Message']}"
            )
            raise
        else:
            return response["Attributes"]

    def delete_data(self, uuid: str, date_received: datetime):
        """
        Delete an item from the table.
        :param uuid:
        :param date_received:
        """
        try:
            self.client.delete_item(
                TableName=self.table,
                Key={
                    "DateReceived": {"S": str(date_received)},
                    "UUID": {"S": uuid},
                },
            )
        except ClientError as exception:
            logger.error(
                f"Couldn't get data from {self.table} table, due to error code: {exception.response['Error']['Code']}, with error message: {exception.response['Error']['Message']}"
            )
            raise
