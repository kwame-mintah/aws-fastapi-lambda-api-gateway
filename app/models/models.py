import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class Example(BaseModel):
    placeholder: str = Field(title="Example message returned")


class Message(BaseModel):
    messageId: int = Field(title="Message ID", examples=[1])
    example: Example = Field(title="Example Model inheriting another model")


class DynamoDBKeySchema(BaseModel):
    UUID: dict = Field(default={"S": "UUID"})
    DateReceived: dict = Field(default={"S": "DateReceived"})


class InsertData(BaseModel):
    UUID: str = Field(
        default=str(uuid.uuid4()), description="Universally Unique Identifier"
    )
    DateReceived: datetime = Field(default=datetime.now(), description="Date")
    Message: str = Field(description="Content of the message")


class Package(BaseModel):
    version: str = Field(default="", title="Package version", examples=["0.115.0"])
