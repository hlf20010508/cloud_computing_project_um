FROM python:3.9.20-alpine3.20

WORKDIR /uploader

COPY uploader.py .
COPY index.html .

RUN pip install sanic==24.6.0 aiohttp==3.11.6

CMD python uploader.py