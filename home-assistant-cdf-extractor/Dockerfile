ARG BUILD_FROM=ghcr.io/hassio-addons/base-python/amd64:9.0.0
FROM $BUILD_FROM

WORKDIR /addon

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apk add --update --no-cache gcc musl-dev libc-dev linux-headers zlib-dev && curl -sSL https://install.python-poetry.org | python3 -
RUN 

COPY . . 
RUN poetry install --no-interaction --no-ansi 
RUN chmod +x run.sh

CMD ["./run.sh"]