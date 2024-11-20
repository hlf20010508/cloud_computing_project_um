from sanic import Sanic
from sanic.response import html
from sanic.request import Request
import os

PORT = int(os.environ.get("PORT", 8002))

app = Sanic(__name__)


@app.route("/", methods=["POST"])
async def render(request: Request):
    data = request.json

    response_html = """
<style>
    table {
        text-align: left;
        margin-top: 20px;
    }
    th {
        min-width: 100px;
    }
</style>
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Total Score</th>
            <th>Max Score Difference</th>
        </tr>
    </thead>
    <tbody>
        %s
    </tbody>
</table>
"""

    data_html = ""
    for line in data:
        data_html += "<tr>"
        for item in line:
            data_html += "<td>" + str(item) + "</td>"
        data_html += "</tr>"

    response_html = response_html % data_html

    return html(response_html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
