# AWS FastAPI Lambda API Gateway

![python](https://img.shields.io/badge/python-3.11.6-informational)
![fastapi-0.115.12-informational](https://img.shields.io/badge/fastapi-0.115.12-informational)

This is a FastAPI application to be deployed as an [Amazon Web Services (AWS) Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function, triggered
via [AWS API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html). This project is to be
built and deployed using [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html).

For demonstration purposes, a simple Create Read Update Delete (CRUD) REST API has been created to perform actions against
an [AWS DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html), the deployed lambda function
IAM Role will need additional permissions when calling the operations defined.

![example-diagram-aws-console](/docs/aws-lambda-function-overview.png)

The underlying infrastructure needed can be found within my Terraform [terraform-aws-certified-devops-engineer-professional](https://github.com/kwame-mintah/terraform-aws-certified-devops-engineer-professional),
alongside CloudFormation templates used to create other resources within my [aws-cloudformation-playground](https://github.com/kwame-mintah/aws-cloudformation-playground).

## Usage

1. Install python packages used for the service

    ```console
   pip install -r requirements.txt
    ```
2. Run the FastAPI server, which will run on port 8000

    ```console
   python app/main.py
    ```

   Alternatively, if you're within your [virtual environment]:
   ```console
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
Endpoint documentation are available on http://127.0.0.1:8000/docs

## Docker

Running the `docker-compose.yml`, will build a new image aws-fastapi-lambda-api-gateway-fastapi:latest
which will be used for the `fastapi` service within the container.

```console
docker-compose up -d
```

![NOTE]
> Running the project via docker compose will on launch the lambda and is not the same as running the
> application via uvicorn. Will need to invoke the lambda by make a post request to the following URL:
> `curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{REPLACE_WITH_EVENT_HERE}'`

## Tests

Unit tests are located in `/tests/unit` directory, run unit tests using:

```console
pytest tests/unit
```

Additionally, a coverage report can be generated using [`pytest-cov`](https://pypi.org/project/pytest-cov/):

```console
pytest --cov=app tests/unit --cov-report=html:coverage_report
```

Will generate a coverage HTML file, in the `/coverage_report/` directory, simply open the `index.html` in your chosen
web browser.

Integration tests are located in `/tests/integration` directory, run integration using:

```console
pytest tests/integration
```

## Contributing

Git hook scripts are very helpful for identifying simple issues before pushing any changes.
Hooks will run on every commit automatically pointing out issues in the code e.g. trailing whitespace.

To help with the maintenance of these hooks, [pre-commit](https://pre-commit.com/) is used, along
with [pre-commit-hooks](https://pre-commit.com/#adding-pre-commit-plugins-to-your-project).

Please following [these instructions](https://pre-commit.com/#install) to install `pre-commit` locally and ensure that
you have run
`pre-commit install` to install the hooks for this project.

Additionally, once installed, the hooks can be updated to the latest available version with `pre-commit autoupdate`.

## GitHub Actions (CI/CD)

GitHub project has three workflow set up, found in `.github/workflows/`:

- '🧹 Run linter' (`run-linter.yml`): To run [Flake8](https://flake8.pycqa.org/en/latest/) and check Python code system
  and comply with various style guides.
- '🧪 Run unit tests' (`run-unit-tests.yml`): To run unit tests within a continuous integration (CI) environment,
  using [`pytest`](https://docs.pytest.org/en/8.2.x/).
