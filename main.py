from flask import Flask, request
from form_service import get_form as get_form_service
import json


app = Flask(__name__)


@app.route("/get_form", methods=['POST'])
def get_form():
    form = request.json
    return json.dumps(get_form_service(form))


if __name__ == "__main__":
    app.run()



