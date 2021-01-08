from flask import Flask, request, jsonify
import json


app = Flask(__name__)

JSON_FILE_PATH = './data/pv_yield.json'

with open(JSON_FILE_PATH) as f:
  data = json.load(f)


@app.route("/api/pv_yield")
def get_energy_data():
  param_state = request.args.get("state")
  param_capacity = request.args.get("capacity")

  for x in data:
    output_dict = x
    if x['state'] == param_state:
      output_dict['yield'] = x['yield'] * int(param_capacity)
      output_json = json.dumps(output_dict)
      break

    else:
      output_json = jsonify(error="Please insert correct state & capacity.")

  return output_json


if __name__ == "__main__":
  app.run()
