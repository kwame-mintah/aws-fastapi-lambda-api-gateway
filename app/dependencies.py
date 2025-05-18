from app.config import env_vars
from app.services.dynamodb_service import AWSDynamoDBService


def get_database_service() -> AWSDynamoDBService:
    """
    Dependency injection example.
    :return: DemoService
    """
    return AWSDynamoDBService(dynamodb_table=env_vars.DYNAMODB_TABLE_NAME)
