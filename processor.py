from sanic import Sanic
from sanic.response import json
from sanic.request import Request
import pandas as pd
from io import BytesIO
import os

PORT = int(os.environ.get("PORT", 8001))

app = Sanic(__name__)


@app.route("/", methods=["POST"])
async def process(request: Request):
    data = pd.read_excel(BytesIO(request.body))

    data_no_name = data.drop(columns=["Name"])

    processed_data = pd.DataFrame()
    processed_data["Name"] = data["Name"]
    processed_data["TotalScore"] = data_no_name.sum(axis=1)
    processed_data["MaxScoreDifference"] = data_no_name.max(axis=1) - data_no_name.min(
        axis=1
    )

    return json(processed_data.values.tolist())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
