FROM python:3.7.13-alpine3.16

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt


ENTRYPOINT [ "python" ]

CMD ["main.py" ]
