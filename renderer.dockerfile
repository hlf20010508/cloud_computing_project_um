FROM python:3.9.20-alpine3.20

WORKDIR /renderer

COPY renderer.py .

RUN pip install sanic==24.6.0

CMD python renderer.py