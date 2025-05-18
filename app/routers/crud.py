from typing import List

from fastapi import APIRouter, Depends, status

from app.dependencies import get_database_service
from app.models.models import Message, InsertData
from app.services.dynamodb_service import AWSDynamoDBService

router = APIRouter(prefix="/dynamodb", tags=["dynamodb"])


@router.get(
    path="",
    operation_id="ddbGetItem",
    summary="Gets all data from the table.",
    response_model=List[dict],
    status_code=status.HTTP_200_OK,
)
async def get_data(
    service: AWSDynamoDBService = Depends(get_database_service),
) -> List[dict]:
    """
    The operation returns a set of attributes for the item with the given primary key.
    :param service:
    :return: Message
    """
    return service.get_all_items()


@router.post(
    path="",
    operation_id="ddbPutItem",
    summary="Adds a data to the table.",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def add_data(
    data: InsertData,
    service: AWSDynamoDBService = Depends(get_database_service),
) -> None:
    """
    An example `POST` endpoint to return a response
    :param service:
    :return: List of Messages stored
    """
    return service.add_data(data=data)


@router.put(
    path="/{message_id}",
    operation_id="ddbUpdateItem",
    summary="Adds a data to the table.",
    response_model=List[Message],
    status_code=status.HTTP_200_OK,
)
async def update_data(
    message: Message,
    service: AWSDynamoDBService = Depends(get_database_service),
) -> List[Message]:
    """
    An example `POST` endpoint to return a response
    :param message:
    :param service:
    :return: List of Messages stored
    """
    return service.update_data()


@router.delete(
    path="/{message_id}",
    operation_id="deleteDemoRoot",
    summary="Demonstrating DEL Request",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def demo_delete(
    message_id: int,
    service: AWSDynamoDBService = Depends(get_database_service),
) -> None:
    """
    An example `DELETE` endpoint to remove a message from
    stub data
    :param message_id: The `messageId` to delete
    :param service: DemoService
    :return: successfully processed the request
    """
    return service.delete_data()
