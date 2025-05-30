import uvicorn
from fastapi import FastAPI, status
from mangum import Mangum

from app.internal import versions
from app.routers import crud

# Provide meta data for API.
# https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api
app = FastAPI(
    title="FastAPI Bigger Applications Template",
    description="An example project for bigger applications",
    contact={
        "name": "Template",
        "url": "https://github.com/kwame-mintah/python-fastapi-bigger-applications-template",
        "email": "email@email.com",
    },
    license_info={
        "name": "Example License",
        "url": "https://choosealicense.com/",
    },
)
app.include_router(crud.router)
app.include_router(versions.router)


@app.get(path="/", tags=["root"], status_code=status.HTTP_200_OK)
async def root() -> dict:
    """
    Example response, when accessing root e.g. `http://localhost:8000/`
    :return: response
    """
    return {"message": "What a wonderful kind of day."}


handler = Mangum(app)

if __name__ == "__main__":
    # Helpful for when running locally.
    uvicorn.run(app="app.main:app", host="0.0.0.0", port=8000)
