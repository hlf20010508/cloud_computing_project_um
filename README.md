# cloud_computing_project_um
Cloud computing project in UM

After deploy, visit http://127.0.0.1:8000

The needed file is `Grade Table.xlsx` in the project folder.

## Description
- uploader service provides functionality of web index, file uploading, and result showing. When receives a file, it firstly transfers the data to processor, then transfers the result from the processor to renderer, and finally show the result.
- processor service calculates total scores and max score difference. It returns the result as a two dimensional list to uploader.
- renderer service renders data to html. It render the data from processor and return the result as html to uploader.

## Deploy with Docker Compose
```sh
docker compose up -d
```

## Deploy Directly
Install dependencies
```sh
# if you are not using poetry, run `pip install poetry`
# or install sanic, aiohttp, pandas, openpyxl manually
poetry install
```

Run uploader
```sh
export PORT=8000
export PROCESSOR_URL=http://127.0.0.1:8001
export RENDERER_URL=http://127.0.0.1:8002
poetry run python uploader.py
```

Run processor
```sh
export PORT=8001
poetry run python processor.py
```

Run renderer
```sh
export PORT=8002
poetry run python renderer.py
```