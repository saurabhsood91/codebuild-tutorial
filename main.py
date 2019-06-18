from flask import Flask
from utils.helpers import squared

app = Flask(__name__)


@app.route("/<int:num>")
def squared_number(num):
    return str(squared(num))

