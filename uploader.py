from sanic import Sanic
from sanic.response import html, text
from sanic.request import Request
from sanic.request.form import File
import os
import aiohttp

PORT = int(os.environ.get("PORT", 8000))
PROCESSOR_URL = os.environ["PROCESSOR_URL"]
RENDERER_URL = os.environ["RENDERER_URL"]

app = Sanic(__name__)


@app.route("/", methods=["GET"])
async def index(request: Request):
    with open("index.html") as file:
        return html(file.read())


@app.route("/upload", methods=["POST"])
async def upload(request: Request):
    file: File = request.files["file"][0]

    data = []

    async with aiohttp.ClientSession() as session:
        async with session.post(PROCESSOR_URL, data=file.body) as resp:
            data = await resp.json()

    async with aiohttp.ClientSession() as session:
        async with session.post(RENDERER_URL, json=data) as resp:
            resp = await resp.text()
            return text(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
