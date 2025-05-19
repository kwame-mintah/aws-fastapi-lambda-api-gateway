from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, status

from app.dependencies import get_database_service
from app.models.models import InsertData
from app.services.dynamodb_service import AWSDynamoDBService

router = APIRouter(prefix="/dynamodb", tags=["dynamodb"])


@router.get(
    path="",
    operation_id="ddbGetItem",
    summary="Demonstrating getting data from the table.",
    response_model=List[dict],
    status_code=status.HTTP_200_OK,
)
async def get_data(
    service: AWSDynamoDBService = Depends(get_database_service),
) -> List[dict]:
    """
    The operation returns a set of attributes for the item with the given key(s).
    :param service: AWSDynamoDBService
    :return: List of items.
    """
    return service.get_all_items()


@router.post(
    path="",
    operation_id="ddbPutItem",
    summary="Demonstrating adding data to the table.",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def add_data(
    data: InsertData,
    service: AWSDynamoDBService = Depends(get_database_service),
) -> None:
    """
    Add data to the table.
    :param data:
    :param service: AWSDynamoDBService
    """
    return service.add_data(data=data)


@router.put(
    path="",
    operation_id="ddbUpdateItem",
    summary="Demonstrating updating data in the table.",
    status_code=status.HTTP_200_OK,
)
async def update_data(
    data: InsertData,
    service: AWSDynamoDBService = Depends(get_database_service),
) -> dict:
    """
    Update an existing item using key(s) and return only updated
    attributes.
    :param data:
    :param service: AWSDynamoDBService
    :return: Updated attributes.
    """
    return service.update_data(data=data)


@router.delete(
    path="/{uuid}/{date_received}",
    operation_id="ddbDelete_item",
    summary="Demonstrating deleting data.",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def demo_delete(
    uuid: str,
    date_received: datetime,
    service: AWSDynamoDBService = Depends(get_database_service),
) -> None:
    """
    Delete an item from the table.
    :param uuid:
    :param date_received:
    :param service: AWSDynamoDBService
    """
    return service.delete_data(uuid=uuid, date_received=date_received)
