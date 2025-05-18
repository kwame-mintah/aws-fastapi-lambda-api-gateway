from pydantic import Field
from pydantic_settings import BaseSettings


class EnvironmentVariables(BaseSettings):
    DYNAMODB_TABLE_NAME: str = Field(
        default="devops-engineer-eu-west-2-dev-dynamodb-table",
        description="The name of the table or Amazon Resource Name (ARN) of the table",
    )
    # Defined runtime environment variables
    # https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
    AWS_REGION: str = Field(
        default="eu-west-2", description="The region the function is running in."
    )


env_vars = EnvironmentVariables()
