from flask import Flask
from flask_pydantic import validate

from db.db import DBService

app = Flask(__name__)

@app.route('/')
@validate()
def index():
    return DBService.query("Select * from test", ())


if __name__ == '__main__':
    app.run()