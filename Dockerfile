FROM python:3.12-alpine

WORKDIR /code

COPY ./src /code/src
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80" ]
