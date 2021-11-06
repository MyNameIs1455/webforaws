import os
import json
import datetime

from flask import Flask
app = Flask(__name__)
base_folder = os.path.dirname(os.path.abspath(__file__))
resource_dir = os.path.join(base_folder,"resources")

data = {}


@app.route("/")
def hello():

    data[datetime.datetime.now().strftime("%d %m %Y %H:%M:%S")] = "Update"

    with open("resources/data_file.json", "w") as write_file:
        json.dump(data, write_file)



    with open(os.path.join(resource_dir,"responce.json")) as f:
        return "%s - %s" % (json.loads(f.read()).get("dataload1"), datetime.datetime.now().strftime("%d %m %Y %H:%M:%S"))


if __name__ == "__main__":

    app.run("0.0.0.0",debug=True)
