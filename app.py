from flask import Flask, request
import json


app = Flask(__name__)

JSON_FILE_PATH = './data/pv_yield.json'

with open(JSON_FILE_PATH) as f:
  data = json.load(f)


@app.route("/api/pv_yield")
def get_energy_data():
  param_state = request.args.get("state")

  for x in data:
    if x['state'] == param_state:
      output_dict = x
      output_json = json.dumps(output_dict)
  return output_json


if __name__ == "__main__":
  app.run(debug=True)
