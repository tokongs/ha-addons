ARG BUILD_FROM 
FROM $BUILD_FROM

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \ 
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 

RUN apk add --no-cache python3-dev gcc libc-dev musl-dev openblas gfortran build-base postgresql-libs postgresql-dev libffi-dev curl zlib-dev

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python
ENV PATH="$POETRY_HOME/bin:$PATH"

COPY . ./
RUN poetry install --no-interaction --no-ansi
RUN chmod +x run.sh
CMD ["./run.sh"]