ARG BUILD_PLATFORM=linux/amd64
# Use python3.11 at the same release date as python3.11.6?
ARG BASE_IMAGE=public.ecr.aws/lambda/python:3.11.2023.08.02.09
FROM --platform=${BUILD_PLATFORM} ${BASE_IMAGE}

# Set working directory as `/code/`
WORKDIR /code

# Copy python modules used within application
COPY ./requirements.txt /code/requirements.txt

# Install all python modules, keep image as small as possible
# don't store the cache directory during install
RUN pip install wheel && \
    pip install --no-build-isolation "Cython<3" "pyyaml==5.4.1" && \
    pip install --no-build-isolation --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application code to `/code/app/`
COPY . /code

# Don't run application as root, instead user called `nobody`
RUN chown -R nobody /code

USER nobody

CMD ["main.handler"]
