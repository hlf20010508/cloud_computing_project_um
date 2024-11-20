FROM python:3.9.20-alpine3.20

WORKDIR /processor

COPY processor.py .

RUN pip install sanic==24.6.0 pandas==2.2.3 openpyxl==3.1.5

CMD python processor.py